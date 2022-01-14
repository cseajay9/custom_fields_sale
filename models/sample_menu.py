from odoo import fields, models


class SampleMenu(models.Model):
    _name = 'sample.menu'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='description')
    tagname_ids = fields.Many2many('sales.tags', string='Tags')
    