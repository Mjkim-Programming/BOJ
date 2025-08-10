N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda point: (point[1], point[0]))

for x, y in points:
    print(x, y)