D = ['1','4','9','2','7','6','0','3','5','8']
pin_code = input()
encoded_pin_code = ''
for c in pin_code:
    encoded_pin_code += D[(12 + D.index(c)) % 10]
print(encoded_pin_code)