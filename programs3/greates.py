a= int(input("enter 1st number"))
b= int(input("enter 2nd number"))
c= int(input("enter 3rd number"))
if a>b:
    if a>c:
        print(f"1st is the greatest number which is {a}")
elif b>c:
    if b>a:
        print(f"2nd is the greatest number which is {b}")
else:
    print(f"3rd is the greatest number which is{c} ")
