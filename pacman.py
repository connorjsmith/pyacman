'''
File: pacman.py
Author: Connor Smith
Title: Pyacman
Description: Pacman Clone written in Python using pygame
'''


"""
To Do:
	Ghost House? (Teleport ghosts out of house at correct time)
	Display GUI
	Level-Up
	Powerups
	Lives
	Game-Over
	Eat Ghosts After Powerups
"""
import pygame
import sys



pygame.init() #initialize pygame
window = pygame.display.set_mode((1337,1000))
#Load pacman sprites to memory
pacRIGHT = [pygame.image.load("pacclosed.png"),pygame.image.load("pacright1.png"),pygame.image.load("pacright2.png"),pygame.image.load("pacright3.png"),pygame.image.load("pacright4.png"),pygame.image.load("pacright5.png")]
pacLEFT = [pygame.image.load("pacclosed.png"),pygame.image.load("pacleft1.png"),pygame.image.load("pacleft2.png"),pygame.image.load("pacleft3.png"),pygame.image.load("pacleft4.png"),pygame.image.load("pacleft5.png")]
pacUP = [pygame.image.load("pacclosed.png"),pygame.image.load("pacup1.png"),pygame.image.load("pacup2.png"),pygame.image.load("pacup3.png"),pygame.image.load("pacup4.png"),pygame.image.load("pacup5.png")]
pacDOWN = [pygame.image.load("pacclosed.png"),pygame.image.load("pacdown1.png"),pygame.image.load("pacdown2.png"),pygame.image.load("pacdown3.png"),pygame.image.load("pacdown4.png"),pygame.image.load("pacdown5.png")]

#load pink ghost sprites
pinkLEFT = pygame.image.load("pinkyleft.png")
pinkUP = pygame.image.load("pinkyup.png")
pinkDOWN = pygame.image.load("pinkydown.png")
pinkRIGHT = pygame.image.load("pinkyright.png")
pinksprite = [pinkLEFT,pinkUP,pinkDOWN,pinkRIGHT]t
#load red ghost sprites
redLEFT = pygame.image.load ("redleft.png")
redDOWN = pygame.image.load ("reddown.png")
redRIGHT = pygame.image.load ("redright.png")
redUP = pygame.image.load ("redup.png")
#load teal ghost sprites
tealLEFT = pygame.image.load("tealleft.png")
tealRIGHT = pygame.image.load("tealright.png")
tealUP = pygame.image.load("tealup.png")
tealDOWN = pygame.image.load("tealdown.png")
#Load the orange ghost sprites
orangeLEFT = pygame.image.load ("orangeleft.png")
orangeRIGHT = pygame.image.load ("orangeright.png")
orangeUP = pygame.image.load ("orangeup.png")
orangeDOWN = pygame.image.load ("orangedown.png")

#Score Board
scoreFont = pygame.font.SysFont ("monospace", 32)
points = 0

#open the map file and store it in the board variable
f = open("map.txt",'r')
board = []
for row in range (31):
	line = f.readline()
	line = line.replace("\n","")
	board.append(line)
f.close()

def updateStatus ():
	'''Updates the score, lives etc. '''
	global scoreFont
	pygame.draw.rect (window,(0,0,0),((870,145),(350,75)),0) #current Score
	text = scoreFont.render("Score: "+str(points),1,(255,255,255))
	textpos = text.get_rect()
	textpos.centerx = 1045
	textpos.centery = 183
	window.blit(text,textpos)
	pygame.display.update((870,145),(350,75))
class Pacman(object):
	"""docstring for pacman"""
	def __init__(self):
		super(Pacman, self).__init__()
		self.row = 16 #Where to start pacman?
		self.col = 14
		self.rowcol = (16,14)
		self.x = 435
		self.y = 495
		self.direction = (1,0)  #started going right
		self.newDirection = (0,0)
		self.sprite = pacRIGHT
		self.image = pacRIGHT[0]
		self.frame = 0
		self.frameDelay = 15
	def move (self):
		"""
		#Redraw current row col space all around figure
		for row in [self.row - 1, self.row, self.row + 1]: #Should never exceed 
			for col in [self.col - 1, self.col, self.col + 1]:
				if row >= 0 and row <= 30 and col >= 0 and col <= 27:
					if board[row][col] == '@':
						pygame.draw.rect (window,(29,40,248),((col*30 + 1,row*30 + 1),(30,30)),0)
					elif board[row][col] == '*':
						pygame.draw.rect (window,(0,0,0),((col*30 + 1,row*30 + 1),(30,30)),0)
						pygame.draw.rect (window,(236,181,10),((col*30 + 12,row*30 + 12),(6,6)),0)
					else:
						pygame.draw.rect (window,(0,0,0),((col*30 + 1,row*30 + 1),(30,30)),0)
		"""
		self.x += self.direction[0]
		self.y += self.direction[1]
		self.row = (self.y - 15) / 30
		self.col = (self.x - 15) / 30
		self.rowcol = (self.row,self.col)
		self.draw()
	def check (self):
		for ghost in ghosts:
			if ghost.rowcol == self.rowcol:
				print "Dead"
		if self.x == 825: #Teleport
			pygame.draw.rect(window, (0,0,0),((810,420),(30,30)),0)
			pygame.display.update((810, 420),(30,30))
			self.col = 0
			self.rowcol = (14,0)
			self.x = 1
		elif self.x == 0: #Teleport
			pygame.draw.rect(window, (0,0,0),((0,420),(30,30)),0)
			pygame.display.update((0, 420),(30,30))
			self.col = 27
			self.rowcol = (14,27)
			self.x = 824
		global points
		if self.x % 30 == 15 and self.y % 30 == 15 and self.col != 27 and self.col != 0:
			#Check Current Direction and potential direction
			if board[self.row][self.col] == '*': #on top of points
				board[self.row] = board[self.row][:self.col] + ' ' + board[self.row][self.col+1:]
				points += 100
				updateStatus()
			if board[self.row + self.newDirection[1]][self.col + self.newDirection[0]] != '@' and self.newDirection != (0,0):
				self.direction = self.newDirection
				if self.newDirection == (1,0):
					self.sprite = pacRIGHT
				elif self.newDirection == (-1,0):
					self.sprite = pacLEFT
				elif self.newDirection == (0,1):
					self.sprite = pacDOWN
				elif self.newDirection == (0,-1):
					self.sprite = pacUP
				self.newDirection = (0,0)
			elif board[self.row + self.direction[1]][self.col + self.direction[0]] == '@':
				self.direction = (0,0)
	def update (self):
		self.frameDelay -= 1
		if self.frameDelay == 0:
			self.frame += 1
			if self.frame > 5:
				self.frame = 0
			self.image = self.sprite[self.frame]
			self.frameDelay = 15
	def draw (self):
		self.update()
		pos = self.image.get_rect()
		pos.centerx = self.x
		pos.centery = self.y
		window.blit(self.image,pos)
		'''
		pygame.draw.rect (window,(255,0,0),((self.x-10,self.y-10),(20,20)),0)
		
		'''
		pygame.display.update((self.x-15, self.y-15),(30,30)) #Make sure this contains all of the sprite
class ghost(object): #orange
	"""docstring for blinky"""
	def __init__(self):
		super(ghost, self).__init__()
		self.direction = (0,-1) #moving up
		self.sprite = orangeUP
		self.x = 375
		self.y = 315
		self.row = 11
		self.col = 16
		self.rowcol = (11,16) #used for comparing this position to pacman
	def draw (self):
		'''
		pygame.draw.rect (window,(255,255,255),((self.posxy[0]-5,self.posxy[1]-5),(10,10)))
		pygame.display.update((self.posxy[0]-30, self.posxy[1]-30),(60,60))
		'''
		pos = self.sprite.get_rect()
		pos.centerx = self.x
		pos.centery = self.y
		window.blit(self.sprite,pos)
		pygame.display.update((self.x-30, self.y-30),(60,60))
	def move (self): #Add direction to posxy and update rowcol if it exceeds current rowcol
		
		#Redraw current row col space all around figure
		for row in [self.row - 1, self.row, self.row + 1]: #Should never exceed 
			for col in [self.col - 1, self.col, self.col + 1]:
				if row >= 0 and row <= 30 and col >= 0 and col <= 27:
					if board[row][col] == '@':
						pygame.draw.rect (window,(29,40,248),((col*30 + 1,row*30 + 1),(30,30)),0)
					elif board[row][col] == '*':
						pygame.draw.rect (window,(0,0,0),((col*30 + 1,row*30 + 1),(30,30)),0)
						pygame.draw.rect (window,(236,181,10),((col*30 + 12,row*30 + 12),(6,6)),0)
					

		#self.posxy = tuple(map(sum,zip(self.posxy,self.direction))) #posxy += direction in tuple form
		self.x += self.direction[0]
		self.y += self.direction[1]
		self.row = self.y / 30 #update row and column position if it made the next step
		self.col = self.x / 30
		self.rowcol = (self.row,self.col)
		self.right = False
		self.left = False
		self.up = False
		self.down = False
		self.draw()	#redraw self
	def turn (self): #execute the turning algorithm (Different for each ghost)
		'''print self.up, self.down, self.right, self.left
								print "UP DOWN RIGHT LEFT"
								pygame.time.wait(1000)'''
		score = 1000
		targetrow = pacman.row
		targetcol = pacman.col
		#Score the square, see which is closer to target tile
		if self.up:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,-1) #change direction to up
				self.sprite = orangeUP
		if self.down:
			temp = (targetrow - (self.row + 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,1) #change direction to down
				self.sprite = orangeDOWN
		if self.right:
			temp = (targetrow - (self.row))**2 + (targetcol - (self.col + 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (1,0) #change direction to right
				self.sprite = orangeRIGHT
		if self.left:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col - 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (-1,0) #change direction to left
				self.sprite = orangeLEFT
		#reset flags
		self.up = False
		self.down = False
		self.left = False
		self.right = False
	def check (self):
		if self.x == 825: #Teleport
			pygame.draw.rect(window, (0,0,0),((810,420),(30,30)),0)
			pygame.display.update((810, 420),(30,30))
			self.col = 0
			self.rowcol = (14,0)
			self.x = 1
		elif self.x == 0: #Teleport
			pygame.draw.rect(window, (0,0,0),((0,420),(30,30)),0)
			pygame.display.update((0, 420),(30,30))
			self.col = 27
			self.rowcol = (14,27)
			self.x = 824
		#Check if the ghost is in middle of square
		if self.x % 30 == 15 and self.y % 30 == 15:
			'''
			if board[self.row + self.direction [1]][self.col + self.direction[0]] == '@':
				self.turn()
				'''
			if self.direction == (1,0): #travelling right
				#Check up, down and right
				self.up = board[self.row - 1][self.col] != '@'
				self.down = board[self.row + 1][self.col] != '@'
				self.right = board[self.row][self.col + 1] != '@'
			elif self.direction == (-1,0): #travelling left
				#check up, down and left
				self.up = board[self.row - 1][self.col] != '@'
				self.down = board[self.row + 1][self.col] != '@'
				self.left = board[self.row][self.col -1] != '@'
			elif self.direction == (0,1): #travelling down
				#check down, left, right
				self.left = board[self.row][self.col -1] != '@'
				self.down = board[self.row + 1][self.col] != '@'
				self.right = board[self.row][self.col + 1] != '@'
			elif self.direction == (0,-1): #travelling up
				#check up, left, right
				self.left = board[self.row][self.col -1] != '@'
				self.up = board[self.row - 1][self.col] != '@'
				self.right = board[self.row][self.col + 1] != '@'
			self.turn()
class pink(ghost):
	"""docstring for pinky"""
	def __init__(self):
		super(pink, self).__init__()
		self.direction = (0,-1) #moving up
		self.sprite = pinkUP
		self.posxy = (375,315)
		self.row = 11
		self.col = 16
		self.rowcol = (11,16) #used for comparing this position to pacman
	def turn (self): #execute the turning algorithm (Different for each ghost)
		'''print self.up, self.down, self.right, self.left
								print "UP DOWN RIGHT LEFT"
								pygame.time.wait(1000)'''
		score = 1000
		targetrow = pacman.row
		targetcol = pacman.col
		#Score the square, see which is closer to target tile
		if self.up:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,-1) #change direction to up
				self.sprite = pinkUP
		if self.down:
			temp = (targetrow - (self.row + 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,1) #change direction to down
				self.sprite = pinkDOWN
		if self.right:
			temp = (targetrow - (self.row))**2 + (targetcol - (self.col + 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (1,0) #change direction to right
				self.sprite = pinkRIGHT
		if self.left:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col - 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (-1,0) #change direction to left
				self.sprite = pinkLEFT
		#reset flags
		self.up = False
		self.down = False
		self.left = False
		self.right = False
class red(ghost):
	"""docstring for pinky"""
	def __init__(self):
		super(red, self).__init__()
		self.direction = (0,-1) #moving up
		self.sprite = redUP
		self.posxy = (375,315)
		self.row = 11
		self.col = 16
		self.rowcol = (11,16) #used for comparing this position to pacman
	def turn (self): #execute the turning algorithm (Different for each ghost)
		'''print self.up, self.down, self.right, self.left
								print "UP DOWN RIGHT LEFT"
								pygame.time.wait(1000)'''
		score = 1000
		targetrow = pacman.row
		targetcol = pacman.col
		#Score the square, see which is closer to target tile
		if self.up:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,-1) #change direction to up
				self.sprite = redUP
		if self.down:
			temp = (targetrow - (self.row + 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,1) #change direction to down
				self.sprite = redDOWN
		if self.right:
			temp = (targetrow - (self.row))**2 + (targetcol - (self.col + 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (1,0) #change direction to right
				self.sprite = redRIGHT
		if self.left:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col - 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (-1,0) #change direction to left
				self.sprite = redLEFT
		#reset flags
		self.up = False
		self.down = False
		self.left = False
		self.right = False
class teal(ghost):
	"""docstring for pinky"""
	def __init__(self):
		super(teal, self).__init__()
		self.direction = (0,-1) #moving up
		self.sprite = tealUP
		self.posxy = (375,315)
		self.row = 11
		self.col = 16
		self.rowcol = (11,16) #used for comparing this position to pacman
	def turn (self): #execute the turning algorithm (Different for each ghost)
		'''print self.up, self.down, self.right, self.left
								print "UP DOWN RIGHT LEFT"
								pygame.time.wait(1000)'''
		score = 1000
		targetrow = pacman.row
		targetcol = pacman.col
		#Score the square, see which is closer to target tile
		if self.up:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,-1) #change direction to up
				self.sprite = tealUP
		if self.down:
			temp = (targetrow - (self.row + 1))**2 + (targetcol - (self.col))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (0,1) #change direction to down
				self.sprite = tealDOWN
		if self.right:
			temp = (targetrow - (self.row))**2 + (targetcol - (self.col + 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (1,0) #change direction to right
				self.sprite = tealRIGHT
		if self.left:
			temp = (targetrow - (self.row - 1))**2 + (targetcol - (self.col - 1))**2
			temp = temp ** 0.5
			if temp < score:
				score = temp
				self.direction = (-1,0) #change direction to left
				self.sprite = tealLEFT
		#reset flags
		self.up = False
		self.down = False
		self.left = False
		self.right = False


def drawBoard(): #used to draw the board
	for row in range(31):
		for column in range(28):
			if board[row][column] == '@':
				pygame.draw.rect (window,(29,40,248),((column*30 + 1,row*30 + 1),(30,30)),0)
			elif board[row][column] == '*':
				pygame.draw.rect (window,(236,181,10),((column*30 + 12,row*30 + 12),(6,6)),0)

	pygame.display.flip()


blinky = teal()
pacman = Pacman ()
items = [blinky,pacman]#,pinky,clyde,inky]

drawBoard()
updateStatus()
while True: #infinite loop to get window events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0) #close the window and return 0
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and pacman.direction != (0,1):
				pacman.newDirection = (0,-1)
			elif event.key == pygame.K_DOWN and pacman.direction != (0,-1):
				pacman.newDirection = (0,1)
			elif event.key == pygame.K_RIGHT and pacman.direction != (-1,0):
				pacman.newDirection = (1,0)
			elif event.key == pygame.K_LEFT and pacman.direction != (1,0):
				pacman.newDirection = (-1,0)
	'''
	for item in items:
		item.move()
		item.check()
	pygame.time.wait(5)
	'''
	blinky.move()
	blinky.check()
	pacman.move()
	pacman.check() #flip is contained in updateStatus
	pygame.time.wait(5) #animation delay for smoothness