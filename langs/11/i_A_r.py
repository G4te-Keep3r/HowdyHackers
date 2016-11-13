import sys

def printFunction(lineRemaining):
	if lineRemaining[0] == '"' and lineRemaining[-1] == '"':
		if len(lineRemaining) > 2:
			#data to print
			lineRemaining = lineRemaining[1:-1]
			print ' '.join(lineRemaining)
		else:
			print

def main(fileName):
	with open(fileName) as f:
		for line in f:
			data = line.split()
			if data[0] == 'A_R':
				printFunction(data[1:])
			else:
				print 'ERROR'
				return

if __name__ == '__main__':
	main(sys.argv[1])