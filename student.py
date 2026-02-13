students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"}
]

search_id = int(input("\nEnter student ID to search: "))

found = False
for student in students:
    if student["id"] == search_id:
        print("Student Name:", student["name"])
        found = True
        break

if not found:
    print("Student not found")