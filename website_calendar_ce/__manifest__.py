# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Website Calendar',
    'version': '1.0',
    'category': 'Marketing/Online Appointment',
    'sequence': 131,
    'summary': 'Schedule bookings with clients',
    'website': 'https://vertel.se/apps/website_calendar_ce',
    'description': """
Allow clients to Schedule Bookings through your Website
-------------------------------------------------------------

""",
    'depends': ['calendar_sms', 'hr'],
    'data': [
        'data/website_calendar_data.xml',
        'views/calendar_views.xml',
        'views/calendar_booking_views.xml',
        'views/website_calendar_templates.xml',
        'security/website_calendar_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'data/website_calendar_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
