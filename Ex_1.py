# #29. Write a Python program to print out a set containing all
# # the colors from color_list_1 which are not
# # present in color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
# print(color_list_1 - color_list_2)
#
# for i in color_list_1:
#     if i not in color_list_2:
#         print(i)
# #    cmmdc - inmultim factorii primi comuni la puterea cea mai mica
# def gcd(x, y):
#  z = x % y
#  while z:
#    x = y
#    y = z
#    z = x % y
#  return y
# print("GCD of 12 & 17 =",gcd(24, 80))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
#
# # var 2
# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
#
# #   cmmmc - inmultim factorii primi comuni si necomuni la puterea cea mai mare
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))
#
# #   cmmdc + cmmmc
# m = int(input("m="))
# n = int(input("n="))
# #rețin valorile initiale
# init_m = m
# init_n = n
# #calculez cmmdc
# while m!=n:
#     if m>n: m = m - n
#     else: n = n - m
# #m va reține cmmdc
# print("cmmdc =",m)
# #calculez cmmmc
# cmmmc = init_m*init_n // m
# print("cmmmc =",cmmmc)
#
# a, b = int(input("a= ")), int(input("b= "))
# c = int(input("c= "))
# if a == b or a == c or b == c:
#     print("Sum= 0")
# else:
#     sum = a + b + c
#     print("Sum= ", sum)
#
# def sum(x, y, z):
#     if x == y or x == z or y == z:
#         return 0
#     else:
#         sum = x + y + z
#         return sum
# print(sum(1,5,7))
# print(sum(1,2,1))

# o = int(input("o= "))
# m = int(input("m= "))
# sum = o + m
# if sum in range(15,21):
#     print("20")
# else:
#     print("Sum= ", sum)

# def f():
#     z = int(input("z= "))
#     m = int(input("m= "))
#     if z == m or z - m == 5 or m - z == 5 or z + m == 5:
#         return True
#     else:
#         return False
#
# print(f())

# a = input().split()
# print(a)

# x = {}
# print(type(x))
#
# my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
# print(max(my_dict.keys()))
#
# my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
# print(sorted(my_dict.values())[0])
# print(sorted(my_dict.values())[1])
# print(sorted(my_dict.values())[2])
# print(sorted(my_dict.values())[3])
# print(sorted(my_dict.values())[4])
##print(my_dict.items()[-1][1])
#
# str = 'Hello World!'
# if str == 'Hello World!':
#     print(str)
#
# def fibonacci(n):
#  assert n >= 0
#  if n < 2:
#     return n
#  else:
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))
#
# a = ["Hello","World","Paris"]
# print(a[:2])
# print(a[0:])
# print(a[:3])
# print(a[:-1])
# print(a[:])
#
# menu_options = {
#     1: 'Option 1',
#     2: 'Option 2',
#     3: 'Option 3',
#     4: 'Exit',
# }
#
# def print_menu():
#     for key in menu_options.keys():
#         print (key, '--', menu_options[key] )
#
# def option1():
#      print('Handle option \'Option 1\'')
#
# def option2():
#      print('Handle option \'Option 2\'')
#
# def option3():
#      print('Handle option \'Option 3\'')
#
# if __name__=='__main__':
#     while(True):
#         print_menu()
#         option = ''
#         try:
#             option = int(input('Enter your choice: '))
#         except:
#             print('Wrong input. Please enter a number ...')
#         #Check what choice was entered and act accordingly
#         if option == 1:
#            option1()
#         elif option == 2:
#             option2()
#         elif option == 3:
#             option3()
#         elif option == 4:
#             print('Thanks message before exiting')
#             exit()
#         else:
#             print('Invalid option. Please enter a number between 1 and 4.')

for i in range(1, 10):
        print(str(i) * i)

count = 1
for i in range(10):
    for j in range(0, i):
        print(count, end='')
        count = count +1
    print()
# input()

for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print()

count = 0
for i in range(10):
    for j in range(0, i):
        print(count,end='')
    count = count +1
    print()

print("Reverse numbers using for loop")
num = 5
# start = 5
# stop = -1
# step = -1

for num in (range(num, -1, -1)):
    print(num, end=" ")

print()

nr = 8
for n in range(nr + 1)[::-1]:
    print(n, end=" ")

numbers = [1, 2, 3, 4, 5]
for i in numbers[::-1]:
    print(i)

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print(' ')

# outer loop
for i in range(1, 6):
    print('Multiplication table of:', i)
    count = 1
    # inner loop to print multiplication table of current number
    while count < 11:
        print(i * count, end=' ')
        count = count + 1
    print('\n')

# par - impar
odd = [1, 5, 7, 9]
even = [i + 1 for i in odd if i % 2 == 1]
print(even)

# enumerate() - index + element
numbers = [4, 2, 5, 7, 8]
for i, v in enumerate(numbers):
    print('Numbers[', i, '] =', v)

# for - index + element
numbers = [1, 2, 4, 6, 8]
size = len(numbers)
for i in range(size):
    print('Index:', i, " ", 'Value:', numbers[i])

# iterate string with for loop
name = "Jessa"
for i in name:
    print(i, end=' ')

name = "Jessa"
for i in name[::-1]:
    print(i, end=' ')

dialogue = "Remember, Red, hope is a good thing, maybe the best of things,\
and no good thing ever dies"
# split on whitespace
for word in dialogue.split():
    print(word)

numbers = [2, 3, 5, 6, 7]
for num in numbers:
    print(num)

numbers = [1, 2, 3, 6, 7]
size = len(numbers)
for i in range(size):
    print(numbers[i])

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1:
    print(i)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1.keys():
    print(i)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for key in dict1:
    print(key, "->", dict1[key])

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1.values():
    print(i)


def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

sampleSet = {"Jodi", "Eric", "Garry"}
#sampleSet.add(1, "Vicki")
print(sampleSet)

p, q, r = 10, 20 ,30
print(p, q, r)

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is True)









