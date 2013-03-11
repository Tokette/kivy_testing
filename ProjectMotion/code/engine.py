# Engine.py
# Sean Duane
# 02/05/2013
# Heart of the application

from code.next_transit import next_transit_system
from code.next_transit import mbta_transit_translator
from code.favorites import favorites_system
from code import transit_manager
from code.user_interface import ui_manager

gEngineInstance = None
def GetInstance():
	global gEngineInstance
	if (gEngineInstance == None):
		gEngineInstance = Engine()
	return gEngineInstance

class Engine():
	mUserInterface = None
	mTransitManager = None
	mNextTransitSystem = None
	mFavoritesSystem = None
	mSchedualerSystem = None
	
	def __init__(self):
		global gEngineInstance
		gEngineInstance = self
	
	def Initialize(self, inScreenManager):
		self.mUserInterface = ui_manager.UIManager(inScreenManager)
		self.mTransitManager = transit_manager.TransitManager()
		self.mFavoritesSystem = favorites_system.FavoritesSystem()
		
		#@HACK These should be split off depending on what transit system we are dealing with.
		# Since idgaf and i'm in Boston, this would be the ideal thing to begin splitting off
		# for not boston transit systems, if you're into that sorta thing.
		self.mNextTransitSystem = next_transit_system.NextTransitSystem(mbta_transit_translator.MBTATransitTranslator())
		
		# Kick off the User Interface
		self.mUserInterface.Startup()
		
		# Favorites system
		self.mFavoritesSystem.Startup()
	
	def Update(self, dt):
		#Update all of our components
		
		# User Interface
		self.mUserInterface.Update()