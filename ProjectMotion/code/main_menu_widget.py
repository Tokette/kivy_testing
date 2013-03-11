from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

#Builder.load_file('MainMenu.kv')
Builder.load_file('code/MainMenu.kv')

class MainMenuWidget(Screen):
	def Initialize(self, inWidgetArgs):
		pass
	
	def ChangeWidget(self, inWidgetName, inWidgetArgs):
		from code import engine
		engine.GetInstance().mUserInterface.ChangeWidget(inWidgetName, inWidgetArgs)
		
	def PreEnter(self):
		pass