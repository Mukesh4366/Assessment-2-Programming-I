
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
            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"

        return self.status

    def display_requisition(self):
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total, sep="")
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

    def requisition_statistics(self, requisitions):
        total = len(requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for req in requisitions:
            if req.status == "Approved":
                approved += 1
            elif req.status == "Pending":
                pending += 1
            elif req.status == "Not approved":
                not_approved += 1

        print("Displaying the Requisition Statistics")
        print("Total requisitions:", total)
        print("Approved requisitions:", approved)
        print("Pending requisitions:", pending)
        print("Not approved requisitions:", not_approved)


# Requisition 1 - Automatically Approved
req1 = Requisition("19/11/2026", "S001", "Ram")
items1 = [{"cost": 100}, {"cost": 200}]
req1.add_requisition(items1)
req1.approve_requisition()

# Requisition 2 - Manager Approved
req2 = Requisition("19/11/2026", "S002", "John")
items2 = [{"cost": 400}, {"cost": 300}]
req2.add_requisition(items2)
req2.approve_requisition()

# Requisition 3 - Manager Not Approved
req3 = Requisition("19/11/2026", "S003", "Sam")
items3 = [{"cost": 350}, {"cost": 250}]
req3.add_requisition(items3)
req3.approve_requisition()

# Requisition 4 - Exactly $500
req4 = Requisition("19/11/2026", "S004", "Alex")
items4 = [{"cost": 300}, {"cost": 200}]
req4.add_requisition(items4)
req4.approve_requisition()

# Requisition 5 - Automatically Approved
req5 = Requisition("19/11/2026", "S005", "Emma")
items5 = [{"cost": 150}, {"cost": 250}]
req5.add_requisition(items5)
req5.approve_requisition()

# Store all five requisitions
requisitions = [req1, req2, req3, req4, req5]

# Display statistics before manager responses
print("--- Initial Statistics ---")
req1.requisition_statistics(requisitions)
print()

# Manager responds to pending requisitions
req2.manager_response("Approved")
req3.manager_response("Not approved")
# req4 remains Pending

# Display all requisitions
print("--- Requisition Details ---")
for req in requisitions:
    req.display_requisition()

# Display final statistics
print("--- Final Statistics ---")
req1.requisition_statistics(requisitions)
