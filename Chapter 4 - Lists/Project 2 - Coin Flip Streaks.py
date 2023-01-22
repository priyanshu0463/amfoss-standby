import random
numberOfStreaks = 0
l=[]
ls=["H","T"]
for experimentNumber in range(10000):
    l1=[]
    l1.append(random.choice(ls))
    for i in range(99):
        l1.append(random.choice(ls))
    l.append(l1)
    i=0  
    while(i< len(l1)):    
        c=1
        for j in range(i+1,len(l1)):
        
            if l1[i]==l1[j]:
            
                c+=1
            else:
                i=j-1
            
                break
        if c>=6:
            numberOfStreaks+=1
            break
        else:
            i+=1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
     
    
    
        
