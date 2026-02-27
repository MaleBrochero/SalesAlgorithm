# PUNTOS DE VENTAS
print("Bienvenido a RiwiTechStore, es un placer para nosotro servirle :)...")
nombre_cliente = input("Por favor ingrese su nombre y apellido ejem: Aurora Quintero")


afirmacion = int(input("¿Desear llevar este producto ? Ingrese solo estos numeros  1.SI  2.NO"))

if afirmacion == 1:

        while True:
            nombre_producto = input("Por favor ingrese el nombre del producto ")
            valor_producto = int("Ingrese el valor del producto ")
            print("Nombre del Producto ", nombre_producto," Precio ", valor_producto)
        else:
            total_valor_producto = valor_producto + valor_producto
            Cliente_VIP = int(input("¿Es cliente VIP? Ingrese opcion valida 1.SI 2.NO "))
            print("Gracias por su compra", Nombre_Cliente,
                "El total de su compra es ", total_valor_producto)

elif afirmacion == 2:
    print("Gracias por su venir", nombre_cliente)
else:
    print("No ha ingresado un numero valido")