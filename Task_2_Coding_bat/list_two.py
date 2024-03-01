'''
problem - 1
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
'''

def count_evens(nums):
    count  = 0 
    for num in nums:
        if num % 2 == 0:
            count += 1 
    return count 

# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))

'''
problem - 2
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
'''
def big_diff(nums):
    min_value = min(nums)
    max_value = max(nums)
    dif = max_value - min_value
    return dif 
# print(big_diff([10, 3, 5, 6]))
# print(big_diff([7, 2, 10, 9]))
# print(big_diff([2, 10, 7, 2]))

'''
problem - 3
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

'''
def centered_average(nums):
    avg = 0 
    if(len(nums) < 3):
        return 0 
    else: 
        nums.sort()
        new_list = nums[1:-1]
        avg = sum(new_list) / (len(new_list))
    return int(avg)
# print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))
# print(centered_average([-10, -4, -2, -4, -2, 0]))

'''
problem - 4
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

'''
def sum13(nums):
    if(nums == []):
        return 0 
    else: 
        for i in range(len(nums) -1):
            if(nums[i] == 13):
                del nums[i]
                del nums[i+1]
    print(nums)

print(sum13([]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([1, 2, 2, 1, 13, 12]))
