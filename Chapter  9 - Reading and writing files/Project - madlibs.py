import re
file = open('md.txt')
sentence = file.read()
file.close()

regexa = re.compile(r'(ADJECTIVE)')
regexn = re.compile(r'(NOUN)')
regexv = re.compile(r'(VERB)')


for i in regexa.findall(sentence):
    if True:
        reg = re.compile(r'{}'.format(i))
        sub = input('Enter %s: ' %i)
        sentence = reg.sub(sub, sentence, 1)
        
for i in regexn.findall(sentence):
    if True:
        reg = re.compile(r'{}'.format(i))
        sub = input('Enter %s: ' %i)
        sentence = reg.sub(sub, sentence, 1)
        
for i in regexv.findall(sentence):
    if True:
        reg = re.compile(r'{}'.format(i))
        sub = input('Enter %s: ' %i)
        sentence = reg.sub(sub, sentence, 1)

print(sentence)

file = open('madlibs', 'w')
file.write(sentence)
file.close()