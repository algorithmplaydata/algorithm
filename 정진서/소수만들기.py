
def solution(nums):
    count = 0
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1): ## num의 제곱근까지의 범위로 판별
            if num % i == 0:
                return False
        return True
    # 반복문으로 세 수의 합
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime(sum):
                    count += 1
                    
    return count
    
nums = [1,2,7,6,4]
solution(nums)