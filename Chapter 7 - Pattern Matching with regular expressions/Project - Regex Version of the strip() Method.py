import re
strip = ' '
tostrip="rahul is doing dragons and rahul likes it"
temp =  input("Strip: ")

if temp != '':
    strip = temp
    
stripperregex=re.compile(f"{strip} \w+")
print(stripperregex.sub("",tostrip))
