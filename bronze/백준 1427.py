numbers = str(input())
sorted_array = ''
new_lists = []
for number in numbers:
    str_to_num = int(number)
    new_lists.append(str_to_num)
new_lists.sort(reverse=True)

for list in new_lists:
    num_to_str = str(list)
    sorted_array += num_to_str

print(sorted_array)


