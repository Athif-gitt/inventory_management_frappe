# Copyright (c) 2026, Athif Faisal and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ABC(Document):
	def before_save(self):
		print("before save")
