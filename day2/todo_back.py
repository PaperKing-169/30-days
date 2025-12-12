import pickle

def get_id():
	try:
		with open("id.txt","r") as f:
			cuu_id = int(f.read())
	except FileNotFoundError:
		with open("id.txt","w") as f:
			_ = f.write(str(0))
			cuu_id = 0
	cuu_id += 1
	with open("id.txt","w") as f:
		_ = f.write(str(cuu_id))
	return int(cuu_id)

class Task:
	def __init__(self, name:str, is_done:bool = False) -> None:
		self.name:str = name
		self.is_done:bool = is_done
		self.id:int = get_id()


class TODOList:
	def __init__(self, name:str) -> None:
		self.name :str = name
		self.task_list :dict[int,Task]= {}
		self.id :int = get_id()
		pass

	def add_task(self,a:Task):
		self.task_list[a.id] = a

	def remove_task(self, id:int):
		del self.task_list[id]

	def get_task(self):
		return self.task_list.values()


class handling:
	def __init__(self) -> None:
		self.list_of_lists :dict[int, TODOList] = {}
		try:
			with open("ab.pkl","rb") as d:
				self.list_of_lists = pickle.load(d)
		except FileNotFoundError:
			with open("ab.pkl","wb") as d:
				pickle.dump({},d)
		pass

	def new_list(self, name:str):
		a = TODOList(name)
		self.list_of_lists[a.id] = a
		pass

	def save(self):
		with open("ab.pkl","wb") as d:
			pickle.dump(self.list_of_lists,d)

	def get_lists(self):
		return self.list_of_lists.values()

	def get_tasks_from_list(self, id:int):
		return self.list_of_lists[id].get_task()

	def add_task(self,id:int,name:str):
		self.list_of_lists[id].add_task(Task(name))

	def remove_task(self,id:int,tsk_id:int):
		self.list_of_lists[id].remove_task(tsk_id)
