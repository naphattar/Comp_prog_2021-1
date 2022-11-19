def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    if  gcd(a,b)==1 or  gcd(b,c) == 1 or gcd(a,c) == 1:
        return True
    else:
        return False

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(1,max_len+1):
        for b in range(c,0,-1):
            for a in range(1,b):
                if is_coprime(a,b,c) and a**2+b**2 == c**2:

                    triple.append([a,b,c])        
    
    return triple

exec(input().strip())
