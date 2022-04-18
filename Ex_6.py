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
