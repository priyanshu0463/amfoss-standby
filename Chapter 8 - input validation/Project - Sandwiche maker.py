import pyinputplus as p

prices = {'wheat': 50, 'white': 40, 'sour dough': 60, 'chicken': 80, 'turkey': 90, 'ham': 100, 'tofu': 70,
          'cheddar': 25, 'swiss': 30, 'mozzarella': 20, 'mayo': 5, 'mustard': 5, 'lettuce': 10,
          'tomato': 5}

contents = []
cost = 0
count = 0

bread = p.inputMenu(['wheat', 'white','sourdough'])
contents.append(bread)
protein = p.inputMenu(['chicken','turkey','ham','tofu'])
contents.append(protein)

if p.inputYesNo('Cheese or nah?')=='yes':
    cheese=p.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    contents.append(cheese)
    
for i in ['mayo','mustard','lettuce','tomato']:
    prompt = f"Add {i}?\n"
    if p.inputYesNo(prompt) == 'yes':
        contents.append(i)
        
while count <1:
    count = p.inputInt("How many sandiwches?: ")

for i in contents:
    cost += prices[i]
    
    
print(count*cost)