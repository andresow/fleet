# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _name = 'value.by.category'

    categ_id        = fields.Many2one('product.category', ' Categoria de gastos')
    total_value     = fields.Float('Kilometraje final')
