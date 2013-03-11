# UserInterface.py
# Sean Duane
# 02/05/2013
# Manages the UI

from code import main_menu_widget, red_park_street_widget, subway_widget
from code.user_interface.widgets import orange_line_widget, red_line_widget, \
	transit_display
from kivy.uix.screenmanager import SlideTransition, Screen

class UIManager():
	_WidgetDictionary = {}
	_WidgetStack = []
	_CurrentWidget = None
	_ScreenManager = None
	#__RootWidget = None
	
	def __init__(self, inScreenManager):
		self._ScreenManager = inScreenManager
		self._ScreenManager.transition=SlideTransition(direction='left')
		
		self.ConstructForms()
		
	def Startup(self):
		#@HACK changing widget to the first form here
		self.ChangeWidget("MainMenu", None)
		
	def ConstructForms(self):
		#@HACK add forms elsewhere!
		#main menu
		self._WidgetDictionary["MainMenu"] = main_menu_widget.MainMenuWidget(name="MainMenu")
		self._ScreenManager.add_widget(self._WidgetDictionary["MainMenu"])
		
		#subway
		self._WidgetDictionary["Subway"] = subway_widget.SubwayWidget(name="Subway")
		self._ScreenManager.add_widget(self._WidgetDictionary["Subway"])
	
		#transit display
		self._WidgetDictionary["TransitDisplay"] = transit_display.TransitDisplayWidget(name="TransitDisplay")
		self._ScreenManager.add_widget(self._WidgetDictionary["TransitDisplay"])
		
		#red line
		self._WidgetDictionary["RedLine"] = red_line_widget.RedLineWidget(name="RedLine")
		self._ScreenManager.add_widget(self._WidgetDictionary["RedLine"])
		
		#park street
		self._WidgetDictionary["RedParkStreet"] = red_park_street_widget.RedParkStreetWidget(name="RedParkStreet")
		self._ScreenManager.add_widget(self._WidgetDictionary["RedParkStreet"])
		
		#orange line
		self._WidgetDictionary["OrangeLine"] = orange_line_widget.OrangeLineWidget(name="OrangeLine")
		self._ScreenManager.add_widget(self._WidgetDictionary["OrangeLine"])
	
	def Update(self):
		pass
		
	def ChangeWidget(self, inWidgetName, inWidgetArgs):
		if (inWidgetName in self._WidgetDictionary):
			print ("Pushing widget named", inWidgetName)
			
			# Set the current widget
			self._CurrentWidget = self._WidgetDictionary[inWidgetName]
			# Push it to the stack
			self._WidgetStack.append(self._CurrentWidget)
			# Clear out other widgets
			#self._ScreenManager.clear_widgets()
			# Add our widget
			#self._ScreenManager.add_widget(self._CurrentWidget)
			self._CurrentWidget.PreEnter()
			self._CurrentWidget.Initialize(inWidgetArgs)
			self._ScreenManager.current = inWidgetName
		else:
			print ("No widget named ", inWidgetName)
			