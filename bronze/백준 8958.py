test_number = int(input())

for _ in range(test_number):
    test = list(str(input()))
    straight = 0
    sum = 0

    for i in range(len(test)):
        if test[i] == 'O':
            straight += 1
            sum += straight
            
        else:
            straight = 0
    print(sum)
    

