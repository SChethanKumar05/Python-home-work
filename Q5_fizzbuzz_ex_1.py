n = 30
count = 0

while count<=30 :
    if(count%3 ==0 and count%5 == 0):
        print("frizzbuzz")
    elif(count%3==0):
        print("frizz")
        
    elif(count%5==0):
        print("buzz")
    else:
        print(count)     
    count +=1

            