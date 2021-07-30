from odoo import fields, models, api


class BookingOrder(models.Model):
    _inherit = 'sale.order'

    is_booking = fields.Boolean()
    employee_team_id = fields.Many2one('employee.team', string='team')
    team_leader = fields.Many2one('hr.employee', string='Team Leader', related='employee_team_id.team_leader')
    employee_ids = fields.One2many('hr.employee', 'sale_order_id', string='Employees',
                                   related='employee_team_id.employee_ids')
    equipment_ids = fields.One2many('product.template', 'sale_order_id', related='employee_team_id.equipments_ids')
    book_start = fields.Datetime(default=fields.Datetime.now, string='Start booking Date')
    book_end = fields.Datetime(string='End booking Date')

    # TODO : method action_check to insure that the team leader is an employee and the equipments has no overlapping with other bookings
    # TODO: override checking method to add other condition


class EmployeeTeam(models.Model):
    _name = 'employee.team'
    _description = 'holding order lines which every order has'

    name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one('hr.employee', string='Team Leader')
    employee_ids = fields.One2many('hr.employee', 'team_id', string='Team Employees')
    equipments_ids = fields.One2many('product.template', 'team_id', string='Equipments',
                                     domain=[('is_equipment', '=', True)])


class HrEmployeeEx(models.Model):
    _inherit = 'hr.employee'

    team_id = fields.Many2one('employee.team')
    sale_order_id = fields.Many2one('sale.order')


class ProductTemplateEx(models.Model):
    _inherit = 'product.template'

    is_equipment = fields.Boolean()
    calender_id = fields.Many2one('calendar.event')
    team_id = fields.Many2one('employee.team', string='Team')
    sale_order_id = fields.Many2one('sale.order')


class CalenderEventEx(models.Model):
    _inherit = 'calendar.event'

    equipment_ids = fields.One2many('product.template', 'calender_id', domain=[('is_equipment', '=', True)])
    equipment_duration = fields.Float('Equipment Duration', compute='_compute_duration', store=True, readonly=False)

    @api.depends('stop', 'start')
    def _compute_duration(self):
        for event in self.with_context(dont_notify=True):
            event.duration = self._get_duration(event.start, event.stop)

class DeliveryOrderExt(models.Model):
    _inherit = 'stock.picking'

    is_booking = fields.Boolean()