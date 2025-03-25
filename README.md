# Projeto: Restaurante em Python

## Descrição
Este repositório contém um projeto de um sistema de restaurante desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O projeto inclui funcionalidades como gerenciamento de cardápio, avaliações de clientes e aplicação de descontos.

## Funcionalidades
- Cadastro e listagem de restaurantes
- Adição de pratos, bebidas e sobremesas ao cardápio
- Sistema de avaliação de restaurantes
- Aplicação de descontos
- Utilização de classes abstratas e herança
- Uso de propriedades (@property) e métodos de classe (@classmethod)

## Estrutura do Projeto
```
projeto_restaurante/
│-- modelos/
│   │-- restaurante.py
│   │-- avaliacao.py 
│   │-- restdocumentdo.py
│   ├── cardapio/
│   │   │-- item_cardapio.py
│   │   │-- bebida.py
│   │   │-- prato.py
│   │   └── sobremesa.py
│-- app.py
│-- README.md
```

## Conceitos Aprendidos e Aplicados

### @property
- Permite criar métodos que podem ser acessados como atributos.
- Foi utilizado para exibir o status do restaurante com emojis.

```python
def ativo(self):
    return '🟢' if self._ativo else '🔴'
```

### @classmethod
- Define métodos que atuam a nível de classe, e não de instância.
- Utilizado para listar todos os restaurantes cadastrados.

```python
@classmethod
def listar_restaurantes(cls):
    for restaurante in cls.restaurantes:
        print(f"{restaurante._nome} - {restaurante.categoria} - {restaurante.ativo}")
```

### Criação de Classes e Herança
- Criamos a classe `ItemCardapio` como classe base.
- As classes `Bebida`, `Prato` e `Sobremesa` herdam de `ItemCardapio`.
- Uso de `super()` para reaproveitar atributos e métodos.

```python
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
```

### Classes Abstratas
- Implementamos a classe `ItemCardapio` como abstrata, garantindo que todas as subclasses tenham o método `aplicar_desconto`.

```python
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    @abstractmethod
    def aplicar_desconto(self):
        pass
```

### Sistema de Avaliação
- Criamos a classe `Avaliacao` para armazenar nome do cliente e nota.
- Implementamos um sistema para calcular a média das avaliações.

```python
@property
def media_avaliacoes(self):
    if not self._avaliacao:
        return 0
    soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
    return round(soma / len(self._avaliacao), 1)
```

### Listagem do Cardápio
- Criamos uma lista `_cardapio` dentro de `Restaurante`.
- Implementamos um método para listar os itens do cardápio.

```python
@property
def listar_cardapio(self):
    print(f'Cardápio do restaurante {self._nome}\n')
    for i, item in enumerate(self._cardapio, start=1):
        print(f"{i}. {item._nome} - R${item._preco}")
```

## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/projeto_restaurante.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd projeto_restaurante
   ```
3. Execute o arquivo `app.py`:
   ```bash
   python app.py
   ```

## Melhorias Futuras
- Implementação de um sistema de pedidos
- Integração com um banco de dados
- Interface gráfica

---
Este projeto foi desenvolvido para fins de estudo e aprimoramento dos conceitos de POO em Python. 🚀
