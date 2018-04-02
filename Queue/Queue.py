class QueueNode:

	def __init__(self, data = None, nextNode = None):
		self.data = data
		self.nextNode = nextNode

	def setData(self, data):
		self.data = data

	def setNext(self, nextNode):
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

class Queue:

	def __init__(self, front = None, last = None):
		self.front = front
		self.last = last

	def isEmpty(self):
		if self.front is None:
			raise valueError("Cannot comply: queue is vacant")

	def push(self, data):

		if self.front == None:
			newNode = QueueNode(data)
			self.front = newNode
			self.last = newNode
		else:
			newNode = QueueNode(data)
			self.last.setNext(newNode)
			self.last = newNode

	def pop(self):

		self.isEmpty()

		tempNode = self.front

		val = tempNode.getData()
		self.front = tempNode.getNext()
		tempNode.setData(None)
		tempNode.setNext(None)

		return val

	def size(self):

		self.isEmpty()

		tempNode = self.front
		count = 0

		while(tempNode):
			count = count + 1
			tempNode = tempNode.getNext()

		return count

	def search(self, data):

		self.isEmpty()

		tempNode = self.front

		while(tempNode):
			if tempNode.getData() == data:
				print("data present")
				return
			tempNode = tempNode.getNext()

		print("Data not found")
		return

	def printQueue(self):

		self.isEmpty()

		tempNode = self.front

		while(tempNode):
			print(tempNode.getData())
			tempNode = tempNode.getNext()
		return