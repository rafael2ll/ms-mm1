from simulacao.simulacao import *

if __name__ == '__main__':
    print('Simulaçao')
    forma_limitante = 0
    
    while forma_limitante < 1 or forma_limitante > 2:
        print('1.Limitar a  simulação por:\n\t1. Número máximo de clientes\n\t2. Número máximo de relógio')
        forma_limitante = int(input('Digite a opção desejada: '))
        if forma_limitante == 1:
            tempo_limite = -1
            numero_clientes = int(input('Digite o numero maximo de clientes a serem atendidos no dia: '))
        elif forma_limitante == 2:
            numero_clientes = -1
            tempo_limite = int(input('Digite o tempo máximo de relogio: '))
    
    print('Distruibuições disponíveis:')
    for e in Distribuicoes:
        print('- '+e.value['name'])
    print('- Constante')
    print('* Obs: Os valores constantes serao multiplicados por 10 posteriormente')
    
    distribuicao_tec, distribuicao_tes = '', ''
    while type(distribuicao_tec) == type(distribuicao_tes) == str:
        try:
            distribuicao_tec = input('Digite qual a distruição que será usada no tempo entre chegadas: ')
            if distribuicao_tec.lower() == 'constante':
                c = float(input('Digite o valor constante: '))
                distribuicao_tec = lambda: c
            else:
                distribuicao_tec = list(filter(lambda a: a.value['name'].lower() == distribuicao_tec.lower(), 
                                               [e for e in list(Distribuicoes)]))[0].value['func']
            
            distribuicao_tes = input('Digite qual a distruição que será usada no tempo de serviço: ')
            if distribuicao_tes.lower() == 'constante':
                c = float(input('Digite o valor constante: '))
                distribuicao_tes = lambda: c
            else:
                distribuicao_tes = list(filter(lambda a: a.value['name'].lower() == distribuicao_tes.lower(), 
                                               [e for e in list(Distribuicoes)]))[0].value['func']
        except Exception as e:
            print(e)
    vars = Variaveis()
    vars.set_tec(distribuicao_tec)
    vars.set_tes(distribuicao_tes)
    simulacao = Simulacao(variaveis = vars, tempo_limite =tempo_limite, clientes=numero_clientes)
    simulacao.simular_tudo()
    df = simulacao.get_tabela()
    print(df)
    mm1 = MM1(df)
    mm1.calcularTudo()
    gerais = mm1.plotMetricasGerais()
    cliente = mm1.plotMetricasCliente()
    tempo = mm1.plotMetricasTempo()