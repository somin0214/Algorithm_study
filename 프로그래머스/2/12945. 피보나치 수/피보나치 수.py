def solution(n):

    nums = [0, 1]
    
    for i in range(2, n+1):
        nums.append((nums[i-1]+ nums[i-2]) % 1234567)
    
    return  nums[-1]