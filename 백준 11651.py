count = int(input())

coord_list = []

for i in range(count):
    coordi = list(map(int, input().split()))
    #y_coord = coordinates[1]
    #x_coord = coordinates[0]
    coord_list.append(coordinates)

coord_list.sort(key=lambda x : ((x[1],x[0])))
for i in coord_list:
    print(i[0], i[1])
