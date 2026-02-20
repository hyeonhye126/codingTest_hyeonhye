N = int(input())

answer = 1

if N == 1:
    answer = 0
else:
    for i in range (N, N - 2, -1):
        answer *= i

print(answer)