N = int(input())

if N == 4 or N == 7:
    print(-1)
elif N % 5 == 0:
    print(N // 5)
elif N % 5 == 4 or N % 5 == 2:
    print((N // 5) + 2)
elif N % 5 == 1 or N % 5 == 3:
    print((N // 5) + 1)


# N = int(input())

# if N % 5 == 0:
#     print(N // 5)
# elif N % 5 == 4 or N % 5 == 2:
#     print((N // 5) + 2)
# elif N % 5 == 1 or N % 5 == 3:
#     print((N // 5) + 1)
# else:
#     print(-1)
