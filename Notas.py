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


