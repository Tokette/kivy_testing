'''
Sean Duane
TransitManager.py
Created on Feb 14, 2013
'''

class DirectionEnum():
    Inbound, Outbound = range(2)

gTransitManagerInstance = None

class TransitManager():
    _TransitSystems = {} # {"Subway" : {"Red Line" : [stops] }
    
    def __init__(self):
        # Shitty Singleton
        global gTransitManagerInstance
        gTransitManagerInstance = self
    
    def Initialize(self):
        # inboundParkStInfo = self._TransitSystems["Subway"]["Red"]["ParkStreet"]["Inbound"]["Alewife"]
        self._TransitSystems["Subway"]       = {}
        self._TransitSystems["CommuterRail"] = {}
        self._TransitSystems["Bus"]          = {}
    
    
    def GetTransitLine(self, inTransitSystemName, inTransitLineName):
        if (not self._TransitSystems.has_key(inTransitSystemName)):
            self._TransitSystems[inTransitSystemName] = {}
        
        if (not self._TransitSystems[inTransitSystemName].has_key(inTransitLineName)):
            self._TransitSystems[inTransitSystemName][inTransitLineName] = {}
        
        return self._TransitSystems[inTransitSystemName][inTransitLineName]
    
    def GetTransitSystem(self, inTransitSystemName):
        if (self._TransitSystems.has_key(inTransitSystemName)):
            return self._TransitSystems[inTransitSystemName]
        return None
    
    '''
    inTransitSystemName : String
    inTransitLineName : String
    inTransitLineStopName : String
    inDestination : String
    
    Returns
    '''
    def GetTransitInfo(self, inTransitSystemName, inTransitLineName, inTransitLineStopName, inDirection):
        if (self._TransitSystems.has_key(inTransitSystemName)                         \
            and self._TransitSystems[inTransitSystemName].has_key(inTransitLineName)  \
            and self._TransitSystems[inTransitSystemName][inTransitLineName].has_key(inTransitLineStopName)
            and self._TransitSystems[inTransitSystemName][inTransitLineName][inTransitLineStopName].has_key(inDirection)
            and self._TransitSystems[inTransitSystemName][inTransitLineName][inTransitLineStopName][inDirection]):
            return self._TransitSystems[inTransitSystemName][inTransitLineName][inTransitLineStopName][inDirection]
        
        return None
    
    '''
    inTransitSystemName : String
    inTransitLineName : String
    inTransitLineStopName : String
    inDirection : DirectionEnum
    inStopInfo : StopInformation
    '''
    def SetTransitInfo(self, inTransitSystemName, inTransitLineName, inTransitLineStopName, inDestination, inStopInfo):
        #ahhhhhhhh fuck this dictionary
        if (not self._TransitSystems.has_key(inTransitSystemName)):
            self._TransitSystems[inTransitSystemName] = {}
            
        if (not self._TransitSystems[inTransitSystemName].has_key(inTransitLineName)):
            self._TransitSystems[inTransitSystemName][inTransitLineName] = {}
            
        if (not self._TransitSystems[inTransitLineName][inTransitLineName].has_key(inTransitLineStopName)):
            self._TransitSystems[inTransitLineName][inTransitLineName][inTransitLineStopName] = {}
        
        self._TransitSystems[inTransitSystemName][inTransitLineName][inTransitLineStopName][inDestination] = inStopInfo