i = 0
while True:    
    size, rpm, second = map(float, input().split())
    if rpm == 0 or second == 0:
        break
    pi = 3.1415927
    distance = ((pi*size*rpm)/12)/5280
    mph = (distance / second)*3600
    i += 1
    print('Trip #{}: {} {}'.format(i, format(distance, ".2f"), format(mph, ".2f")))