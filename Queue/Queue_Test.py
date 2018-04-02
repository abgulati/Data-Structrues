from Queue import *

my_queue = Queue()

def printer():

	print("Size of current queue is:",my_queue.size())
	print("Current queue is:")
	my_queue.printQueue()

max = input("Create queue from 0 to ... ?")
max = int(max)

for i in range(1, max+1):
	my_queue.push(i)

printer()

print("type X and press enter to close program")
while True:
	cmd = input("Enter pop to retrieve front of queue, or push to enter more data: ")

	if cmd == "pop":
		y = my_queue.pop()
		print(y)
	elif cmd == "push":
		x = input("enter data: ")
		my_queue.push(int(x))
	elif cmd == "X":
		break

printer()