#!/usr/bin/env python

class Node():
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value
		self.parent = None
		self.height = None

	def insertLeft(self,node):
		self.left = node

	def insertRight(self,node):
		self.right = node

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setParent(self,node):
		self.parent = node

	def getParent(self):
		return self.parent

	def getValue(self):
		return self.value

	def getHeight(self):
		return self.height

	def setHeight(self,currentHeight):
		self.height = currentHeight
		


class BinaryTree():
	def __init__(self,root):
		self.root = root
		self.maxHeight = 0


	def insertChild(self,newNode,root,currentHeight):

		root.setHeight(currentHeight)
		

		if newNode.getValue() < root.getValue() :
			if root.getLeft() == None :
				root.insertLeft(newNode)
				newNode.setHeight(currentHeight+1)
				if self.maxHeight < currentHeight+1 :
					self.maxHeight = currentHeight+1
			else : 
				self.insertChild(newNode,root.getLeft(),currentHeight+1)

		elif newNode.getValue() > root.getValue() :
			if root.getRight() == None :
				root.insertRight(newNode)
				newNode.setHeight(currentHeight+1)
				if self.maxHeight < currentHeight+1 :
					self.maxHeight = currentHeight+1

			else :
				self.insertChild(newNode,root.getRight(),currentHeight+1)



	def printTree(self,root):
		if root == None :
			pass
		else :
			self.printTree(root.getLeft())
			print root.getValue(),root.getHeight()
			self.printTree(root.getRight())	
	

	def printGraph(self,root):
		if root == None :
			pass
	
		else :
			


input = [70,31,93,14,73,94,23]

tree = BinaryTree(Node(input[0]))

for newValue in input :
	newNode = Node(newValue)
	tree.insertChild(newNode,tree.root,0)	


tree.printTree(tree.root)
tree.printGraph(tree.root)
