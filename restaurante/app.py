from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_big = Restaurante('Big', 'Gourmet')

bebida_suco = Bebida('Suco De Maracuja', 5.0, '400ML')
prato_pao = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
restaurante_big.add_cardapio(bebida_suco)
restaurante_big.add_cardapio(prato_pao)

sobre = Sobremesa('Leitinho', 5.00, 'Doce', 'Médio')
restaurante_big.add_cardapio(sobre)
def main():
    restaurante_big.listar_cardapio

if __name__ == '__main__':
    main()