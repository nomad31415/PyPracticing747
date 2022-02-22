import collections



Card = collections.namedtuple('Card', ['rank', 'suit'])

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()




cards = [Card(rank, suit) for suit in suits
for rank in ranks]


print(cards)











