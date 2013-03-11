from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

#Builder.load_file('./user_interface/widgets/RedLine.kv')
Builder.load_file('code/user_interface/widgets/RedLine.kv')

class RedLineWidget(Screen):
	def Initialize(self, inWidgetArgs):
		pass
		
	def ChangeWidget(self, inWidgetName, inWidgetArgs):
		from code import engine
		engine.gEngineInstance.mUserInterface.ChangeWidget(inWidgetName, inWidgetArgs)
		
	def PreEnter(self):
		pass