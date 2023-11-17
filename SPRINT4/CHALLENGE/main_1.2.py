import numpy as np
import random
import time

'''Creo tablero de la máquina con sus barcos posicionados'''

tablero_maquina = np.full((10,10), fill_value= ' ') 
def crear_barcos_maquina():
    #Barcos eslora 1
    tablero_maquina[0, 0] = 'O'
    tablero_maquina[1, 2] = 'O'
    tablero_maquina[0, 9] = 'O'
    tablero_maquina[9, 9] = 'O'
    #Barcos eslora 2
    tablero_maquina[4,2:4] ='O'
    tablero_maquina[3:5,9] ='O'
    tablero_maquina[8:10,1] ='O'
    #Barcos eslora 3
    tablero_maquina[1:5,6] ='O' 
    tablero_maquina[6,6:9] ='O'
    #Barco eslora 4
    tablero_maquina[2:6,0] ='O'
    return tablero_maquina

crear_barcos_maquina()

'''Creo el tablero del usuario con sus barcos posicionados'''

inicar_tablero_user = np.full((10,10), fill_value = ' ')
def crear_barcos_usuario():
    #Barcos eslora 1
    inicar_tablero_user[1, 0] = 'O'
    inicar_tablero_user[9, 0] = 'O'
    inicar_tablero_user[0, 9] = 'O'
    inicar_tablero_user[9, 9] = 'O'
    #Barcos eslora 2
    inicar_tablero_user[3:5,0] ='O'
    inicar_tablero_user[1,3:5] ='O'
    inicar_tablero_user[3:5,6] ='O'
    #Barcos eslora 3
    inicar_tablero_user[7,0:3] ='O' 
    inicar_tablero_user[9,2:5] ='O'
    #Barco eslora 4
    inicar_tablero_user[6,4:8] ='O'
    return inicar_tablero_user

crear_barcos_usuario()

''' Creo un tablero invisible, donde se indicarán los disparos del usuario, y donde podremos ver si ha
dada a barco (X) o agua (A)'''

tablero_maquina_invisible = np.full((10,10), fill_value=' ')
tablero_maquina_invisible

'''Creo funcion de disparo del usuario que funciona con un input donde nos tendrá que dar primer la coordenada
x y luego la coordenada y'''

def disparos_user():
    coord_x = int(input("JUGADOR, INSERTE COORDENADA X:"))
    coord_y =int(input("JUGADOR, INSERTE COORDENADA Y:"))
    disparo = [coord_x,coord_y]
    print(disparo)

    if tablero_maquina[coord_x,coord_y] == ' ':
        tablero_maquina[coord_x,coord_y] = 'A'
        tablero_maquina_invisible[coord_x,coord_y] ='A'
        print(tablero_maquina_invisible)
        print("Agua",disparo)

    elif tablero_maquina[coord_x,coord_y] =='X':
        print("Coordenadas repetidas, elija nuevas coordenadas", disparo)  ## Aviso que has repetido coordenadas
        
    elif tablero_maquina[coord_x,coord_y] == 'A':
        print("Coordenadas reptidas, elija nuevas coordenadas", disparo)  ## Aviso que has repetido coordenadas


    elif tablero_maquina[coord_x,coord_y] == 'O':
        tablero_maquina[coord_x,coord_y] = 'X'
        tablero_maquina_invisible[coord_x,coord_y] = 'X'
        print(tablero_maquina_invisible)
        print("Barco",disparo)
    
    return tablero_maquina[coord_x,coord_y]

''' Creo lista de todas las coordenadas posibles, para luego poder utilizar random choice en los disparos 
random de la máquina'''

lista_coordenadas_maquina = [(0, 0), (0, 1), (0, 2), (0, 3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
        (1, 0), (1, 1), (1, 2), (1, 3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
        (2, 0), (2, 1), (2, 2), (2, 3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
        (3, 0), (3, 1), (3, 2), (3, 3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
        (4, 0), (4, 1), (4, 2), (4, 3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
        (5, 0), (5, 1), (5, 2), (5, 3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
        (6, 0), (6, 1), (6, 2), (6, 3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
        (7, 0), (7, 1), (7, 2), (7, 3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
        (8, 0), (8, 1), (8, 2), (8, 3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
        (9, 0), (9, 1), (9, 2), (9, 3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9),]

''' Creo función para los disparos de la máquina que funcionan a través de un random.choice'''

def disparos_maquina():
    coordenadas_maquina = random.choice(lista_coordenadas_maquina)
    lista_coordenadas_maquina.remove(coordenadas_maquina)
    #print(coordenadas_maquina)
    #print(lista_coordenadas_maquina)


    if inicar_tablero_user[coordenadas_maquina] == ' ':
        inicar_tablero_user[coordenadas_maquina] = 'A'
        print(inicar_tablero_user)
    

    elif inicar_tablero_user[coordenadas_maquina] == 'O':
        inicar_tablero_user[coordenadas_maquina] = 'X'
        print(inicar_tablero_user)
    
    return inicar_tablero_user[coordenadas_maquina]

''' Creo la función jugar, donde se inicia la bienvenida, el input para que se pueda introducir el nombre de 
usuario, se inicia tabler usuario y tablero máquina invisible'''

def jugar():
    introduccion = print("Bienvenido al juego hundir la flota")
    nombre_user = print(input("Indroduzca su nombre: "))    
    inicar_tablero_user
    tablero_maquina_invisible
    

    return introduccion, nombre_user, "Tablero usuario", inicar_tablero_user, "Disparos", tablero_maquina_invisible


      

''' Creo 2 variables, una para buscar si hay barcos en el tablero máquina y otra para lo mismo pero en tablero
usuario'''
busqueda_barcos_maquina = any('O' in sub for sub in tablero_maquina)
busqueda_barcos_usuario = any('O' in sub for sub in inicar_tablero_user)



''' AQUI INICIA EL JUEGO'''
jugar()
crear_barcos_maquina()
print(crear_barcos_usuario())
print(tablero_maquina_invisible)

juego = True
jugador = True
maquina = False
vidas_user = 20
vidas_maquina = 20


# while juego:
    
#     while jugador:
#         if disparos_user() == 'A':
#             jugador = False
#             maquina = True
#             print("Has fallado, turno de la máquina", disparos_maquina())
            
        
#         elif disparos_user() == 'X':
#             vidas_maquina = vidas_maquina - 1
#             print("Has dado barco, sigue disparando", disparos_user())
            
#     while maquina:
#         if disparos_maquina() == 'A':
#             maquina = False
#             jugador = True
#             print("La máquina ha fallado, te toca", disparos_user())
                

#         elif disparos_maquina() == 'X':
#             vidas_user = vidas_user -1
#             print("Te han dado", disparos_maquina())

# if vidas_user == 0:
#     print("Has perdido")

# elif vidas_maquina == 0:
#     print("Has ganado")

#----------------------------------------------------------------
while juego:
    
    if vidas_maquina == 0 or vidas_user == 0:
        break

    elif jugador:
        disparo = disparos_user()
        if disparo == 'A':
            jugador = False
            maquina = True
            print("Has fallado, turno de la máquina")
        else:
            vidas_maquina = vidas_maquina - 1
            print("Has dado barco, sigue disparando")        
            
    elif maquina:
        disparo = disparos_maquina()
        if disparo == 'A':
            maquina = False
            jugador = True
            print("La máquina ha fallado, te toca")
        else:
            vidas_user = vidas_user - 1
            print("La máquina sigue disparando")

if vidas_user == 0:
    print("Has perdido")

elif vidas_maquina == 0:
    print("Has ganado")