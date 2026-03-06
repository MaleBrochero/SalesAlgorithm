#PUNTOS DE VENTAS

#To init the program, you must ejecute py main.py...
print("Bienvenido a RiwiTechStore, es un placer para nosotro servirle :)...")
nombre_cliente = input("Por favor ingrese su nombre y apellido ejem: Aurora Quintero ")
nombre_producto = input("Por favor ingrese el nombre del producto  ")

try:
    cantidad_producto = int(input("Ingrese  cantidad del producto en unidades : Ejempo  1, 2, 3, ... "))
    valor_producto = int(input("Ingrese el valor del producto en numeros "))
    cliente_vip = int(input("¿Es cliente VIP? Ingrese opcion valida 1.SI 2.NO "))
    valor_total = valor_producto*cantidad_producto
    
    if cliente_vip == 1:
        valor_final_pagar = valor_total *0.9
        valor_descuento = valor_total *0.1
        print (f"""El cliente {nombre_cliente}
            Compró {nombre_producto } 
            Cantidad en unidades {cantidad_producto} 
            precio total  {valor_total} Descuento 10% {valor_descuento}
            Nuevo total a pagar  {valor_final_pagar}
            Gracias por su compra :) """)
        
    elif cliente_vip == 2:
        print (f"""El cliente {nombre_cliente} 
                Compró {nombre_producto } 
                Cantidad en unidades {cantidad_producto} 
                precio total a pagar {valor_total}
                Gracias por su compra :)""")
    else :
        print("No ingreso un valor valido")
        
        
except :
    print("Caracter invalido")
