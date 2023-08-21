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
        


if __name__ == '__main__':



    pl = player()
    gm = game()
    id = 'X'

    def post_player(id, name):

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



    App = QtWidgets.QApplication([])
    Tela = uic.loadUi(resource_path('template.ui'))



    Tela.show()
    Tela.frame_p1.show()
    Tela.frame_p2.close()
    Tela.framegame.close()


    Tela.pushButton_p1.clicked.connect(lambda: post_player('X', Tela.lineEdit_p1.text().strip(' ')))
    Tela.pushButton_p2.clicked.connect(lambda: post_player('O', Tela.lineEdit_p2.text().strip(' ')))


    App.exec()





    

    # while True:

    #     if gamer.def_player('O', input('Digite o nome do jogador (O): ')):
    #         break  


    # while True:

    #     name = gamer.players[id]

    #     if play.count < 9:
    #         print(f'{name}, é sua vez!')
    #         position = int(input('Escolha um campo para jogar: '))
    #         play.move(position, id)

    #         if play.winner(id):
    #             print(f'{name}, você venceu!!!')
    #             break

    #         if id == 'X':
    #             id = 'O'
    #         else:
    #             id = 'X'

    #     else:
    #         print(f'VELHA!!!')
    #         break

 