from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #Usado p indicar o metodo da classe.
    def listar_restaurante(cls):
        print(f'{'nome do restaurante'.ljust(25)} | {'Categoria do restaurante'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status do restaurante'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property #Usado para op matematicas, pegar valor e atribuir em um so valor, dar visiblidade para boleean em ves de aparecer 'TRUE' OU 'FALSE' aparecer as bolinhas. 
    def ativo(self):
        return '🟢' if self._ativo else '🔴'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_nota = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_d_nota = len(self._avaliacao)
        media = round(soma_das_nota / qtd_d_nota , 1)
        if media > 5:
            media = 5
        return media

    def add_cardapio (self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    

    
    @property
    def listar_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tipo'):
                mensagem_sobre = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho} | Tipo: {item.tipo}'
                print(mensagem_sobre)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)