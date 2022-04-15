self_list = []
self_creater = []

def dn(n):
    str_n = str(n)
    for i in range(len(str_n)):
        n += int(str_n[i])
    return n



for i in range(0, 10000):
    self_num = dn(i)
    if self_num not in self_list:
        self_list.append(self_num)
    else:
        continue

for j in range(0, 10000):
    if j not in self_list:
        print(j)