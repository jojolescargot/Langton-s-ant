import numpy as np

import random




class ant:
    def __init__(self, size,sequence):
        self.size = size
        self.board = np.zeros([size,size],dtype= int)        
        self.ant_pos = np.array([size//2, size//2])
        self.ant_direct = 0
        self.ant_direction_list = np.array([[0,1],[1,0],[0,-1],[-1,0]])

        sample = ['L','R']
        sequence = ''

        for i in range(8):
            sequence += sample[random.randint(0,1)]

        print(sequence)

        dictionnaire_positions = {}

        for index, lettre in enumerate(sequence):
            if lettre == 'L':
                dictionnaire_positions[index] = -1
            elif lettre == 'R':
                dictionnaire_positions[index] = 1

        self.rules_dic = dictionnaire_positions
        self.numberOfStates = len(self.rules_dic)

    def step(self):
        self.ant_direct = (self.ant_direct + self.rules_dic[self.board[self.ant_pos[0], self.ant_pos[1]]]) % 4
        self.board[self.ant_pos[0], self.ant_pos[1]] = (self.board[self.ant_pos[0], self.ant_pos[1]] + 1) % self.numberOfStates
        self.ant_pos = (self.ant_pos + self.ant_direction_list[self.ant_direct]) % [self.size,self.size]