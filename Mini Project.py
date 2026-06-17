students = {}

while True :

    print("\n 1. Add student")
    print("2. View students")
    print("3. Exits")

    choice = input("Enter choice :")

    if choice == "1" :
        name = input("Enter name :")
        marks = int(input("Enter marks :"))
        students[name] = marks

    elif choice == "2" :
        print(students)

    elif choice == "3" :
        break

    else :
        print("Invalid choice")
