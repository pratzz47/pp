#creating a list
lst = [10,20,30,40,50]

print("Accessing list : ", lst)

print("\nSearching element from list")
print("10 in list : ", 10 in lst)

print("\nDeleting element from list")
print(lst[2],"Deleting from list")
del(lst[2])
print(lst)

print("\nInsert in a list : ")
print("60 insert in a list")
lst.insert(5,60)
print(lst)
