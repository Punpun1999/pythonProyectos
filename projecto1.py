from Producto import Producto
print ("############################")
print ("####### MINI COBRADOR ######")
print ("############################")
def agregarCarrito(lista,carrito):
        print ('---------------------------')
        nombre= input('Ingrese el nombre del producto ==>').capitalize()
        buscar= [producto1 for producto1 in lista if nombre==producto1.getNombre()]
        print ('---------------------------')
        if len(buscar)!=0:
            cantidad= int(input('Ingrese la cantidad ==> '))
            miCompra= (buscar[0],cantidad)
            carrito.append(miCompra)
        else:
            print ('---------------------------')
            print ('el producto no existe')
            print ('---------------------------')
def quitarCarrito(carrito):
        print ('---------------------------')
        nombre1= input('Ingrese el Nombre del producto que deseas quitar ==>').capitalize()
        buscar= [compra for compra in  carrito if compra[0].getNombre()== nombre1]
        print ('---------------------------')
        if len(buscar)==0:
            print ('---------------------------')
            print ('el producto ya fue removido')
            print ('---------------------------')    
        else:
            carrito.remove(buscar[0])    
def agregar(lista):
        print ('---------------------------')
        Nombreproduc= input ('ingrese el producto ==> ').capitalize()
        Stock= int(input ('ingrese la cantidad de producto ==> '))
        precio= float(input ('ingrese el precio ==> ').replace(',','.'))
        print ('---------------------------')
        producto = Producto(Nombreproduc,Stock,precio)
        buscar= [producto1 for producto1 in lista if producto.getID()==producto1.getID()]
        if len(buscar)!=0:
            print ('---------------------------')
            print ('el producto ya esta en la lista')
            print ('el producto ya tiene precio')
            print ('---------------------------')
        else:
            lista.append(producto)
def quitar(lista):
    print ('---------------------------')
    nombre= input('ingrese el Nombre del producto que desea remover ==> ').capitalize()
    print ('---------------------------')
    buscador= [producto for producto in lista if producto.getNombre()==nombre]
    if len(buscador)==0:
        print ('---------------------------')
        print ('el producto ya fue removido')
        print ('---------------------------')
    else:
        lista.remove(buscador[0])

def total(carrito):
    suma = 0
    print ('---------------------------')
    for compra in carrito:
        print (compra[0].getNombre()+"\n Cantidad: "+str(compra[1]))
        print ('---------------------------')
    for producto,cantidad in carrito:
        producto.setStock (producto.getStock()-cantidad)
        suma+=producto.getPrecio()*cantidad
    carrito.clear()#Vacio el carrito
    print('El total es $',suma)
    print ('---------------------------')

listaProducto=[]
carrito= []
while True:
    print ('---------------------------')
    print ('1.Agregar Producto')
    print ('2.Remover Producto')
    print ('3.Mostrar Los Productos Disponibles')
    print ('4.Añadir al carrito')
    print ('5.Retirar del carrito')
    print ('6.Mostrar Carrito')
    print ('7.cobrar')
    print ('8.Salir')
    print ('---------------------------')
    opcion= input('Ingrese una opcion ==> ').capitalize()
    if (opcion == '1' or opcion == 'Agregar producto'):
        agregar(listaProducto)
    elif (opcion == '2' or opcion == 'remover producto'):
        quitar(listaProducto)
    elif (opcion == '3' or opcion == 'Mostrar los productos disponibles'):
        print ('---------------------------')
        for producto1 in listaProducto:
            print(producto1)
        print ('---------------------------')
    elif (opcion == '4' or opcion == 'Añadir al carrito'):
        agregarCarrito(listaProducto,carrito)
    elif (opcion == '5' or opcion == 'Retirar del carrito'):
        quitarCarrito(carrito)
    elif (opcion == '6' or opcion == 'Mostrar Carrito'):
        print ('---------------------------')
        for compra in carrito:
            print (compra[0].getNombre()+"\nCantidad: "+str(compra[1]))
        print ('---------------------------')
    elif (opcion == '7' or opcion == 'Cobrar'):
        print ('---------------------------')
        total(carrito)
        print ('---------------------------')
    elif (opcion == '8' or opcion == 'Salir'):
        break
    else:
        print('ingrese una opcion valida')