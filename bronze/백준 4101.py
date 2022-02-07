

while (True):
    first_number, second_number = map(int, input().split())

    if first_number > second_number:
        print("Yes")

    elif first_number==0 and second_number==0:
        break
    else:
        print("No")