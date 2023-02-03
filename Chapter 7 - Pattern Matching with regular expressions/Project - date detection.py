import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
def dateValidator(day,month,year):    
    if not (0<day<32 and 0<month<13 and 999<year<3000):
        return False
    
    if month % 2!=0:
        if day <= 31:
            return True
    
    if month % 2==0 and month !=2:
        if day <= 30:
            return True

    if month ==2 and year%100 !=0:
        if day <= 29:
            return True

    if month ==2 and year%100 == 0 and year%400 == 0:
        if day <= 29:
            return True

    if month ==2 and year%100 == 0 and year%400 != 0:
        if day <= 28:
            return True

inputDate = dateRegex.search(input('Date: '))
day,month,year=["","",""]
# print(day,month,year)

while inputDate != None:
    day,month,year = int(inputDate.group(1)),int(inputDate.group(2)),int(inputDate.group(3))
    if dateValidator(day,month,year):
        print('Date exists')
        break
    else:
        print('This dont date happen on earth bruh')
        break
else:
    print('DD/MM/YYYY is the format')