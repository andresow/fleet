# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class RouteTravelState(models.Model):
    _name = 'route.travel.state'
    _description = 'Etapa del viaje'

    name = fields.Char('Nombre de la etapa')
