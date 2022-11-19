class Card:
 def __init__(self, value, suit):
     self.value = value
     self.suit = suit
 
 def __str__(self):
     return "("+str(self.value)+" "+str(self.suit)+")"
 
 def getScore(self):
     alpha = {"A":1,"J":10,"Q":10,"K":10}
     if self.value in "2345678910":
         return int(self.value)
     else:
         return alpha[self.value]
 
 def sum(self, other):
     score =  int(self.getScore() + other.getScore())
     return score%10

     
 
 def __lt__(self, rhs):
     val = {"J":11,"Q":12,"K":13,"A":14,"2":15}
     for i in range(3,11):
         val[str(i)] = i
     dok = {"club":1, "diamond":2, "heart":3, "spade":4}
     card1 = (val[self.value],dok[self.suit])
     card2 = (val[rhs.value],dok[rhs.suit])
     return card1 < card2
 
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].getScore())
print("----------")
for i in range(n-1):
 print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
 print(cards[i])