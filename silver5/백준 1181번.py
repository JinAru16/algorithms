N = int(input())
a = []
for _ in range(N):
    word_input = input()
    a.append(word_input)

set_a = set(a)

list_a = list(set_a)

list_a.sort()
list_a.sort(key=len)
a.sort(key=len)

for i in list_a:
    print(i)