## Módulo `simulacao`

### Classes

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