from  odoo import http
from odoo.http import request


class PropertyController(http.Controller):

    @http.route(['/properties'], type='http', website=True, auth="public")
    def show_properties(self):
        propery_ids = request.env['estate.property'].sudo().search([])
        print(propery_ids)
        return request.render("real_estate_ads.property_list", {"property_ids": propery_ids})