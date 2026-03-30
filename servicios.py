lista = []

def request_identifier():
    continuar = True
    while continuar:
        try:
            identificador = int(input("Please enter your ID: "))
            if identificador < 0:
                print("The price cannot be negative.")
            else:
                return identificador
        except ValueError:
            print("Invalid entry, please enter a valid number.")
            
def ask_age():
    continuar = True
    while continuar:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("The amount cannot be negative.")
            else:
                return age
        except ValueError:
            print("Invalid entry. Please enter a whole number.")
            
def ask_name():
    name = input("Please enter your name: ")
    return name
def ask_curse():
    curse = input("Please enter your course or program: ")
    return curse
def ask_state():
    state = input("Please enter your status (Activate or inactivate): ")
    return state


def register_new_students():
    identi = request_identifier()
    name = ask_name()
    age = ask_age()
    curse = ask_curse()
    state = ask_state()
    
    student = {
        "identi": identi,
        "name": name,
        "age": age,
        "curse": curse,
        "state": state
    }    
    
    lista.append(student)
    
    print(f"ID: {identi} | Name: {name} | Age: {age} | Curse: {curse} | State: {state}")
    
    
def Check_the_student_list():
    if not lista:
        print("It's empty")
        return
    
    for student in lista:
        print(f"ID: {student["identi"]} | Name: {student["name"]} | Age: {student["age"]} | Curse: {student["curse"]} | State: {student["state"]}")
        
def Search_for_a_student_by_some_criterion():
    name = input("Please enter the name or criteria to search for: ")
    for student in lista:
        if student["name"].lower() == name.lower():
                print(f"Found: {student}")
                return
    
def Update_a_student_is_information():
    name = input("Please enter the name or criteria you wish to update: ")
    for student in lista:
        if student["name"].lower() == name.lower():
            new_name = input("Please enter your new name or criteria: ")
            if new_name != "":
                student["name"] = new_name
            student["indeti"] = request_identifier()
            student["age"] = ask_age()
            student["curse"] = ask_curse()
            student["state"] = ask_state()
            print("Updated")
            return
        print("It was not found.")
        
def Delete_student():
    name = input("Please enter the name or criterion you wish to delete: ")
    for student in lista:
        if student["name"].lower() == name.lower():
            lista.remove(student)
            print(f"student {name} Deleted, no longer found.")
            return
    print("It was not found to update.")
