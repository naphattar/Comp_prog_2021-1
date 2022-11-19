def tar(x,n):
    return x**(1/2**n)

def cube_root(y):
    return y**((1/2**2)*(1+1/(2**2))*(1+1/(2**4))*(1+1/(2**8))*(1+1/(2**16))*(1+1/(2**32)))

def main():
    q = float(input())
    print(cube_root(q))

main()