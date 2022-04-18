print(" <---------- The reverse of a list of numbers")
def invers():
    list1 = [100, 200, 3, 400, 500]
    list2 = [100, 200, 3, 400, 500]
    l = []
    list1.sort()
    print(list1)
    list1.sort(reverse=True)
    print(list1)

    list2.reverse()                 # -------------------------------
    print(list2)

    list3 = [100, 200, 3, 400, 500]
    print(list3[::-1])              # -------------------------------

    i = 0
    while i in range(len(list3)):
        l.append(list3[i])
        print("-", l)
        i = i + 1
    print("-", l)

invers()

print("\n <---------- Concatenate the elements of two lists with the same index")
def concatenare():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    list3 = [i + j for i, j in zip(list1,list2)]
    print("Folosind ZIP : ", list3)

    l = []
    for i in list1:
        for j in list2:
            a = list1.index(i)
            b = list2.index(j)
            if a == b:
                l.append(i+j)
    print("Cu indecsi :   ", l)

    k = 0
    p = 0
    while k in list1:
        while p in list2:
            a = list1.index(k)
            b = list2.index(p)
            if a == b:
                l.append(k+p)
    print("Cu WHILE :     ", l)

concatenare()

print("\n <---------- Square of the elements of a list")
def square():
   numbers = [1, 2, 3, 4, 5, 6, 7]
   print("numbers  :  ", numbers)
   l = []
   i = 0
   while i in range(len(numbers)):
       l.append(numbers[i] * numbers[i])
       i = i + 1
   print("Cu WHILE :  ", l)

   numbers = [1, 2, 3, 4, 5, 6, 7]
   res = []
   for i in numbers:
       res.append(i * i)
   print("Cu FOR :    ", res)

   z = [x * x for x in numbers]
   print("Cu FOR scurt :", z)

square()

print("\n <---------- Concatenate the elements of two lists with different index")
def conc2():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    l = []
    for i in list1:
        for j in list2:
            l.append(i + j)
    print("Lista:      ", l)

    res = [x + y for x in list1 for y in list2]
    print("Pe scurt:   ", res)
conc2()

print("\n <---------- Ranges")
def ordin():
    for num in range(-2,-5,-1):
        print(num, end=", ")
    print()
    for num in range(-2,10,1):
        print(num, end=", ")
    print()
    for num in range(10,-5,-1):
        print(num, end=", ")
    print()
    for num in range(20,50,5):
        print(num, end=", ")

    var = 10
    for i in range(10):
        for j in range(2, 10, 1):
            if var % 2 == 0:
                continue
                var += 1
        var+=1
    else:
        var+=1
    print(var)
ordin()

print("\n <---------- Boolean and other exercises")
def dif_exercises():
    a, b = 12, -12
    if a + b:
        print('\nTrue')
    else:
      print('\nFalse')
    print()
    for l in 'Jhon':
       if l == 'o':
          pass
       else:
        print(l, end=", ")
    print()
    x = 0
    while (x < 100):
        x += 5
        print(x, end=", ")
    print()
    number = 97
    print("\nASCII equivalent of 97 is: ", chr(number))
    print()
    l = "welcome to the beautiful world of python"
    print("String is:          ", l)
    print("String capitalized: ", l.capitalize())
    print("String titled is:   ", l.title())
    print()
    str1 = "PYnative"
    print("String is: ", str1)
    print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
    print()
    str1 = "My salary is 7000"
    str2 = "7000"
    print(f"str1 = {str1} \nstr2 = {str2}")
    print("Is str1 a number: ", str1.isdigit())
    print("Is str2 a number: ", str2.isdigit())
    print()
    str1 = 'Welcome'
    print(str1*2)
    print()
    strg = "my name is James bond";
    print ("Bond capitalized: ", strg.capitalize())
    print()
    print(ascii('char'))
    print(ord('c'))     # din caracter da codul ASCII
    print(chr(99))      # din codul ASCII da caracterul
    print()
    print("John > Jhon: ", "John" > "Jhon")
    print("Emma < Emm:  ", "Emma" < "Emm")
    print()
    print("string.count(value, start, end)")
    str1 = "my isname isisis jameis isis bond"
    sub = "is"
    print(f'   "is" found in "{str1}" starting from index 3 for  ->  {str1.count(sub, 3)} times')
    print(f'   "is" found in "{str1}" starting from index 12 for  ->  {str1.count(sub, 12)} times')
    print()
    print("'isalnum' checks if all the characters in a text are alphanumeric")
    str1 = "My salary is 7000"
    str2 = "Mysalaryis7000!  "
    str3 = "Mysalaryis7000now"
    print(str1, " -> ", str1.isalnum())
    print(str2, " -> ", str2.isalnum())
    print(str3, " -> ", str3.isalnum())
    print()
    strOne = str("pynative")
    strTwo = "pynative"
    print(strOne == strTwo)
    print(strOne is strTwo)
# # Yes, strings are immutable in Python. You cannot modify the string once created. \
# # If you change a string, Python creates a new string with the updated value \
# # and assigns it to the variable.
    print("\nStrings are immutable!\n--->")
    str1 = "first"
    print("str1: ", str1)
    print("Address of str1: ", id(str1))
    str1 = str1 + " Two"
    print("NEW str1: ", str1)
    print("Address of the NEW str1: ", id(str1))
    print()

dif_exercises()

print("\n <---------- List and elements of the string")
# # Python does not support a character type; a single character is treated
# # as strings of length one.
def elemente_sir():
    str1 = 'Jamesiaaaal'
    print("Sirul: ", str1)

    print("Indexul elementului din mijlocul sirului: ", int(len(str1)/2))
    l = []
    for i in range(len(str1)):
        if i == 0:
            print("Primul element al sirului:     ", str1[i])
            l.append(str1[i])
        elif i == int(len(str1)/2):
            print("Al doilea element al sirului:  ", str1[i])
            l.append(str1[i])
        elif i == len(str1)-1:
            print("Ultimul element al sirului:    ", str1[i])
            l.append(str1[i])
        else:
            continue
    print("Lista elementelor anterioare: ",  l)
elemente_sir()
