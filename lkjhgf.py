# what,*marks = input().split()
# op = []

# print(what,marks)


# marks = ",".join(marks)
# op.append(marks)
# print(op)


# i ['k', ' ', '9', '0', ' ', '8', '9', ' ', '7', '8', ' ', '6', '7']

# lis = [9,8,7,7,89,9]


# s = "neelima navik"

# lis = s.strip().split()
# final_s = []
# first , second = lis[0] , lis[1]
# first = first.capitalize()
# second = second.capitalize()
# final_s.append(first)
# final_s.append(second)

# final_s = " ".join(final_s)

# print(final_s)

# s = "1 2 2 3 4 5 6 7 8  9"

# lis, *other = s.strip().split()

# final_s = []
# lis = lis.capitalize()

# final_s.append(lis)
# for i in other:
#     if i.isdigit():
#         print(i,end="")
    
#     # i = i.capitalize()
#     # final_s.append(i)

# final_s = " ".join(final_s)
# print(final_s)

# s = "1 2 2 3 4 5 6 7 8  9"

# lis, *other = s.strip().split()  # .split() already handles extra spaces
# final_s = []

# lis = lis.capitalize()
# final_s.append(lis)

# for i in other:
#     if i.isdigit():
#         print(i, end="")
#     i = i.capitalize()
#     final_s.append(i)

# final_s = " ".join(final_s)
# print(final_s)

# k = "String"
# k[1] = "p"

# print(k)

# import textwrap
# def merge_the_tools(string, k):
#     parts = textwrap.wrap(string,k)
#     for i in parts:
#         uniques = (dict.fromkeys(i))
#         print(uniques)


# stri = "AABCAAADA"
# merge_the_tools(stri,k=3)


# k = int(input())
# same_room = list(map(int,input().split()))

# for i in same_room:
#     if same_room.count(i) > 1:
#         same_room = same_room.remove(i)
        


# # print(same_room)

# from collections import Counter

# k = int(input())
# same_room = list(map(int, input().split()))

# counts = Counter(same_room)
# # print(counts.items())



# a , b = "1" , "4"

# print(a)
# print(b)

# a = {3,2,4,5,2,3}
# b = {3,2,4,6,3,1}
# l = a.issuperset(b)
# print(l)


# a = 9 
# b = 9
# f = a==b
# c = 8 
# d = 8
# g = c==d
# if f and g:
#     print("samjha")

# l = [True,False,True,False,False]
# print(any(l))

# x , k = (input().split())
# x = int(x)
# k = int(k)
# P = x**3 + x**2 + x + 1
# if P == k:
#     print(True)
# else:
#     print(False)


 
# P = int(input())
# print(P)



# print(type(eval('len')))



# l = [1]
# print(id(l[0]))   # memory address of the int 1
# print(id(1))      # same address — same object!

# X= int(input("enter the number of shoes:"))
# size_shoe = list(map(int,input().split()))
# N = int(input())
# earning = 0
# for i in range(N):
#     size ,price = input().split( )
#     if int(size) in size_shoe:
#         earning += int(price)
#         print(earning)
#         size_shoe.remove(int(size))
    
# print(earning)

from collections import *

# c = Counter(cats = 5 , dogs = 7)
# print(c)

c = Counter([1,2,1,2,3,2,1,3])
e = Counter([1,2,2,2,2,2,1,1,4,3])
# print(c)

# print(list(c.elements()))
# print(e | c)
# i = bin(9)
# print(i)

# number = 10
# print(bin(number))          # Output: 0b1010
# print(f"{number:b}")

# i = 10
# print(f"{i:o}")

number = 17

# for i in range(1,number):
    # print(f"{i}   {i:o}   {i:X}   {i:b}")
    

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001

# T = int(input())
# for _ in range(T):
#     a , b = input().split()
#     a = int(a)
#     try:
#         print(a/b)
#     except (ZeroDivisionError,ValueError) as e:
#         print(f"Error code : {e}")


# This prints out "Hello, John!"
name = "John"
# print(f"Hello, {name}!")
age = 34
print("Hello, %s is your age %d"%(name,age))

divison = 3/4
print("The divion result is %.4f" % divison )