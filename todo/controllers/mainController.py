# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class TodoPortal(http.Controller):
    @http.route('/todo/site', auth='public', website=True)
    def helloworld(self, **kwargs):
        return request.render('todo.todosite')

    @http.route('/todo/ajaxtest',type='http' , auth='public', website=True)
    def ajaxtest(self, **kwargs):
        todo=request.env['todo.main']
        todosearch=todo.search([])
        #print(tododic)
        '''
        dict={}
        dict['phase']='stage1'
        json.dumps(dict)
        '''
        '''
        todoread=todo.read(todosearch)
        '''
        #print(todosearch)
        #print(type(todosearch))
        datalist=[]
        datadict={}
        for todo in todosearch:
            datadict['id']=todo.id
            datadict['record_date']=str(todo.record_date)
            datadict['state']=todo.state
            datalist.append(datadict)
        datajson=json.dumps(datalist,ensure_ascii=False)
        print(type(datajson))
        print(datajson)
        return datajson