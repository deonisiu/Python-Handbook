fin = open('input.txt')
fout = open('output.txt', 'w')

a, b, c = map(int, fin.readline().split())
result = 'NO'
if(a * b == c):
    result = 'YES'
fout.write(str(result))

fin.close()
fout.close()