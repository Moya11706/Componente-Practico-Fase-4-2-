
# SIMULACIONES DEL SISTEMA
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaTecnica


print("\n========== SIMULACIONES DEL SISTEMA ==========")



# SIMULACIÓN 1
# Registro válido de cliente


print("\n--- SIMULACIÓN 1: CLIENTE VÁLIDO ---")

try:

    cliente1 = Cliente("Juan Pérez", "1023456789")

    print("Cliente registrado correctamente")
    print(cliente1)

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 2
# Registro inválido de cliente


print("\n--- SIMULACIÓN 2: CLIENTE INVÁLIDO ---")

try:

    cliente2 = Cliente("", "12345")

    print(cliente2)

except Exception as e:

    print("Error:", e)


# SIMULACIÓN 3
# Servicio válido


print("\n--- SIMULACIÓN 3: SERVICIO VÁLIDO ---")

try:

    servicio1 = ReservaSala("Sala VIP", 50000, 20)

    print(servicio1.mostrar_info())

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 4
# Servicio inválido


print("\n--- SIMULACIÓN 4: SERVICIO INVÁLIDO ---")

try:

    servicio2 = ReservaSala("Sala Empresarial", -1000, 15)

    print(servicio2.mostrar_info())

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 5
# Reserva exitosa


print("\n--- SIMULACIÓN 5: CÁLCULO EXITOSO ---")

try:

    costo = servicio1.calcular_costo(2)

    print(f"Costo total: ${costo}")

except Exception as e:

    print("Error:", e)


# SIMULACIÓN 6
# Horas inválidas


print("\n--- SIMULACIÓN 6: HORAS INVÁLIDAS ---")

try:

    costo = servicio1.calcular_costo(0)

    print(costo)

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 7
# Alquiler de equipo válido


print("\n--- SIMULACIÓN 7: ALQUILER EQUIPO ---")

try:

    equipo1 = AlquilerEquipo("Computadores", 30000, "Portátiles")

    print(equipo1.mostrar_info())

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 8
# Asesoría técnica válida

print("\n--- SIMULACIÓN 8: ASESORÍA TÉCNICA ---")

try:

    asesoria1 = AsesoriaTecnica("Soporte TI", 40000, "Ingeniero de Sistemas")

    print(asesoria1.mostrar_info())

except Exception as e:

    print("Error:", e)



# SIMULACIÓN 9
# Servicio con nombre vacío

print("\n--- SIMULACIÓN 9: NOMBRE VACÍO ---")

try:

    servicio3 = ReservaSala("", 20000, 10)

    print(servicio3.mostrar_info())

except Exception as e:

    print("Error:", e)


# SIMULACIÓN 10
# Verificar continuidad del sistema


print("\n--- SIMULACIÓN 10: CONTINUIDAD DEL SISTEMA ---")

try:

    servicio4 = ReservaSala("Sala Multimedia", 60000, 30)

    print(servicio4.mostrar_info())

    costo = servicio4.calcular_costo(3)

    print(f"Costo total: ${costo}")

    print("El sistema continúa funcionando correctamente.")

except Exception as e:

    print("Error:", e)


print("\n========== FIN DE LAS SIMULACIONES ==========")
