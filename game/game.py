import random


def jugar():
	usuario = input("Realiza tu seleccion: 'pi para piedra, 'pa' para piedra, 'ti' para tijera.\n").lower()

	computadora = random.choice(['pi', 'pa', 'ti'])

	if(usuario == computadora):
		return '¡Empate!'

	if jugador_gano(usuario, computadora):
		return '¡Ganaste!'

	return '¡Perdiste!'

def jugador_gano(jugador, oponente):
	# retornar true (si gana el jugador)
	#pi > ti
	#ti > pa
	#pa > pi
	if((jugador == 'pi' and oponente == 'ti')
		or (jugador == 'ti' and oponente == 'pa')
		or (jugador == 'pa' and oponente == 'pi')
		):
		return True
	else:
		return False


print(jugar())
