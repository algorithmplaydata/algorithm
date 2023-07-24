N = int(input())

for _ in range(N):
    R, s = map(str, input().split())

    for char in s:
        print(char * int(R), end="")

    print()