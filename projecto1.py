print ("############################")
print ("####### MINI COBRADOR ######")
print ("############################")
lista=[]
precio=[]
suma=0
while True:
        print ("1.añadir producto")
        print ("2.quitar producto")
        print ("3.mostrar lista")
        print ("4.total")
        print ("5.salir")
        print('############################')
        opcion= input ("")
        if opcion == "1" or opcion == "añadir producto":
            print ('############################')
            nombre= input ("ingrese el producto: ").capitalize()
            cantidadP= input ("ingrese la cantidad: ")
            precio= input ("ingrese el precio del producto= ")
            producto= (nombre,cantidadP,precio)
            print ('############################')
            busca=[producto for producto in lista if producto[0]==nombre]
            if len(busca)!=0:
                print ('############################')
                print("el producto ya esta en la lista ")
                print('el producto ya tiene precio')
                print ('############################')
            else:
                lista.append(producto)
        elif opcion == "2" or opcion == "quitar producto":
            print ('############################')
            nombre1= input("Ingrese el producto que desea quitar: ").capitalize()
            print ('############################')
            busca=[producto for producto in lista if producto[0]==nombre1]
            if len(busca)==0:
                print ('############################')
                print("este producto no esta en la lista")
                print ('############################')
            else:
                lista.remove(busca[0])
        elif opcion == "3" or opcion == "mostrar lista": 
            print ('############################')       
            print (lista)
            print ('############################')
        elif opcion =="4" or opcion == "total":
            print ('############################')
            for producto in lista:
                precio=producto[2].replace(',','.')
                suma+=float(precio)*int(producto[1])
            print(suma)
            print ('############################')
        elif opcion == "5" or opcion == "salir":
            break
        else:
            print ('ingrese una opcion valida')
"""
productos=['televisor-Samsung42','celular-iphoneX','Microfono-Noganet ']
productos.append(input("ingrese un producto = "))
for x in productos:
    print (x)

productos.remove(input("ingrese el producto que quiera eliminar = "))
for x in productos:
    print (x)
carrito=[]
while carrito==0:
    carrito.append(input ("ingrese el producto que desea comprar = "))
    for i in carrito:
        print (i)
"""