import random
import copy
import bonus
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
        self.mult = {3:[5,7,10,15,20,25],
                4:[5,10,15,20,30,50],
                5:[25,30,40,50,75,100] }


    def evaluate_line(self, line):
        """ This method returns the win amount for a given payline """
        count = 0
        #print('Payline is',line)
        wild_count = 0
        pay_sym = line[0]
        if line[0] != 'w' and line[0] !='z':
            Pay_sym = line[0]
            for i in range(1, 5):
                if line[i] == pay_sym or line[i] == 'w':
                    count = count + 1
                else:
                    break
            # In case first symbol is not wild
            if pay_sym !='z':
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
                win = bonus.ev(self.mult[count]) #37.92078
                self.bonus_win = self.bonus_win + win
                #print('Line is', line)
                return win
            else:
                return 0
            """elif count == 4:
                self.bonus_win = self.bonus_win + 60.11831
                #print('Line is', line)
                return 60.11831
            elif count == 5:
                self.bonus_win = self.bonus_win + 147.9835
                #print('Line is', line)
                return 147.9835
            """


            
        

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
                        #print(self.matrix)
                        self.scatter_count = self.scatter_count + 1
            if self.scatter_count >=3:
                self.freegames = self.freegames + self.scatter_freepins[self.scatter_count]

            for line in self.paylines:
                payline = ''
                payline = payline + self.free_matrix[line[0]][0] + self.free_matrix[line[1]][1] + self.free_matrix[line[2]][2] + self.free_matrix[line[3]][3] + self.free_matrix[line[4]][4]
                #print(payline)
                current_win = self.evaluate_line(payline) #self.evaluate_matrix
                win = win + current_win #+ current_free_win
            self.freegames = self.freegames - 1

        self.total_free_win = self.total_free_win + win
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
                self.bet = self.bet+1
                #print(payline)


                current_win = self.evaluate_line(payline) #self.evaluate_matrix
                self.total_win = self.total_win + current_win
                self.base_win = self.base_win + current_win
            current_free_win = self.evaluate_free_win()
            self.free_win = self.free_win + current_free_win
            self.total_win = self.total_win + current_free_win
            count = count + 1



        print('RTP is',self.total_win*100/(len(self.paylines)*spins))
        print('Bonus RTP is',self.bonus_win*100/self.bet)
        print('Free hit frequency',spins/self.free_hits)
        print('Bonus hit frequency is',spins/self.bonus_hits)
        print('Base RTP is ',self.base_win*100/self.bet)
        print('Free RTP is ',self.free_win*100/self.bet)
        print(self.combinations)
        return
