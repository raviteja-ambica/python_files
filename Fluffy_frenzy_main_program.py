import paytable
import paylines
import reelstrip
import time
import pandas as pd
from openpyxl import load_workbook
import slot_helper

def main():
    start_time = time.time()
    pay_table = paytable.little_wild_panda_paytable
    pay_lines = paylines.little_wild_panda_paylines
    #reels = reelstrip.little_wild_panda_reels
    #reels_free = reelstrip.little_wild_panda_reels_free
    xl = pd.ExcelFile("./reels.xlsx")
    df = xl.parse("Sheet1")
    reels = { 'reel1' : df['Base'][0],
              'reel2' : df['Base'][1],
              'reel3' : df['Base'][2],
              'reel4' : df['Base'][3],
              'reel5' : df['Base'][4] }
    
    #print(df['Base'])
    #data = df.to_dict()
    print(reels)
    #df = xl.parse("Sheet2")
    reels_free = { 'reel1' : df['Free'][0],
              'reel2' : df['Free'][1],
              'reel3' : df['Free'][2],
              'reel4' : df['Free'][3],
              'reel5' : df['Free'][4] }
    print('Free Reels are')
    print(reels_free)
    rows = 3
    cols = 5
    line_waybar = True
    
    
    symbols = ['w','a','b','c','d','e','f','g','h','s','z']
    s = slot_helper.Slot(pay_table,reels,rows,cols,pay_lines,symbols,reels_free)
    s.run_simulation(1000000)
    print('Time taken in seconds :',time.time() - start_time)

main()
