'''
problem - 1
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

'''
def first_last6(nums):
    first_ele = nums[0]
    last_ele = nums[len(nums) - 1]
    if(first_ele == 6 or last_ele == 6):
        return True 
    else:
        return False 

# print(first_last6([6,1, 2, 6,5]))
    
'''
problem - 2
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

'''
def same_first_last(nums):
    if(len(nums) > 1):
        if(nums[0] == nums[len(nums) -1]):
            return True 
        else: 
            return False 
    else:
        return False 
  
# print(same_first_last([1, 2, 3]))
# print(same_first_last([1, 2, 3, 1]))
    
'''
problem - 3
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

'''
def make_pi():
    return [3,1,4]

'''
problem - 4
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
'''
def common_end(a, b):
    if(len(a) > 0 and len(b) > 0):
        if(a[0] == b[0] or a[len(a)-1] == b[len(b) -1]):
            return True 
        else: 
            return False 
    else:
        return False 
# print(common_end([1, 2, 3], [10, 3, 2]))
# print(common_end([1, 2, 3], [7, 3]))
# print(common_end([1, 2, 3], [1, 3]))

'''
problem -- 5
Given an array of ints length 3, return the sum of all the elements.

'''
def sum3(nums):
    sum = 0 
    for n in nums:
        sum += n 
    return sum 
# print(sum3([1, 2, 3]))


'''
problem -- 6
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
'''
def rotate_left3(nums):
    first_el = nums[0]
    remaining_el = nums[1:]
    
    return remaining_el + [first_el]
# print(rotate_left3([7, 0 , 0]))


'''
problem - 7
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

'''
def reverse3(nums):
    nums.reverse()
    return nums 
# print(reverse3([1, 2, 3]) )

'''
problem - 8
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

'''
def max_end3(nums):
    first_el  = nums[0]
    last_el = nums[len(nums) - 1]
    if(first_el > last_el):
        for i in range(len(nums)):
            nums[i] = first_el
    else:
        for i in range(len(nums)):
            nums[i] = last_el
    return nums 
# print(max_end3([1, 2, 3]) )

'''
problem - 9
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

'''
def sum2(nums):
    sum = 0 
    if(len(nums) == 0):
        sum = 0 
    elif(len(nums) <2):
        for i in nums:
            sum += i 
    else: 
        for i in range(2):
            sum += nums[i]
    return sum  
# print(sum2([1,1 ,1,1]))
# print(sum2([1, 2, 3]))
# print(sum2([1,1]))

'''
problem -- 10
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
'''
def middle_way(a, b):
    new_list = [a[1]] + [b[1]]
    return new_list
# print(middle_way([1, 2, 3], [4, 5, 6]))
# print(middle_way([7, 7, 7], [3, 8, 0]) )

'''
problem -- 11
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

'''
def make_ends(nums):
    
    if(len(nums) <1):
        return 0
    else:
        first_el = nums[0]
        last_el = nums[len(nums) - 1]
        return [first_el, last_el]
# print(make_ends([1, 2, 3]))
# print(make_ends([1, 2, 3, 4]))

'''
problem - 12
Given an int array length 2, return True if it contains a 2 or a 3.
'''
    
def has23(nums):
    status = False 
    for i in nums:
        if (i== 2 or i == 3):
            status = True
    return status
# print(has23([2, 5]))
# print(has23([0, 5, 3]))


    
