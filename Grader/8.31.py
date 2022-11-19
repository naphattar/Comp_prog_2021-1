def total(pocket):
    sum = 0
    for key in pocket :
        sum = sum+ int(key)*int(pocket[key])
    return sum
def take(pocket, money_in):
    for key in money_in:
        if key in pocket:
            pocket[key] = int(pocket[key])
            pocket[key] += int(money_in[key])
        else:
            pocket[key] = int(money_in[key])
    return pocket
def pay(pocket, amt):
    if amt > total(pocket):
        return {}
    else:
        money = []
        result = {}
        for key in pocket:
            money.append(key)
        money.sort()
        for i in range(len(money)-1,-1,-1):
            n = min(amt//(money[i]),pocket[money[i]])
            result[money[i]] = n
            pocket[money[i]] -= n
            if result[money[i]] == 0:
                del result[money[i]]
            amt = amt - (n*money[i])
        return result

exec(input().strip())
        