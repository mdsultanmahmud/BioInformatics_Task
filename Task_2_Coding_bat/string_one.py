'''
problem - 1
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
'''
def hello_name(name):
  return "Hello " + name +'!'

# res = hello_name('X')
# print(res)

'''
problem  - 2
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
'''
def make_abba(a, b):
    return a + b + b + a 
# res = make_abba("Hi", "Bye")
# print(res)

'''
problem - 3
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
'''
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
# res=  make_tags('i', 'Hello')
# print(res)

'''
problem - 4
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

'''
def make_out_word(out, word):
    first_char = out[:2]
    last_char = out[2:]
    text = "{0}{1}{2}".format(first_char, word, last_char)
    return text
# res =make_out_word('[[]]', 'word') 
# print(res)

'''
problem - 5
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
'''
def extra_end(str):
    if(len(str)<2):
        return 0 
    last_char = str[-2:]
    copied = last_char * 3 
    return copied 
# print(extra_end("Sultan"))

'''
problem - 6
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

'''
def first_two(str):
  if(len(str) < 2):
     return str 
  else:
     return str[:2]
# print(first_two(""))

'''
problem - 7
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

'''
def first_half(str):
    ran = int(len(str) / 2)
    return str[:ran]
# print(first_half("HelloThere"))
# print(first_half("abcdef"))

'''
problem - 8
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

'''
def without_end(str):
    if(len(str) <2):
       return 0
    return str[1:-1]
# print(without_end("java")) 
# print(without_end("coding")) 

'''
problem -- 9
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
'''
def combo_string(a, b):
   if(len(a) > len(b)):
      return b + a + b 
   else: 
      return a + b + a 
# print(combo_string("Hello", "Hi"))
# print(combo_string('aaa', 'b'))
# print(combo_string('hi', 'Hello') )

'''
problem- 10
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

'''
def non_start(a, b):
    if(len(a) < 1 or len(b) < 1):
       return 0 
    return a[1:] + b[1:]

# print(non_start("hello", 'there'))
# print(non_start("java", 'code'))
# print(non_start("shotl", 'java'))

'''
problem - 11
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

'''
def left2(str):
    if(len(str) <2):
       return 0 
    elif(len(str) == 2):
       return str 
    first_two = str[:2]
    remaing_char = str[2:]
    new_str = remaing_char + first_two 
    return new_str

print(left2("Hello"))
print(left2("java"))
print(left2("Hi"))





