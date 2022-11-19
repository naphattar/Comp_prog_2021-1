def f1(x): 
    c = []
    for i in range(len(x)):
        if x[i] in 'python':
            c.insert(len(c),i)
    return c
print(f1(["y","p"]))
def f2(x):
    return ["python".index(c[i]) if c[i] in "python"]
print(f2(["y","p"]))