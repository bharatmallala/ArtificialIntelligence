#Bharat Mallala,2017
#collaborated with Jyothi Pranavi Devineni
import copy
import sys
import cProfile

from queue import PriorityQueue
#converting the input file into list of lists
#code line 10-12 taken from "https://stackoverflow.com/questions/31363453/in-python-how-to-get-integer-lists-from-a-txt-file-with-space-separated-and"
	N = (sys.argv[1])
	with open(N) as x:
		ini_board = [[int(num) for num in line.split()] for line in x]
	print(ini_board)
goal_board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]





#solving for problem using A* using number of misplaced tiles as h(s) which is consistent
#since our h(s) is consistent we are using search Algorithm 3 which also discards the revisited states making the it much more efficient in finding goal


#calculating the f(s) = h(s) + g(s).....Here the heuristic is the sum of the Manhattan distance/3 to the goal state
def heuristic(board):
	#print("In heuristic")
	h = 0
	i = 0
	conflict = 0
	for r in range(0,len(board)):
		for c in range(0,len(board)):
			if board[r][c] != 0:
				if board[r][c] != goal_board[r][c]:
					x = r
					y = c
					if ((r+1<len(board) and board[r][c]==goal_board[r+1][c] and board[r+1][c] == goal_board[r][c] ) or
					(r+2<len(board) and board[r][c]==goal_board[r+2][c]and board[r+2][c]==goal_board[r][c]) or
					(r+3<len(board) and board[r][c]==goal_board[r+3][c] and board[r+3][c] == goal_board[r][c]) or 
					(c+1<len(board) and board[r][c]==goal_board[r][c+1]and board[r][c+1]==goal_board[r][c]) or
					(c+2<len(board) and board[r][c]==goal_board[r][c+2] and board[r][c+2]==goal_board[r][c]) or
					(c+3<len(board) and board[r][c]==goal_board[r][c+3] and board[r][c+3]==goal_board[r][c])):
						conflict = conflict+1
					#print (conflict)
					for r1 in range(0,len(board)):
						for c1 in range(0,len(board)):
							if goal_board[r1][c1] == board[r][c]:
								x1 = r1
								y1 = c1
							
							
					h = h + abs(x1-x)+abs(y1-y)
	#print (conflict,h/3)		
	return(h/3+conflict*2)
	
# finding the path to the state
	

#checking for goal state
def goal_check(board):	
	#print("In goal_check")
	if board == goal_board:
		return True
	else:
		return False

		
		
def newcopy(board):
	newboard=[]
	for i in range(0,len(board)):
		newboard1 =[]
		for j in range(0, len(board)):
			
			newboard1.append(board[i][j])
		newboard.append(newboard1)
	#a= board[0]
	#b = board[1]
	#c= board[2]
	#3d= board[3]
	
	return newboard
	
#prioritizing based on the heuristic function

	
#calculating the sucessors. Here we can movve one,two or three tiles at a time
def successors(board):
	#print("In successors")
	x=0
	y=0
	for r in range(0,len(board)):
		for c in range(0,len(board)):
			if board[r][c] ==0:
				x = r
				y = c
	final = []
	final.extend(moove1(board,x,y))
	final.extend(moove2(board,x,y))
	final.extend(moove3(board,x,y))
	
	return final
#function which returns all possible 1 moves	
def moove1(board,r,c):
	#print("In moove 1")
	suc =[]
	if r+1< len(board):
		
		newboard = newcopy(board)
		newboard[r][c], newboard[r+1][c] = newboard[r+1][c] ,newboard[r][c]
		suc.append([newboard, 'U1'+str(c+1)])
		#path.append('D1'+str(c))
		
	if c+1< len(board):
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c+1] = newboard[r][c+1] ,newboard[r][c]
		suc.append([newboard,'L1'+str(r+1)])
		#path.append('L1'+str(r))

	if  r-1>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r-1][c] = newboard[r-1][c] ,newboard[r][c]
		suc.append([newboard,'D1'+str(c+1)])
		#path.append('U1'+str(c))
		

	if c-1>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c-1] = newboard[r][c-1] ,newboard[r][c]
		suc.append([newboard,'R1'+str(r+1)])
		#path.append('R1'+str(r))
	return suc
	
#function which returns all possible 2 moves	
def moove2(board,r,c):
	suc = []
	#print("In moove 2")
	if r+2< len(board):
		newboard = newcopy(board)
		newboard[r][c], newboard[r+1][c],newboard[r+2][c] = newboard[r+1][c] ,newboard[r+2][c],newboard[r][c] 
		suc.append([newboard,'U2'+str(c+1)])
		#path.append('D2'+str(c))
	if c+2< len(board):
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c+1],newboard[r][c+2] = newboard[r][c+1] ,newboard[r][c+2],newboard[r][c]
		suc.append([newboard,'L2'+str(r+1)])
		#path.append('L2'+str(r))
	if  r-2>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r-1][c],newboard[r-2][c] = newboard[r-1][c] ,newboard[r-2][c],newboard[r][c]
		suc.append([newboard,'D2'+str(c+1)])
		#path.append('U2'+str(c))
	if c-2>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c-1],newboard[r][c-2] = newboard[r][c-1] ,newboard[r][c-2],newboard[r][c]
		suc.append([newboard,'R2'+str(r+1)])
		#path.append('R2'+str(r))
	return suc
	
#function which returns all possible 3 moves
def moove3(board,r,c):
	suc = []
	#print("In moove 3")
	if r+3< len(board):
		newboard = newcopy(board)
		newboard[r][c], newboard[r+1][c],newboard[r+2][c],newboard[r+3][c] = newboard[r+1][c] ,newboard[r+2][c],newboard[r+3][c],newboard[r][c] 
		suc.append([newboard,'U3'+str(c+1)])
		#path.append('D3'+str(c))
	if c+3< len(board):
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c+1],newboard[r][c+2],newboard[r][c+3] = newboard[r][c+1] ,newboard[r][c+2],newboard[r][c+3],newboard[r][c]
		suc.append([newboard,'L3'+str(r+1)])
		#path.append('L3'+str(r))
		
	if  r-3>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r-1][c],newboard[r-2][c],newboard[r-3][c] = newboard[r-1][c] ,newboard[r-2][c],newboard[r-3][c],newboard[r][c]
		suc.append([newboard,'D3'+str(c+1)])
		#path.append('U3'+str(c))
	if c-3>=0:
		newboard = newcopy(board)
		newboard[r][c], newboard[r][c-1],newboard[r][c-2],newboard[r][c-3] = newboard[r][c-1] ,newboard[r][c-2],newboard[r][c-3],newboard[r][c]
		suc.append([newboard,'R3'+str(r+1)])
		#path.append('R3'+str(r))
	return suc

#def permute(board):
#	count = 0
#	for i in range(0,len(board)):
#		for j in range(0,len(board)):
#			if  i > board[i][j] and board[i][j] != 0:
#				count = count+1
#				print (count)
#	for r in range(0,len(board)):
#		for c in range(0,len(board)):
#			if board[r][c] ==0:
#				x = r
#	count = count+r
#	if count%2 != 1:
#		return "no solution"
#	else:
#		return "solution exit"
		
def Astar(ini_board):
	path = ""
	revisited = {}
	alpha = 3
	g = 0
	fringe = PriorityQueue()
	if goal_check(ini_board): #checking if initital state is goal state
		print("Solution found............!!!!    No mooves required")

		return(ini_board)
		#path = []
	else:
		fringe.put((heuristic(ini_board)*alpha,(ini_board,'00',0))) #placing initial board in fringe
		while len(fringe.queue)>0:
			#print("in while")
			board_final=fringe.get()
			#s = board_final[0]
			#print (board_final)
			board = board_final[1][0]	# retreiving the state which has the lowest priority
			#print (board)
			#print("after while")
			path = board_final[1][1]
			#print("Path in while --> " + str(path))
			#print("board_final[1][1] --> " + str(board_final[1][1]))
			#print(board)
			temp = tuple(tuple(x) for x in board) # code taken from "https://stackoverflow.com/questions/5506511/python-converting-list-of-lists-to-tuples-of-tuples"
			revisited.update({temp:4}) # adding the current state to revisited
			if goal_check(board): # checking if the current state is the goal state
				#print("solution found")
				return path

				#for i in range (1,len(finalpath)):
				#	print(finalpath[i])
				
				#return(path)
			g = g+1
			for k in successors(board):
				#print ( "sucessors", k)
				if goal_check(k[0]):
					#print ("p --> " + str(path))
					#print ("k[1] -->" + str(k[1]))
					#x = path.extend(k[1])
					#print (x)
					#return x
					#print ("y --> " + str(path))
					#return path+[k[1]]
					final_path = (path+" "+k[1]).replace('00 ', '')
					print(final_path)
					return final_path 
					
					#getting the successors of current state and appeding it to fringe
					#s=k[0]
					#print (heuristic(k[0]))
				
				temp = tuple(tuple(x) for x in k[0]) # code taken  from https://stackoverflow.com/questions/5506511/python-converting-list-of-lists-to-tuples-of-tuples
				
				if revisited.get(temp,3)==3:
					#print("in if")
					
					#print (temp)
					revisited.update({temp:4})
						
						

					if k[0] in fringe.queue:
							#if k[0] == fringe.queue[i][1][0]:
						for i in range(0,len(fringe.queue)):
							if g < fringe.queue[i][1][2]:
								fringe.get(i)
					#print("abc --> " + str(path))
					#print("def --> " + str(k[1]))
					x = path+ " "+k[1]
					#print ("x --> " + str(x))
					#fringe.put((heuristic(k[0])+g,[k[0],path+[k[1]],g]))
					fringe.put(((heuristic(k[0]))*alpha+g,[k[0],x,g]))
						#else:
						#	for i in range(0,len(fringe.queue)):
						#fringe1.append(fringe.queue[i][1])
						#		if k[0] == fringe.queue[i][1][0]:
						#			if heuristic(k[0])< fringe.queue[i][0]:
						#				fringe.queue[i][0] = heuristic(k[0])+g
						#				fringe.queue[i][1]=k
										
						
	#return False			

#def solve_puzzle2(board):
#	fringe = PriorityQueue()
#	finalpath = []
#	g = 0
#	if goal_check(ini_board):
#		return ini_board
#	else:
#		fringe.put((1,[ini_board,'']))
#		#print (fringe.queue) #placing initial board in fringe
#	while len(fringe.queue)>0:
#		print("in while")
#		#print (fringe.queue) #placing initial board in fringe

#		board_final=fringe.get()[1]
#		board = board_final[0]
#		print (board)# retreiving the state which has the lowest priority
#		print("after while")

#		finalpath.append(board_final[1])
		
#		if goal_check(board) == True: # checking if the current state is the goal state
#				return finalpath

				#for i in range (1,len(finalpath)):
				#	print(finalpath[i])
#		else:
#			g= g+1
#			for k in successors(board):
#				s=k[0]
#				fringe.put((heuristic(s)+g,k))

		
print("-------------Finding solution---------------")
print()
print(cProfile.run('print(Astar(ini_board))'))
solution=Astar(ini_board)
print("------------Solution found----------------")
print(solution)