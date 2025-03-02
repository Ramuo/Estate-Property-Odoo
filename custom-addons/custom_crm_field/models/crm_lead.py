from odoo import models, fields



class CRMLead(models.Model):
    _inherit = 'crm.lead'


    custom_field = fields.Char(string= "Custom Field")
    complexity_rating = fields.Selection([
        ('0', 'Simple'),
        ('1', '⭐ Medium'),
        ('2', '⭐⭐ Complex'),
        ('3', '⭐⭐⭐ Very Complex')
    ], string="Complexity", default='one', help="Rate the complexity of the lead.")