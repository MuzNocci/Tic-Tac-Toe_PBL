from player import *

class game:


    def __init__(self) -> None:

        self.fields = {}
        self.count = 0

        for field in range(9):
            self.fields.update({field : ''})


    def move(self, position, id):

        self.position = position
        self.id = id
        if self.fields[position] == '':
            self.fields.update({self.position : self.id})
            self.count += 1
        else:
            print('Posição já escolhida.')


    def winner(self, id):
        
        if self.fields[0] == self.fields[1] == self.fields[2] == id:
            return True
        elif self.fields[3] == self.fields[4] == self.fields[5] == id:
            return True
        elif self.fields[6] == self.fields[7] == self.fields[8] == id:
            return True
        elif self.fields[0] == self.fields[3] == self.fields[6] == id:
            return True
        elif self.fields[1] == self.fields[4] == self.fields[7] == id:
            return True
        elif self.fields[2] == self.fields[5] == self.fields[8] == id:
            return True
        elif self.fields[6] == self.fields[4] == self.fields[2] == id:
            return True
        elif self.fields[0] == self.fields[4] == self.fields[8] == id:
            return True
        
        return False
        
