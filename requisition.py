
# Assessment 2 - Requisition System

class Requisition:
    next_id = 10001

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def add_requisition(self, items):
        self.total = 0

        for item in items:
            self.total += item["cost"]

        return self.total

    
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status

    def manager_response(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "Rejected":
                self.status = "Rejected"

        return self.status
    
# Test the requisition system
req1 = Requisition("19/11/2026", "S001", "Ram")

items = [
    {"cost": 100},
    {"cost": 200}
]

req1.add_requisition(items)
req1.approve_requisition()

print("Requisition ID:", req1.requisition_id)
print("Staff Name:", req1.staff_name)
print("Total:", req1.total)
print("Status:", req1.status)
print("Approval Reference:", req1.approval_reference)



