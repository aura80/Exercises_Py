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
