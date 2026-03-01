#PUNTOS DE VENTAS
print("Bienvenido a RiwiTechStore, es un placer para nosotro servirle :)...")
nombre_cliente = input("Por favor ingrese su nombre y apellido ejem: Aurora Quintero ")
afirmacion = int(input("¿Desear llevar este producto ? Ingrese solo estos numeros  1.SI  2.NO "))

if afirmacion == 1:
    
        while afirmacion == 1:
            nombre_producto = input("Por favor ingrese el nombre del producto  ")
            valor_producto = int(input("Ingrese el valor del producto "))
            total_valor_producto = valor_producto + valor_producto
            print("Nombre del Producto ", nombre_producto," Precio ", valor_producto)
            afirmacion = int(input("¿Desear llevar este producto ? Ingrese solo estos numeros  1.SI  2.NO "))
            
        else:
            cliente_vip = int(input("¿Es cliente VIP? Ingrese opcion valida 1.SI 2.NO "))
            
            
            if cliente_vip == 1:
                descuento_vip = total_valor_producto*0.80
                print("Gracias por su compra", nombre_cliente,
                "El total de su compra es ", descuento_vip)
                
            else:
                print("Gracias por su compra", nombre_cliente,"El total de su compra es ", total_valor_producto)
if afirmacion == 2:
    print("Gracias por su venir", nombre_cliente)

else:
    print("No ha ingresado un numero valido")