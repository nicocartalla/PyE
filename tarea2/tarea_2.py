import random

class JuegoDeDados():

        def points(self) -> int:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            if dado1 == 4:
                return dado2
            if dado2 == 4:
                return dado1
            else:
                return 0

        def player_1(self) -> int:    
            points = self.points()
            if points < 4:
                # volver a tirar ya que sacó menos de 4
                return random.randint(1, 6)
            return points
        
        def player_2(self,player1) -> int:
            points = self.points()

            # si es menor a jugador, prefiere volver a tirar
            if points < player1:
                return random.randint(1, 6)
            
            # si es igual a jugador, prefiere volver a tirar siempre y cuando sea menor o igual a 4
            if points == player1 and points <= 4:
                return random.randint(1, 6)
            # Si el puntaje es igual al jugador 1 y es mayor a 4, prefiere empatar
            if points == player1 and points > 4:
                return points
            # de lo contrario el jugador 2 gana
            return points
        
        def play(self) -> list:
            player1 = self.player_1()
            player2 = self.player_2(player1)
            # caso de que gane el jugador 1
            if player1 > player2:
                return [1,0,0]
            # caso de que gane el jugador 2
            if player2 > player1:
                return [0,1,0]
            
            # caso de empate
            return [0,0,1]

def game(iter):
    juego = JuegoDeDados()
    result = [0,0,0]
    for i in range(iter):
        result = [result[i] + juego.play()[i] for i in range(3)]

    # calculo de probabilidad que el jugador 1 gane
    prob_j1 = result[0]/iter
    # calculo de probabilidad que el jugador 2 gane
    prob_j2 = result[1]/iter
    # calculo de probabilidad que el resultado sea empate
    prob_empate = result[2]/iter
    print(f"-------------------------{iter}-------------------------------")
    print(f"Resultado de iterar {iter} veces")
    print("Juan|Maria|Empate")
    print(f"{result[0]}|{result[1]}|{result[2]}")
    print("--------------------")
    print("Estadisticas")
    print(f"Probabilidad de que Juan (jugador 1) gane: {prob_j1}")
    print(f"Probabilidad de que María (jugador 2) gane: {prob_j2}")
    print(f"Probabilidad de que el resultado sea empate: {prob_empate}")

if __name__ == '__main__':
    game(1000)
    game(10000)
    game(100000)
    