#Arquivo que será executado para iniciar o programa com o jogo

#Importando classe do menu principal do jogo
from menu import Menu

if __name__ == '__main__':
    menu = Menu()
    menu.show_menu()