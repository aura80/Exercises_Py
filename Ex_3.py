#Numere prime
def main():
    a = int(input("Introduceti a: "))
    b = int(input("Introduceti b (b>a): "))

    m = 0
    for i in range(a, b + 1):
        k = 0
        for j in range(2, round(i / 2) + 1):
            if i % j == 0:
                k = 1
        if k == 0:
            print(i, end=' ')
            m = 1
    if m == 1:
        print("sunt numerele prime dintre {} si {}".format(a, b))
    else:
        print("intre {} si {} nu sunt numere prime".format(a, b))

main()

#Divizorii unui numar
def main():
    n=int(input("Introduceti un numar intreg, n: "))
    k=0
    for i in range(2,round(n/2)+1):  #round rotunjeste argumentul; daca n=7, atunci range(2,5)=2,3,4
        if n%i==0:
            print(i, end=' ')
            k=1
    if k==1:
        print("sunt divizorii lui",n)
    else:
        print("Numarul {} este prim".format(n))
main()

#Factorialul unui numar
def main():
    n = int(input("Introduceti un numar intreg, n (in intervalul [0, 100])>>"))
    while n < 0 or n > 100:
        print("Numarul introdus nu apartine intervalului!")
        n = int(input("Introduceti un numar intreg, n (in intervalul [0, 100])>>"))

    if n > 0:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
    else:
        fact = 1

    print("Factorialul lui {} este {}".format(n, fact))


main()

#Eliminarea dublurilor dintr-un dictionar
student={'id1':{'nume':['Alex'],'an':2, 'grupa':1421},
        'id2':{'nume':['Andra'], 'an':3,'grupa':1434},
        'id3':{'nume':['Alex'],'an':2, 'grupa':1421},
        'id4':{'nume':['Stefan'],'an':2,'grupa':1422}}

result={}
for key,value in student.items():
    if value not in result.values():
        result[key]=value
print(result)

#Break vs Continue
for i in range(6):
    if i==3:
        break
    print(i)

for i in range(6):
    if i==3:
        continue
    print(i)

for i in range(0,11):
    if i==3 or i==7:
        continue
    print(i, end=' ')

