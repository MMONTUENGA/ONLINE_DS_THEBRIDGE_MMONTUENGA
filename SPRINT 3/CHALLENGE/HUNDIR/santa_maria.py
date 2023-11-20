#CONSTANTES

Class Tablero

self.id=
self.dimensiones=
self.barcos={
    "barco1":2,
    "barco2":2,
    "barco3":3
}

tablero_user=Tablero()
tablero_maquina=Tablero()




#FUNCIONES

def iniciar_tablero_user(): 
def iniciar_tablero_maquina(): #tablero invisible donde se indican los disparos del usuario y se ve si ha dado al barco (X) o agua(" ")

def posicionar_barco_user(): #funcion que posiciona aleatoriamente los barcos indicados en la clase barco
def posicionar_barco_maquina():

def disparo_user(): #pide 2 coordenadas al usuario y ejecuta el disparo en el tablero maquina indicando si barco o agua
def disparo_maquina(): #elige 2 coordenadas al azar y las ejecuta sobre el tablero usuario indicando si barco o agua y guárdandolas para no volver a usarlas

def busqueda_barcos_user(): #busca si hay barcos(X) en el tablero de usuario
def busqueda_barcos_maquina(): #busca si hay barcos(X) en el tablero de maquina

def jugar(): #da la bienvenida e instrucciones y crea los 2 tableros
introduccion=print("Bienvenido a Hundir la Flota")
nombre_user=input("Introduce tu nombre:")
iniciar_tablero_user()
iniciar_tablero_maquina()


return introduccion,tablero_user


#MAIN

jugar()
posicionar_barco_user()
posicionar_barco_maquina()
busqueda_barcos_user()
busqueda_barcos_maquina()

while busqueda_barcos_user==True and busqueda_barcos_maquina==True:

    while disparo_user()=="X":
        print("Tocado, te toca de nuevo")
        disparo_user()

        if disparo_user()==" ":
            disparo_maquina()

    while disparo_maquina()=="X":
        disparo_maquina()

        if disparo_maquina()==" ":
            print("Agua, me toca")
            disparo_user()


if busqueda_barcos_user==False and busqueda_barcos_maquina==True:
    print("Perdiste")

elif busqueda_barcos_user==True and busqueda_barcos_maquina==False:
    print("Ganaste")