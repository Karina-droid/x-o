import console

x_o = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#positions in which smb wins
end = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5)]
turn = ['X', 'O']
#contains all the postions that are already taken
taken = []

class Color:
	def __init__(self, value):
		self.value = value
		self.red = 1
		self.green = 1
		self.blue = 1
		
	def switch_color(self):
		#all numbers will be white, 'X' - red, 'O' - blue
		if self.value == 'X':
			self.red, self.green, self.blue = 1, 0, 0
		elif self.value == 'O':
			self.red, self.green, self.blue = 0, 0, 1
		else:
			self.red, self.green, self.blue = 0, 0, 0
		console.set_color(self.red, self.green, self.blue)
	
	@classmethod	
	#asks where to put 'X'/'O' and replaces a number with it, making it an object of Color
	def putXO(cls, t):
		place = int(input(f'Where to put {t}? '))
		if place not in range(1, 10):
			place = int(input('Enter a number from 1 to 9: '))
		else:
			while place in taken:
				place = int(input('This position is already taken. Enter a number that not taken by X or O: '))
			else:
				x_o[place-1] = cls(t)
				taken.append(place)
			


def to_Color(list):
	#makes all numbers in list to be Color objects
	for i in range(len(list)):
		list[i] = Color(list[i])

def printXO(list):
	#makes the symbols to be printed in the color they need to be
	for num, i in enumerate(list,1):
		i.switch_color()
		#to print the 3 symbols in line
		if num%3 == 0:
			print(i.value)
		else:
			print(i.value, end='  ')
			
#when to end the game
def end_game():
	for tuple in end:
		x,y,z = tuple
		if x_o[x].value == x_o[y].value == x_o[z].value:
			if x_o[x].value == 'X':
				print(f'{X} won!')
			else:
				print(f'{O} won!')
			return True
				
	for n in x_o:
		if n != 'X' or n != 'O':
			return False
			break
		else:
			print('Well done! You have a draw.')
			return True
	return False
						

to_Color(x_o)
printXO(x_o)
X = input("Who is the 'X' player? ")
O = input("Who is the 'O' player? ")

game_over = False
while not game_over:
	for t in turn:
		game_over = end_game()
		if game_over == True:
			break
		Color.putXO(t)
		printXO(x_o)
		console.set_color(0, 0, 0)
