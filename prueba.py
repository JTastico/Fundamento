#lista vacia
clientes = {}


#Definir una funcion para agregar un cliente y RUC
def agregar():
    empresa = input("Ingrese nombre del cliente: ")
    ruc = input("Ingrese RUC: ")
    clientes[ruc] = empresa
    print("Cliente agregado con éxito.")

    # Guardar el cliente en un archivo de texto
    with open("clientes.txt", "a") as archivo:
        archivo.write(f"Empresa: {empresa}\n")
        archivo.write(f"RUC: {ruc}\n")
        archivo.write("\n")
        print("Datos del cliente guardados en el archivo. clientes.txt")


# Definir una función para buscar un cliente por RUC
def buscar():
    for cliente in clientes:
        ruc = input("Ingrese el ruc del cliente a buscar: ")
        if ruc in clientes:
            print("\nLa empresa -->", clientes[ruc])
            print("RUC --------->", ruc, "\n")


# Definir una función para mostrar todos los clientes
def mostrar():
    for empresa, ruc in clientes.items():
        print("RUC -----  EMPRESA")
        print(empresa, "-", ruc)

# Definir una funcion para eliminar un cliente
def eliminar():
    ruc = input("Ingrese el RUC deel cliente que quiere eliminar: ")
    if ruc in clientes:
        del clientes[ruc]
        print("Eliminado con exito")

def terminos():
    print("\nPara poder mantener un registro\n"
          "de las empresas con las cuales\n"
          "se ha trabajado, se mantendran\n"
          "registrados tanto el nombre como\n"
          "el RUC de la misma, para asi poder\n"
          "tener un historial completo de los\n"
          "clientes, estos registros no podran\n"
          "ser borrados para asi mantener nuestra\n"
          "integridad y veracidad\n"
          "Una vez cerrado el programa no se\n"
          "podran visualizar las empresas registradas\n"
          "por lo cual si quieren ver el registro completo\n"
          "tendran que hacer la revicion desde el archivo\n"
          "                     clientes.txt\n")