print("Creating Tuple : ")
t1 = (10,20,30,40)

print("\nAccessing Tuple : ", t1)
print("tuple[0] : ", t1[0])

print("\nUpdating Tuple : ")
t1_list = list(t1)
t1_list.remove(10)
t1 = tuple(t1_list)
print("\tRemoving 10 from tuple t1 : ", t1)

t1_list = list(t1)
t1_list.append(50)
t1 = tuple(t1_list)
print("\tAdding 50 to tuple t1 : ", t1)

#del t1
print("\nDeleting tuple using del() : ")
