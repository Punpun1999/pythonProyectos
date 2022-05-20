class Producto:
    #Atributos:
    #self.__sgtID
    #self.__nombre
    #self.__stock
    #self.__precio
    id = 0

    def __init__(self,nombre,stock,precio):#Contructor
        self.__sgtID = self.__class__.id
        self.__nombre = nombre
        self.__stock = stock
        self.__precio = precio
        self.__class__.id += 1

    def getNombre(self):
        return self.__nombre
    
    def getStock(self):
        return self.__stock

    def getPrecio(self):
        return self.__precio

    def setPrecio(self,nuevoPrecio):
        self.__precio = nuevoPrecio

    def setStock(self,nuevoStock):
        self.__stock = nuevoStock
    def getID(self):
        return self.__sgtID

    def __str__(self):
        return "ID: "+str(self.__sgtID)+"\nNombre: "+self.__nombre+"\nStock: "+str(self.__stock)+"\nPrecio: "+str(self.__precio)