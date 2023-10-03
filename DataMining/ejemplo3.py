cubo_de_datos = {
    '2023': {
        'Nueva York': {
            'Televisor' : 5000,
            'Telefono' : 3000,
        },
        'San Francisco' : {
            'Televisor' : 4000,
            'Telefono' : 3500,
        },
    },
    '2022' : {
        'Nueva York': {
            'Televisor' : 4500,
            'Telefono' : 2900,
        },
        'San Francisco' : {
            'Televisor' : 3900,
            'Telefono' : 3400,
        },
    }
}

#Funcion para aniadir datos al cubo
def add_datos(tiempo, ubicacion, producto, ventas):
    if tiempo not in cubo_de_datos:
        cubo_de_datos[tiempo] = {}
    if ubicacion not in cubo_de_datos[tiempo]:
        cubo_de_datos[tiempo][ubicacion] = {}
    cubo_de_datos[tiempo][ubicacion][producto] = ventas

#Funcion para consultar el cubo de datos
def consultar_ventas(tiempo, ubicacion, producto):
    try:
        return cubo_de_datos[tiempo][ubicacion][producto]
    except KeyError:
        return "Informacion no disponible"

#permitir al usuario aniadir datos
tiempo = input("Ingrese el anio (por ejemplo, 2023): ")
ubicacion = input("Ingrese la ubicacion (por ejemplo, Nueva York)")
producto = input("Ingrese el tipo de producto (por ejemplo, Televisor)")
ventas = int(input("Ingrese la cantidad total de ventas: "))

add_datos(tiempo, ubicacion, producto, ventas)

#Permitir al usuario hacer una consulta
tiempo_consulta = input("ingrese el anio que desea consultar: ")
ubicacion_consulta = input("Ingese la ubicacion que desea consultar: ")
producto_consulta = input("Ingrese el tipo de producto que desea consultar: ")

print("Ventas totales: ", consultar_ventas(tiempo_consulta, ubicacion_consulta, producto_consulta))

