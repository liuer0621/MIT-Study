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


	def printGraph(self):
		queue = [self.root]
		out = []
		current_level = self.root.getHeight()
		zeroNode = Node(-1)
		zeroNode.setHeight(-1)
		cellWidth = 2
		maxWidth = (cellWidth + 1) * 2**self.maxHeight
		blankNo = int((maxWidth/(2**0) - cellWidth) / 2)
		
		while len(queue) > 0 :
			
			current_node = queue.pop(0)
#			import pdb;pdb.set_trace()
			
			if current_node.getHeight() > current_level :
				current_level += 1
                                blankNo = int((maxWidth/(2**current_level) - cellWidth) / 2)
				out.append("\n")
				for i in range(blankNo):
					out.append(' ')
			
			else :
				for i in range(blankNo) :
					out.append(' ')

			if current_node.getValue() == -1 :
				out.append(' ')
			else :
				out.append(str(current_node.getValue()))
			for i in range(blankNo) :
				out.append(' ')

			if current_node.getLeft() is not None :
				queue.append(current_node.getLeft())
			elif current_node is not zeroNode :
				queue.append(zeroNode)

			if current_node.getRight() is not None :
				queue.append(current_node.getRight())

			elif current_node is not zeroNode :
				queue.append(zeroNode)

		output = "".join(out).split("\n")
		print output
		print "".join(out)
		
						
			


input = [70,31,93,14,73,94,23]

tree = BinaryTree(Node(input[0]))

for newValue in input :
	newNode = Node(newValue)
	tree.insertChild(newNode,tree.root,0)	


#tree.printTree(tree.root)
tree.printGraph()
