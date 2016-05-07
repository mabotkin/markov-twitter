from pickle import load

MAX = 10

dic = load(open("dict.pkl","rb"))

freq = [0 for i in range(MAX+1)]
for i in dic:
	x = len(dic[i])
	if x > MAX:
		x = MAX
	freq[x] += 1

for i in range(len(freq)):
	print "Length: " + str(i) + " Frequency: " + str(freq[i])
