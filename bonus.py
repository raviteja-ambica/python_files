
import random as ri

def ev(mult):
    sum = 0
    n = len(mult)
    #mult = [1,2,3,4,5,6]
    collect_list = [ 0,0,0,0,0,0]
    while True:
        r = ri.randint(1,n)
        if collect_list[r-1] == 1:
            return sum
    
        sum = sum + mult[r-1]
        collect_list[r-1] = 1