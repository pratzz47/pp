#creating set
s1 = {1,1.5,"a", "abc"}

#Accessing set
for i in s1:
    print(i)

#Update set
s1.add("pqr")
print("Updated Set after inserting pqr : ", s1)


s1.remove("abc")
print("Updated Set after removing abc: ", s1)


s1.pop()
print("Updated Set after pop() : ", s1)


s1.clear()
print("Updated Set after clear() : ", s1)

#Delete set
del s1
print("Updated Set after del : ", s1)
