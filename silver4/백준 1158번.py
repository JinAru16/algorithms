N, K = map(int, input().split())


a = [x for x in range(1, N+1)]
answer = []
circle_index = K - 1



for j in range(N):

    if len(a) > N:
        answer.append(a.pop(circle_index))
        circle_index += K-1
    elif len(a) <= N:
        circle_index = circle_index % len(a)
        answer.append(a.pop(circle_index))
        circle_index += K -1


print("<",', '.join(str(x) for x in answer), ">", sep= "")