'''
Sean Duane
TransitTranslator.py
Created on Feb 13, 2013
'''

class TransitTranslator():
    mNextTransitSystem = None
    
    def __init__(self):
        pass
    
    def SetNextTransitSystem(self, inTransitSystem):
        print "Next transit system set!"
        self.mNextTransitSystem = inTransitSystem
    
    '''
    Retreives the next transit time for the given transit system.
    '''
    def FetchTransitInfo(self, inTransitSystem, inTransitLine, inTransitStop):
        pass