# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tutorial(models.Model):
#     _name = 'tutorial.tutorial'
#     _description = 'tutorial.tutorial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import fields, models


class Game(models.Model):
    _name = "tutorial.game"
    _description = "Game model of Tutorial App"

    name = fields.Char("Name", required=True)
    image = fields.Binary("Cover")

    hidden = fields.Boolean("Hidden", default=False, readonly=True)

    released_date = fields.Date()
    publisher_ids = fields.Many2many(
        "res.partner", relation="publisher_rel", string="Publishers"
    )
    developer_ids = fields.Many2many(
        "res.partner", relation="developer_rel", string="Developers"
    )

    def toggle_hidden(self):
        self.ensure_one()
        for game in self:
            game.hidden = False if game.hidden else True
        return True