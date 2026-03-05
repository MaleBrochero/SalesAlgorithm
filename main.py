#PUNTOS DE VENTAS


print("Bienvenido a RiwiTechStore, es un placer para nosotro servirle :)...")
nombre_cliente = input("Por favor ingrese su nombre y apellido ejem: Aurora Quintero ")
nombre_producto = input("Por favor ingrese el nombre del producto  ")

try:

    valor_producto = int(input("Ingrese el valor del producto en numeros "))
    cantidad_producto = int(input("Ingrese  cantidad del producto en unidades : Ejempo  1, 2, 3, ... "))
    cliente_vip = int(input("¿Es cliente VIP? Ingrese opcion valida 1.SI 2.NO "))
    valor_total = valor_producto*cantidad_producto
    
    if cliente_vip == 1:
        valor_final_pagar = valor_total *0.9
        valor_descuento = valor_total *0.1
        print("El cliente ",nombre_cliente, "su descuento es ", valor_descuento , "precio total a pagar ", valor_final_pagar)
        
    elif cliente_vip == 2:
        print ("El cliente ",nombre_cliente,  "precio total a pagar ",valor_total)
    else :
        print("No ingreso un valor valido")
        
        
except :
    print("Caracter invalido")
