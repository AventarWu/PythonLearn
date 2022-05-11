# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:43:28 2022

@author: wh878
"""

#it's a new file

import collections

cards = collections.namedtuple('card', ['rank', 'number'])

class Card:
     number = [str(n) for n in range(2,10)] + list('JQKA')
     rank   = 'spades diamonds clubs hearts'.split()
     
     def __init__(self):
         self._cards = [cards(n,m) for n in self.rank 
                                   for m in self.number]
         
     def __getitem__(self, pos):
         return self._cards[pos]
         
     def __len__(self):
         return len(self._cards)
     
     def __foo4__(self):
         return 1


color = ['w','b', 'r']
size  = [1,2,3,4]

t = ('c=%r, s=%r' % (c, s) for c in color for s in size)