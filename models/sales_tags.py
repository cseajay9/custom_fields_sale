from odoo import models, fields


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    tag_name = fields.Char(string='Tag')


class SalesTags(models.Model):
    _name = 'sales.tags'

    tag_name = fields.Char(string='Tag', required=True)
