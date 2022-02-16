
while True:
    n = input()
    palindrom = n[::-1]
    if n=='0':
        break

    if n==palindrom:
        print('yes')
    else:
        print('no')