import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
from simulacao import *

class MM2:
    def __init__(self, df = None, chegada = None, atendimento = None):  
        if df is not None:
            #self.chegada = sum(df['tec'])/len(df['cliente'])
            #self.atendimento = sum(df['tes'])/len(df['cliente'])
            #self.intensidadeTrafego = (self.chegada / 2) / self.atendimento
            pass
            
        else:
            self.s = 2
            self.chegada = chegada
            self.atendimento = atendimento
            self.intensidadeTrafego = self.chegada/(self.atendimento * self.s)
    
    def setPi0(self):
        i = 0
        soma = 0
        
        while i <= self.s - 1:
            fat = self.fatorial(i)
            soma += ((self.s * self.intensidadeTrafego)**i)/fat
            i = i + 1
            
        soma += ((self.s * self.intensidadeTrafego)**self.s)/(self.fatorial(self.s) * (1 - self.intensidadeTrafego))
        self.pi0 = 1/soma
        
    def setPj(self):
        # Define a probabilidade de todos os servidores estarem ocupados
        self.setPi0()
        self.pj = ( ((self.s * self.intensidadeTrafego)**self.s) * self.pi0)
        self.pj = self.pj/(self.fatorial(self.s) * (1 - self.intensidadeTrafego))
    
    def setLq(self):
        self.setPj()
        self.lq = (self.pj * self.intensidadeTrafego)/(1 - self.intensidadeTrafego)
    
    def setLs(self):
        # L = Ls + Lq -> Ls = L - Lq
        self.setL()
        self.ls = self.l - self.lq
    
    def setL(self):
        self.setLq()
        self.l = self.lq + (self.chegada/self.atendimento)
    
    def setWs(self):
        # W = Ws + Wq -> Ws = W - Wq
        self.setW()
        self.setWq()
        self.ws = self.w - self.wq
    
    def setW(self):
        self.setL()
        self.w = self.l/self.chegada
    
    def setWq(self):
        self.setLq()
        self.wq = self.lq/self.chegada
    
    def calcularTudo(self):
        self.setPi0()
        self.setPj()
        self.setLq()
        self.setLs()
        self.setL()
        self.setW()
        self.setWs()
        self.setWq()
     
    def plotPieGraph(self, labels, metrics, colors, title):
        fig1, ax1 = plt.subplots()
        ax1.pie(metrics, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title(title)
        plt.show()
    
    def plotMetricasGerais(self):
        objects = ('λ', 'μ')
        y_pos = np.arange(len(objects))
        performance = [self.chegada, self.atendimento]
        plt.bar(y_pos, performance, align='center', color='mediumorchid')
        plt.xticks(y_pos, objects)
        plt.ylabel('Unidade')
        plt.title('Métricas de Gerais do Sistema')
        plt.show()
    
    def plotMetricasTrafego(self):
        labels = ['ρ', 'π0']
        metrics = [self.intensidadeTrafego, self.pi0]
        colors=['lightcoral', 'gray']
        self.plotPieGraph(labels, metrics, colors, 'Métricas de Tráfego do Sistema')
        
    def plotMetricasTempo(self):
        labels = ['Ws', 'Wq']
        metrics = [self.ws*100/self.w, self.wq*100/self.w]
        colors = ['orange', 'cornflowerblue']
        self.plotPieGraph(labels, metrics, colors, 'Métricas de Tempo do Sistema')
    
    def plotMetricasCliente(self):
        objects = ('L', 'Ls', 'Lq')
        y_pos = np.arange(len(objects))
        performance = [self.l, self.ls, self.lq]

        plt.bar(y_pos, performance, align='center', color='crimson')
        plt.xticks(y_pos, objects)
        plt.ylabel('Unidade')
        plt.title('Métricas de Clientes do Sistema')

    def plot(self):
        self.plotMetricasGerais()
        self.plotMetricasCliente()
        self.plotMetricasTempo()
    
    def fatorial(self, n):
            if n == 0 or n == 1: return 1
        else: 
            i = 2
            fat = 1
            while i <= n:
                fat = fat * i
                i = i + 1
                
            return fat

    def gerarTabelaMM2(self):
        self.calcularTudo()
        colunas = ['λ', 'μ', 'ρ', 'π0', 'W', 'Ws', 'Wq', 'L', 'Ls', 'Lq']
        dic = dict.fromkeys(colunas, True)
        dic['λ'] = self.chegada
        dic['μ'] = self.atendimento
        dic['ρ'] = self.intensidadeTrafego
        dic['π0'] = self.pi0
        dic['W'] = self.w
        dic['Ws'] = self.ws
        dic['Wq'] = self.wq
        dic['L'] = self.l
        dic['Ls'] = self.ls
        dic['Lq'] = self.lq
        
        return pd.DataFrame([dic], columns=colunas)