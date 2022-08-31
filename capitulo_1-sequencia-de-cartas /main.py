#### collections.namedtuple constrói uma classe simples 
#### para representar cartas individuais, coleções de atributos com nenhum métodos personalizados
#### como um registro de banco de dados

import collections
from random import choice
from os import system 
system('clear')
 
Card = collections.namedtuple('Card', ['rank', 'suit']) # rank = 

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 
    suits = 'spades diamonds clubs hearts'.split() # suits = naipe

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card) # Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(len(deck)) # 52

# usando o __getitem__

print(deck[0]) # Card(rank='2', suit='spades')
print(deck[-1]) # Card(rank='A', suit='hearts')

# pegar uma carta aleatória

print(choice(deck)) # cada vez sairá um valor diferente
print(choice(deck))
print(choice(deck))

print(deck[:3]) # retorna os três primeiros [Card(rank='2', suit='spades'), 
#Card(rank='3', suit='spades'), 
#Card(rank='4', suit='spades')]

print(deck[12::13]) # só os de índice 12 e pulando o de 13
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), 
# Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

for card in deck:
    print(card)

# Card(rank='2', suit='spades') ... Card(rank='A', suit='hearts')

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck) # True
print(Card('7', 'beasts') in deck) # False
