# Copyright 2018-20 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl

{
    'name': 'MIS Reports - Netherlands - RGS Accounting (3.5.2)',
    'version': '3.1',
    'category': 'Accounting/Localizations/Account Charts',
    'author': 'Onestein',
    'website': 'http://www.onestein.eu',
    'depends': [
        'l10n_nl_rgs',
        'mis_builder'
    ],
    "data": [
        "data/mis_report_styles.xml",
        "data/mis_report_balance_sheet.xml",
        "data/mis_report_profit_loss.xml",
    ],
    "installable": True,
}