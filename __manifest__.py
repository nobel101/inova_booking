# -*- coding: utf-8 -*-
{
    'name': "Inova Booking System",

    'summary': """
        To allow users to create bookings for employees and equipments """,

    'description': """
        this module is a testing module for Inova company for booking system 
    """,

    'author': "OMAR KHALID ALI",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'hr','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_team.xml',
        'views/equipments.xml',
        'views/booking_order.xml',
        'views/delivery_order.xml',
        'data/sequence.xml',


    ],

}
