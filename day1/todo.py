import pickle


class List:
	def __init__(self, name) -> None:
		self.name = name
		self.todo = []

	def add(self):
		self.todo.append(input("> "))

	def rem(self):
		for i, j in enumerate(self.todo, 1):
			print(f"({i}) {j}")
		self.todo.pop(int(input("> ")) - 1)

	def show(self):
		for j in self.todo:
			print(f"[ ] {j}")


class Handler:
	def __init__(self) -> None:
		self.index = 0
		try:
			self.list_of_lists = []
			with open("Main.pkl", "rb") as f:
				self.list_of_lists = pickle.load(f)
		except FileNotFoundError:
			self.list_of_lists = []
			self.save_state()
		except Exception as e:
			print(e)

	def new_list(self, name):
		obj = List(name)
		self.list_of_lists.append(obj)
		self.save_state()

	def show_list(self):
		stra = []
		for i, j in enumerate(self.list_of_lists, 1):
			print(f"({i}) {j.name}")
			stra.append(j.name)
		return stra


	def rem_list(self):
		self.show_list()
		x = int(input("> ")) - 1
		self.list_of_lists.pop(x)
		self.save_state()

	def clear_list(self):
		self.list_of_lists.clear()
		self.save_state()

	def open_obj(self, i):
		self.index = i - 1

	def save_state(self):
		with open("Main.pkl", "wb") as f:
			pickle.dump(self.list_of_lists, f)

	def add_to_list(self):
		self.list_of_lists[self.index].add()
		self.save_state()

	def rem_from_list(self):
		self.list_of_lists[self.index].rem()
		self.save_state()

	def show_list_in_list(self):
		self.list_of_lists[self.index].show()

	def get_name(self):
		return self.list_of_lists[self.index].name


if __name__ == "__main__":

	hand = Handler()
	n = 0
	print("----TODO----")
	while n == 0:
		print("1. Create New List\n2.Open existing list")
		match int(input("> ")):
			case 1:
				hand.new_list(input("Enter Name Of List: "))
			case 2:
				hand.show_list()
				hand.open_obj(int(input("> ")))
				n = 1

	print(f"{hand.get_name()} List------------------")
	print("1. Add New Task\n2. Remove A Task\n3. Show Tasks\n4. Exit")
	while True:
		x = int(input(f"{hand.get_name()} > "))
		match x:
			case 1:
				hand.add_to_list()
			case 2:
				hand.rem_from_list()
			case 3:
				hand.show_list_in_list()
			case 4:
				exit()
