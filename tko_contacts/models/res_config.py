# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class CRMSettings(models.TransientModel):

    _name = 'contact.config.settings'
    _inherit = 'res.config.settings'

    module_tko_partner_multiple_phones = fields.Boolean("Manage Multiple Phones ?",
                                                        help="Manage multiple partner phones")

    tko_partner_multiple_emails = fields.Boolean("Manage Multiple Emails ?",
                                                        help="Manage multiple partner Emails")
    #
    # @api.multi
    # def execute(self):
    #     to_install = list(self.modules_to_install())
    #     _logger.info('Selecting addons %s to install', to_install)
    #
    #     IrModule = self.env['ir.module.module']
    #     modules = []
    #     for name in to_install:
    #         module = IrModule.search([('name', '=', name)], limit=1)
    #         modules.append((name, module))