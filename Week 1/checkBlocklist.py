blocklist = []
try:
	with open('blocklist.txt') as f:
		for x in f:
			blocklist.append(x.rstrip('\n'))
except OSError:
	print("blocklist not available. sad dog")

try:
	with open('visitors.txt') as f:
		count = 0
		blocked = []
		for visitor in f:
			count += 1
			for block in blocklist:
				if block == visitor.rstrip('\n'):
					blocked.append(block)
		print(count)
		print(blocked)
except OSError:
	print("visitors not available. sad dog")					