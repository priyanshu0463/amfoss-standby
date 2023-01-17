def collatz(number):
    if number%2==0:
        z=number//2
        print(z)
        if z==1:
            return
        else:
            collatz(z)
    else:
        z=number*3 +1
        print(z)
        if z==1:
            return

        else:
            collatz(z)
while True:
    try:
        number=int(input("enter a no. \n"))
        collatz(number)
        break
    except ValueError:
        print("invalid input Data-type")
        
            
            
            
      

    
    
