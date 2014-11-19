#!/usr/bin/python

class Cell:
	"""A cell"""
	state = 0 #0 is False = cell is dead // 1 is True = cell is alive
	
	def __init__(self,state):
		self.state = state

	def getState(self):
		return self.state

	def setState(self, state):
		if state == 1 or state == 0:
			self.state = state
		else:
			print "***Setting state error***"

	def __str__(self):
		return str(self.getState())

class Board:
	"""Class defining a  board"""
	lines = []
	size = 0

	def __init__(self, size):
		self.size = size
		for i in range(0,size):
			aLine = []
			for j in range(0,size):
				aLine.append(Cell(0))
			self.lines.append(aLine) 	

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

		#TODO change state of cell in function of alives 

def countAlives(cells):
	alives = 0
	for cell in cells:
		if cell.getState():
			alives += 1
	return alives
