students={}
while True:
    print("1. Add student")
    print("2. Update student")
    print("3. Remove student")
    print("4. View all students")
    print("5. Search student")
    print("6. Total students")
    print("7. Exit")
    choice=input("enter your choice")
    if choice=='1':
        roll_no=input("enter roll_no:")
        name=input("enter name:")
        students[roll_no]=name
        print("student added")
    elif choice=='2':
        roll_no=input("enter the roll no to be updated")
        if roll_no in students:
            name=input("enter new name")
            students[roll_no]=name
            print("student updated")
        else:
            print("student not found")
    elif choice=='3':
        roll_no=input("enter the roll no to be removed")
        if roll_no in students:
            students.pop(roll_no)
            print("student removed")
        else:
            print("student not found")
    elif choice=='4':
        print(students.items())
    elif choice=='5':
        roll_no=input("enter the roll no to search")
        if roll_no in students:
            print(f"name={students[roll_no]}")
        else:
            print("no student found")
    elif choice == '6':
        print("Total students:", len(students))
        
    elif choice == '7':
        print("Exiting")
        break    
    else:
        print("Invalid choice. Please enter 1–7.")
        