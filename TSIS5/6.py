s = ''
with open(r'Test1.txt','r') as f:
    for text in f:
        if text != '\n':
            s+=text
    print(s)