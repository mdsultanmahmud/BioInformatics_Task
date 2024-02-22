'''
problem - 1
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

'''
def cigar_party(cigars, is_weekend):
    if not is_weekend:
        if(cigars >= 40 and cigars<=60):
            return True 
        else: 
            return False
    else:
        if(cigars >= 40):
            return True
        else:
            return False 
        
# print(cigar_party(30, False))
# print(cigar_party(50, False))
# print(cigar_party(70, True))


'''
problem - 2
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

'''
def date_fashion(you, date):
    result = 1
    if(you >= 8 or date >= 8):
        result = 2
    if(you <=2 or date <=2):
        result = 0
    return result 
# print(date_fashion(5, 10) )
# print(date_fashion(5, 2))
# print(date_fashion(5, 5))
# print(date_fashion(10, 2))
# print(date_fashion(2, 9))    
# print(date_fashion(3, 7))

'''
problem - 3
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

'''
def squirrel_play(temp, is_summer):
    upper_lim = 90
    if(is_summer):
        upper_lim = 100
    if(temp >= 60 and temp <= upper_lim):
        return True
    else: return False
# print(squirrel_play(70, False))
# print(squirrel_play(95, False))
# print(squirrel_play(95, True))


'''
problem - 4
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

'''
def caught_speeding(speed, is_birthday):
    result = 0 
    if(is_birthday):
        if(speed <= 65):
            result = 0 
        elif(speed >= 66 and speed <= 85):
            result = 1 
        elif(speed >= 86):
            result = 2
    else:
        if(speed <= 60):
            result = 0 
        elif(speed >= 61 and speed <= 80):
            result = 1 
        elif(speed >= 81):
            result = 2
    return result 
# print(caught_speeding(60, False))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))

'''
problem - 5
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

'''
def sorta_sum(a, b):
    sum = a + b 
    if(sum >= 10 and sum <= 19):
        sum = 20 
    return sum 
# print(sorta_sum(3, 4))
# print(sorta_sum(9, 4))
# print(sorta_sum(10, 11))

'''
problem - 6
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

'''
def alarm_clock(day, vacation):
    alarm = "7.00"
    if((day == 0 or day == 6)):
        if not vacation:
            alarm = "10.00"
        else: alarm = "off"
    else:
        if not vacation:
            alarm = "7.00"
        else: alarm = "10.00"
    return "{0}".format(alarm) 
# print(alarm_clock(1, False))
# print(alarm_clock(5, False))
# print(alarm_clock(0, False))
# print(alarm_clock(0, True))
# print(alarm_clock(1, True))


'''
problem - 7
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

'''
def love6(a, b):
    sum = a +b 
    diff = a - b
    if(a ==  6 or b  == 6 or abs(diff) == 6 or sum == 6):
        return True
    else: return False 
# print(love6(6, 4))
# print(love6(4, 5))
# print(love6(1, 5))


'''
problem - 8
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

'''
def in1to10(n, outside_mode):
    if(outside_mode):
        if(n <= 1 or n>= 10):
            return True
        else: return False 
    else:
        if(n>=1 and n<=10):
            return True 
        else: return False 

# print(in1to10(5, False) )
# print(in1to10(11, False))
# print(in1to10(11, True) )


'''
problem - 9
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

'''
def near_ten(num):
    reminder = num % 10 
    return reminder <= 2 or reminder >= 8 
# print(near_ten(12))
# print(near_ten(17))
# print(near_ten(19))
    
