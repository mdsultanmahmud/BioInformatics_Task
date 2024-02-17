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



    

