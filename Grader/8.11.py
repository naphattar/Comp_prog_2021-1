def reverse(d):
    key,value = [],[]
    newd = {}
    for k in d:
        key.append(k)
        value.append(d[k])
    for i in range(len(key)):
        newd[value[i]] = key[i]
    return newd
 


def keys(d, v):
    result = []
    for key in d:
        if d[key] == v:
            result.append(key)
    return result

exec(input().strip()) 