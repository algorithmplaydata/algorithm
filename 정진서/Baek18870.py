N = int(input())
origin = list(map(int, input().split()))
sorted_array = sorted(origin)
ranking_dict = {}

rank = 0
for a in sorted_array:
    if a not in ranking_dict:
        ranking_dict[a] = rank
        rank += 1

result = []
for key in origin:
    ranking = ranking_dict[key]
    result.append(ranking)

print(*result)