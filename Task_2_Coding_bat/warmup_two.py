'''
problem -1
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


'''
def string_times(str, n):
    return str *n 
# res = string_times("Hi", 1)
# print(res)

'''
problem - 2
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


'''

def front_times(str, n):
    if(len(str) < 3):
        return str * n
    else:
        tem_str = str[:3]
        return tem_str * n
# res = front_times('not bad', 5)
# print(res)
    
'''
problem - 3
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
'''
def string_bits(str):
    return str[::2]

'''
problem - 4
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''
def string_splosion(str):
    tem_str = ''
    for i in range(0,len(str)):
        tem_str += str[:i+1]
    return tem_str  

# res = string_splosion('ab')
# print(res)


'''
problem - 5 
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
'''
def last2(str):
    if len(str) < 2:
        return "String is too short!!"
    last_two_char = str[-2:]
    count = 0 
    for i in range(len(str)-1):
        sub_str = str[i:i+2]
        if sub_str == last_two_char:
            count += 1            
    if(count >=1):
        return  count - 1
    return count

# res = last2('hixx')
# print(res)


'''
problem - 6
Given an array of ints, return the number of 9's in the array.
'''
def array_count9(nums):
    count = 0 
    for i in nums:
        if i == 9:
            count += 1
    return count 

# res = array_count9([1,4,5,9, 4,9,5,8,9, 85,9])
# print(res)

'''
problem - 7
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
'''

def array_front9(nums):
    array_range = 4 
    count = 0 
    if len(nums) < 4:
        array_range = len(nums)
    for i in range(array_range):
        if nums[i] == 9:
            count += 1
    if count:
        return True
    else:
        return False
# res = array_front9([1, 2, 3,4,9]) 
# print(res)

'''
problem - 8
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''
def array123(nums):
    spefic_list = [1,2,3]
    status = False
    for i in range(len(nums)):
        if(nums[i:i+3] == spefic_list):
            status = True
    return status
# res = array123([1, 1, 2, 1, 2, 3]) 
# print(res)


'''
problem - 9
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''

def string_match(a, b):
    count = 0
    if(len(a) > len(b)):
        for i in range(len(b) - 1):
            
            if(b[i:i+2] == a[i:i+2]):
                count += 1
    else:
        for i in range(len(a) - 1):
            
            if(a[i:i+2] == b[i:i+2]):
                count += 1
    return count 
res = string_match('xxcaazz', 'xxbaaz')
print(res)
    

