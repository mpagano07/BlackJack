import random

def generar_mazos(cantidadMazos):
    cartas = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    mazo = cartas * 4

    variosMazo = mazo * cantidadMazos
    return variosMazo

def jugar(variosMazo):

    sumaCartas = 0
    for carta in variosMazo:
        cartaRamdom = random.choice(variosMazo)
        variosMazo.remove(cartaRamdom)
        sumaCartas += cartaRamdom 

        if sumaCartas < 21 :
            pass
        elif sumaCartas >= 21 :
            #print(sumaCartas)
            return sumaCartas
        
def jugar_varios(variosMazo, jugadores):
    totales = []
    for i in range(jugadores):
        totales.append(jugar(variosMazo))
        
    return totales

def ver_quien_gano(totales):
    # resultados = []
    # print(totales)
    for i in totales:
        if i == 21:
            print("gano")
        else:
            print("perdio")

    # resultados.append(i)

ver_quien_gano(jugar_varios(generar_mazos(2),2))

