from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva, registrar_evento

clientes = []
servicios = []
reservas = []

while True:
    print("\n====== SISTEMA DE RESERVAS ======")
    print("1. Crear cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Mostrar reservas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    # -------------------------
    # CREAR CLIENTE
    # -------------------------
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        documento = input("Ingrese el documento del cliente: ")
        try:
            cliente = Cliente(nombre, documento)
            clientes.append(cliente)
            registrar_evento(f"Cliente creado: {nombre}")
            print("✅ Cliente creado exitosamente")
        except ValueError as e:
            print("❌ Error:", e)

    # -------------------------
    # CREAR SERVICIO
    # -------------------------
    elif opcion == "2":
        try:
            nombre = input("Nombre del servicio: ")
            precio = float(input("Precio por hora: "))
            capacidad = int(input("Capacidad de la sala (número de personas): "))
            
            servicio = ReservaSala(nombre, precio, capacidad)
            servicios.append(servicio)
            registrar_evento(f"Servicio creado: {nombre}")
            print("✅ Servicio creado exitosamente")
            
        except ValueError as e:
            print("❌ Error:", e)

    # -------------------------
    # CREAR RESERVA
    # -------------------------
    elif opcion == "3":
        try:
            if not clientes or not servicios:
                print("⚠️ Debe crear al menos un cliente y un servicio primero.")
                continue 

            # 🔹 Seleccionar cliente
            print("\n--- CLIENTES DISPONIBLES ---")
            for i, c in enumerate(clientes, 1):
                print(f"{i}. {c.get_nombre()}")

            op_cliente = int(input("Seleccione un cliente: "))
            if op_cliente < 1 or op_cliente > len(clientes):
                print("❌ Opción inválida")
                continue

            cliente = clientes[op_cliente - 1]

            # 🔹 Seleccionar servicio
            print("\n--- SERVICIOS DISPONIBLES ---")
            for i, s in enumerate(servicios, 1):
                try:
                    print(f"{i}. {s} | {s.describir()}")
                except:
                    print(f"{i}. {s}")

            op_servicio = int(input("Seleccione un servicio: "))
            if op_servicio < 1 or op_servicio > len(servicios):
                print("❌ Opción inválida")
                continue

            servicio = servicios[op_servicio - 1]

            # 🔹 Datos de reserva
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

            horas = float(input("Ingrese horas del servicio: "))
            if horas <= 0:
                print("❌ Las horas deben ser mayores a 0")
                continue

            descuento = float(input("Ingrese descuento (% opcional, 0 si no aplica): "))
            if descuento < 0 or descuento > 100:
                print("❌ Descuento inválido (0 a 100)")
                continue

            # 🔹 Confirmación
            confirmar = input("¿Confirmar reserva? (s/n): ").lower()
            if confirmar != "s":
                print("⚠️ Reserva cancelada por el usuario")
                continue

            # 🔹 Crear reserva
            reserva = Reserva(cliente, servicio, fecha)
            reserva.horas = horas
            reserva.descuento = descuento

            reservas.append(reserva)

            registrar_evento(f"Reserva creada: {cliente.get_nombre()} - {horas}h - {fecha}")
            print("✅ Reserva creada exitosamente")

        except ValueError as e:
            print("❌ Error:", e)

    # -------------------------
    # MOSTRAR RESERVAS
    # -------------------------
    elif opcion == "4":
        if not reservas:
            print("⚠️ No hay reservas registradas.")
        else:
            print("\n====== LISTA DE RESERVAS ======")
            print(f"Total reservas: {len(reservas)}")

            for i, r in enumerate(reservas, 1):
                print(f"\n📌 Reserva #{i}")
                print("Cliente:", r.cliente.get_nombre())
                print("Servicio:", r.servicio)
                print("Fecha:", r.fecha)
                print("Horas:", getattr(r, "horas", "No definido"))

                try:
                    horas = getattr(r, "horas", 1)
                    descuento = getattr(r, "descuento", 0)

                    costo = r.servicio.calcular_costo(horas, descuento=descuento)

                    print(f"💰 Costo con descuento: {costo}")

                    # 🔥 Impuesto (simulación)
                    impuesto = costo * 0.19
                    total = costo + impuesto

                    print(f"💸 Costo con impuesto (19%): {round(total, 2)}")

                except Exception as e:
                    print("❌ Error al calcular costo:", e)

                print("----------------------------------")

    # -------------------------
    # SALIR
    # -------------------------
    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción no válida")
            
             
             



