import re
def strength(password):
    passregex_u = re.compile(r'[A-Z]+')
    passregex_l = re.compile(r'[a-z]+')
    passregex_n = re.compile(r'[0-9]+')
    
    if len(password)>=8:
        if not passregex_u.search(password):
            return False
        if not passregex_n.search(password):
            return False
        if not passregex_l.search(password):
            return False        
        
        else:
            return True 
    else:
        print("Pass too short")
                
passkey = input("TYpe pass: ")
if strength(passkey):
    print("Good pass")
    
else:
    print("Bruh")
    