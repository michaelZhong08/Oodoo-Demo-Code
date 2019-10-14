from odoo import fields,models

class BookCategory(models.Model):
    _name='library.book.category'
    _description='Library Book Category'
    _partent_store=True

    name=fields.Char(translate=True,required=True)
    partent_id=fields.Many2one(
        'library.book.category',
        'Partent Category',
        ondelete='restrict',
    )
    partent_path=fields.Char(index=True)

    child_ids=fields.One2many(
        'library.book.category',
        'partent_id',
        'Subcategories'
    )

    hightlighted_id=fields.Reference(
        [('library.book','Book'),('res.partner','Author')],
        'Category Highlight'
    )