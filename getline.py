r = open("./result.csv", mode = 'rb')
r.readline()
line = str(r.readline())
print(line)
print(type(line))
r.close()
ip = ""
for a in line:
	if a == 'b' or a == '\\' or a == '\'' or a == 'n':
		continue
	else:
		ip += a
w = open("ips.txt", mode = 'a')
w.write(ip + '\n')