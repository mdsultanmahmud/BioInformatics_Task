# problem 1 

def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False

  

# result  = sleep_in(False, True) #True
# sleep_in(True, False)  #False
# sleep_in(False, True) #True
# print(result)
    
#correct 
    





'''
# problem 2 
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
'''

# solution 

def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True or a_smile !=  True and b_smile != True):
        return True 
    else:
        return False

# result   = monkey_trouble(True, False) 
# print(result)
    

'''
problem - 3

Given two int values, return their sum. Unless the two values are the same, then return double their sum.


'''

# solution 
def sum_double(a, b):
    sum = 0 
    if(a == b):
        sum = (a + b) * 2
    else:
        sum = a +b 
    return sum 

# sum_double(1, 2) 
# sum_double(3, 2) 
# sum_double(2, 2)

'''
problem - 4

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
'''
# solution 
def diff21(n):
    dif = abs(n - 21)
    if (n > 21):
        dif = dif * 2 
    return dif 
# diff21(25)

'''
problem - 5

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
'''
def parrot_trouble(talking, hour):
    if (talking == True):
        if(hour > 20 or hour < 7):
            return True
        else:
            return False 
    else:
        return False 
    
# res = parrot_trouble(False, 6)
# print(res)


'''
problem - 6

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
'''
def makes10(a, b):
    if(a == 10 or b == 10 or a +b == 10):
        return True 
    else:
        return False
    
# res = makes10(1,9)
# print(res)
    

'''
problem -- 7
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
'''

# solution 
def near_hundred(n):
    if (abs(n - 100) <= 10 or abs(n - 200) <= 10):
        return True 
    else:
        return False 

# res= near_hundred(195)
# print(res)


'''
problem - 8

Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
'''
# solution 
def pos_neg(a, b, negative):
    if(negative == True):
        if(a < 0 and b <0):
            return True
        else: 
            return False
    elif(a < 0 and b >0 or b <0 and a >0):
        return True 
    else: 
        return False
    
# res = pos_neg( 1, 1, True)
# print(res)
  

'''
problem -- 9
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


'''
def not_string(str):
    tem_str = str[:3]
    if(tem_str == 'not'):
        return str 
    else:
        return 'not ' + str 
    
# res = not_string('not bad')
# print(res)

'''
problem - 10

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
'''
def missing_char(str, n):
  if(n < 0 or n> len(str) - 1):
      return "Please enter a valid index!"
  else:
      return str[:n] + str[n+1:]
  
# res= missing_char('kitten', 4)
# print(res)
  
'''
problem -- 11
Given a string, return a new string where the first and last chars have been exchanged.

'''
def front_back(str):
    first_letter = str[0:1]
    last_letter = str[len(str) -1:]
    remaining_letter = str[1:len(str)-1]

    if(len(str) < 3):
        if(first_letter == last_letter):
            return first_letter
    return last_letter+ remaining_letter + first_letter
# res = front_back("aa")
# print(res)

'''
problem -- 12
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

'''
def front3(str):
    if(len(str) < 3):
        return str * 3
    else:
        tem_str = str[:3]
        return tem_str * 3
res = front3('ab')
print(res)
  


