'''
Sean Duane
TransitStop.py
Created on Feb 13, 2013
'''

class TransitStop():
    _StopID = 0
    _TransitSystem = None

    '''
    inStopID : int
    inTransitSystem : TransitSystem
    '''
    def __init__(self, inStopID, inTransitSystem):
        self._StopID = inStopID
        self._TransitSystem = inTransitSystem