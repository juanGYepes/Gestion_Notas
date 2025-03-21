#Listas
users = [] 
grades = []  

def user_register():
    print("\n--- Registro ---")
    user = input("Ingrese nombre de usuario: ")
    type = input("Ingrese tipo (profesor/estudiante): ")
    password = input("Ingrese contraseña: ")
    users.append({"usuario": user, "tipo": type, "contrasena": password})
    print("Usuario registrado con éxito.\n")

user_register()

#Funcion login
def login():
    print("\n--- Login ---")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    for u in users:
        if u["usuario"] == user and u["contrasena"] == password:
            print("Login exitoso\n")
            return u
    print("Usuario o contraseña incorrectos.\n")
    return None

#funcion de agregar notas
def add_note():
    print("\n--- Agregar Nota ---")
    student = input("Ingrese nombre del estudiante: ")
    subject = input("Ingrese la materia: ")
    note = float(input("Ingrese la nota: "))
    grades.append({"estudiante": student, "materia": subject, "nota": note})
    print("Nota agregada con éxito.\n")

#funcion para ver las notas
def check_note():
    print("\n--- Ver Notas ---")
    student = input("Ingrese su nombre para ver sus notas: ")
    found = [n for n in grades if n["estudiante"] == student]
    if found:
        for n in found:
            print(f"Materia: {n['materia']}, Nota: {n['nota']}")
    else:
        print("No se encontraron notas.\n")

#Funcion del menu
def menu(usuario):
    while True:
        print("\n--- Menú ---")
        print("1. Ver Notas")
        if usuario["tipo"] == "profesor":
            print("2. Agregar Nota")
        print("3. Cerrar Sesión")
        option = input("Seleccione una opción: ")
        match  option:
            case "1":
                check_note()
            case "2":
                if usuario["tipo"] == "profesor":
                    add_note()
            case "3":
                print("Cerrando sesión...\n")
                break
            case _:
                print("Opción inválida.\n")




