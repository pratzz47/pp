per = int(input("Enter percentage to check grades : "))

if per >= 75 :
    print("Distinct")
elif per>=60 and per<75:
    print("First class")
elif per>=50 and per<60:
    print("Second class")
elif per>=40 and per<50:
    print("Pass class")
else:
    print("Fail")
