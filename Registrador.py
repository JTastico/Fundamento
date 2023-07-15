from prueba import agregar, eliminar, buscar, mostrar, terminos
# Menú principal
while True:
    print("\n-- MANTENIMIENTO DE CLIENTES ---")
    print("1 - Agregar cliente")
    print("2 - Buscar cliente por RUC")
    print("3 - Mostrar todos los clientes")
    print("4 - Eliminar cliente")
    print("5 - Salir")
    print("6 - Terminos")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        mostrar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Hasta luego")
        break
    elif opcion == "6":
        terminos()
    else:
        print("Opción inválida. Intente nuevamente.")
