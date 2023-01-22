def commacode(ls):
    if len(ls)==0:
        ls=list(eval(input("enter the list \n")))
        return commacode(ls)
    else:
        
        l=len(ls)
        s=str(ls[0])
        for i in range(1,l):
            if i==l-1:
                s=s+" and "+str(ls[i])
            else:
                s=s+" , "+str(ls[i])
        return s
        
ls=list(eval(input("enter the list \n")))
print(commacode(ls))
