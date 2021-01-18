from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from six import iteritems
from email_reply_parser import EmailReplyParser
from frappe.utils import (flt, getdate, get_url, now,
	nowtime, get_time, today, get_datetime, add_days)

class DuplicationError(frappe.ValidationError): pass
from erpnext.projects.doctype.project.project import Project

class CustomProject(Project):
    def copy_from_template(self):
        '''
        Copy tasks from template
        '''
        if self.project_template and not frappe.db.get_all('Task', dict(project=self.name), limit=1):

            # has a template, and no loaded tasks, so lets create
            if not self.expected_start_date:
                # project starts today
                self.expected_start_date = today()

            template = frappe.get_doc('Project Template', self.project_template)

            if not self.project_type:
                self.project_type = template.project_type

            # create tasks from template
            for task in template.tasks:
                frappe.get_doc(dict(
                    doctype='Task',
                    subject=task.subject,
                    project=self.name,
                    status='Open',
                    parent_task=task.parent_task,
                    exp_start_date=add_days(self.expected_start_date, task.start),
                    exp_end_date=add_days(self.expected_start_date, task.start + task.duration),
                    description=task.description,
                    task_weight=task.task_weight
                )).insert()

