k = int(input())

def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # recursion case

     # 캐시(사전)에 저장된 값이 없다면 캐시에 저장
    if n not in cache.keys():
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]




def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

print(fib(k))