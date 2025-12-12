import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from todo_back import handling

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

#NOTE:--------------------------------------------------------------------------------------------------------------------------

		self.setWindowTitle("TODO GUI")

#NOTE:--------------------------------------------------------------------------------------------------------------------------
		self.Title_box : QHBoxLayout
		self.Title : QLabel
		self.tabs_group : QVBoxLayout
		self.lists : QComboBox
		self.button : QPushButton
		self.main_layout : QVBoxLayout
#NOTE:--------------------------------------------------------------------------------------------------------------------------
		self.defines()
		self.layout_manage()
		self.styles()
		self.addToLayouts()

	def styles(self):
		self.Title.setStyleSheet(
				"border: 5px solid #8B65CD;"+
				"border-radius: 10px;"
				)
		self.Title.setAlignment(Qt.AlignCenter)

		pass

	def defines(self):
		self.Title = QLabel(text="%TODO TITLE%")
		self.tabs_group = QVBoxLayout()
		self.button = QPushButton(text="Commit!")
		self.Title_box = QHBoxLayout()
		self.lists = QComboBox()
		tb = handling()
		self.lists.addItem("Select List")
		self.lists.setCurrentIndex(-1)
		tb.new_list("test")
		tb.new_list("test2")
		for i in tb.get_lists():
			self.lists.addItem(i.name)

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
		self.main_layout.addLayout(self.tabs_group,stretch=8)
		self.main_layout.addWidget(self.button,stretch=1)
		
		self.tabs_group.addWidget(Item("text"))
		self.tabs_group.addWidget(Item("test2"))
		self.tabs_group.addWidget(QLabel(""))
		pass

class Item(QWidget):
	def __init__(self,a:str):
		super().__init__()
		self.setObjectName("Item")
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
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
