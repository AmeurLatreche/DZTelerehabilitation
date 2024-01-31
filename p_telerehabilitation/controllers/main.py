# -*- coding: utf-8 -*-

from odoo.http import Controller, route, request


class MyController(Controller):
    @route('/aa', auth='user')
    def handler(self,**kw):
            User = request.env.user
            return request.render('p_telerehabilitation.sale_details_page', {'my_details': User.name})

    @route('/aa2', auth='user')
    def handler2(self,**kw):
            User = request.env.user
            return request.render('p_telerehabilitation.sale_details_page2', {'my_details': User.name})
