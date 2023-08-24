from PyQt6 import QtWidgets, QtGui, QtCore, uic
import sys

from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)



class player:


    def __init__(self) -> None:

        self.players = {}

    
    def valid_player(self, name):

        self.name = name

        if name != '' and len(name) >= 3 and isinstance(name, str):
            return True

        return False
    
    
    def def_player(self, char, name):
        
        if self.valid_player(name):
            self.players.update({
                char : name
            })
            return True
        
        return False



class game:


    def __init__(self) -> None:

        self.fields = {}
        self.count = 0

        for field in range(9):
            self.fields.update({field : ''})


    def post_player(self, id='X', name=None):

        if pl.def_player(id, name):
            if id == 'X':
                Tela.frame_p1.close()
                Tela.frame_p2.show()
                Tela.lineEdit_p1.setText('')
                Tela.label_informations.setText('')
            elif id == 'O':
                Tela.frame_p2.close()
                Tela.framegame.show()
                Tela.lineEdit_p2.setText('')
                start_player = pl.players['X']
                Tela.label_informations.setText(f'{start_player}, é sua vez.')
            return
        
        Tela.lineEdit_p1.setText('')
        Tela.lineEdit_p2.setText('')
        Tela.label_informations.setText('Nome inválido!')


    def move(self, position, id):

        self.position = position
        self.id = id
        global ident
        

        if self.fields[position] == '':
            self.fields.update({self.position : self.id})
            self.count += 1
            self.update()
            if self.winner(self.id) == False and self.count <= 8:
                if self.id == 'X':
                    ident = 'O'
                    start_player = pl.players[ident]
                    Tela.label_informations.setText(f'{start_player}, é sua vez.')
                elif self.id == 'O':
                    ident = 'X'
                    start_player = pl.players[ident]
                    Tela.label_informations.setText(f'{start_player}, é sua vez.')
            else:
                if self.count <= 8:
                    start_player = pl.players[self.id]
                    Tela.labelwin.setText(f'{start_player}, você venceu!') 
                    Tela.framewin.show()
                else:
                    Tela.labelwin.setText(f'Deu velha!!!') 
                    Tela.framewin.show()
            
        else:
            print('Posição já escolhida.')

    
    def update(self):

        Tela.pushButton_c0.setText(self.fields[0])
        Tela.pushButton_c1.setText(self.fields[1])
        Tela.pushButton_c2.setText(self.fields[2])
        Tela.pushButton_c3.setText(self.fields[3])
        Tela.pushButton_c4.setText(self.fields[4])
        Tela.pushButton_c5.setText(self.fields[5])
        Tela.pushButton_c6.setText(self.fields[6])
        Tela.pushButton_c7.setText(self.fields[7])
        Tela.pushButton_c8.setText(self.fields[8])


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
    
    
    def new_game(self):

        self.count = 0
        for field in range(9):
            self.fields.update({field : ''})
        self.update()
        Tela.framegame.show()
        Tela.framewin.close()



if __name__ == '__main__':
 

    pl = player()
    gm = game()
    ident = 'X'
    endgame = False


    App = QtWidgets.QApplication([])
    Tela = uic.loadUi(resource_path('template.ui'))


    Tela.show()
    Tela.frame_p1.show()
    Tela.frame_p2.close()
    Tela.framegame.close()
    Tela.framewin.close()


    Tela.pushButton_p1.clicked.connect(lambda: gm.post_player('X', Tela.lineEdit_p1.text().strip(' ')))
    Tela.pushButton_p2.clicked.connect(lambda: gm.post_player('O', Tela.lineEdit_p2.text().strip(' ')))

    Tela.pushButton_c0.clicked.connect(lambda: gm.move(0, ident))
    Tela.pushButton_c1.clicked.connect(lambda: gm.move(1, ident))
    Tela.pushButton_c2.clicked.connect(lambda: gm.move(2, ident))
    Tela.pushButton_c3.clicked.connect(lambda: gm.move(3, ident))
    Tela.pushButton_c4.clicked.connect(lambda: gm.move(4, ident))
    Tela.pushButton_c5.clicked.connect(lambda: gm.move(5, ident))
    Tela.pushButton_c6.clicked.connect(lambda: gm.move(6, ident))
    Tela.pushButton_c7.clicked.connect(lambda: gm.move(7, ident))
    Tela.pushButton_c8.clicked.connect(lambda: gm.move(8, ident))

    Tela.pushButtonwin.clicked.connect(gm.new_game)

    App.exec()