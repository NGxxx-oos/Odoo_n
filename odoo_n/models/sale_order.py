import random
import string
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    responsible_delivery_id = fields.Many2one(
        'hr.employee', 
        string='Ответственный за выдачу товара', 
        required=True
    )
    
    new_field = fields.Char(
        string='New Field',
        default=lambda self: self._get_default_new_field()
    )

    @api.model
    def _get_default_new_field(self):
        return ''.join(random.choices(string.ascii_letters, k=10))

    @api.onchange('order_line', 'date_order')
    def _onchange_order_line_or_date(self):
        if self.date_order:
            formatted_date = fields.Datetime.to_string(self.date_order)
            # Приводим к формату ДД/ММ/ГГГГ ЧЧ:ММ:СС
            dt = fields.Datetime.from_string(formatted_date)
            formatted_date = dt.strftime('%d/%m/%Y %H:%M:%S')
            self.new_field = f"{formatted_date} + {self.amount_total:.2f}"

    @api.constrains('new_field')
    def _check_new_field_length(self):
        for record in self:
            if record.new_field and len(record.new_field) > 30:
                raise ValidationError(_("Длина текста должна быть меньше 30 символов!"))
