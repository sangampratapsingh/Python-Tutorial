# Operators in Python:
# Arthematic Operator
# Assignment Operator
# Comparison Operator
# Logical Operator
# Identity Operator
# Membership Operator
# Bitwise Operator

# Arthematic Operator

# Arithmetic operators are used with numeric values to perform common mathematical operations:
#      Operator             Name                                                Example
#      +                    Addition                                            x + y
#      -                    Subtraction                                         x - y
#      *                    Multiplication                                      x * y
#      /                    Division                                            x / y
#      %                    Modulus(Gives Remainder)                            x % y
#      **                   Exponentiation                                      x ** y
#      //                   Floor division(Gives integer value of quotient)     x // y

print("5+6 is", 5+6)
print("5-6 is", 5-6)
print("5*6 is", 5*6)
print("5/6 is", 5/6)
print("5//6 is", 5//6)
print("5**6 is", 5**6)
print("5%6 is", 5%6)
# Assignment Operators:-
# Assignment operators are used to assign values to variables:

# Operator Example Same As
# = x = 5 x = 5
# += x += 3 x = x + 3
# -= x -= 3 x = x - 3
# *= x *= 3 x = x * 3
# /= x /= 3 x = x / 3
# %= x %= 3 x = x % 3
# //= x //= 3 x = x // 3
# **= x **= 3 x = x ** 3
# &= x &= 3 x = x & 3
# |= x |= 3 x = x | 3
# ^= x ^= 3 x = x ^ 3
# >>= x >>= 3 x = x >> 3
# <<= x <<= 3 x = x << 3
# print("Assignment Operators")

# x=2
# print(x)
# x **= 3
# print(x)

# Comparison Operator
#Comparison operators are used to compare two values:

# Operator Name Example
# == Equal x == y
# != Not equal x != y
# > Greater than x > y
# < Less than x < y
# >= Greater than or equal to x >= y
# <= Less than or equal to x <= y

# i=8
# print(i==5)
# print(i!=8)
# print(i>8)
# print(i<8)
# print(i>=8)
# print(i<=8)

# Logical Operators
# Logical operators are used to combine conditional statements:

#     Operator                    Description                                                         Example
#     and                         Returns True if both statements are true                            x < 5 and x < 10
#     or                          Returns True if one of the statements is true                       x < 5 or x < 4
#     not                         Reverse the result, returns False if the result is true             not(x < 5 and x < 6)

a=True
b=False

print(a and a)
print(b and a)
print(b and b)

print(a or a)
print(b or a)
print(b or b)

var = not (a and b)
print(var)

#Identity Operators
#Identity operators are used to compare the objects, not if they are equal,
#but if they are actually the same object, with the same memory location:

# Operator       Description                                                          Example
# is             Returns True if both variables are the same object                   x is y
# is not         Returns True if both variables are not the same object               x is not y

a=True
b=False

print(a is b)
print(a is not b)

# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

#             Operator            Description                                         Example
#             in                  Returns True if a sequence with the
#                                 specified value is present in the object            x in y
#             not in              Returns True if a sequence with the
#                                 specified value is not present in the object        x not in y
l1 = [1,2,3,4,5]
print(2 in l1)
print(2 not in l1)

# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
#      Operator           Name             Description
#      &                  AND              Sets each bit to 1 if both bits are 1
#      |                  OR               Sets each bit to 1 if one of two bits is 1
#      ^                  XOR              Sets each bit to 1 if only one of two bits is 1
#      ~                  NOT              Inverts all the bits
#     <<                  Zero             fill left shift Shift left by pushing zeros in from the right
#                                          and let the leftmost bits fall off
#     >>                  Signed           right shift Shift right by pushing copies of the leftmost bit in
#                                          from the left, and let the rightmost bits fall off
