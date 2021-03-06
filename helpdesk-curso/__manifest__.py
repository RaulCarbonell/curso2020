# Copyright 2020 Raul Carbonell - raul.carbonell@processcontrol.es
# License AGPL-3.0 or later
{
    "name": "HelpDesk Curso",
    "summary":
        "Module to Support Teams",
    "version": "13.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Raul Carbonell",
    "license": "AGPL-3",
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "wizard/helpdesk_set_responsable_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_stage_views.xml",
        "views/helpdesk_team_views.xml",
        "views/res_users_views.xml",
    ],
    "depends": [
        "base",
        "mail",
    ],
    "application": True,
    "installable": True,
}
