print("Find the type of an dictionary element: ")
x = {}
print(type(x))

print("\nNumerical keys of dictionary: ")
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 8: "Avaya"}
print("my_dict = ", my_dict)
print("*Maximum value of my_dict numerical keys is: ", max(my_dict.keys()))

print("\nSorted dictionary: ")
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
print("Dictionary: ", my_dict)
print("Sorted keys dictionary:    ", sorted(my_dict.keys()))
print("*Keys with indexes:")
print(sorted(my_dict.keys())[0])
print(sorted(my_dict.keys())[1])
print(sorted(my_dict.keys())[2])
print(sorted(my_dict.keys())[3])
print(sorted(my_dict.keys())[4])
print("Sorted values dictionary:  ", sorted(my_dict.values()))
print("*Values with indexes:")
print(sorted(my_dict.values())[0])
print(sorted(my_dict.values())[1])
print(sorted(my_dict.values())[2])
print(sorted(my_dict.values())[3])
print(sorted(my_dict.values())[4])
print("Dictionary items(): ", my_dict.items())

str = 'Hello World!\n'
print("\nStrings: ")
if str == 'Hello World!\n':
    print(str)

print("\nFibonacci recursiv: ")
def fibonacci(n):
 assert n >= 0
 if n < 2:
    return n
 else:
    return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(10) = ", fibonacci(10))

print("\nList and indexes: ")
a = ["Hello","World","Paris"]
print("a = ", a)
print("a[:2]  = ", a[:2])
print("a[0:]  = ", a[0:])
print("a[:3]  = ", a[:3])
print("a[:-1] = ", a[:-1])
print("a[:]   = ", a[:])
