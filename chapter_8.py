import os


f = open ('file.txt',  'r')

firstline = f.readline()
print(firstline)

x = open ('file.txt', 'r')

for i in x:
    print(i, end = '')

x.close()

y = open ('file.txt', 'a')

y.write('/nThis is first new text')
y.write('/nThis is second new text')

y.close()

