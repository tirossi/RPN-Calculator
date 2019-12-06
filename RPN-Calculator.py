def calcular(postfix):
    auxStack = []

    for i in postfix:
        if i == "+":
            n1 = auxStack.pop()
            n2 = auxStack.pop()
            aux = n1 + n2
            auxStack.append(aux)
        elif i == "-":
            n1 = auxStack.pop()
            n2 = auxStack.pop()
            aux = n1 - n2
            auxStack.append(aux)
        elif i == "*":
            n1 = auxStack.pop()
            n2 = auxStack.pop()
            aux = n1 * n2
            auxStack.append(aux)
        elif i == "/":
            n1 = auxStack.pop()
            n2 = auxStack.pop()
            aux = n1 / n2
            auxStack.append(aux)
        elif i == "^":
            n1 = auxStack.pop()
            n2 = auxStack.pop()
            aux = n1 ** n2
            auxStack.append(aux)
        else:
            auxStack.append(i)

    print('O resultado de ' + infix + ' é:')
    print(auxStack)

def convert(s):
    s = s.split(' ')
    s = list(s)
    opStack = []
    postfix = []

    for i in range (len(s)):
        if s[i] != '(':
            if s[i].isnumeric():
                postfix.append(int(s[i]))
            else:
                op = s[i]
                opStack.append(op)
                if len(opStack)>1 and (opStack[len(opStack)-1] == '+' or opStack[len(opStack)-1] == '-'):
                    if opStack[(len(opStack)-2)] == '+' or (len(opStack)-2) == '-' or opStack[(len(opStack)-2)] == '*' or opStack[(len(opStack)-2)] == '/' or opStack[(len(opStack)-2)] == '^':
                        postfix.append(opStack[len(opStack) - 2])
                        del opStack[len(opStack) - 2]
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == '*' or (opStack[len(opStack)-1]) == '/':
                    if opStack[(len(opStack)-2)] == '*' or (len(opStack)-2) == '/' or (len(opStack)-2) == '^':
                        postfix.append(opStack[len(opStack) - 2])
                        del opStack[len(opStack) - 2]
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == '^':
                    if opStack[(len(opStack) - 2)] == '^':
                        postfix.append(opStack[len(opStack) - 2])
                        del opStack[len(opStack) - 2]
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == ')':
                    while len(opStack) > 1:
                        postfix.append(opStack[len(opStack)-2])
                        del opStack[len(opStack)-2]
                    del opStack[len(opStack)-1]


    if len(opStack) !=0:
        for i in (opStack):
            postfix.append(i)
            opStack.pop()

    print('pilha RPN')
    print(postfix)
    calcular(postfix)
print('----------------------------------------------------------------------------------------------------------')
print('Para que o programa funcione corretamente, é necessário que tudo esteja espaçado, inclusive os parêntesis')
print('----------------------------------------------------------------------------------------------------------')
print('expressão infixa:')
infix = input()

convert(infix)