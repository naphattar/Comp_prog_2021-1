class Tweet:
  def __init__(self,tweet):
      self.tweet = tweet
      self.id = tweet["id"]
      self.user = tweet["user"]
      self.words = tweet["words"]
      self.time = tweet["time"]




  def __lt__(self,rhs):
      time1 = self.time
      time2 = self.time
      y1,m1,d1,h1,n1 = int(time1[0:4]),int(time1[5:7]),int(time1[8:10]),int(time1[11:13]),int(time1[14:16])
      y2,m2,d2,h2,n2 = int(time2[0:4]),int(time2[5:7]),int(time2[8:10]),int(time2[11:13]),int(time2[14:16])
      t1 = [y1,m1,d1,h1,n1]
      t2 = [y2,m2,d2,h2,n2]
      if t1< t2:
          return True
      elif t2>t1:
          return False
      else:
          return len(self.words) < len(rhs.words)




  def __str__(self):
      ans = ""
      words = " ".join(self.words)
      return str(self.time)+": "+"["+str(self.user)+"] "+words+" "+"("+str(self.id)+")"


  def similarity(self,other):
      word1 = set(self.words)
      word2 = set(other.words)
      inte = word1.intersection(word2)
      uni = word1.union(word2)
      return len(inte)/len(uni)



def find_similarity(tweets):
    ans = []
    for i in range(len(tweets)):
        for j in range(i+1,len(tweets)):
            tw1,tw2 = tweets[i],tweets[j]
            sim = tw1.similarity(tw2)
            result = (sim,(tw1.id,tw2.id))
            ans.append(result)
    ans.sort()
    return ans
        







def show_tweets(tweets):
    tweet = sorted(tweets)
    for i in range(len(tweet)):
        print(tweet[i])


tw1=Tweet({'id':1,'user':'abc','words':['this','is','a','blockchain','made','from','scratch','in','~50','lines','of','python','code'],'time':'2021-11-18 16:38'})
tw2=Tweet({'id':2,'user':'cdg','words':['javascript', 'java', 'python', 'php', 'and', 'their', 'learning', 'curves'],'time':'2021-11-06 14:28'})
tw3=Tweet({'id':3,'user':'def123','words':['python', 'and', 'javascript'],'time':'2021-11-01 07:56'})
tw4=Tweet({'id':4,'user':'def123','words':['only','python'],'time':'2021-11-01 07:56'})
tweets=[tw1,tw2,tw3,tw4]

print(find_similarity(tweets))