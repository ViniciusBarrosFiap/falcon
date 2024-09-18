#Esse arquivo é responsável por controlar o menu do jogo e chamar as funções responsáveis pela lógica do jogo

#Importando classes
from falcon_simulation import Simulation 
from data_performance import Performance

class Menu:
    def __init__(self):
        self.simulation = Simulation()
        self.performance = Performance(self.simulation)
    
    def show_menu(self):
        while True:
            print('--- Menu Principal ---')
            print('1. Realizar simulação')
            print('2. Analisar resultados')
            print('3. Sair')
            
            choice = int(input('Digite o número da opção: '))
            
            if choice == 1:
                difficulty = int(input('Selecione a dificuldade:\n1. Fácil\n2. Médio\n3. Difícil\n'))
                self.simulation.run_simulation(difficulty)
            elif choice == 2:
                self.performance.show_performance()
                generate_chart = input('Deseja gerar um gráfico do desempenho ? (s/n)')
                if generate_chart.lower() == 's':
                    self.performance.plot_chart()
                elif generate_chart.lower() == 'n':
                    self.show_menu()
                else:
                    print('Opção inválida')
            elif choice == 3:
                print('Saindo do jogo...')
                break
            else:
                print('Opção inválida')
        