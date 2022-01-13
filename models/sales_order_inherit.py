from odoo import models, fields


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'
    _name = 'sales.order.inherit'

    tags = fields.Char(string='Tag')
