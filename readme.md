## `Simulação e M/M/1`

### `Instalação`
```
git clone https://github.com/rafael2ll/ms-mm1.git
```
### `Instalação de pacotes`
```bash
pip3 install -r requirements.txt
```
### `Uso`
```python
from simulacao import Distribuicoes
from simulacao import Variaveis
from simulacao import Simulacao
from simulacao import GeradorSimulacaoExponencial
from simulacao import MM1
```

### `Demo`
Para visualizar como a biblioteca pode ser utilizada para gerar simulações e modelos de fila M/M/1, cheque a [demonstração](https://github.com/rafael2ll/ms-mm1/blob/master/simulacao/Demo.ipynb), a qual contém alguns exemplos de código usando a biblioteca.

### `Interface`
Para executar o projeto com inserção de dados pelo usuário, execute o código a seguir:
```bash
python3 interface.py
```