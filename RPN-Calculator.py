


def convert(s):
    s = s.split(' ')
    s = list(s)
    aux = ''
    op = ''
    numStack = []
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
                        op = ''
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == '*' or (opStack[len(opStack)-1]) == '/':
                    if opStack[(len(opStack)-2)] == '*' or (len(opStack)-2) == '/' or (len(opStack)-2) == '^':
                        postfix.append(opStack[len(opStack) - 2])
                        del opStack[len(opStack) - 2]
                        op = ''
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == '^':
                    if opStack[(len(opStack) - 2)] == '^':
                        postfix.append(opStack[len(opStack) - 2])
                        del opStack[len(opStack) - 2]
                        op = ''
                elif len(opStack)>1 and (opStack[len(opStack)-1]) == ')':
                    for k in range (len(opStack)):
                        if opStack[k] != ')':
                            postfix.append(opStack[k])
                            del opStack[k]
                        else:
                            del opStack[k]

    if len(opStack) > 0:
        for l in range (len(opStack)):
            if opStack[l] != ')':
                postfix.append(opStack[l])
                del opStack[l]


    print(opStack)
    print()
    print('pilha RPN')
    print(postfix)
    print(opStack)

print('expressão infixa:')
infix = input()

convert(infix)