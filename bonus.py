
import random as ri

def find_bonus_win(mult):
    """ This will trigger a bonus wheel round. The wheel keeps spinning and with each spin multiplier added to pot and sector becomes collect """
    sum = 0
    n = len(mult)
    collect_list = [ 0,0,0,0,0,0]
    while True:
        r = ri.randint(1,n)
        if collect_list[r-1] == 1:
            return sum
    
        sum = sum + mult[r-1]
        collect_list[r-1] = 1