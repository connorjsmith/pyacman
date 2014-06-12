import pygame
import sys


pygame.init() #initialize pygame
window = pygame.display.set_mode((900,700))


#open the map file and store it in the board variable
f = open("map.txt",'r')
board = []
for row in range (31):
	line = f.readline()
	line = line.replace("\n","")
	board.append(line)
f.close()

class pacman(object):
	"""docstring for pacman"""
	def __init__(self, arg):
		super(pacman, self).__init__()
		self.arg = arg
		row = 16 #Where to start pacman?
		column = 14
	def move ():
		pass

class pink(object):
	"""docstring for pinky"""
	def __init__(self):
		super(pink, self).__init__()
		self.direction = (-1,0) #moving to the left
		self.posxy = (400,300)
		self.row = 5
		self.col = 5
		self.rowcol = (5,5) #used for comparing this position to pacman
	def draw (self):
		pygame.draw.rect (window,(255,255,255),((self.posxy[0]-5,self.posxy[1]-5),(10,10)))
		pygame.display.flip()
	def move (self): #Add direction to posxy and update rowcol if it exceeds current rowcol
		#Redraw current row col space all around figure
		for row in [self.row - 1, self.row, self.row + 1]: #Should never exceed 
			for col in [self.col - 1, self.col, self.col + 1]:
				if row >= 0 and row <= 30 and col >= 0 and col <= 27:
					if board[row][col] == '@':
						pygame.draw.rect (window,(29,40,248),((col*21 + 1,row*21 + 1),(21,21)),0)
					elif board[row][col] == '*':
						pygame.draw.rect (window,(236,181,10),((col*21 + 9,row*21 + 9),(5,5)),0)
					else:
						pygame.draw.rect (window,(0,0,0),((col*21 + 1,row*21 + 1),(21,21)),0)
		'''
		self.posxy[0] += self.direction[0] #move the sprite
		self.posxy[1] += self.direction[1]
		'''
		self.posxy = tuple(map(sum,zip(self.posxy,self.direction)))
		print (self.posxy)
		self.row = self.posxy[1] / 21 #update row and column position if it made the next step
		self.col = self.posxy[0] / 21
		self.rowcol = (self.row,self.col)
		print self.row
		print self.col
		self.draw()	#redraw self
	def turn (self): #execute the turning algorithm (Different for each ghost)
		print "Turned"
		pygame.time.wait(1000)
		self.direction = (0,-1)
		pass
class blue(object):
	"""docstring for blinky"""
	def __init__(self):
		super(blue, self).__init__()
		self.direction = (-1,0) #moving to the left
		self.posxy = (400,300)
		self.row = 5
		self.col = 5
		self.rowcol = (5,5) #used for comparing this position to pacman
	def draw (self):
		pygame.draw.rect (window,(255,255,255),((self.posxy[0]-5,self.posxy[1]-5),(10,10)))
		pygame.display.flip()
	def move (self): #Add direction to posxy and update rowcol if it exceeds current rowcol
		#Redraw current row col space all around figure
		for row in [self.row - 1, self.row, self.row + 1]: #Should never exceed 
			for col in [self.col - 1, self.col, self.col + 1]:
				if row >= 0 and row <= 30 and col >= 0 and col <= 27:
					if board[row][col] == '@':
						pygame.draw.rect (window,(29,40,248),((col*21 + 1,row*21 + 1),(21,21)),0)
					elif board[row][col] == '*':
						pygame.draw.rect (window,(236,181,10),((col*21 + 9,row*21 + 9),(5,5)),0)
					else:
						pygame.draw.rect (window,(0,0,0),((col*21 + 1,row*21 + 1),(21,21)),0)
		'''
		self.posxy[0] += self.direction[0] #move the sprite
		self.posxy[1] += self.direction[1]
		'''
		self.posxy = tuple(map(sum,zip(self.posxy,self.direction)))
		print (self.posxy)
		self.row = self.posxy[1] / 21 #update row and column position if it made the next step
		self.col = self.posxy[0] / 21
		self.rowcol = (self.row,self.col)
		print self.row
		print self.col
		self.draw()	#redraw self
	def turn (self): #execute the turning algorithm (Different for each ghost)
		print "Turned"
		pygame.time.wait(1000)
		self.direction = (0,-1)
		pass

blinky = blue()
for i in range(100):
	blinky.move()
	pygame.time.wait(25)
blinky.turn()
for i in range(100):
	print "Entered"
	blinky.move()
	pygame.time.wait(25)
while True: #infinite loop to get window events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0) #close the window and return 0
