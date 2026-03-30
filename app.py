from servicios import register_new_students, Check_the_student_list, Search_for_a_student_by_some_criterion, Update_a_student_is_information, Delete_student

def menu():
    continuar = True

    while continuar:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Register new students")
        print("2. Check the student list")
        print("3. Search for a student by some criterion (name)")
        print("4. Update a student's information")
        print("5. Delete student")
        print("6. Go out")
        
        try:
            opcion = int(input("Select an option: "))
        except ValueError:
            print("You must enter a number.")
            continue
        
        if opcion == 1:
            register_new_students()
        elif opcion == 2:
            Check_the_student_list()
        elif opcion == 3:
            Search_for_a_student_by_some_criterion()
        elif opcion == 4:
            Update_a_student_is_information()
        elif opcion == 5:
            Delete_student()
        elif opcion == 6:
            print("Leaving the program...")
            continuar = False
        else:
            print("Invalid option. Please try again.")    
            
menu()