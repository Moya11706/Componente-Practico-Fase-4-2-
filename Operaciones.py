
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaTecnica

print("\n========== SIMULACIONES ==========")

# SIMULACIÓN 1
try:
    cliente1 = Cliente(
        "Juan Pérez",
        "juan@gmail.com",
        "1023456789"
    )

    print("\nSIMULACIÓN 1 EXITOSA")
    print(cliente1)

except Exception as e:
    print("Error:", e)


# SIMULACIÓN 2
try:
    cliente2 = Cliente(
        "",
        "correo@gmail.com",
        "12345"
    )

except Exception as e:
    print("\nSIMULACIÓN 2 FALLIDA")
    print("Error:", e)


# SIMULACIÓN 3
try:
    servicio1 = ReservaSala(
        "Sala VIP",
        50000,
        20
    )

    print("\nSIMULACIÓN 3 EXITOSA")
    print(servicio1.describir())

except Exception as e:
    print("Error:", e)


# SIMULACIÓN 4
try:
    servicio2 = ReservaSala(
        "Sala Empresarial",
        -1000,
        10
    )

except Exception as e:
    print("\nSIMULACIÓN 4 FALLIDA")
    print("Error:", e)


# SIMULACIÓN 5
try:
    costo = servicio1.calcular_costo(2)

    print("\nSIMULACIÓN 5 EXITOSA")
    print("Costo:", costo)

except Exception as e:
    print("Error:", e)


# SIMULACIÓN 6
try:
    costo = servicio1.calcular_costo(0)

except Exception as e:
    print("\nSIMULACIÓN 6 FALLIDA")
    print("Error:", e)


# SIMULACIÓN 7
try:
    equipo = AlquilerEquipo(
        "Computadores",
        30000,
        5
    )

    print("\nSIMULACIÓN 7 EXITOSA")
    print(equipo.describir())

except Exception as e:
    print("Error:", e)


# SIMULACIÓN 8
try:
    asesoria = AsesoriaTecnica(
        "Soporte TI",
        40000,
        "Ingeniero Carlos"
    )

    print("\nSIMULACIÓN 8 EXITOSA")
    print(asesoria.describir())

except Exception as e:
    print("Error:", e)


# SIMULACIÓN 9
try:
    servicio3 = ReservaSala(
        "",
        20000,
        15
    )

except Exception as e:
    print("\nSIMULACIÓN 9 FALLIDA")
    print("Error:", e)


# SIMULACIÓN 10
try:
    servicio4 = ReservaSala(
        "Sala Multimedia",
        60000,
        30
    )

    total = servicio4.calcular_costo(3)

    print("\nSIMULACIÓN 10 EXITOSA")
    print(servicio4.describir())
    print("Total:", total)

except Exception as e:
    print("Error:", e)

print("\n========== FIN ==========")
