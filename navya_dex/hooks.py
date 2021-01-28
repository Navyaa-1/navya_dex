# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "navya_dex"
app_title = "Navya Dex"
app_publisher = "Dexciss"
app_description = "Navya custom app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@dexciss.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/navya_dex/css/navya_dex.css"
# app_include_js = "/assets/navya_dex/js/navya_dex.js"

# include js, css files in header of web template
# web_include_css = "/assets/navya_dex/css/navya_dex.css"
# web_include_js = "/assets/navya_dex/js/navya_dex.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "navya_dex/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Project Template": "public/js/project_template.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "navya_dex.install.before_install"
# after_install = "navya_dex.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "navya_dex.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Task": {
		"validate": "navya_dex.navya_dex_custom.validate_working_status",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"navya_dex.tasks.all"
# 	],
# 	"daily": [
# 		"navya_dex.tasks.daily"
# 	],
# 	"hourly": [
# 		"navya_dex.tasks.hourly"
# 	],
# 	"weekly": [
# 		"navya_dex.tasks.weekly"
# 	]
# 	"monthly": [
# 		"navya_dex.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "navya_dex.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "navya_dex.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "navya_dex.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

override_doctype_class = {
	"Project": "navya_dex.navya_dex.project.CustomProject"
}
