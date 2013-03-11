from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ObjectProperty

#Builder.load_file('RedParkStreet.kv')
Builder.load_file('code/RedParkStreet.kv')

class RedParkStreetWidget(Screen):
	label_wid = ObjectProperty()
	_SecondsToNext = NumericProperty(0)
		
	def ChangeWidget(self, inWidgetName, inWidgetArgs):
		from code import engine
		uiInstance = engine.gEngineInstance.mUserInterface
		uiInstance.ChangeWidget(inWidgetName, inWidgetArgs)
		
	def PreEnter(self):
		#@HACK shoving time fetching and setting code here. This has to be moved
		#to its own system after the presentation.
		from code import engine
		engineInstance = engine.gEngineInstance
		nextTransitSystem = engineInstance.mNextTransitSystem
		nextTransitSystem.FetchNextTransitSystemTimes("ParkStreet", "red", "Subway")