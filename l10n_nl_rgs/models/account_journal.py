# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 Onestein (<http://www.onestein.eu>).

from odoo.exceptions import ValidationError
from odoo import api, fields, models, _


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _prepare_liquidity_account_vals(self, company, code, vals):
        account_vals = super()._prepare_liquidity_account_vals(company, code, vals)

        if company.account_fiscal_country_id.code == 'NL':
            account_vals.setdefault('tag_ids', [])
            account_vals['tag_ids'].append((4, self.env.ref('l10n_nl_rgs.account_tag_1003000').id))

        return account_vals

    @api.model
    def _fill_missing_values(self, vals):
        chart_template = self.env.company.chart_template_id
        is_rgs = chart_template == self.env.ref('l10n_nl_rgs.l10nnl_rgs_chart_template')
        is_bank = vals.get('type') == "bank"
        if not vals.get("default_account_id") and is_bank and is_rgs:
            raise ValidationError(_("Bank Account is required."))
        return super()._fill_missing_values(vals)
