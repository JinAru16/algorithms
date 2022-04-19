N = int(input())
count = 0
for _ in range(N):
    word_input = input()
    
    judge_list = []
    for i in range(len(word_input)):
        if word_input[i] not in judge_list:

            judge_list.append(word_input[i])
        else:
            if word_input[i-1] == word_input[i]:
                judge_list.append(word_input[i])
            else:
                break
    if len(word_input) == len(judge_list):
        count += 1
        
print(count)

