<<<<<<< HEAD
# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpDeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "HelpDesk Team"

    name = fields.Char(string="name" )
    ticket_ids = fields.One2many(
        string="Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="team_id",
    )

    user_ids = fields.One2many(
        string="Users",
        comodel_name="res.users",
        inverse_name="team_id",
    )
=======
# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpDeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "HelpDesk Team"

    name = fields.Char(string="name" )
    ticket_ids = fields.One2many(
        string="Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="team_id",
    )

    user_ids = fields.One2many(
        string="Users",
        comodel_name="res.users",
        inverse_name="team_id",
    )
>>>>>>> 48929ae6924474d487592eea31356d6d8a12d3ea
