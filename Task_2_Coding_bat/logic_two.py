'''
problem - 1
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
'''
def make_bricks(small, big, goal):
    bricks_length = big * 5 
    if goal > bricks_length:
        remaining_goal_len = goal - bricks_length 
        return remaining_goal_len <= small
    else:
        return goal <= small + bricks_length and goal % 5 <= small

# print(make_bricks(3, 2, 9))  
'''
problem - 2
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

'''
def lone_sum(a, b, c):
    sum = a +b + c
    if(a==b):
        sum = c 
    if(a ==c):
        sum = b 
    if(b == c):
        sum = a
    if(a ==b and b == c and a == c):
        sum = 0 
    
    return sum 

# print(lone_sum(3, 3,3))
# print(lone_sum(3, 2,3))
# print(lone_sum(1, 2,3))

'''
problem - 3
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
'''
def lucky_sum(a, b, c):
    sum = a +b + c
    if(a == 13):
        sum = 0 
    elif(b==13):
        sum = a 
    elif(c==13):
        sum = a +b 
    return sum 
# print(lucky_sum(1,2,3))
# print(lucky_sum(1,2,13))
# print(lucky_sum(1,13,13))
# print(lucky_sum(13,13,13))

'''
problem - 4
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
teen values ==> 13, 14, 17, 18, 19

'''
def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0 
    return n 
def no_teen_sum(a, b, c):
    sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
    return sum 
# print(no_teen_sum(1,2,3)) 
# print(no_teen_sum(2,1,14)) 
# print(no_teen_sum(2,13,1))

'''
problem - 5
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

'''
def round10(num):
    right_most_digit = num % 10 
    counting_value = num // 10
    if(right_most_digit >=5): 
        num = (counting_value + 1) * 10 
    elif(right_most_digit <5):
        num = counting_value * 10  
    return num 

def round_sum(a, b, c):
    sum = round10(a) + round10(b) + round10(c)
    return sum 
# print(round_sum(6, 5,4))
# print(round_sum(16, 17, 18))
# print(round_sum(16, 12, 18))

'''
problem - 6
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

'''
def close_far(a, b, c):
    status = False
    if(abs(a- b) < 2 and abs(a - c) >= 2 and abs(b -c) >= 2):
        status = True 
    elif abs(a-c) < 2 and abs(a-b)>=2 and abs(b-c) >=2:
        status= True
    else: status = False
    return status 

# print(close_far(1, 2, 10))    
# print(close_far(1, 2, 3))    
# print(close_far(4, 1, 3))    

'''
problem - 7
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

'''

def make_chocolate(small, big, goal):
    length_big_bars = big * 5 
    remaining_goal = 0 
    if(length_big_bars == goal):
        return 0 
    elif length_big_bars > goal:
        remaining_goal = goal % 5 
    else:
        remaining_goal = goal - length_big_bars 
    if(remaining_goal <= small):
        return remaining_goal  
    else: 
        return -1

# print(make_chocolate(4, 1, 9))
# print(make_chocolate(4, 1, 10))
# print(make_chocolate(4, 1, 7))
# print(make_chocolate(6,2,7))
# print(make_chocolate(4,1,4))
# print(make_chocolate(5,4,9))




