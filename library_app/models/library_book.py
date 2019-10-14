from odoo import api, fields, models
from odoo.exceptions import Warning


class Book(models.Model):
        '''
        _name = 'library.book'
        _description = 'Book'
        name = fields.Char('Title', required=True)
        isbn = fields.Char('ISBN')
        active = fields.Boolean('Active?', default=True)
        date_published = fields.Date()
        image = fields.Binary('Cover')
        publisher_id = fields.Many2one('res.partner', string='Publisher')
        author_ids = fields.Many2many('res.partner', string='Authors')
        '''
        _name = 'library.book'
        _description = 'Book'
        # String fields
        name = fields.Char('Title', required=True)
        isbn = fields.Char('ISBN')
        book_type = fields.Selection(
            [('paper', 'Paperback'),
            ('hard', 'Hardcover'),
            ('electronic', 'Electronic'),
            ('other', 'Other')],
            'Type')
        notes = fields.Text('Internal Notes')
        descr = fields.Html('Description')

        # Numeric fields:
        copies = fields.Integer(default=1)
        avg_rating = fields.Float('Average Rating', (3,2))
        price = fields.Monetary('Price', 'currency_id')
        currency_id = fields.Many2one('res.currency') # price helper

        # Date and time fields
        date_published = fields.Date()
        last_borrow_date = fields.Datetime(
            'Last Borrowed On',
            default=lambda self: fields.Datetime.now())

        # Other fields
        active = fields.Boolean('Active?', default=True)
        image = fields.Binary('Cover')

        # Relational Fields
        publisher_id = fields.Many2one('res.partner', string='Publisher')
        author_ids = fields.Many2many('res.partner', string='Authors')
        '''
        # Book <-> Authors关联(使用关键字参数)
        author_ids = fields.Many2many(
                comodel_name='res.partner', # 关联模型(必填)
                relation='library_book_res_partner_rel', # 关联表名
                column1='a_id', # 本记录关联表字段
                column2='p_id', # 关联记录关联表字段
                string='Authors') # string标签文本
        '''

        publisher_country_id=fields.Many2one(
                'res.country',
                String='Publiser Country',
                related='publisher_id.country_id'
        )
        @api.multi
        def _check_isbn(self):
                self.ensure_one()
                if self.isbn=='isbn':
                        return True
                else:
                        return False
        @api.multi
        def button_check_isbn(self):
                for book in self:
                        if not book.isbn:
                                raise Warning('Please provide an ISBN for %s' % book.name)
                        if book.isbn and not book._check_isbn():
                                raise Warning('%s is an invalid ISBN' % book.isbn)
                return {}