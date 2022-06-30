

f = open('../file.txt', 'r')

firstLine = f.readline()
print(firstLine)

x = open('../file.txt', 'r')

for i in x:
    print(i, end='')

x.close()

y = open('../file.txt', 'a')

y.write('/nThis is first new text')
y.write('/nThis is second new text')

y.close()
