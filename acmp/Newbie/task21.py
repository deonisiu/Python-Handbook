fin = open('input.txt')
fout = open('output.txt', 'w')

a, b, c = map(int, fin.readline().split())
maxValue = max(a, b, c)
minValue = min(a, b, c)

result = maxValue - minValue
fout.write(str(result))

fin.close()
fout.close()