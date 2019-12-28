# -*- coding: utf-8 -*-
# Made in Busissnesys. Author: JO Carrizoza

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    car_brand = fields.Many2one('car.brands', string=_('Car Brand'))
    car_model = fields.Many2one('car.models', string=_('Car Model'))
    car_color = fields.Many2one('car.colors', string=_('Car Color'))
    car_year  = fields.Integer(string=_('Car Year'))
    car_plates = fields.Char(string=_('Car Plates'), size=30, help="the plates of my car")
    

    @api.onchange('car_brand')
    def check_change(self):
        model_list = []
        if self.car_brand:
            for model in self.car_brand.models_ids:
                model_list.append(model.id)
            return {
                'domain': { 'car_model': [('id', 'in', model_list)]}
            }
