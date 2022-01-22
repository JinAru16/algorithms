
if __name__ == '__main__':
    equation = ''
    equationLength = int(input())

    for _ in range(equationLength + (equationLength-1)):
        equation += input()
    equation = equation.replace('/','//')
    print(eval(equation))

