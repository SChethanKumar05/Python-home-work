n=int(input("enter the no to check whether its a prime factor or not : "))

if n>1:

    for i in range(2 ,n):
        if n% i == 0 :
            print("not a prime no")
            break
    else:
            print("its a prime no")   
else:
    print("not a prime no")            

   
