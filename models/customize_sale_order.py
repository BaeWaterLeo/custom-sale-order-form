from odoo import api, fields, models
from datetime import datetime, timedelta

class CustomizeSalOrder(models.Model):
    _inherit = 'sale.order'

    loai_don_hang = fields.Selection([
        ('Bình thường', 'Hàng bình thường'),
        ('Dễ vỡ', 'Hàng dễ vỡ'),
        ('Mai thúy', 'Hàng cấm')
    ], string='Loại đơn hàng', default='Bình thường')
    dia_chi = fields.Char('Địa chỉ', size=400)
    district_id = fields.Many2one('dk.add.district', string='District', required=True)
    city_id = fields.Many2one('dk.add.city', string='City')
    country_id = fields.Many2one('res.country', string='Country')

    expiry_date = fields.Date(string="Quotation Expiry Day")
    state = fields.Selection(selection_add=[('expired', 'Quotation expired')])

    def cancel_old_sales_order(self, force_limit: None):
        limit = 2
        if force_limit:
            limit = force_limit
        date_today = datetime.today()
        cancel_date = date_today - timedelta(days=limit)
        old_order = self.env['sale.order'].search(
            [('date_order', '<', cancel_date), ('state', 'in', ['draft', 'sent'])])
        old_order.action_cancel()
