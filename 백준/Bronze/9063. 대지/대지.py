import sys
input = sys.stdin.readline

n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]

xs = [x for x, y in coords]
ys = [y for x, y in coords]

width = max(xs) - min(xs)
height = max(ys) - min(ys)

print(width * height)