## Módulo `MM1`

### Classes

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
Retorna um objeto do tipo `MM2`. 

Params:
```
df: DataFrame (default = None)
chegada: float (default = None)
atendimento: float (default = None)
```

Uso: 
```python
mm2 = MM2(df= df)
```

Uso: 
```python
mm2 = MM2(chegada = 10, atendimento = 15)
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
mm2 = MM2(df= df)
mm2.calcularTudo()
```

##### `plotMetricasGerais`
Exibe graficamente as seguintes métricas do sistema: taxa de chegada (λ), taxa de atendimento (μ), intensidade de tráfego (ρ), ociosidade (1 - ρ).

Uso: 
```python
mm2 = MM2(df= df)
mm2.calcularTudo()
mm2.plotMetricasGerais()
```

##### `plotMetricasTempo`
Exibe graficamente as métricas em relação a análise de tempo gasto do sistema, as quais são W, Ws e Wq.

Uso: 
```python
mm2 = MM1(df= df)
mm2.calcularTudo()
mm2.plotMetricasTempo()
```

##### `plotMetricasCliente`
Exibe graficamente as métricas em relação a análise do número de clientes do sistema, as quais são L, Ls e Lq.

Uso: 
```python
mm2 = MM1(df= df)
mm2.calcularTudo()
mm2.plotMetricasCliente()
```

##### `gerarTabelaMM1`
Gera uma tabela do modelo M/M/2. Retorna um objeto do tipo `DataFrame`.

Uso: 
```python
mm2 = MM2(df= df)
mm2.calcularTudo()
mm2.gerarTabelaMM1()
```