fin = open('input.txt')
fout = open('output.txt', 'w')

a = int(fin.readline())
result = a * 100 + 99 - a
fout.write(str(result))

fin.close()
fout.close()