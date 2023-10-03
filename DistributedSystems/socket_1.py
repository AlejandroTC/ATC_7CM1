import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datos_servidor = ("localhost", 4000)
print(sys.stderr, "Empezando a levantar %s puerto %s" % datos_servidor)
s.bind(datos_servidor)
s.listen(1)
while True:
    print(sys.stderr, "Esperando para realizar conexion")
    connection, datos_cliente = s.accept()
    try:
        print(sys.stderr, "conexion desde", datos_cliente)
        while True:
            data = connection.recv(19)
            print(sys.stderr, '"recibido %s"' % data.decode())
            if data:
                print(sys.stderr, "devolviendo mensaje al cliente")
                #data = input().encode()
                connection.sendall(data)
            else:
                print(sys.stderr, "no hay mas datos", datos_cliente)
            break
    finally:
        connection.close()