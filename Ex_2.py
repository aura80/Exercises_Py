print("Print a set containing all the colors from color_list_1 which are not present in color_list_2:")
def set_list():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    print("Method 1: ", color_list_1 - color_list_2)

    print("Method 2: ")
    for i in color_list_1:
        if i not in color_list_2:
            print(" ", i)
set_list()

print("\nCMMDC - inmultim factorii primi comuni la puterea cea mai mica (divide si pe x si pe y)")
def cmmdc(x, y):
     z = x % y
     while z:
       x = y
       y = z
       z = x % y
     return y
print("CMMDC of 12 & 17 =",cmmdc(24, 80))
print("CMMDC of 4 & 6 =",cmmdc(4, 6))
print("CMMDC of 12 & 16 =",cmmdc(12, 16))
print("CMMDC of 24 & 8 =",cmmdc(24, 8))
print("CMMDC of 336 & 360 =",cmmdc(336, 360))

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

print("\nCMMMC - inmultim factorii primi comuni si necomuni la puterea cea mai mare")
def cmmmc(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          cmmmc = z
          break
      z += 1
  return cmmmc
print("CMMMC of 4 & 6 = ", cmmmc(4, 6))
print("CMMMC of 12 & 16 = ", cmmmc(12, 16))
print("CMMMC of 15 & 17 = ", cmmmc(15, 17))
print("CMMMC of 336 & 360 = ", cmmmc(336, 360))

print("\nCMMDC + CMMMC: ")
def cmmdc_cmmmc():
    m = int(input("m = "))
    n = int(input("n = "))
    #rețin valorile initiale
    init_m = m
    init_n = n
    #calculez cmmdc
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    #m va reține cmmdc
    print("cmmdc = ",m)
    #calculez cmmmc
    cmmmc = init_m * init_n // m
    print("cmmmc = ",cmmmc)
cmmdc_cmmmc()

print("\nInt, input, if else, strings: ")
def suma():
    a, b = int(input("a = ")), int(input("b = "))
    c = int(input("c = "))
    if a == b or a == c or b == c:
        print("Sum = 0000000")
    else:
        sum = a + b + c
        print("Sum = ", sum)
suma()

print("\nIf else, or, return: ")
def sum(x, y, z):
    if x == y or x == z or y == z:
        return 0
    else:
        sum = x + y + z
        return sum
print(sum(1,5,7))
print(sum(1,2,1))

print("\nRange, input, if else: ")
def condition():
    o = int(input(" Numarul o = "))
    m = int(input(" Numarul m = "))
    sum = o + m
    if sum in range(15,21):
        print("20")
    else:
        print("Sum = ", sum)
condition()

print("\nBoolean, input, if else: ")
def f():
    z = int(input("z= "))
    m = int(input("m= "))
    if z == m or z - m == 5 or m - z == 5 or z + m == 5:
        return True
    else:
        return False

print(f())

print("\nSplit() a string into a list:")
print("Write a sentence:")
a = input().split()
print(a)




