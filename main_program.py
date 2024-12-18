import paytable
import paylines
import reelstrip
import time
import slot_helper

def main():
    start_time = time.time()
    pay_table = paytable.little_wild_panda_paytable
    pay_lines = paylines.little_wild_panda_paylines
    reels = reelstrip.little_wild_panda_reels
    reels_free = reelstrip.little_wild_panda_reels_free
    
    rows = 3
    cols = 5
    line_waybar = True
    
    
    symbols = ['w','a','b','c','d','e','f','g','h','s','z']
    s = slot_helper.Slot(pay_table,reels,rows,cols,pay_lines,symbols,reels_free)
    s.run_simulation(10000000)
    print('Time taken in seconds :',time.time() - start_time)

main()
