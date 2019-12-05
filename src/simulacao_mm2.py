import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from distribuicoes import Distribuicoes
from variaveis import Variaveis

class SimulacaoMM2:
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
                    tempo_relogio = max([self.simulacao[-1]["tf_servico_relogio_s1"], self.simulacao[-1]["tf_servico_relogio_s2"]])
            df  = self.get_tabela()
            chegada = sum(df['tec'])/len(df['cliente'])
            atendimento = sum(df['tes'])/len(df['cliente'])
            if atendimento > chegada:
                break
                
    def simular(self):
        if len(self.simulacao) == 0:
            cliente = 1
            tec = abs(self.variaveis.tec_funcao())
            t_chegada_relogio = tec
            tes = abs(self.variaveis.tes_funcao())
            ti_servico_relogio = tec
            t_fila = 0
            tf_servico_relogio_s1= tec+tes
            tf_servico_relogio_s2= 0
            tempo_cliente_sistema = tes
            t_livre_operador_s1 = tec
            t_livre_operador_s2 = tec
        else:
            cliente = self.simulacao[-1]['cliente']+1   
            tec = abs(self.variaveis.tec_funcao())
            t_chegada_relogio =  self.simulacao[-1]['t_chegada_relogio'] +tec
            tes = abs(self.variaveis.tes_funcao())
            ti_servico_relogio =  min([self.simulacao[-1]['tf_servico_relogio_s1'],self.simulacao[-1]['tf_servico_relogio_s2'] ])
            t_fila = max([0,  ti_servico_relogio - t_chegada_relogio])
            tempo_final_servico_relogio= t_chegada_relogio+t_fila+tes
            tf_servico_relogio_s1 = tempo_final_servico_relogio if self.simulacao[-1]['tf_servico_relogio_s1'] < self.simulacao[-1]['tf_servico_relogio_s2'] else self.simulacao[-1]['tf_servico_relogio_s1']
            tf_servico_relogio_s2 = tempo_final_servico_relogio if self.simulacao[-1]['tf_servico_relogio_s1'] > self.simulacao[-1]['tf_servico_relogio_s2'] else self.simulacao[-1]['tf_servico_relogio_s2']
            tempo_cliente_sistema = t_fila + tes
            t_livre_operador_s1 = max([0, t_chegada_relogio -self.simulacao[-1]['tf_servico_relogio_s1']])
            t_livre_operador_s2 = max([0, t_chegada_relogio -self.simulacao[-1]['tf_servico_relogio_s2']])
        
        iteracao ={
                'cliente': cliente, 
                'tec': tec,
                't_chegada_relogio': t_chegada_relogio,
                'tes': tes,
                'ti_servico_relogio': ti_servico_relogio,
                't_fila': t_fila,
                'tf_servico_relogio_s1': tf_servico_relogio_s1,
                'tf_servico_relogio_s2': tf_servico_relogio_s2,
                't_cliente_sistema': tempo_cliente_sistema,
                't_livre_operador_s1': t_livre_operador_s1,
                't_livre_operador_s2': t_livre_operador_s2
                }
        self.simulacao.append(iteracao)
        
    def get_tabela(self):
          return pd.DataFrame(self.simulacao, columns=['cliente', 'tec', 't_chegada_relogio', 'tes', 'ti_servico_relogio', 't_fila', 'tf_servico_relogio_s1', 'tf_servico_relogio_s2', 't_cliente_sistema', 't_livre_operador_s1', 't_livre_operador_s2'])

class GeradorSimulacaoExponencialMM2:
    def __init__(self):
        """
            Gera uma simulação usando dist. exponencial com p < 1, ou seja,
            chegada < atendimento 
        """

        while True:
            vars = Variaveis()
            vars.set_tes(Distribuicoes.EXPONENCIAL.value['func'])
            vars.set_tec(Distribuicoes.EXPONENCIAL.value['func'])
            s = SimulacaoMM2(variaveis=vars, tempo_limite=10000)
            s.simular_tudo()
            df = s.get_tabela()
            chegada = sum(df['tec'])/len(df['cliente'])
            atendimento = sum(df['tes'])/len(df['cliente'])

            if atendimento > chegada:
                self.dfSimulacao = df
                break