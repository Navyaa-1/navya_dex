from __future__ import unicode_literals
import frappe
from frappe.utils import today, add_days
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
                parent_task = None
                depends_task = None
                if task.parent_task:
                    pro_temp_task = frappe.get_doc("Project Template Task", task.parent_task)
                    if pro_temp_task:
                        pro_temp_task_sub = frappe.get_list("Task", filters={'subject': pro_temp_task.subject}, fields= 'name', order_by= 'creation desc',limit= 1)
                        if pro_temp_task_sub:
                            parent_task = pro_temp_task_sub[0]['name']
                if task.depends_on_task:
                    pro_temp_task = frappe.get_doc("Project Template Task", task.depends_on_task)
                    if pro_temp_task:
                        pro_temp_task_dep = frappe.get_list("Task", filters={'subject': pro_temp_task.subject},
                                                            fields='name', order_by='creation desc', limit=1)
                        if pro_temp_task_dep:
                            depends_on_task = pro_temp_task_dep[0]['name']
                            depends_task = [dict(task= depends_on_task)]
                task_id = frappe.get_doc(dict(
                    doctype='Task',
                    subject=task.subject,
                    project=self.name,
                    status='Open',
                    parent_task=parent_task,
                    exp_start_date=add_days(self.expected_start_date, task.start),
                    exp_end_date=add_days(self.expected_start_date, task.start + task.duration),
                    expected_time=task.expected_duration_time,
                    description=task.description,
                    task_weight=task.task_weight,
                    employee=task.employee,
                    employee_name=task.employee_name,
                    is_group=task.is_group,
                    depends_on=depends_task
                )).insert(ignore_mandatory=True)




