#!/bin/python

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

	#def evolution(self,line,column):
		#if line == 0 and column == 0: #if up-left corner
			#TODO				
				
	
def countAlives(cells):
	alives = 0
	for cell in cells:
		if cell.getState():
			alives += 1
	return alives

board = Board(2)
print(str(countAlives([Cell(0),Cell(1), Cell(0)])))
