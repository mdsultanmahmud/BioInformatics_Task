'''
problem - 1
Given a string, return a string where for every char in the original, there are two chars.
'''

def double_char(str):
    new_str = '' 
    for i in range(len(str)):
        tem_s = str[i] * 2 
        new_str += tem_s
    return new_str 
# print(double_char("The"))
# print(double_char("AAbb"))
    
'''
problem  - 2
Return the number of times that the string "hi" appears anywhere in the given string.

'''
def count_hi(str):
    count = 0 
    word = 'hi'
    for i in range(len(str) - 1):
        tem_str = str[i] + str[i+1]
        if(tem_str == word):
            count += 1
    return count 
# print(count_hi("hihi"))
# print(count_hi("hihi baby hi"))
# print(count_hi("abc hi ho"))
# print(count_hi("ABChi hi"))

'''
problem - 3
Return True if the string "cat" and "dog" appear the same number of times in the given string.

'''
def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str) - 2):
        tem_str = str[i] + str[i+1] + str[i+2]
        if(tem_str == 'cat'):
            cat_count += 1
        if(tem_str == 'dog'):
            dog_count += 1
    if(cat_count == dog_count):
        return True 
    else: return False 
# print(cat_dog("catdog"))
# print(cat_dog("catcat"))
# print(cat_dog("1cat1cadodog"))

'''
problem - 4
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

breakdown: code ==> i and i+1 = co and i+2 = ja issa tai and i + 3 = e hlei cholbe
'''
def count_code(str):
    count = 0 
    for i in range(len(str) - 3):
        if(str[i:i+2] == 'co' and str[i+3] == 'e'):
            count += 1 
    return count 
# print(count_code("aaacodebbb"))
# print(count_code("codexxcode"))
# print(count_code("cozexxcope"))
    
'''
problem - 5
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

'''
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)
# print(end_other('Hiabc', 'abc') )
# print(end_other('AbC', 'HiaBc')) 
# print(end_other('abc', 'abXabc')) 
# print(end_other('Hiabcx', 'bc') )


'''
problem -- 6
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

'''
def xyz_there(str):
    status = False
    for i in range(len(str) -1):
        if(str[i:i+3] == 'xyz'):
            if(str[i-1] != '.'):
                status = True
            else: status = False
    return status
# print(xyz_there('abcxyz'))
# print(xyz_there('abc.xyz') )
# print(xyz_there('xyz.abc') )
# print(xyz_there('abc.xyzxyz'))