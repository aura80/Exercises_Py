for i in range(1, 10):
        print(str(i) * i)

count = 1
for i in range(10):
    for j in range(0, i):
        print(count, end='')
        count = count +1
    print()

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

print("\nReverse numbers using for loop:")
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

print()

numbers = [1, 2, 3, 4, 5]

for i in numbers[::-1]:
    print(i, end=" ")

print()

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print(' ')

print()

# iterate string with for loop
name = "Jessa"
for i in name:
    print(i, end=' ')

print("\n")

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
print("Numere pare intre 0 si 10:")
odd = [1, 5, 7, 9]
even = [i + 1 for i in odd if i % 2 == 1]
print(even)

print()

# enumerate() - index + element
print("Enumerate - index + value of the element:")
numbers = [4, 2, 5, 7, 8]
for i, v in enumerate(numbers):
    print('Numbers[', i, '] =', v)

# for - index + element
print("\nPrint index - number: ")
numbers = [1, 2, 4, 6, 8]
print(numbers)
size = len(numbers)
for i in range(size):
    print('Index:', i, " ", 'Value:', numbers[i])

print("\nReverse of a string: ")
name = "Jessa"
for i in name[::-1]:
    print(i, end=' ')

print("\n\nSplit() on strings:")

dialogue = "Remember, Red, hope is a good thing, maybe the best of things,\
and no good thing ever dies"
print(dialogue)
# split on whitespace
for word in dialogue.split():
    print(' ', word)

print()

numbers = [2, 3, 5, 6, 7]
for num in numbers:
    print(num, end = " ")

print()

numbers = [1, 2, 3, 6, 7]
size = len(numbers)
for i in range(size):
    print(numbers[i], end = " ")

print()

print("\nDictionary key - value:")
dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1:
    print(" ", i)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1.keys():
    print("   ", i)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for i in dict1.values():
    print("     ", i)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for key in dict1:
    print(key, "->", dict1[key])

def calculate (num1, num2=4):
  res = num1 * num2
  print("\n", res)

calculate(5, 6)

sampleSet = {"Jodi", "Eric", "Garry"}
print(sampleSet)

p, q, r = 10, 20 ,30
print(p, q, r)

for i in range(1, 5):
    print(i)
else:
    print("this is else branch of the for block statement\n" )

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is True)

print("\nFind() start index of 'na' in string cuv = 'banananana': ")
cuv = "banananana"
i = cuv.find("na")
print(i)
print("Count() how many times 'na' is in cuv = 'banananana': ")
print(cuv.count('na'))
