'''
Sean Duane
TransitSystem.py
Created on Feb 13, 2013
'''
class TransitSystem():
    _TransitID = 0
    _TransitType = ""

    '''
    inTransitID : int
    inTransitType : string
    '''
    def __init__(self, inTransitID, inTransitType):
        self._TransitID = inTransitID
        self._TransitType = inTransitType
