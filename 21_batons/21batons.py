#!usr/bin/venv python3
# -*- coding: utf-8 -*-

'''
     21 Batons | Marlene Softwares | Yannick HEUDE (Ayckinn)
 ayckinn@pm.me | https://github.com/AyckinnLisa | Version 1.0
'''

import time
import random
import lisa
import messages as msg
import fontcolor as fc



def main():
    TITLE = "21 BATONS"
    AI = "LISA"

    player_one = ""
    player_two = ""
    current_player = ""
    other_player = ""


    game_loop = True
    while game_loop:
        sticklist = ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']

        msg.rules()
        msg.game_menu()

        select_opponent = input("\n Votre choix >> ").lower()

        if '1' in select_opponent:
            msg.rules()
            print("\n Vous jouez contre " + fc.magenta_font("LISA") + " !")
            player_one = input("\n Joueur, entrez votre nom : ").upper()
            msg.lisa_init()
                     
            random_player = random.randint(1, 2)
            msg.random_player()

            if random_player == 1:
                current_player = player_one
                msg.current_player_first(current_player, player_one, None)
            elif random_player == 2:
                current_player = AI
                msg.current_player_first(current_player, player_one, None)


            while (len(sticklist)) > 0:
                msg.rules()
                msg.display_sticks(TITLE, sticklist, (len(sticklist)))

                if current_player == AI:
                    if (len(sticklist)) == 21:
                        lisa.len_sticklist_equal_to_bearing(sticklist)

                    elif (len(sticklist)) <= 20 and (len(sticklist)) >= 18:
                        lisa.len_sticklist_between_x_and_y(sticklist, 17)

                    elif (len(sticklist)) == 17:
                        lisa.len_sticklist_equal_to_bearing(sticklist)

                    elif (len(sticklist)) <= 16 and (len(sticklist)) >= 14:
                        lisa.len_sticklist_between_x_and_y(sticklist, 13)

                    elif (len(sticklist)) == 13:
                        lisa.len_sticklist_equal_to_bearing(sticklist)

                    elif (len(sticklist)) <= 12 and (len(sticklist)) >= 10:
                        lisa.len_sticklist_between_x_and_y(sticklist, 9)

                    elif (len(sticklist)) == 9:
                        lisa.len_sticklist_equal_to_bearing(sticklist)

                    elif (len(sticklist)) <= 8 and (len(sticklist)) >= 6:
                        lisa.len_sticklist_between_x_and_y(sticklist, 5)

                    elif (len(sticklist)) == 5:
                        lisa.len_sticklist_equal_to_bearing(sticklist)

                    elif (len(sticklist)) <= 4 and (len(sticklist)) >= 2:
                        lisa.len_sticklist_between_x_and_y(sticklist, 1)

                    elif(len(sticklist)) <= 3 and (len(sticklist)) > 1:
                        if (len(sticklist)) == 3:
                            msg.lisa_picks_2_sticks()
                            del sticklist[-2:]
                        elif(len(sticklist)) == 2:
                            msg.lisa_picks_1_stick()
                            del sticklist[-1:]
                        else:
                            lisa_sticks = random.randint(1, 2)

                            if lisa_sticks == 1:
                                msg.lisa_picks_1_stick()
                                del sticklist[-1:]
                            else:
                                msg.lisa_picks_2_sticks()
                                del sticklist[-2:]

                    elif (len(sticklist)) == 1:
                        print(f"\n" + fc.magenta_font("LISA") + " retire 1 bâton...")
                        time.sleep(2)
                        sticklist.clear()   

                    if current_player == player_one:
                        current_player = AI
                    else:
                        current_player = player_one
                        
                else:
                    remove_stick = input(f"\n {player_one}, combien de bâtons voulez-vous retirer (1, 2 ou 3) ? ")

                    if remove_stick == '1':
                        print(f"\n Vous retirez 1 bâton...")
                        time.sleep(2)
                        del sticklist[-1:]

                    elif remove_stick == '0' or remove_stick > '3':
                        msg.wrong_entry()

                    elif '!q' in remove_stick:
                        msg.gameover()

                    else:
                        print(f"\n Vous retirez {remove_stick} bâtons...")
                        time.sleep(2)
                        del sticklist[-(int(remove_stick)):]
                    
                    if current_player == player_one:
                        current_player = AI
                    else:
                        current_player = player_one

                if len(sticklist) == 0:
                    msg.rules()
                    msg.display_sticks(TITLE, sticklist, (len(sticklist)))

                    if current_player == player_one:
                        print()
                        print(fc.red_font("\n LISA a perdu !"))
                        print(fc.green_font(f"\n {player_one} ! VOUS GAGNEZ LA PARTIE !! :)"))
                    else:
                        print(fc.red_font(f"\n {player_one} ! Vous avez perdu ! :("))
                        print(fc.green_font("\n LISA GAGNE LA PARTIE !"))


        elif '2' in select_opponent:
            msg.rules()
            player_one = input("\n\n Joueur 1, entrez votre nom : ").upper()
            player_two = input(" Joueur 2, entrez votre nom : ").upper()
            print(f"\n {player_one} et {player_two}, vous jouez l'un contre l'autre !")
            time.sleep(2)
            
            random_player = random.randint(1, 2)
            msg.random_player()

            if random_player == 1:
                current_player = player_one
                msg.current_player_first(current_player, player_one, player_two)
            elif random_player == 2:
                current_player = player_two
                msg.current_player_first(current_player, player_one, player_two)

            while len(sticklist) > 0:
                msg.rules()
                msg.display_sticks(TITLE, sticklist, (len(sticklist)))

                remove_stick = input(f"\n {current_player}, combien de bâtons voulez-vous retirer (1, 2 ou 3) ? ")

                if remove_stick == '1':
                    print(f"\n Vous retirez 1 bâton...")
                    time.sleep(2)
                    del sticklist[-1:]

                elif remove_stick == '0' or remove_stick > '3':
                    msg.wrong_entry()

                elif '!q' in remove_stick:
                    msg.gameover()

                else:
                    print(f"\n Vous retirez {remove_stick} bâtons...")
                    time.sleep(2)
                    del sticklist[-(int(remove_stick)):]
                    
                if current_player == player_one:
                    current_player = player_two
                    other_player = player_one
                else:
                    current_player = player_one
                    other_player = player_two

            if len(sticklist) == 0:
                msg.rules()
                msg.display_sticks(TITLE, sticklist, (len(sticklist)))
                print(fc.red_font(f"\n {other_player} ! vous avez perdu :("))
                print(fc.green_font(f"\n {current_player} ! VOUS GAGNEZ LA PARTIE !! :)"))

        elif '!q' in select_opponent:
            msg.gameover()
        else:
            msg.wrong_entry()

        replay = input("\n Voulez-vous rejouer (o/n) ? ").lower()
        if 'o' in replay:
            continue
        else:
            msg.gameover()


if __name__ == '__main__':
    main()
