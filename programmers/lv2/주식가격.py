def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            if (prices[j] - prices[i] >= 0):
                time += 1
            else:
                time += 1
                break
         
        answer.append(time)        
    return answer


a = [1, 2, 3, 2, 3]
print(solution(a))