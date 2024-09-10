# ----- ALL MESSAGES IN THE GAME -----

import fontcolor as fc
import time


def rules():
    import os
    os.system('clear')

    print('''
\033[;95m     21 Batons\033[;m | \033[;92mMarlene Softwares\033[;m | \033[;91mYannick HEUDE (Ayckinn)\033[;m  
\033[;93m ayckinn@pm.me\033[;m | \033[;96mhttps://github.com/AyckinnLisa\033[;m | Version 1.0
          
          
 [Command/Windows + clic gauche] sur le lien de "Github" pour 
 visiter ma page.\n
''')
    
    print(fc.magenta_font(" +") + fc.magenta_font("-" * 59) + fc.magenta_font("+"))
    print(fc.magenta_font(" |"), end="")
    print(fc.yellow_font(" REGLES DU JEU :") + (' ' * 43) + fc.magenta_font("|"))
    print(fc.magenta_font(" |") + " " * 58 + fc.magenta_font(" |"))
    print(fc.magenta_font(" |"), end="")
    print((' ' * 5) + fc.blue_font("01. Le pateau de jeu contient 21 bâtons") + (' ' * 15) + fc.magenta_font("|"))
    print(fc.magenta_font(" |"), end="")
    print((' ' * 5) + fc.blue_font("02. Chaque joueur peut enlever 1, 2 ou 3 bâtons") + (' ' * 7) + fc.magenta_font("|"))
    print(fc.magenta_font(" |"), end="")
    print((' ' * 5) + fc.blue_font("03. Le joueur prenant le dernier bâton perd la partie") + (' ' * 1) + fc.magenta_font("|"))
    print(fc.magenta_font(" |"), end="")
    print((' ' * 5) + fc.blue_font("04. Pour quitter la partie, tapez [!q]") + (' ' * 16) + fc.magenta_font("|"))
    print(fc.magenta_font(" +") + fc.magenta_font("-" * 59) + fc.magenta_font("+"))



def display_sticks(title, stlist, remaining_sticks):
    print("")
    print((' ' * 8), fc.magenta_font('-' * 45))
    print((' ' * 18), fc.yellow_font(f"{title}  - "), fc.blue_font(f"RESTANTS : {remaining_sticks}"))
    print((' ' * 8), fc.magenta_font('=' * 45))
    print((' ' * 10), fc.green_font(' '.join(stlist)))
    print((' ' * 8), fc.magenta_font('=' * 45))



def gameover():
    print(fc.red_font("\n FIN DE PARTIE... A BIENTOT !"))
    exit()



def wrong_entry():
    print(fc.red_font("\n Mauvais choix..."))
    time.sleep(2)



def game_menu():
    print("\n Choisissez votre adversaire :")
    print(" " * 4 + "[1] " + fc.magenta_font("LISA"))
    print(" " * 4 + "[2] " + fc.green_font("JOUEUR"))



def lisa_init():
    print("\n Initialisation de " + fc.magenta_font("LISA") + "...")
    time.sleep(2)



def random_player():
    print("\n Tirage aléatoire du joueur qui débute la partie...")
    time.sleep(2)



def current_player_first(cp, p1, p2):
    if cp == p1:
        print(f"\n {cp}, vous commencez...")
        time.sleep(2)
    elif cp == p2:
        print(f"\n {cp}, vous commencez...")
        time.sleep(2)
    else:
        print("\n" + fc.magenta_font(" LISA") + " commence...")
        time.sleep(2)



def lisa_picks_1_stick():
    print("\n" + fc.magenta_font(" LISA") + " retire 1 bâton...")
    time.sleep(2)
    


def lisa_picks_2_sticks():
    print("\n" + fc.magenta_font(" LISA") + " retire 2 bâtons...")
    time.sleep(2)



def lisa_picks_n_sticks(n_stx):
    print("\n" + fc.magenta_font(" LISA") + f" retire {n_stx} bâtons...")
    time.sleep(2)
    