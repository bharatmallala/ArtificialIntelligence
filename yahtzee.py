#yahtzee code
#Bharat Mallala
#returns the score of each board
def score(board):
	if board[0] ==board[1] and board[1] == board[2]:
		return 25
	else:
		return sum(board)
		
#the output list is in the order of these rolls in sequence a,b,c,ab,ac,bc,abc		
def chancenode(s):
	rolla = 0
	rollb = 0
	rollc =0
	rollab = 0
	rollac = 0
	rollbc = 0
	rollabc =0
	newscore =[]
	newscore1=[]
	newscore2=[]
	exp =0
	finalscore=[]
	for a in range (0,2):
		for b in range(0,2):
			for c in range(0,2):
				#for i in range(1,7):
				if a==0 and b==0 and c==0:
					newscore.append(score([s[0],s[1],s[2]]))	
				if a==1 and b==0 and c==0:
					for i in range(1,7):
						newscore.append(score([i,s[1],s[2]]))
				if a==0 and b==1 and c==0:
					for i in range(1,7):
						newscore.append(score([s[0],i,s[2]]))
				if a==0 and b==0 and c==1:
					for i in range(1,7):
						newscore.append(score([s[0],s[1],i]))
				#print (newscore)
				if a==1 and b==1 and c==0:
					for i in range(1,7):
						for j in range(1,7):
							newscore1.append(score([i,j,s[2]]))
				if a==1 and b==0 and c==1:
					for i in range(1,7):
						for j in range(1,7):
							newscore1.append(score([i,s[1],j]))
				if a==0 and b==1 and c==1:
					for i in range(1,7):
						for j in range(1,7):
							newscore1.append(score([s[0],i,j]))
				if a==1 and b==1 and c==1:
					for i in range(1,7):
						for j in range(1,7):
							for k in range(1,7):
								newscore2.append(score([i,j,k]))
	rollnone = newscore[0]
	for i in range (1,7):
		rollc+=newscore[i]/6
	for i in range(7,13):
		rollb += newscore[i]/6	
	for i in range(13,19):
		rolla+=newscore[i]/6
	for i in range(0,36):
		rollbc+=newscore1[i]/36
	for i in range(36,72):
		rollac+=newscore1[i]/36
	for i in range(72,108):
		rollab+=newscore1[i]/36
	for i in range(0,len(newscore2)):
		rollabc+=newscore2[i]/216
	finalscore.append(rollnone)
	finalscore.append(rolla)
	finalscore.append(rollb)
	finalscore.append(rollc)
	finalscore.append(rollab)
	finalscore.append(rollac)
	finalscore.append(rollbc)
	finalscore.append(rollabc)
	#print(rollnone,rolla,rollb,rollc,rollab,rollbc,rollac,rollabc)
	return finalscore
	
board = eval(input("Enter a list with the initial state"))
solution = chancenode(board)
print("the output list is in the order of these rolls in sequence a,b,c,ab,ac,bc,abc") 
print(solution)
ele=solution.index(max(solution))
if ele ==0:
	print("..........do not reroll any dice.............")
if ele ==1:
	print("........reroll the dice a.......")
if ele ==2:
	print(".............reroll the dice b ..........")
if ele ==3:
	print(".............reroll the dice c..............")
if ele ==4:
	print("..............reroll the dice a and b...........")
if ele ==5:
	print("..............reroll the dice a and c...............")
if ele ==6:
	print("..............reroll the dice b and c...............")
if ele ==7:
	print("..............reroll the dice a,b and c...............")
