from odoo import api, fields, models


class AddDistrict(models.Model):
    _name = 'dk.add.district'

    code = fields.Char(string='Code', size=11, required=True)
    name = fields.Char(string='Name', size=128, required=True)
    city_id = fields.Many2one('dk.add.city', string='City', required=True)
    country_id = fields.Many2one('res.country', string='Country')
