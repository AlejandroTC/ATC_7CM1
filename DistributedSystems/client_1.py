import socket #Biblioteca para hacer uso de los sockets en el sistema
import sys  #Biblioteca para actualizar y usar componentes exclusivos del sistema

#se instancia un nuevo socket, que usara la faminila AF_inet que posee los protocolos y direcciones necesarias
# asi como el tipo de socket, siendo en este caso un SOCK_STEAM o TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
# Se declaran los datos del servior, en este caso son el host y el puerto a conectarse
datos_servidor = ("localhost", 4000)
# Se imprime para saber los datos y el proceso que esta ejecutando el script
print(sys.stderr, "Empezando a levantar %s puerto %s" % datos_servidor)
# Se conecta al servidor usando los datos 
s.connect(datos_servidor)

try:
    mensaje = "Aqui va el mensaje".encode()
    print(sys.stderr, 'enviando "%s"' % mensaje.decode())
    s.sendall(mensaje)
    cantidad_recibida = 0
    cantidad_esperada = len(mensaje)
    while cantidad_recibida < cantidad_esperada:
        data = s.recv(19)
        cantidad_recibida += len(data)
    print(sys.stderr, 'recibiendo "%s' % data.decode())
finally:
    print(sys.stderr, "cerrando socket")
    s.close()