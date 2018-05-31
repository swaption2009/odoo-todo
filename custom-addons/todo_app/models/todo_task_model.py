from odoo import models, fields

class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.partner', string='Responsibility', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')