# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def add_employee_in_task(doc, method):
    if doc.project:
        query = """elect tptt.employee, tptt.employee_name from `tabProject Template Task` as tptt
            inner join `tabProject Template` as tpt on tpt.name = tptt.parent
            inner join `tabProject` as tp on tp.project_template = tpt.name
            where tp.name = '{0}' limit 1""".format(doc.project)
        reslt = frappe.db.sql(query,as_dict=True)
        if reslt:
            doc.employee = reslt[0].employee
            doc.employee_name = reslt[0].employee_name
            doc.db_update()