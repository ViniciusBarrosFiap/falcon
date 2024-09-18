#Esse arquivo gerencia as funções utilizadas no jogo e armazena dos dados para avaliar o desempenho

import pandas as pd
import random

class Simulation:
    def __init__(self):
        #Iniciando o dataFrame com os atribustos que avaliam o desempenho do aluno
        self.results = pd.DataFrame(columns=['fase', 'dificuldade', 'pontuacao', 'erros', 'tempo'])
        
    #Função para rodar a simulação da cirurgia
    def run_simulation(self, difficulty):
        print(f'Iniciando a simulação na dificuldade: {difficulty}')
        
        input('Pressione Enter para simular a cirurgia...')
        
        #Gerando os dados do aluno
        score = self.generate_score(difficulty)
        
        result = pd.DataFrame([{
            'fase': len(self.results) + 1,
            'dificuldade': difficulty,
            'pontuacao': score,
            'erros': random.randint(0, 10),
            'tempo': random.uniform(5.0, 20.0)
        }])
        #Adicionando e exibindo resultados da simulação
        self.results = pd.concat([self.results, result], ignore_index=True)
        
        print(f'Simulação finalizada. Resultado: \n{result}')
    
    #Função para gerar pontuação de acordo com a dificuldade
    def generate_score(self, difficulty):
        if difficulty == 1:
            return random.randint(60, 100)
        elif difficulty == 2:
            return random.randint(35, 100)
        elif difficulty == 3:
            return random.randint(20, 100)
    