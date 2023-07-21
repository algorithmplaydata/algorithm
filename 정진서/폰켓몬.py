from collections import Counter

def solution(nums):
    answer = []
    nums_poke = Counter(nums)
    N = len(nums)//2

    return min(len(nums_poke), N)
solution(nums=[3,3,3,2,2,2])