import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
from simulacao import *

class MM2:
    def __init__(self, df = None, chegada = None, atendimento = None):  
        if df is not None:
            self.chegada = sum(df['tec'])/len(df['cliente'])
            self.atendimento = sum(df['tes'])/len(df['cliente'])
            self.intensidadeTrafego = (self.chegada / 2) / self.atendimento
            self.ociosidade = 1 - self.intensidadeTrafego
            
        else:
            self.chegada = chegada
            self.atendimento = atendimento
            self.intensidadeTrafego = (self.chegada /2 )/self.atendimento
            self.ociosidade =  1- self.intensidadeTrafego
    def setProbabilidadeFila(self):
        self.probabilidadeFila = 1/(1+(2*self.intensidadeTrafego)+(self.intensidadeTrafego**2)/(1-self.intensidadeTrafego))
    
    def setLq(self):
        self.lq = (self.probabilidadeFila*self.intensidadeTrafego)/(1-self.intensidadeTrafego)
        
    def setLs(self):
        self.ls = self.chegada/self.atendimento
    
    def setL(self):
        self.l = self.lq + self.ls
    
    def setWq(self):
        self.wq = self.lq/self.chegada

    def setW(self):
        self.w = self.wq + 1/self.atendimento

    def setWs(self):
        self.ws =self.w - self.wq
    
 
    
    def calcularTudo(self):
        self.setProbabilidadeFila()
        self.setLq()
        self.setLs()
        self.setL()
        self.setWq()
        self.setW()
        self.setWs()
        
    
     
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
        labels = ['ρ', '1 - ρ']
        metrics = [self.intensidadeTrafego, self.ociosidade]
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
        plt.plot()
    
    def fatorial(n):
        return fatorial(n-1) if n > 0 else 1

    def gerarTabelaMM2(self):
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