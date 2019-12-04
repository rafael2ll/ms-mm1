import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from distribuicoes import Distribuicoes
from variaveis import Variaveis

class Simulacao:
    def __init__(self, variaveis = Variaveis(), tempo_limite=-1, clientes=-1):
        self.variaveis = variaveis
        self.simulacao = list()
        self.tempo_limite = tempo_limite
        self.numero_clientes = clientes
    
    def simular_tudo(self):
        while True:
            self.simulacao = []
            if self.numero_clientes > 0:
                for i in range(self.numero_clientes):
                    self.simular()
            elif self.tempo_limite > 0:
                tempo_relogio = 0
                while tempo_relogio < self.tempo_limite:
                    self.simular()
                    tempo_relogio = self.simulacao[-1]["tempo_final_servico_relogio"]
            df  = self.get_tabela()
            chegada = sum(df['tec'])/len(df['cliente'])
            atendimento = sum(df['tes'])/len(df['cliente'])
            if atendimento > chegada:
                break
                
    def simular(self):
        if len(self.simulacao) == 0:
            cliente = 1
            tec = abs(self.variaveis.tec_funcao())
            tempo_chegada_relogio = tec
            tes = abs(self.variaveis.tes_funcao())
            tempo_inicio_servico_relogio = tec
            tempo_fila = 0
            tempo_final_servico_relogio= tec+tes
            tempo_cliente_sistema = tes
            tempo_livre_operador = tec
        else:
            cliente = self.simulacao[-1]['cliente']+1   
            tec = abs(self.variaveis.tec_funcao())
            tempo_chegada_relogio =  self.simulacao[-1]['tempo_chegada_relogio'] +tec
            tes = abs(self.variaveis.tes_funcao())
            tempo_inicio_servico_relogio = max([tempo_chegada_relogio, self.simulacao[-1]['tempo_final_servico_relogio']])
            tempo_fila = max([0,  self.simulacao[-1]['tempo_final_servico_relogio'] - tempo_chegada_relogio])
            tempo_final_servico_relogio= tempo_chegada_relogio+tempo_fila+tes
            tempo_cliente_sistema = tempo_fila + tes
            tempo_livre_operador = max([0, tempo_chegada_relogio -self.simulacao[-1]['tempo_final_servico_relogio']])
        
        iteracao ={
                'cliente': cliente, 
                'tec': tec,
                'tempo_chegada_relogio': tempo_chegada_relogio,
                'tes': tes,
                'tempo_inicio_servico_relogio': tempo_inicio_servico_relogio,
                'tempo_fila': tempo_fila,
                'tempo_final_servico_relogio': tempo_final_servico_relogio,
                'tempo_cliente_sistema': tempo_cliente_sistema,
                'tempo_livre_operador': tempo_livre_operador
                }
        self.simulacao.append(iteracao)
        
    def get_tabela(self):
          return pd.DataFrame(self.simulacao, columns=['cliente', 'tec', 'tempo_chegada_relogio', 'tes', 'tempo_inicio_servico_relogio', 'tempo_fila', 'tempo_final_servico_relogio', 'tempo_cliente_sistema', 'tempo_livre_operador'])

class GeradorSimulacaoExponencial:
    def __init__(self):
        """
            Gera uma simulação usando dist. exponencial com p < 1, ou seja,
            chegada < atendimento 
        """

        while True:
            vars = Variaveis()
            vars.set_tes(Distribuicoes.EXPONENCIAL.value['func'])
            vars.set_tec(Distribuicoes.EXPONENCIAL.value['func'])
            s = Simulacao(variaveis=vars, tempo_limite=10000)
            s.simular_tudo()
            df = s.get_tabela()
            chegada = sum(df['tec'])/len(df['cliente'])
            atendimento = sum(df['tes'])/len(df['cliente'])

            if atendimento > chegada:
                self.dfSimulacao = df
                break