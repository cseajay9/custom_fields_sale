from odoo import models, fields


class SalesTags(models.Model):
    _name = 'sales.tags'

    name = fields.Char(string='Tag Name', required=True)


    
    
    

