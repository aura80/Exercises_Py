# # def invers():
# #     list1 = [100, 200, 3, 400, 500]
# #     list2 = [100, 200, 3, 400, 500]
# #     l = []
# #     list1.sort(reverse=True)
# #     print(list1)
# #     list2.reverse()                 # -------------------------------
# #     print(list2)
# #
# #     list3 = [100, 200, 3, 400, 500]
# #     print(list3[::-1])              # -------------------------------
# #
# #     i = 0
# #     while i in range(len(list3)):
# #         l.append(list3[i])
# #         print("-", l)
# #         i = i + 1
# #     print("-", l)
# #
# # invers()
# #
# # def concatenare():
# #     list1 = ["M", "na", "i", "Ke"]
# #     list2 = ["y", "me", "s", "lly"]
# #     list3 = [i + j for i, j in zip(list1,list2)]
# #     print("Folosind ZIP : ", list3)
# #     l = []
# #     for i in list1:
# #         for j in list2:
# #             a = list1.index(i)
# #             b = list2.index(j)
# #             if a == b:
# #                 l.append(i+j)
# #     print("Cu indecsi :   ", l)
# #
# #     k = 0
# #     p = 0
# #     while k in list1:
# #         while p in list2:
# #             a = list1.index(k)
# #             b = list2.index(p)
# #             if a == b:
# #                 l.append(k+p)
# #     print("Cu WHILE :     ", l)
# #
# # concatenare()
# #
# # def square():
# #    numbers = [1, 2, 3, 4, 5, 6, 7]
# #    print("numbers  :  ", numbers)
# #    l = []
# #    i = 0
# #    while i in range(len(numbers)):
# #        l.append(numbers[i] * numbers[i])
# #        i = i + 1
# #    print("Cu WHILE :  ", l)
# #
# #    numbers = [1, 2, 3, 4, 5, 6, 7]
# #    res = []
# #    for i in numbers:
# #        res.append(i * i)
# #    print("Cu FOR :    ", res)
# #
# #    z = [x * x for x in numbers]
# #    print("Cu FOR scurt :", z)
# #
# # square()
# #
# # def conc2():
# #     list1 = ["Hello ", "take "]
# #     list2 = ["Dear", "Sir"]
# #     l = []
# #     for i in list1:
# #         for j in list2:
# #             l.append(i + j)
# #     print("Lista:      ", l)
# #
# #     res = [x + y for x in list1 for y in list2]
# #     print("Pe scurt:   ", res)
# # conc2()
#
# for num in range(-2,-5,-1):
#     print(num, end=", ")
#
# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)
#
#
# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')
#
# for l in 'Jhon':
#    if l == 'o':
#       pass
#    print(l, end=", ")
#
# x = 0
# while (x < 100):
#   x += 2
# print(x)
#
# number = 97
# print(chr(number))
#
# l = "welcome to the beautiful world of python"
# print(l.capitalize())
# print(l.title())
#
# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
#
# str1 = "My salary is 7000";
# str2 = "7000"
#
# print(str1.isdigit())
# print(str2.isdigit())
#
# str1 = 'Welcome'
# print(str1*2)
#
# str = "my name is James bond";
# print (str.capitalize())
#
# print(ascii('char'))
# print(ord('c'))     # din caracter da codul ASCII
# print(chr(99))      # din codul ASCII da caracterul
#
# print("John" > "Jhon")
# print("Emma" < "Emm")
#
# #   string.count(value, start, end)
# str1 = "my isname isisis jameis isis bond";
# sub = "is"
# print(str1.count(sub, 4))
#
# str = "My salary is 7000"
# print(str.isalnum())
#
# # strOne = str("pynative")
# # strTwo = "pynative"
# # print(strOne == strTwo)
# # print(strOne is strTwo)
#
# # Yes, strings are immutable in Python. You cannot modify the string once created. \
# # If you change a string, Python creates a new string with the updated value \
# # and assigns it to the variable.
# str1 = "first"
# print(id(str1))
# str1 = str1+ " Two"
# print(id(str1))
#
# # Python does not support a character type; a single character is treated
# # as strings of length one.
#
# str1 = 'Jamesiaaaal'
# print(int(len(str1)/2))
# l = []
# for i in range(len(str1)):
#     if i == 0:
#         print(str1[i])
#         l.append(str1[i])
#     elif i == int(len(str1)/2):
#         print(str1[i])
#         l.append(str1[i])
#     elif i == len(str1)-1:
#         print(str1[i])
#         l.append(str1[i])
#     else:
#         continue
# print(l, end = " ")
#
# str1 = 'James'
# print("Original String is", str1)
#
# res = str1[0]
# l = len(str1)
# mi = int(l / 2)
# res = res + str1[mi]
# res = res + str1[l - 1]
# print("New String:", res)
#
# str1 = "JhonDipPeta"
# print(f'Sirul are --- {len(str1)} --- caractere')
#
# print(f'Mijlocul sirului este la --- {int(len(str1)/2)} ---')
# for i in range(len(str1)):
#     if i == int(len(str1)/2):
#         print("Sirul din mijloc este: ", str1[i-1:i+2])
#
# s1 = "Ault"
# s2 = "Kelly"
#
# for i in range(len(s1)):
#     if i == int(len(s1)/2):
#
#         print(s1[0:i] + s2 + s1[i:])
#
# s1 = "America"
# s2 = "Japan"
#
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if i == int(len(s1)/2) and j == int(len(s2)/2):
#             print(s1[0] + s2[0] + s1[i] + s2[j] + s1[-1] + s2[-1])
#
# str1 = 'PyNaTive'
# for i in range(len(str1)):
#         if str1[i].islower():
#             str2 = str1[i]
#             print(str2, end = "")
# for j in range(len(str1)):
#         if str1[j].isupper():
#             str3 = str1[j]
#             print(str3, end = "")
#
# str1 = "PYnAtivE"
# print('\nOriginal String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)
#
# # Join both list
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)
#
# str1 = "P@#yn26at^&i5ve"
# nr = 0
# li = 0
# si = 0
#
# for i in range(len(str1)):
#     if str1[i].isdigit():
#         nr += 1
#     elif str1[i].isalpha(): # or str1[i].islower() or str1[i].isupper():
#         li += 1
#     else:
#         si += 1
# print("Numere: ", nr)
# print("Litere: ", li)
# print("Simboluri: ", si)
#
# s1 = "Abc"
# s2 = "Xyz"
# #  AzbycX
# print(s1[0] + s2[-1] + s1[1] + s2[1] + s1[-1] + s2[0])
# l = []
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         pass
#     if i == 0:
#         a = s1[i] + s2[j]
#         l.append(a)
#     elif i == 1:
#         b = s1[i] + s2[j-1]
#         l.append(b)
#     elif i == 2:
#         c = s1[i] + s2[j-2]
#         l.append(c)
#
# print(a + b + c)
#
# def f():
#     s1 = "Yn"
#     s2 = "PYnative"
#
#     if s1 in s2:
#         return True
#     else:
#         return False
# print(f())
#
# def string_balance_test(s1, s2):
#     flag = True
#     for char in s1:
#         if char in s2:
#             continue
#         else:
#             flag = False
#     return flag
#
# s1 = "Yn"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)
#
# s1 = "Ynf"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d = dict()
r = {}
for i, j in sample_dict.items():
    for k in range(len(keys)):
        if i == keys[k]:
            d.update({i:j})
            r.update({i: j})
            print(i,j)
print(d)
print(r)

for k in keys:
    del sample_dict[k]
print(" - ", sample_dict)

for k in keys:
    if k in sample_dict:
        sample_dict.pop({k:sample_dict[k]})
print(" * ", sample_dict)

a = '''  hfasyugd
         jhdfbhd
         dkjvnjkv'''
b = """ ighsrui
 kcfjvkl
 klvmfkdm"""
c = "' ghurgn" \
    "jnkjdfnvj" \
    "fkvfvv" \
    "yhdjgufrdhbfgyh '"
print(a)
print(b)
print(c)

# Python3 program for demonstration
# of list index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print the index of '4' in list1
print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

# Will print the index of 'cat' in list2
print(list2.index('cat'))




















