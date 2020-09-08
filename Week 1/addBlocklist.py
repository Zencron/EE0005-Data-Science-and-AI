try:
	with open('blocklist.txt' , 'a') as f:
		f.write('\nalice@wonderland.co.uk')
except OSError:
	print("no file. sad dog.")