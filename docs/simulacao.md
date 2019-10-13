## Módulo `simulacao`

### Classes

#### `Distribuicoes`
Define as diferentes distribuições disponibilizadas pela biblioteca.
```
NORMAL: enum
EXPONENCIAL: enum
POISSON: enum
BINOMIAL: enum
```

Uso: 
```python
Distribuicoes.POISSON.value['func']()
```

#### `Variaveis`
Define as variáveis disponibilizadas pela biblioteca. 
```
tec_funcao: method
tes_funcao: method
```

##### `set_tec`
Define o tempo esperado de chegada.

Params:
```
f: float
```

Uso: 
```python
vars = Variaveis()
vars.set_tec(Distribuicoes.EXPONENCIAL.value['func'])
```

##### `set_tes`
Define o tempo esperado de serviço.

Params:
```
f: float
```

Uso: 
```python
vars = Variaveis()
vars.set_tes(Distribuicoes.EXPONENCIAL.value['func'])
```

##### `get_tec`
Devolve o tempo esperado de chegada. Retorna um `float`. 

Uso: 
```python
vars = Variaveis()
vars.set_tec(Distribuicoes.EXPONENCIAL.value['func'])
vars.get_tec()
```

##### `get_tes`
Devolve o tempo esperado de serviço. Retorna um `float`. 

Uso: 
```python
vars = Variaveis()
vars.set_tes(Distribuicoes.EXPONENCIAL.value['func'])
vars.get_tes()
```

#### `Simulacao`
Gera uma simulação de acordo com os parâmetros definidos pelo usuário. 
```
variaveis: Variaveis
simulacao: list
tempo_limite: int
numero_clientes: int
```

##### `init`
Retorna um objeto do tipo `Simulacao`. 

Params:
```
variaveis: Variaveis (default = Variveis())
tempo_limite: int (default = -1)
clientes: int (default = -1)
```

Uso: 
```python
s = Simulacao(variaveis=vars, tempo_limite=1000)
```

##### `simular`
Método interno da classe utilizada para gerar uma iteração da simulação.

##### `simular_tudo`
Gera todas as iterações da simulação.

Uso: 
```python
s = Simulacao(variaveis=vars, tempo_limite=1000)
s.simular_tudo()
```

##### `get_tabela`
Devolve uma tabela contendo as informações da simulação inteira. Retorna um `DataFrame`.

Uso: 
```python
s = Simulacao(variaveis=vars, tempo_limite=1000)
s.simular_tudo()
s.get_tabela()
```

#### `GeradorSimulacaoExponencial`
Gera uma simulação utilizando a distribuição exponencial com p < 1. 
```
dfSimulacao: DataFrame
```

##### `init`
Retorna um objeto do tipo `DataFrame` contendo a simulação que utiliza distribuição exponencial. 

Uso: 
```python
dfS = GeradorSimulacaoExponencial()
```

#### `MM1`
Gera um modelo de filas do tipo M/M/1. 
```
chegada: float
atendimento: float
intensidadeTrafego: float
ociosidade: float
probabilidadeFila: float
l: float
ls: float
lq: float
w: float
ws: float
wq: float
```

##### `init`
Retorna um objeto do tipo `MM1`. 

Params:
```
df: DataFrame (default = None)
chegada: float (default = None)
atendimento: float (default = None)
```

Uso: 
```python
mm1 = MM1(df= df)
```

Uso: 
```python
mm1 = MM1(chegada = 10, atendimento = 15)
```

##### `setProbabilidadeFila`
Método interno da classe que calcula a probabilidade de haver fila no sistema. 

##### `setL`
Método interno da classe que calcula o número médio de clientes no sistema.

##### `setLs`
Método interno da classe que calcula o número esperado de clientes em atendimento no sistema.

##### `setLq`
Método interno da classe que calcula o número esperado de clientes na fila do sistema.

##### `setW`
Método interno da classe que calcula o tempo esperado gasto pelo cliente no sistema.

##### `setWs`
Método interno da classe que calcula o tempo esperado gasto no serviço. 

##### `setWq`
Método interno da classe que calcula o tempo esperado gasto na fila.

##### `calcularTudo`
Calcula todas as métricas do modelo de filas. 

Uso: 
```python
mm1 = MM1(df= df)
mm1.calcularTudo()
```

##### `plotMetricasGerais`
Exibe graficamente as seguintes métricas do sistema: taxa de chegada (λ), taxa de atendimento (μ), intensidade de tráfego (ρ), ociosidade (1 - ρ).

Uso: 
```python
mm1 = MM1(df= df)
mm1.calcularTudo()
mm1.plotMetricasGerais()
```

##### `plotMetricasTempo`
Exibe graficamente as métricas em relação a análise de tempo gasto do sistema, as quais são W, Ws e Wq.

Uso: 
```python
mm1 = MM1(df= df)
mm1.calcularTudo()
mm1.plotMetricasTempo()
```

##### `plotMetricasCliente`
Exibe graficamente as métricas em relação a análise do número de clientes do sistema, as quais são L, Ls e Lq.

Uso: 
```python
mm1 = MM1(df= df)
mm1.calcularTudo()
mm1.plotMetricasCliente()
```

##### `gerarTabelaMM1`
Gera uma tabela do modelo M/M/1. Retorna um objeto do tipo `DataFrame`.

Uso: 
```python
mm1 = MM1(df= df)
mm1.calcularTudo()
mm1.gerarTabelaMM1()
```