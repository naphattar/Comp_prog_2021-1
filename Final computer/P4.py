NP = { 'Kaeng Krachan': {'Phetchaburi', 'Prachuap Khiri Khan'},
       'Khao Sam Roi Yot' : {'Prachuap Khiri Khan'},
       'Khao Yai' : {'Prachinburi', 'Nakhon Nayok', 'Saraburi', 'Nakhon Ratchasima'},
       'Mae Wong': {'Kamphaeng Phet', 'Nakhon Sawan'},
       'Khlong Wang Chao' : {'Kamphaeng Phet', 'Tak'},
       'Thap Lan': {'Prachinburi', 'Nakhon Ratchasima'}
     }
def has_np(NP,p):
    allpro = set()
    for i in NP:
        pro = NP[i]
        allpro = allpro.union(pro)
    if p in allpro:
        return True
    else:
        return False

def find_parks(NP, p):
    ans = []
    for name in NP:
        pro = NP[name]
        if p in pro:
            ans.append(name)
    ans.sort()
    return ans

def print_greenest_province(NP):
    ans = []
    maxi = 0
    allpro = set()
    for i in NP:
        pro = NP[i]
        allpro = allpro.union(pro)
    allpro = list(allpro)
    allpro.sort()
    for i in allpro:
        n = len(find_parks(NP,i))
        maxi = max(n,maxi)
    for i in range(len(allpro)):
        if len(find_parks(NP,allpro[i])) == maxi:
            ans.append(allpro[i])
    
NP = dict()
while True:
    d = input().split(' : ')
    if len(d) == 1 : 
        break
    else:
        pro = d[0]
        park = d[1]
        if park in NP:
            NP[park] = (NP[park]).union({pro})
        else:
            NP[park] = {pro}
for key in NP:
    listpark = sorted(list(NP[key]))
    NP[park] = set(listpark)



print(NP)     

 
