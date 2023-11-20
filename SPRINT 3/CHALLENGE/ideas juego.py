# antes de cada disparo el jugardor tiene la opción de salir
jugar()
posicionar_barco_user()
posicionar_barco_maquina()

while busqueda_barcos_user() and busqueda_barcos_maquina():
    opcion = input("¿Quieres disparar (D) o salir (S)? ").upper()
    if opcion == "D":
        while disparo_user() == "X":
            print("Tocado, te toca de nuevo")
            disparo_user()
            if disparo_user() == " ":
                disparo_maquina()
        while disparo_maquina() == "X":
            disparo_maquina()
            if disparo_maquina() == " ":
                print("Agua, me toca")
                disparo_user()
    elif opcion == "S":
        print("Has decididosalirdeljuego.")
        break
    else:
        print("Opciónno válida.Porfavor,eligeentre'D'(disparar) o'S'(salir).")

if not busqueda_barcos_user() and busqueda_barcos_maquina():
    print("Perdiste")
elif busqueda_barcos_user() and not busqueda_barcos_maquina():
    print("Ganaste")





def disparo_maquina2():
    x,y=np.meshgrid(np.arange(dimension_maquina[0]),np.arange(dimension_maquina[1]))
    coordenadas_maquina=list(zip(x.ravel(),y.ravel()))
    coordenadas_disparo=random.choice(coordenadas_maquina)
    coordenadas_maquina.remove(coordenadas_disparo)

    if niveldificultad=="facil":
        disparos=1
    elif niveldificultad=="medio":
        disparos=2
    elif niveldificultad=="dificil":
        disparos=3
   
    for _ in range(disparos):
        if tablero_user[coordenadas_disparo]=="O" or tablero_user[coordenadas_disparo]=="X":
            tablero_user[coordenadas_disparo]="X"
            print("TOCADO")
            print(tablero_user)
            break
        else:
            tablero_user[coordenadas_disparo]="-"
            print("AGUA")
            print(tablero_user)

# Ejemplo de uso
disparo_maquina()




def jugar():     #inicia el juego, bienvenida y saludo   
    intro=print("Bienvenido a...\n"
                """
  _    _                 _ _         _           __ _       _        
 | |  | |               | (_)       | |         / _| |     | |       
 | |__| |_   _ _ __   __| |_ _ __   | | __ _   | |_| | ___ | |_ __ _ 
 |  __  | | | | '_ \ / _` | | '__|  | |/ _` |  |  _| |/ _ \| __/ _` |
 | |  | | |_| | | | | (_| | | |     | | (_| |  | | | | (_) | || (_| |
 |_|  |_|\__,_|_| |_|\__,_|_|_|     |_|\__,_|  |_| |_|\___/ \__\__,_|
                                                                    
    """)
    user_name=input("¿Cómo te llamas?: ")
    print(f"Hola {user_name} ,vamos a empezar el juego")
    while True:
        niveldificultad=input("Elige un nivel de dificultad (facil, medio, dificil): ").lower()
        if niveldificultad in ["facil", "medio", "dificil"]:
            break
        else:
            print("Opción no válida. Por favor, elige entre 'facil', 'medio' o 'dificil'.")
    return niveldificultad

