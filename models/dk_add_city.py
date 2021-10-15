from odoo import api, fields, models


class AddCity(models.Model):
    _name = 'dk.add.city'

    code = fields.Char(string='Code', size=4, required=True)
    name = fields.Char(string='Code', size=100, required=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)
    district_id = fields.One2many('dk.add.district', 'city_id', string='District')
