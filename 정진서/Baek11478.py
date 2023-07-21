s = input()

substrings_set = set()
for i in range(len(s)):
    start_index = 0
    end_index = i + 1
    while end_index <= len(s):
        substrings_set.add(s[start_index:end_index]) # 슬라이스는 자동으로 범위를 조정함
        start_index += 1
        end_index += 1

print(len(substrings_set))