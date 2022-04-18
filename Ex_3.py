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
