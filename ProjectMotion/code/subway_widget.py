from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

#Builder.load_file('Subway.kv')
Builder.load_file('code/Subway.kv')

class SubwayWidget(Screen):
	def Initialize(self, inWidgetArgs):
		pass
		
	def ChangeWidget(self, inWidgetName, inWidgetArgs):
		from code import engine
		engine.gEngineInstance.mUserInterface.ChangeWidget(inWidgetName, inWidgetArgs)
		
	def PreEnter(self):
		pass