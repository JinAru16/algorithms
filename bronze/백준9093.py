input_line = int(input())

for j in range(input_line):
    input_strings = list(map(str, input().split()))
    arr = []
    sentance = ""

    for i in range(len(input_strings)):
        if i > 0:
            arr.append(" ")

        for k in range(len(input_strings[i])):
            arr.append((input_strings[i][len(input_strings[i])-1 - k]))
    for m in range(len(arr)):
        sentance += arr[m]
    print(sentance)



    # for string in input_strings:
