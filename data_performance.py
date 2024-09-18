#Esse arquivo analisa e apresenta os resultados de performance do aluno de acordo com seus resultados da simulação

import matplotlib.pyplot as plt

class Performance:
    def __init__(self, simulation):
        self.simulation = simulation
    
    def show_performance(self):
        if not self.simulation.results.empty:
            print('Resultados das simulações:')
            print(self.simulation.results)
        else:
            print('Nenhuma simulação realizada')
    
    def plot_chart(self):
        if not self.simulation.results.empty:
            fases = self.simulation.results['fase']
            pontuacao = self.simulation.results['pontuacao']
            
            plt.plot(fases, pontuacao, marker='o')
            plt.title('Desempenho do aluno')
            plt.xlabel('Fases')
            plt.ylabel('Pontuação')
            plt.show()
        else:
            print('Nenhuma simulação realizada')