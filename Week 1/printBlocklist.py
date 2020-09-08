try:
	blocklist = open('blocklist.txt')
except OSError:
	print("no file. sad dog.")
else:
	for x in blocklist:
		print(x)
	blocklist.close()