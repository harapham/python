import re

s=''
while True:
    try:
        s+=input()
    except EOFError :
        break

s=re.findall('[\w\s:,]+',s)
for i in s:
    ss = i.lower().split()
    ss[0]=ss[0].title()
    print(' '.join(ss))