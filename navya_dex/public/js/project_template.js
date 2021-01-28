frappe.ui.form.on('Project Template', {
    setup: function(frm) {
		frm.fields_dict['tasks'].grid.get_field("parent_task").get_query = function(doc, cdt, cdn) {
            var child = locals[cdt][cdn];
            return {
                filters:[
                       ['parent', '=', frm.doc.name],
                       ['name', '!=', child.name],
                       ['is_group', '=', 1]
                    ]
            }
        }
		frm.fields_dict['tasks'].grid.get_field("depends_on_task").get_query = function(doc, cdt, cdn) {
            var child = locals[cdt][cdn];
            return {
                filters:[
                       ['parent', '=', frm.doc.name],
                       ['name', '!=', child.name],
                       ['is_group', '=', 0]
                    ]
            }
        }
	}
});