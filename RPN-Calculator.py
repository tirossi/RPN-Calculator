def separate(s):
    s = s.split(' ')
    s = list(s)
    numStack = []
    opStack = []
    postfix = []

    for i in range (len(s)):
        if s[i].isnumeric():
            num = s[i]
            numStack.append(num)
        else:
            op = s[i]
            opStack.append(op)
    print('pilha sinais:')
    print(s)
    print('pilha números:')
    print(numStack)
    print('pilha operadores:')
    print(opStack)

print('expressão infixa:')
infix = input()

separate(infix)