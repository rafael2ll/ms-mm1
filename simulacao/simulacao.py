import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum

class Distribuicoes(Enum):
    NORMAL = {'name': 'Normal', 'func': np.random.normal}
    EXPONENCIAL= {'name': 'Exponencial', 'func': np.random.exponential}
    POISSON = {'name': 'Poisson', 'func': np.random.poisson}
    BINOMIAL = {'name': 'Binomial', 'func': np.random.binomial}

class Variaveis:
    def __init___(self):
        self.tec_funcao = lambda:  1
        self.tes_funcao = lambda:  1
    
    def set_tec(self, f):
        """
            params: 
                f: (func) função de aridade 0 de retorno inteiro
        """
        self.tec_funcao = f
        
    def get_tec(self):
        return self.tec_funcao()
    
    def set_tes(self, f):
        """
            params:
                f: (func) função de aridade 0 de retorno inteiro
        """
        self.tes_funcao = f
        
    def get_tes(self):
        return  self.tes_funcao()

class Simulacao:
    def __init__(self, variaveis = Variaveis(), tempo_limite=-1, clientes=-1):
        self.variaveis = variaveis
        self.simulacao = list()
        self.tempo_limite = tempo_limite
        self.numero_clientes = clientes
    
    def simular_tudo(self):
        self.simulacao = []
        if self.numero_clientes > 0:
            for i in range(self.numero_clientes):
                self.simular()
        elif self.tempo_limite > 0:
            tempo_relogio = 0
            while tempo_relogio < self.tempo_limite:
                self.simular()
                tempo_relogio = self.simulacao[-1]["tempo_final_servico_relogio"]
    def simular(self):
        if len(self.simulacao) == 0:
            cliente = 1
            tec = abs(self.variaveis.tec_funcao()*10)
            tempo_chegada_relogio = tec
            tes = abs(self.variaveis.tes_funcao()*10)
            tempo_inicio_servico_relogio = tec
            tempo_fila = 0
            tempo_final_servico_relogio= tec+tes
            tempo_cliente_sistema = tes
            tempo_livre_operador = tec
        else:
            cliente = self.simulacao[-1]['cliente']+1   
            tec = abs(self.variaveis.tec_funcao()*10)
            tempo_chegada_relogio =  self.simulacao[-1]['tempo_chegada_relogio'] +tec
            tes = abs(self.variaveis.tes_funcao()*100)
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
            s = Simulacao(variaveis=vars, tempo_limite=100000)
            s.simular_tudo()
            df = s.get_tabela()
            chegada = sum(df['tec'])/len(df['cliente'])
            atendimento = sum(df['tes'])/len(df['cliente'])

            if atendimento > chegada:
                self.dfSimulacao = df
                break

class MM1:
    def __init__(self, df = None, chegada = None, atendimento = None):  
        if df is not None:
            self.chegada = sum(df['tec'])/len(df['cliente'])
            self.atendimento = sum(df['tes'])/len(df['cliente'])
            self.intensidadeTrafego = self.chegada/self.atendimento
            self.ociosidade = 1 - self.intensidadeTrafego
            
        else:
            self.chegada = chegada
            self.atendimento = atendimento
            self.intensidadeTrafego = self.chegada/self.atendimento
            self.ociosidade = 1 - self.intensidadeTrafego
        
    def setProbabilidadeFila(self):
        pi0 = self.ociosidade
        pi1 = self.intensidadeTrafego * (1 - self.intensidadeTrafego)
        self.probabilidadeFila = 1 - pi0 - pi1
    
    def setL(self):
        self.l = self.chegada/(self.atendimento - self.chegada)
        
    def setLs(self):
        self.ls = self.intensidadeTrafego
    
    def setLq(self):
        self.lq = self.intensidadeTrafego**2/(1- self.intensidadeTrafego)
    
    def setW(self):
        self.w = 1/(self.atendimento - self.chegada)
    
    def setWs(self):
        self.ws = 1/self.atendimento
    
    def setWq(self):
        self.wq = self.chegada/(self.atendimento * (self.atendimento - self.chegada))
    
    def calcularTudo(self):
        self.setProbabilidadeFila()
        self.setL()
        self.setLq()
        self.setLs()
        self.setW()
        self.setWs()
        self.setWq()
    
    def plotMetricasGerais(self):
        objects = ('λ', 'μ', 'ρ', '1 - ρ')
        y_pos = np.arange(len(objects))
        performance = [self.chegada, self.atendimento, self.probabilidadeFila, self.ociosidade]

        plt.bar(y_pos, performance, align='center', color='mediumorchid')
        plt.xticks(y_pos, objects)
        plt.ylabel('Unidade')
        plt.title('Métricas de Gerais do Sistema')
        plt.show()
        
    def plotMetricasTempo(self):
        objects = ('W', 'Ws', 'Wq')
        y_pos = np.arange(len(objects))
        performance = [self.w, self.ws, self.wq]

        plt.bar(y_pos, performance, align='center', color='deepskyblue')
        plt.xticks(y_pos, objects)
        plt.ylabel('Unidade de Tempo')
        plt.title('Métricas de Tempo do Sistema')
        plt.show()
    
    def plotMetricasCliente(self):
        objects = ('L', 'Ls', 'Lq')
        y_pos = np.arange(len(objects))
        performance = [self.l, self.ls, self.lq]

        plt.bar(y_pos, performance, align='center', color='crimson')
        plt.xticks(y_pos, objects)
        plt.ylabel('Unidade')
        plt.title('Métricas de Clientes do Sistema')
        plt.show()
        
    def gerarTabelaMM1(self):
        colunas = ['λ', 'μ', 'ρ', '1 - ρ', 'W', 'Ws', 'Wq', 'L', 'Ls', 'Lq']
        dic = dict.fromkeys(colunas, True)
        dic['λ'] = self.chegada
        dic['μ'] = self.atendimento
        dic['ρ'] = self.intensidadeTrafego
        dic['1 - ρ'] = self.ociosidade
        dic['W'] = self.w
        dic['Ws'] = self.ws
        dic['Wq'] = self.wq
        dic['L'] = self.l
        dic['Ls'] = self.ls
        dic['Lq'] = self.lq
        
        return pd.DataFrame([dic], columns=colunas)