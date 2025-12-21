import sys
from typing import cast
from PyQt5.QtWidgets import QApplication, QBoxLayout, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QInputDialog, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from todo_back import handling

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setObjectName("main_window")

#NOTE:--------------------------------------------------------------------------------------------------------------------------

		self.setWindowTitle("TODO GUI")

#NOTE:--------------------------------------------------------------------------------------------------------------------------
		self.Title_box : QHBoxLayout
		self.Title : QLabel
		self.tabs_group : QVBoxLayout
		self.lists : QComboBox
		self.button : QPushButton
		self.main_layout : QVBoxLayout
		self.handle : handling
		self.addTask : QPushButton
#NOTE:--------------------------------------------------------------------------------------------------------------------------
		self.defines()
		self.layout_manage()
		self.styles()
		self.addToLayouts()
		self.setIds()
	
	def setIds(self):
		self.scrolll.setObjectName("scroll_box")
		self.scroll_widget.setObjectName("hlo")
		
		

	def styles(self):
		self.Title.setStyleSheet(
				"border: 5px solid #8B65CD;"+
				"border-radius: 10px;"
				)
		self.Title.setAlignment(Qt.AlignCenter)

		pass

	def defines(self):
		self.Title = QLabel(text="%TODO TITLE%")
		self.scrolll = QScrollArea()
		self.scroll_widget = QWidget()
		self.tabs_group = QVBoxLayout(self.scroll_widget)
		self.scrolll.setWidget(self.scroll_widget)
		self.button = QPushButton(text="Commit!")
		self.Title_box = QHBoxLayout()
		self.lists = QComboBox()
		self.lists.setCurrentIndex(-1)
		self.handle = handling()
		self.scrolll.setWidgetResizable(True)
		self.button.clicked.connect(self.commit)
		self.lists.activated.connect(self.dropdown)
		self.addTask = QPushButton(text="Add New Task")
		self.addTask.clicked.connect(self.newTask)
		self.refresh_combo()
		self.lists.setCurrentIndex(-1)


	def refresh_combo(self):
		self.lists.clear()
		for i in self.handle.get_lists():
			self.lists.addItem(i.name,userData=i.id)

		self.lists.addItem("New List")
	def commit(self):
		rem_arr = []
		for i in range(self.tabs_group.count()):
			a = self.tabs_group.itemAt(i)
			try:
				b = a.widget()
			except AttributeError:
				continue
			if not b:
				continue
			b = cast(Item,b)
			if b.check_bx.isChecked():
				rem_arr.append(b.id)
		for i in rem_arr:
			self.handle.remove_task(self.lists.currentData(),i)
		self.update_list()

	def newTask(self):
		tt, acc = QInputDialog.getText(self,"Task Title",": ")
		if tt and acc:
			print("booo")
			self.handle.add_task(self.lists.currentData(),tt)
		self.update_list()



	def dropdown(self,index):
		if self.lists.itemText(index) == "New List":
			text, acc = QInputDialog.getText(self,"List Name","Name: ")

			if text and acc:

				self.handle.new_list(text)
				self.refresh_combo()

		else:
			self.update_list()

	def update_list(self):
		while self.tabs_group.count():
			item = self.tabs_group.takeAt(0)
			if item.widget():
				item.widget().deleteLater()
		for i in self.handle.get_tasks_from_list(self.lists.currentData()):
			self.tabs_group.insertWidget(0,Item(i.name,i.id))
			print("adderd: " + i.name)


	def layout_manage(self):
		central = QWidget()
		
		self.main_layout = QVBoxLayout()
		central.setLayout(self.main_layout)
		self.setCentralWidget(central)
		pass

	def addToLayouts(self):
		self.Title_box.addWidget(self.lists,stretch=3)
		self.Title_box.addWidget(self.Title,stretch=7)
		self.main_layout.addLayout(self.Title_box,stretch=1)
		self.main_layout.addWidget(self.scrolll,stretch=8)
		self.main_layout.addWidget(self.addTask,stretch=1)
		self.main_layout.addWidget(self.button,stretch=1)
		self.tabs_group.addStretch()
		pass

class Item(QWidget):
	def __init__(self,a:str,id:int):
		super().__init__()
		self.setObjectName("Item")
		self.setAttribute(Qt.WA_StyledBackground, True)
		self.id : int = id
		self.setFixedHeight(200)
		layout = QGridLayout(self)
		self.check_bx = QCheckBox()
		self.task_name = QLabel(a)
		layout.addWidget(self.check_bx,0,0)
		layout.addWidget(self.task_name,0,1)
		self.check_bx.setStyleSheet("""
							  QCheckBox::indicator {
								width:60px;
								height:60px;
							  }
							  """)
		self.task_name.setStyleSheet("""
							   font-size: 50px;
							   """)

		self.setLayout(layout)
		self.check_bx.stateChanged.connect(self.clicked)
	

	def clicked(self,state):
		if(state==2):
						self.task_name.setStyleSheet("""
											font-size: 45px;
											font-style: italic;
											text-decoration: line-through;
											""")
		if(state==0):
						self.task_name.setStyleSheet("""
											font-size: 50px;
											font-style:normal;
											text-decoration:none;
											""")

def main():
	app = QApplication(sys.argv)

	with open("style.qss") as f:
		app.setStyleSheet(f.read())
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
