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

print("\n <---------- Calculate elements of the string")
def elem_sir():
    str1 = 'James'
    print("Original String is: ", str1)

    res = str1[0]
    l = len(str1)
    mi = int(l / 2)
    res = res + str1[mi]
    res = res + str1[l - 1]
    print("New String: ", res)
    print()
    str2 = "JhonDipPeta"
    print(f'Sirul "{str2}" are --- {len(str2)} --- caractere')
    print(f'Mijlocul sirului este la indexul: {int(len(str2) / 2)}')
    for i in range(len(str1)):
        if i == int(len(str1) / 2):
            print("Sirul din mijloc este: ", str1[i - 1:i + 2])
    print()
    s1 = "Ault"
    s2 = "Kelly"
    for i in range(len(s1)):
        if i == int(len(s1) / 2):
            print(s1[0:i] + s2 + s1[i:])
    print()
    s1 = "America"
    s2 = "Japan"
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == int(len(s1) / 2) and j == int(len(s2) / 2):
                print(s1[0] + s2[0] + s1[i] + s2[j] + s1[-1] + s2[-1])
    print()
    str1 = 'PyNaTive'
    print("Literele mici din str1: ")
    for i in range(len(str1)):
        if str1[i].islower():
            str2 = str1[i]
            print(str2, end="")
    print("\nLiterele mari din str1: ")
    for j in range(len(str1)):
        if str1[j].isupper():
            str3 = str1[j]
            print(str3, end="")
    print()
    str1 = "PYnAtivE"
    print('\nOriginal String: ', str1)
    lower = []
    upper = []
    for char in str1:
        if char.islower():
            # add lowercase characters to lower list
            lower.append(char)
            print(lower)
        else:
            # add uppercase characters to upper list
            upper.append(char)
            print(upper)
    # Join both list
    sorted_str = ''.join(lower + upper)
    print('Result:', sorted_str)

elem_sir()

print("\n <---------- Count numbers, letters and symbols")
def numere_litere_simboluri():
    str1 = "P@#yn26at^&i5ve"
    print("str1 = ", str1)
    nr = 0
    li = 0
    si = 0
    for i in range(len(str1)):
        if str1[i].isdigit():
            nr += 1
        elif str1[i].isalpha(): # or str1[i].islower() or str1[i].isupper():
            li += 1
        else:
            si += 1
    print("Numere: ", nr)
    print("Litere: ", li)
    print("Simboluri: ", si)
numere_litere_simboluri()

print("\n <---------- Combining two strings")
def combine_strings():
    print('\nFrom "Abc"  and "Xyz" obtain "AzbycX": ')
    s1 = "Abc"
    s2 = "Xyz"
    #  AzbycX
    print("     Method 1: ", s1[0] + s2[-1] + s1[1] + s2[1] + s1[-1] + s2[0])
    l = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            pass
        if i == 0:
            a = s1[i] + s2[j]
            l.append(a)
        elif i == 1:
            b = s1[i] + s2[j-1]
            l.append(b)
        elif i == 2:
            c = s1[i] + s2[j-2]
            l.append(c)

    print("     Method 2: ", a + b + c)
combine_strings()

print("\n <---------- String in another string")
def f():
    s1 = "Yn"
    s2 = "PYnative"
    print(f"\nString '{s1}' in another string '{s2}' : ")

    if s1 in s2:
        return True
    else:
        return False
print(f())

print("\n <---------- Combining two strings")
def string_contained_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag

s1 = "Yn"
s2 = "PYnative"
flags = string_contained_test(s1, s2)
print("s1 and s2 are balanced:", flags)

s1 = "Ynfd"
s2 = "PYnative"
flagss = string_contained_test(s1, s2)
print("s1 and s2 are balanced:", flagss)

print("\n <---------- Dictionary keys")
def dict_work():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    print(sample_dict)
    print()

    # Keys to extract
    keys = ["name", "salary"]
    d = dict()
    r = {}
    for i, j in sample_dict.items():
        for k in range(len(keys)):
            if i == keys[k]:
                d.update({i:j})
                print("Key to extract: ", i,j)
    print("Dictionary Keys to extract: ", d)

    for k in keys:
        del sample_dict[k]
    print("Delete previous keys - ", sample_dict)

    for k in keys:
        if k in sample_dict:
            sample_dict.pop({k:sample_dict[k]})
    print("Pop previous keys * ", sample_dict)

dict_work()

print("\n <---------- List index() method")
def indexare():
    list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

    # Will print the index of '4' in list1
    print()
    print("list1 = ", list1)
    print(f"The index of '{list1[3]}' in list1 is: {list1.index(4)} ")
    print(f"The index of '{list1[8]}' in list1 is: {list1.index(5)} ")

    list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
    print("\nlist2 = ", list2)
    # Will print the index of 'cat' in list2
    print(f"The index of '{list2[0]}' in list2 is: {list2.index('cat')} ")
    print(f"The index of '{list2[1]}' in list2 is: {list2.index('bat')} ")
    print(f"The index of '{list2[2]}' in list2 is: {list2.index('mat')} ")
    print(f"The index of '{list2[4]}' in list2 is: {list2.index('pet')} ")
indexare()

print("\n <---------- Indenting")

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
