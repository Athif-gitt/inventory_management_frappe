# Copyright (c) 2026, Athif Faisal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class InventoryAlert(Document):
	def before_insert(self):
		print("before_insert") 

	def validate(self):
		if self.minimum_qty < 0:
			frappe.throw("Minimum Qty cannot be negative")
			
		

		
