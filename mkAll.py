import os

nextVarDict = {}
lets = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')
for i in range(len(lets)-1):
	nextVarDict[lets[i]] = lets[i+1]
pt1 = []
pt2 = []
with open('pt1') as f:
	for line in f:
		pt1.append(line)
with open('pt2') as f:
	for line in f:
		pt2.append(line)

def nextStatement(statement, i): #called with the index to change. start at len(statement)-1
	if i == -1: #whole new statement
		#return 'a'*(len(statement)+1)
		return 'a'+statement #should be all 'a's
	#else, change next char (the i one)
	stmntList = list(statement)
	if stmntList[i] == '_':
		#increment next
		stmntList[i] = 'a'
		return nextStatement(''.join(stmntList), i-1)
	#else, just increment, do not need to step to the next one
	stmntList[i] = nextVarDict[stmntList[i]]
	return ''.join(stmntList)

def makeLang(s, dirNum):
	#lang file
	with open('langs/'+dirNum+'/file.'+s+'', 'w+') as lw:
		#a " Howdy Hackers "
		lw.write(s+' " Howdy Hackers "')
	#interpreter file
	with open('langs/'+dirNum+'/'+s+'.py', 'w+') as iw:
		#interpreter
		for line in pt1:
			iw.write(line)
		iw.write(s)
		for line in pt2:
			iw.write(line)

def main():
	count = 0
	s = 'a'
	#s = 'i____' #last one in the folder-i think
	#s = nextStatement(s, len(s)-1) #go to next
	dirCounter = 0
	os.makedirs('/mnt/hgfs/HowdyHackers/langs/'+str(0))
	for i in range(1000*100):
		#print s
		makeLang(s, str(dirCounter))
		s = nextStatement(s, len(s)-1)
		count += 1
		if count % (1000*10) == 0:
			print "{:,}".format(count/(1000*10)), '10k'
			dirCounter += 1
			os.makedirs('/mnt/hgfs/HowdyHackers/langs/'+str(dirCounter))

if __name__ == '__main__':
	main()