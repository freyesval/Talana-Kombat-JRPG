
# El programa debe recibir un json en el cual, existen dos jugadores
# Cada jugador puede moverse para la izquierda (A), derecha (D), arriba (W) o abajo (S). 
# Además de dar golpes (P) o patadas (K)


# Inicio de la partida:
# Parte el jugador que envía al inicio una combinación menor de movimientos y patadas
# Si hay empate, parte el que tenga menos movimientos
# Si hay empate de movimientos, inicia el que tenga menos golpes
# En caso de empate de golpes, parte el jugador 1

# Restricciones / Limitaciones:
#
# Cada personaje inicia con 6 Puntos de vida
# Un personaje muere si sus Puntos de vida llegan a 0
# Tony SIEMPRE ataca hacia la derecha
# Arnaldor SIEMPRE ataca hacia la izquierda
# Los jugadores juegan por turnos (1 a la vez)
# Los golpes no pueden ser bloqueados (son efectivos)

# Restricciones / Limitaciones archivo .json
# 
# Los movimientos pueden ser string de largo máximo 5 (puede ser Vacío)   -> "AWSDS", "", "A"
# Los golpes son de máximo largo 1 (puede ser Vacío)     -> "K", "P", ""

# Lista de Combinaciones de ataque:

# Para Tony
    # MOVIMIENTO    PTOS DE VIDA      NOMBRE DE ATAQUE
    #  DSD + P            3              Taladoken
    #   SD + K            2              Remuyuken
    #   P o K             1            Puño o Patada
    
# Para Arnaldor
    # MOVIMIENTO    PTOS DE VIDA      NOMBRE DE ATAQUE
    #   SA +K            3              Remuyuken
    #  ASA + P           2              Taladoken
    #   P o K            1            Puño o Patada
    
    
# Ejemplos de archivo json:
gameplay = {
    "player1":
    {
        "movimientos":["D","DSD","S","DSD","SD"],
        "golpes":["K","P","","K","P"]
    },
    "player2": 
    {
        "movimientos":["SA","SA","SA","ASA","SA"],
        "golpes":["K","","K","P","P"]
    }
} 

# Se pueden realizar movimientos y combinación de ataques especiales (un DSDSD + P -> Taladoken o SDDSD + K -> Remuyuken por ejemplo)
import re
import time
def validate_special_attacks(string, words):
    regex = f'({words})$'
    if re.search(regex, string):
        return True
    else:
        return False


def validate_special_attacks_player1(string):
    special_attacks = ["DSDP", "SDK","P","K"]
    j = 3
    for i in range(len(special_attacks)):
        regex = f'({special_attacks[i]})$'
        if re.search(regex,string):
            break
        else: 
            j-=1
    return j


def validate_special_attacks_player2(string):
    special_attacks = ["SAK", "ASAP","P","K"]
    j = 3
    for i in range(len(special_attacks)):
        regex = f'({special_attacks[i]})$'
        if re.search(regex,string):
            break
        else: 
            j-=1
    return j


def starting_player(player1, player2):
    # Parte el jugador que envía al inicio una combinación menor de movimientos y patadas
    # Si hay empate, parte el que tenga menos movimientos
    # Si hay empate de movimientos, inicia el que tenga menos golpes
    # En caso de empate de golpes, parte el jugador 1
    movimiento_golpe_p1 = player1["movimientos"][0] + player1["golpes"][1]
    movimiento_golpe_p2 = player2["movimientos"][0] + player2["golpes"][1]
    
    if len(movimiento_golpe_p1) < len(movimiento_golpe_p2):
        return "player1"
    elif len(movimiento_golpe_p2) < len(movimiento_golpe_p1):
        return "player2"
    elif len(player1["movimientos"][0]) < len(player2["movimientos"][0]):
        return "player1"
    elif len(player2["movimientos"][0]) < len(player1["movimientos"][0]):
        return "player2"
    elif len(player1["golpes"][1]) < len(player2["golpes"][1]):
        return "player1"
    elif len(player2["golpes"][1]) < len(player1["golpes"][1]):
        return "player2"
    else:
        return "player1"
        

def concatenate_mov_golpes(player):
    movimientos = player["movimientos"]
    golpes = player["golpes"]
    return [a + b for a,b in zip(movimientos, golpes)]


def attack(player_name, attack_type, player, jugadas_1, jugadas_2, turno):
    if attack_type == 3 and player == "player1":
        print(f"{player_name} ha lanzado un Taladoken!")
        return 3
    elif attack_type == 3 and player == "player2":
        print(f"{player_name} ha lanzado un Remuyuken!")
        return 3
    elif attack_type == 2 and player == "player1":
        print(f"{player_name} ha lanzado un Remuyuken!")
        return 2
    elif attack_type == 2 and player == "player2":
        print(f"{player_name} ha lanzado un Taladoken!")
        return 2
    elif attack_type == 1 and player == "player1":
        print(f"{player_name} ha lanzado un puñetazo")
        return 1
    elif attack_type == 1 and player == "player2":
        print(f"{player_name} ha lanzado un puñetazo!")
        return 1
    elif attack_type == 0 and player == "player1":
        print(f"{player_name} ha lanzado una patada")
        return 1
    elif attack_type == 0 and player == "player2":
        print(f"{player_name} ha lanzado una patada!")
        return 1
    elif attack_type == -1:
        largo = len(jugadas_1[turno]) if player == "player1" else len(jugadas_2[turno])
        if largo == 0:
            print(f"{player_name} se ha quedado quieto!")
        else:
            print(f"{player_name} se ha movido")


def gameplay(gameplay):
    player1_hp = 6
    player2_hp = 6
    
    start_player = starting_player(gameplay["player1"], gameplay["player2"])
    second_player = "player1" if start_player == "player2" else "player2"
    turno = 0 # Turno
    
    jugadas_1 = concatenate_mov_golpes(gameplay[start_player])
    jugadas_2 = concatenate_mov_golpes(gameplay[second_player])
    nombre1 = "Tony" if start_player == "player1" else "Arnaldor"
    nombre2 = "Arnaldor" if second_player == "player2" else "Tony"
    print("Empieza la partida!")
    time.sleep(0.1)
    while(player1_hp >=0 or player2_hp >=0):
        tipo_ataque = validate_special_attacks_player1(jugadas_1[turno]) if start_player == "player1" else validate_special_attacks_player2(jugadas_2[turno])
        
        
        
        if tipo_ataque == 3 and start_player == "player1":
            print(f"{nombre1} ha lanzado un Taladoken!")
            player2_hp-=3
        elif tipo_ataque == 3 and start_player == "player2":
            print(f"{nombre1} ha lanzado un Remuyuken!")
            player2_hp-=3
        elif tipo_ataque == 2 and start_player == "player1":
            print(f"{nombre1} ha lanzado un Remuyuken!")
            player2_hp-=2
        elif tipo_ataque == 2 and start_player == "player2":
            print(f"{nombre1} ha lanzado un Taladoken!")
            player2_hp-=2
        elif tipo_ataque == 1 and start_player == "player1":
            print(f"{nombre1} ha lanzado un puñetazo")
            player2_hp-=1
        elif tipo_ataque == 1 and start_player == "player2":
            print(f"{nombre1} ha lanzado un puñetazo!")
            player2_hp-=1
        elif tipo_ataque == 0 and start_player == "player1":
            print(f"{nombre1} ha lanzado una patada")
            player2_hp-=1
        elif tipo_ataque == 0 and start_player == "player2":
            print(f"{nombre1} ha lanzado una patada!")
            player2_hp-=1
        elif tipo_ataque == -1:
            largo = len(jugadas_1[turno]) if start_player == "player1" else len(jugadas_2[turno])
            if largo == 0:
                print(f"{nombre1} se ha quedado quieto!")
            else:
                print(f"{nombre1} se ha movido")
        time.sleep(0.1)
        tipo_ataque = validate_special_attacks_player1(jugadas_1[turno]) if second_player == "player1" else validate_special_attacks_player2(jugadas_2[turno])
        if tipo_ataque == 3 and start_player == "player1":
            print(f"{nombre1} ha lanzado un Taladoken!")
            player1_hp-=3
        elif tipo_ataque == 3 and start_player == "player2":
            print(f"{nombre1} ha lanzado un Remuyuken!")
            player1_hp-=3
        elif tipo_ataque == 2 and start_player == "player1":
            print(f"{nombre1} ha lanzado un Remuyuken!")
            player1_hp-=2
        elif tipo_ataque == 2 and start_player == "player2":
            print(f"{nombre1} ha lanzado un Taladoken!")
            player1_hp-=2
        elif tipo_ataque == 1 and start_player == "player1":
            print(f"{nombre1} ha lanzado un puñetazo")
            player1_hp-=1
        elif tipo_ataque == 1 and start_player == "player2":
            print(f"{nombre1} ha lanzado un puñetazo!")
            player1_hp-=1
        elif tipo_ataque == 0 and start_player == "player1":
            print(f"{nombre1} ha lanzado una patada")
            player1_hp-=1
        elif tipo_ataque == 0 and start_player == "player2":
            print(f"{nombre1} ha lanzado una patada!")
            player1_hp-=1
        elif tipo_ataque == -1:
            largo = len(jugadas_1[turno]) if start_player == "player1" else len(jugadas_2[turno])
            if largo == 0:
                print(f"{nombre1} se ha quedado quieto!")
            else:
                print(f"{nombre1} se ha movido")
        
        turno+=1
    
    if player1_hp <=0:
        print(f"{nombre1} ha sido derrotado!")
    else:
        print(f"{nombre2} ha sido derrotado!")
        
    print('Fin del juego')
        