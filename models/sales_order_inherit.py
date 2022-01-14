from odoo import models, fields


class SalesOrderInherit(models.Model):
    _inherit ='sale.order'

    tag_ids = fields.Many2many('sales.tags',  string='Tags')
