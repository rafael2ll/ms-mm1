## Módulo `variaveis`

### Classes

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