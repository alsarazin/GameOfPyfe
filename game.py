#!/usr/bin/python

import copy,time

class Cell:
	"""A cell"""
	state = 0 #0 is False = cell is dead // 1 is True = cell is alive
	
	def __init__(self,state):
		self.state = state

	def setState(self, state):
		if state == 1 or state == 0:
			self.state = state
		else:
			print "***Setting state error***"

	def __str__(self):
		return str(self.state)

class Board:
	"""Class defining a  board"""

	def __init__(self, size):
		self.size = size
		self.lines = []
		for i in range(0,size):
			aLine = []
			for j in range(0,size):
				aLine.append(Cell(0))
			self.lines.append(aLine) 	

	def __str__(self):
		res = ""
		for line in self.lines:
			for cell in line:
				if cell.state:
					res += "X"
				else:
					res += "."
				res += " "
			res += "\n"
		return res

	def evolution(self,line,column):
		alives = 0
		
		if line == 0: #if up line
			cell_down = self.lines[line+1][column] 
			
			if column == 0:	#if up-left corner
				alives = countAlives([self.lines[line][column+1],cell_down,self.lines[line+1][column+1]])
			
			elif column == self.size-1: #if up-right corner
				alives = countAlives([self.lines[line][column-1],cell_down,self.lines[line+1][column-1]])
			
			else:
				alives = countAlives([self.lines[line][column-1],self.lines[line][column+1],self.lines[line+1][column-1],cell_down,self.lines[line+1][column+1]])
		
		elif line == self.size-1: #if bottom line
			cell_up = self.lines[line-1][column]
			
			if column == 0: #if down-left corner
				alives = countAlives([self.lines[line][column+1], cell_up, self.lines[line-1][column+1]])
			
			elif column == self.size-1: #if down-right corner
				alives = countAlives([self.lines[line][column-1], cell_up, self.lines[line-1][column-1]])
			
			else:
				alives = countAlives([self.lines[line][column-1], self.lines[line][column+1], self.lines[line-1][column-1], cell_up, self.lines[line-1][column+1]])
		
		elif column == 0: #if left column except corners
			alives = countAlives([self.lines[line-1][column],self.lines[line-1][column+1],self.lines[line][column+1],self.lines[line+1][column+1], self.lines[line+1][column]])
		
		elif column == self.size-1: # if right column except corners
			alives = countAlives([self.lines[line-1][column],self.lines[line-1][column-1],self.lines[line][column-1],self.lines[line+1][column-1], self.lines[line+1][column]])
		
		else: #all the other cells
			alives = countAlives([self.lines[line-1][column-1],self.lines[line-1][column],self.lines[line-1][column+1],self.lines[line][column-1],self.lines[line][column+1],self.lines[line+1][column-1], self.lines[line+1][column],self.lines[line+1][column+1]])

		new_state = self.lines[line][column].state

		if new_state: #if cell is alive
			if alives < 2 or alives > 3:
				new_state = 0
		else: #if cell is dead
			if alives == 3:
				new_state = 1

		return new_state

	def tick(self):
		new_board = copy.deepcopy(self)
		for line in range(0,new_board.size-1):
			for column in range(0,new_board.size-1):
				new_board.lines[line][column].state = board.evolution(line,column)

		board.lines = new_board.lines

def countAlives(cells):
	alives = 0
	for cell in cells:
		if cell.state:
			alives += 1
	return alives

board = Board(40)

#----------GUN SLIDER-------------
board.lines[4][0].state = 1
board.lines[5][0].state = 1
board.lines[4][1].state = 1
board.lines[5][1].state = 1

board.lines[2][13].state = 1
board.lines[2][12].state = 1
board.lines[3][11].state = 1
board.lines[4][10].state = 1
board.lines[5][10].state = 1
board.lines[6][10].state = 1
board.lines[7][11].state = 1
board.lines[8][12].state = 1
board.lines[8][13].state = 1
board.lines[7][15].state = 1

board.lines[5][14].state = 1
board.lines[3][15].state = 1
board.lines[7][15].state = 1

board.lines[4][16].state = 1
board.lines[5][16].state = 1
board.lines[6][16].state = 1
board.lines[5][17].state = 1

board.lines[2][20].state = 1
board.lines[3][20].state = 1
board.lines[4][20].state = 1
board.lines[2][21].state = 1
board.lines[3][21].state = 1
board.lines[4][21].state = 1
board.lines[1][22].state = 1
board.lines[5][22].state = 1
board.lines[0][24].state = 1
board.lines[1][24].state = 1
board.lines[5][24].state = 1
board.lines[6][24].state = 1

board.lines[2][35].state = 1
board.lines[3][35].state = 1
board.lines[2][34].state = 1
board.lines[3][34].state = 1
#--------------------------------------------

print board
while 1:
	time.sleep(0.1)
	board.tick()
	print board
