import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cliente import Cliente
from servicio import *
from reserva import Reserva
from excepciones import *
import datetime


def guardar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


lista_reservas = []


# OPERACIÓN 1
try:
    cliente1 = Cliente("Paula", "paula@gmail.com", "300111111")
    guardar_log("Cliente Paula registrado")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 2
try:
    cliente2 = Cliente("", "correo", "123")
except Exception as e:
    print(e)
    guardar_log(str(e))


# OPERACIÓN 3
try:
    servicio1 = ReservaSala("Sala VIP", 100000, 3)
    guardar_log("Servicio Sala VIP creado")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 4
try:
    servicio2 = AlquilerEquipo("Computadores", 50000, 2)
    guardar_log("Servicio de equipos creado")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 5
try:
    servicio3 = AsesoriaTecnica("Asesoría Python", 120000, "Experto Python")
    guardar_log("Servicio de asesoría creado")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 6
try:
    reserva1 = Reserva(cliente1, servicio1, datetime.date.today(), horas=3)
    reserva1.confirmar()
    lista_reservas.append(reserva1)
    guardar_log("Reserva 1 confirmada")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 7
try:
    reserva2 = Reserva(cliente1, servicio2, datetime.date.today(), horas=2)
    lista_reservas.append(reserva2)
    guardar_log("Reserva 2 creada")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 8
try:
    reserva3 = Reserva(cliente1, servicio3, datetime.date.today(), horas=-1)
except Exception as e:
    print(e)
    guardar_log(str(e))


# OPERACIÓN 9
try:
    total = reserva1.procesar_pago(0.19)
    print("Total a pagar:", total)
    guardar_log("Pago procesado")
except Exception as e:
    guardar_log(str(e))


# OPERACIÓN 10
try:
    reserva2.cancelar()
    guardar_log("Reserva cancelada")
except Exception as e:
    guardar_log(str(e))


print("\nLISTA DE RESERVAS")

for reserva in lista_reservas:
    reserva.mostrar_reserva()
