# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class RouteFleet(models.Model):
    _name = 'route.fleet'
    _description = 'Viaje'

    departure_travel    = fields.Datetime('Hora y fecha de salida')
    return_travel       = fields.Datetime('Hora y fecha de salida')
    origen              = fields.Many2one('res.country.state', 'Ciudad de origen')
    destination         = fields.Many2one('res.country.state', 'Ciudad de destino')
    folio_route         = fields.Integer('Folio')
    description         = fields.Text('Descripción')
    loaded              = fields.Boolean('Cargado de salida')
    route_type          = fields.Selection(selection=[('local','Local'),('foraneo','Foraneo')],string='Tipo de ruta',default='local')
    initial_km          = fields.Float('Kilometraje inicial')
    final_km            = fields.Float('Kilometraje final')
    weight              = fields.Integer('Peso ida')
    fleet_id            = fields.Many2one('fleet.vehicle', 'Vehiculo')
    sale_id             = fields.Many2one('sale.order', 'Venta')
    #Campos relacionados a la flota

    driver_id           = fields.Many2one('res.partner', 'Nombre del empleado',related='fleet_id.driver_id') 
    number_employee     = fields.Integer('Numero del empleado',related='fleet_id.id') 

    #Campos relacionados a la venta

    #cfdi_bill           = fields.Integer('res.partner', 'Nombre del empleado',related='fleet_id.driver_id') 
    amount_total        = fields.Monetary('Monto total',related='sale_id.amount_total') 
    amount_tax          = fields.Monetary('Impuestos',related='sale_id.amount_tax') 
    currency_id         = fields.Many2one('res.currency','Moneda',related='sale_id.currency_id') 
    note_sale           = fields.Html('Notas de la venta', related='sale_id.note')



    
    @api.onchange('fleet_id')
    def _onchange_fleet(self):

        if self.fleet_id.odometer:
            self.initial_km = self.fleet_id.odometer

