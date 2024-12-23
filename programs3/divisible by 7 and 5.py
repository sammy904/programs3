a=int(input("enter a number"))
if a%2==0 and a%7==0:
    print("double seven")
elif a%2==0:
    print("even")
elif a%7==0:
    print("lucky seven")
else:
    print(f"{a}")
    
