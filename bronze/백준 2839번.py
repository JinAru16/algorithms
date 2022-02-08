kgrams = int(input())
count = 0

while kgrams >= 0:
    if kgrams % 5 == 0:
        count += (kgrams // 5)
        print(count)
        break

    kgrams -= 3
    count += 1

else:
    print(-1)
