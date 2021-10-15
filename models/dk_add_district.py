from odoo import api, fields, models<?xml version="1.0"?>
<odoo>
    <data>

        <record id="view_sale_order_add_city" model="ir.ui.view">
            <field name="name">sale.order.add.city.form</field>
            <field name="model">sale.order</field>
            <field name="inherit_id" ref="sale.view_order_form"/>
            <field name="arch" type="xml">
                <xpath expr="//field[@name='partner_id']" position="after">

                                    <field name="country_id" string="Country"/>
                                    <field name="city_id" string="City"
                                           domain="[('country_id', '=', country_id)]"/>
                                    <field name="district_id" string="District"
                                           domain="[('city_id', '=', city_id)]"/>
                                    <field name="name" string="Ward"
                                           domain="[('district_id', '=', district_id)]"/>

                <field name="loai_don_hang" string="Ward"/>
                <field name="name" string="Ward"/>
                <field name="country_id" string="Country"/>
                <field name="city_id" string="City"/>
                <field name="district_id" string="District"/>
                <field name="name" string="Ward"/>
            </field>
        </record>

    </data>
</odoo>


class AddDistrict(models.Model):
    _name = 'dk.add.district'

    code = fields.Char(string='Code', size=11, required=True)
    name = fields.Char(string='Name', size=128, required=True)
    city_id = fields.Many2one('dk.add.city', string='City', required=True)
    country_id = fields.Many2one('res.country', string='Country',
                                 related='city_id.country_id')
