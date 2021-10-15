from odoo import api, fields, models


class CustomizeSalOrder(models.Model):
    _inherit = 'sale.order'

    loai_don_hang = fields.Selection([
        ('Bình thường', 'Hàng bình thường'),
        ('Dễ vỡ', 'Hàng dễ vỡ'),
        ('Mai thúy', 'Hàng cấm')
    ], string='Loại đơn hàng', default='Bình thường')
    dia_chi = fields.Char('Địa chỉ', size=400)
    district_id = fields.Many2one('dk.add.district', string='District', required=True)
    city_id = fields.Many2one('dk.add.city', string='City',
                              related='district_id.city_id')
    country_id = fields.Many2one('res.country', string='Country',
                                 related='district_id.country_id')
