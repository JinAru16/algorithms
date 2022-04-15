X, Y = map(int, input().split())

def Rev(n):
    num_to_str = str(n)
    answer = ""
    for i in range(len(num_to_str)):
        answer += num_to_str[len(num_to_str)-1 - i]
    answer_to_num = int(answer)
    return (answer_to_num)

print(Rev(Rev(X) + Rev(Y)))