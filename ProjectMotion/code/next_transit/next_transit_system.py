'''
Sean Duane
NextTransitSystem.py
Created on Feb 13, 2013
'''	

class NextTransitSystem():
	# Members
	_TransitListeners = []
	_TransitTranslator = None
	
	# Methods
	'''
	inTransitTranslator : TransitTranslator
	'''
	def __init__(self, inTransitTranslator):
		self._TransitTranslator = inTransitTranslator
		self._TransitTranslator.SetNextTransitSystem(self)
		
	''' Adds objects as event listeners '''
	def RegisterAsListener(self, inListener):
		if (not inListener in self._TransitListeners):
			print ("NextTransit Registering new interface")
			self._TransitListeners.append(inListener)
		
	''' Removes objects as event listeners '''
	def UnRegisterAsListener(self, inListener):
		self._TransitListeners.remove(inListener)
	
	''' Fetches the asked transit time. '''
	def FetchNextTransitSystemTimes(self, inTransitSystem, inTransitLine, inTransitStop):
		# Let the translator handle the request, just give them the transit line.
		self._TransitTranslator.FetchTransitInfo(inTransitSystem, inTransitLine, inTransitStop)
		
	''' Times were updated for a time, inform application. '''
	def NextTransitSystemTimeUpdated(self, inUpdatedTransitSystem, inUpdatedTransitLine, inUpdatedTransitStop):
		# Times were updated for the given transit line.
		# Inform all the transit lines of the update
		for listener in self._TransitListeners:
			print ("NextTransit firing updated info %s, %s, %s") % (inUpdatedTransitSystem, inUpdatedTransitLine, inUpdatedTransitStop)
			listener.TransitUpdate(inUpdatedTransitSystem, inUpdatedTransitLine, inUpdatedTransitStop)
	
	'''  '''
	def PreEnter(self):
		#@HACK shoving time fetching and setting code here. This has to be moved
		#to its own system after the presentation.
		pass
		
		