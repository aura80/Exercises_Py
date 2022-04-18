print("1. Afișați pe ecran toate cifrele impare, una sub alta.")
def impare():
    for i in range(0,10):
        if i % 2 != 0:
            print(i)
impare()

print("\n2. Afișați toate numerele naturale formate din trei cifre, care se împart exact la 100, \
în ordine descrescătoare pe aceeaşi linie, cu un spaţiu între ele.")

def nr_trei_cifre():
    for i in range(900, 0, -1):
        if i % 100 == 0:
            print(i, end = " ")
    print()
    l = []
    for j in range(1, 1000, 1):
        if j % 100 == 0:
            l.append(j)
            l.sort(reverse = True)
            print(l)
    print()
    lista = []
    for k in range(1, 1000, 1):
        if k % 100 == 0:
            lista.append(k)
    lista.reverse()
    print(lista)
nr_trei_cifre()

print("\n3. Afișați cifrele 1 2 3 4 5 pe aceeaşi linie cu un spaţiu între ele, \
iar pe linia următoare aceleaşi cifre în ordine descrescătoare. Afișați pe ecran expresia 1+2+3+4+5=15.")

def afis_nr():
    print(1,'',2,"",3," ","4"," ","5")
    for i in range(1,6):
        print(i, end = " ")
    print()
    for i in range(5, 0, -1):
        print(i, end=" ")
    print()
    print(1,'+',2,'+',3,'+',4,'+',5,'=',15)

afis_nr()

print("\n4. Afișați dreptunghiul de mai jos, folosind numai cracterul + şi spaţiul.\n\
++++++\n\
+    +\n\
++++++")

def forma1():
    print(" ->")
    for i in range(1,4):
        for j in range(1,7):
            if i == 2 and (j != 1 and j != 6):
                print(end=" ")
            else:
                print("+", end="")
        print()
forma1()

print("\n4. Afișați triunghiul de mai jos, folosind numai caracterul *.\n\
*\n\
**\n\
***\n\
****")

def steluta():
    for i in range(0, 4):
        print((i + 1) * '*')
steluta()

print("\n5. Afișați pătratul de mai jos cu interiorul plin, folosind numai cracterul +.\n\
++++\n\
++++\n\
++++\n\
++++")

def patrat_plus():
    print(" ->")
    for i in range(0, 4):
        for j in range(0, 4):
            print("+", end="")
        print()
patrat_plus()
