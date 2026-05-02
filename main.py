from cliente import Cliente
from servicio import ServicioSala
from reserva import Reserva

cliente1 = Cliente("Juan Pérez", "123456789") #cliente ejemplo

servicio1 = ServicioSala(2) #servicio ejemplo 2 horas

reserva1 = Reserva(cliente1, servicio1, "2026-05-01")
print("----RESERVA INICIAL----")
reserva1.mostrar_reserva() #muestra datos iniciales

print("\n----CONFIRMAR RESERVA----")
reserva1.confirmar() #confirma la reserva
reserva1.mostrar_reserva() 

print("\n----CANCELAR RESERVA----")
reserva1.cancelar() #cancela la reserva
reserva1.mostrar_reserva()


