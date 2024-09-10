# ----- LISA's ACTIONS -----

import messages as msg


def len_sticklist_equal_to_bearing(slist):
    import random

    stx_removed = random.randint(1, 3)

    if stx_removed == 1:
        msg.lisa_picks_1_stick()
    else:
        msg.lisa_picks_n_sticks(stx_removed)

    del slist[-stx_removed:]
        


def len_sticklist_between_x_and_y(slist, bearing):
    stx_removed = (int(len(slist)) - bearing)

    if stx_removed == 1:
        msg.lisa_picks_1_stick()
    else:
        msg.lisa_picks_n_sticks(stx_removed)

    del slist[-stx_removed:]
