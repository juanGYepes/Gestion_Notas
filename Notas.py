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


