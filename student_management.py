students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        students.append({
            "name": name,
            "roll": roll,
            "marks": marks
        })

        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List")
        for student in students:
            print("Name:", student["name"])
            print("Roll No:", student["roll"])
            print("Marks:", student["marks"])
            print("----------------")

    elif choice == "3":
        search = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"].lower() == search.lower():
                print("Name:", student["name"])
                print("Roll No:", student["roll"])
                print("Marks:", student["marks"])
                found = True

        if not found:
            print("Student not found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
