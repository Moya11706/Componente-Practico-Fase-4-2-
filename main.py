from cliente import Cliente
from servicio import ServicioSala
from reserva import Reserva

clientes = []
servicios = []
reservas = []

while True:
    print("\n---MENÚ---")
    print("1. Crear cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Mostrar reservas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        documento = input("Ingrese el documento del cliente: ")
        try:
            cliente = Cliente(nombre, documento)
            clientes.append(cliente)
            print("Cliente creado exitosamente")
        except ValueError as e:
            print("Error:", e)
    elif opcion == "2":
        try:
            horas = int(input("Horas de reserva: "))
            
            servicio = ServicioSala(horas)
            servicios.append(servicio)
            print("Servicio creado exitosamente")
            
        except ValueError as e:
            print("Error:", e)
        
    elif opcion == "3":
        try:
            if not clientes or not servicios:
                print("Debe crear al menos un cliente y un servicio antes de crear una reserva.")
                continue 
            cliente = clientes [-1] #último cliente
            servicio = servicios [-1] #último servicio
            fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
            reserva = Reserva(cliente, servicio, fecha)
            reservas.append(reserva)
            print("Reserva creada exitosamente")
        except ValueError as e:
            print("Error:", e)
    
    elif opcion == "4":
        for r in reservas:
            print("Cliente: ", r.cliente.get_nombre())
            print("Servicio: ", r.servicio.get_nombre())
            print("Fecha: ", r.fecha)
            print("Costo total: ", r.servicio.calcular_costo())
            print("--------------------------------------------")
    
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor seleccione una opción del menú.")
            
             
             



