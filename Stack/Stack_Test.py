from Stack import *

my_stack = Stack()

def printer():
	print("The size of the stack is:", my_stack.size())
	print("The stack is:")
	my_stack.printStack()

max = input("Create stack from 0 to... ? : ")
max = int(max)

for i in range(1, max+1):
	my_stack.push(i)

printer()

print("type X and press enter to close program")
while True:
	cmd = input("Enter pop to retrieve top of the stack, or push to enter more data: ")

	if cmd == "pop":
		y = my_stack.pop()
		print(y)
	elif cmd == "push":
		x = input("enter data: ")
		my_stack.push(int(x))
	elif cmd == "X":
		break

printer()