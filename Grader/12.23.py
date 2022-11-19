class Card:
 def __init__(self, value, suit):
     self.value = value
     self.suit = suit
 
 def __str__(self):
     return "("+str(self.value)+" "+str(self.suit)+")"

 
 def next1(self):
     val = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
     dok = ["club", "diamond", "heart", "spade"]
     valpos,suitpos= val.index(self.value),dok.index(self.suit)
     newsuit = dok[(suitpos+1)%4]
     if (suitpos+1)%4 ==0:
         newval = val[(valpos+1)%13]
     else:
         newval = self.value
     newcard = Card(newval,newsuit)
     return newcard
        



     
 
 def next2(self):
     val = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
     dok = ["club", "diamond", "heart", "spade"]
     valpos,suitpos= val.index(self.value),dok.index(self.suit)
     self.suit = dok[(suitpos+1)%4]
     if  (suitpos+1)%4 == 0:
         self.value = val[(valpos+1)%13]
     
    
 
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])