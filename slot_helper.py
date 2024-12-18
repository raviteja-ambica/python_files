import random
import copy
import bonus
import math

class Slot:
    """ This defines the blueprint of the slot """
    def __init__(self,paytable,reels,rows, columns,paylines,symbols,reels_free):
        """ This is the constructor of the slot class """
        self.paytable = paytable
        self.reels = reels
        self.reels_free = reels_free
        self.rows = rows
        self.columns = columns
        self.paylines = paylines
        self.symbols = symbols
        self.combinations = { sym : [0]*5 for sym in self.symbols }
        self.free_combinations = { sym : [0]*5 for sym in self.symbols }
        self.matrix = []
        self.total_win = 0
        self.scatter_count = 0
        self.scatter_freepins = { 3:8, 4:12, 5:20}
        self.freegames = 0
        self.total_free_win = 0
        self.base_win = 0
        self.free_win = 0
        self.bonus_win = 0
        self.bet = 0
        self.free_hits = 0
        self.bonus_hits = 0
        self.free_flag = False
        self.mult = {3:[5,7,10,15,20,25],
                4:[5,10,15,20,30,50],
                5:[25,30,40,50,75,100] }
        self.std_dev = 0
        self.hitrate = 0
        self.max_win = 0
        self.max_matrix = []
        


    def evaluate_line(self, line):
        """ This method returns the win amount for a given payline """
        count = 0
        #print('Payline is',line)
        wild_count = 0
        pay_sym = line[0]
        if line[0] == 's':
            return 0
        if line[0] != 'w' and line[0] !='z':
            Pay_sym = line[0]
            for i in range(1, 5):
                if line[i] == pay_sym or line[i] == 'w':
                    count = count + 1
                else:
                    break
            # In case first symbol is not wild
            if pay_sym !='z':
                if self.free_flag == True:
                    self.free_combinations[pay_sym][count] = self.free_combinations[pay_sym][count] + 1
                else:
                    self.combinations[pay_sym][count] = self.combinations[pay_sym][count] + 1
                return self.paytable[pay_sym][count]
    
        elif line[0] == 'z':
            
            count = 1
            
            for i in range(1,5):
                if line[i] == 'z':
                    count = count + 1
                else:
                    break

            
            
            if count >= 3:
                self.bonus_hits = self.bonus_hits + 1
                win = bonus.find_bonus_win(self.mult[count])
                self.bonus_win = self.bonus_win + win
                #print('Line is', line)
                return win
            else:
                return 0


    def evaluate_free_win(self):
        """ This method evaluates the free game win """
        self.scatter_count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == 's':
                    self.scatter_count = self.scatter_count + 1
        
        if self.scatter_count < 3:
            return 0
        win = 0

        if self.scatter_count >5:
            print(self.matrix)
            print('Error')
        self.free_hits = self.free_hits + 1
        self.free_flag = True
        self.freegames = self.scatter_freepins[self.scatter_count]
        n1, n2, n3, n4, n5 = len(self.reels_free['reel1']),len(self.reels_free['reel2']),len(self.reels_free['reel3']),len(self.reels_free['reel4']),len(self.reels_free['reel5'])
        while self.freegames > 0:
            r1 = random.randint(0,n1-1)
            r2 = random.randint(0,n2-1)
            r3 = random.randint(0,n3-1)
            r4 = random.randint(0,n4-1)
            r5 = random.randint(0,n5-1)
            self.free_matrix = self.generate_matrix(r1,r2,r3,r4,r5,n1,n2,n3,n4,n5,self.reels_free )
            self.scatter_count = 0
            #print('We have entered Free spins')
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.free_matrix[i][j] == 's':
                        self.scatter_count = self.scatter_count + 1
            if self.scatter_count >=3:
                self.freegames = self.freegames + self.scatter_freepins[self.scatter_count]

            for line in self.paylines:
                payline = ''
                payline = payline + self.free_matrix[line[0]][0] + self.free_matrix[line[1]][1] + self.free_matrix[line[2]][2] + self.free_matrix[line[3]][3] + self.free_matrix[line[4]][4]

                current_win = self.evaluate_line(payline)
                win = win + current_win 
            self.freegames = self.freegames - 1

        self.total_free_win = self.total_free_win + win
        self.free_flag = False
        return win
        


    def generate_matrix(self,r1,r2,r3,r4,r5,n1,n2,n3,n4,n5,reels):
        matrix = []
        for row in range(self.rows):
            matrix_row = [reels['reel1'][(r1+row)%n1],reels['reel2'][(r2+row)%n2],
                      reels['reel3'][(r3+row)%n3],reels['reel4'][(r4+row)%n4],reels['reel5'][(r5+row)%n5]]
            matrix.append(matrix_row)
        return matrix
        #print(self.matrix)
        #ch = input('Press enter to continue')

    def run_simulation(self,spins):
        """ This is the heart of the script """
        n1, n2, n3, n4, n5 = len(self.reels['reel1']),len(self.reels['reel2']),len(self.reels['reel3']),len(self.reels['reel4']),len(self.reels['reel5'])
        cycle = n1 * n2 * n3 * n4 * n5
        count = 0
        
        while count < spins:
            spin_win = 0
            if count % 1000000 == 0:
                print( 'percent completed = ', count*100/spins)
            r1 = random.randint(0,n1-1)
            r2 = random.randint(0,n2-1)
            r3 = random.randint(0,n3-1)
            r4 = random.randint(0,n4-1)
            r5 = random.randint(0,n5-1)
            self.matrix = self.generate_matrix(r1,r2,r3,r4,r5,n1,n2,n3,n4,n5,self.reels)
           
            for line in self.paylines:
                payline = ''
                #print('Matrix is')
                #print(self.matrix)
                
                payline = payline + self.matrix[line[0]][0] + self.matrix[line[1]][1] + self.matrix[line[2]][2] + self.matrix[line[3]][3] + self.matrix[line[4]][4]
                self.bet = self.bet + 1
                #print(payline)


                current_win = self.evaluate_line(payline)
                spin_win = spin_win + current_win
                self.total_win = self.total_win + current_win
                self.base_win = self.base_win + current_win
            current_free_win = self.evaluate_free_win()
            if spin_win > 0:
                self.hitrate = self.hitrate + 1
                if spin_win > self.max_win:
                    self.max_win = spin_win
                    self.max_matrix = self.matrix
            spin_win = spin_win + current_free_win
            self.free_win = self.free_win + current_free_win
            self.total_win = self.total_win + current_free_win
            self.std_dev = self.std_dev + math.pow((0.92 - spin_win/20),2)
            count = count + 1
        if spins > 1:
            self.std_dev = self.std_dev/(spins - 1)
        self.std_dev = math.pow(self.std_dev,0.5)
        



        print('Game RTP is',self.total_win*100/(len(self.paylines)*spins))
        print('Base RTP is ',(self.base_win-self.bonus_win)*100/self.bet)
        print('Free RTP is ',self.free_win*100/self.bet)
        print('Bonus RTP is',self.bonus_win*100/self.bet)
        print('Free hit frequency',spins/self.free_hits)
        print('Bonus hit frequency is',spins/self.bonus_hits)
        print('Base game hits are :')
        print('Sym 3X 4X 5X')
        for sym in self.symbols:
            print(sym,' ',self.combinations[sym][2],' ',self.combinations[sym][3],' ',self.combinations[sym][4])
        print('Free game hits are :')
        print('Sym 3X 4X 5X')
        for sym in self.symbols:
            print(sym,' ',self.free_combinations[sym][2],' ',self.free_combinations[sym][3],' ',self.free_combinations[sym][4])
        print('Standard Deviation of game is ',self.std_dev)
        print('Hit rate of game is',self.hitrate*100/spins)
        print('Maximum win in game is',self.max_win)
        print('Maximum matrix is',self.max_matrix)
        return
