# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _

def add_employee_in_task(doc, method):
    if doc.project:
        query = """select tptt.employee, tptt.employee_name from `tabProject Template Task` as tptt
            inner join `tabProject Template` as tpt on tpt.name = tptt.parent
            inner join `tabProject` as tp on tp.project_template = tpt.name
            where tp.name = '{0}' and subject = '{1}' limit 1""".format(doc.project,doc.subject)
        reslt = frappe.db.sql(query,as_dict=True)
        if reslt:
            doc.employee = reslt[0].employee
            doc.employee_name = reslt[0].employee_name
            doc.db_update()

def validate_working_status(doc, method):
    if doc.get("__islocal"):
        if doc.status in ["Working", "Completed"]:
            if doc.depends_on:
                for d_task in doc.depends_on:
                    d_task_doc = frappe.get_doc("Task", d_task.task)
                    if d_task_doc.status != "Completed":
                        frappe.throw(_("Please Complete first Dependent Tasks!"))

        if doc.employee and doc.status == "Working":
            task_list = frappe.db.sql("""select name from `tabTask` where status = 'Working' and employee = %s""", (doc.employee), as_dict=True)
            if task_list:
                frappe.throw(_("Only One task allow for WorKing at a time!"))
    else:
        if doc.status in ["Working", "Completed"]:
            if doc.depends_on:
                for d_task in doc.depends_on:
                    d_task_doc = frappe.get_doc("Task", d_task.task)
                    if d_task_doc.status != "Completed":
                        frappe.throw(_("Please Complete first Dependent Tasks!"))
        if doc.employee and doc.status == "Working":
            task_list = frappe.db.sql("""select name from `tabTask` where status = 'Working' and employee = %s and name != %s""", (doc.employee,doc.name), as_dict=True)
            if task_list:
                frappe.throw(_("Only One task allow for WorKing at a time!"))
