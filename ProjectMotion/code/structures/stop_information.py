'''
Sean Duane
StopInformation.py
Created on Feb 13, 2013
'''

class StopInformation():
    _TransitSystem = None
    _StopName = ""
    _Destination = ""
    _TransitTimes = []
    _LastTransitTimesTimestamp = 0
    _NextTransitTime = 0
    _LastNextTrainTimestamp = 0

    '''
    inStopName : String
    inTransitSystem : TransitSystem
    inDestination : String
    '''
    def __init__(self, inStopName, inTransitSystem, inDestination):
        self._StopName = inStopName
        self._TransitSystem = inTransitSystem
        self._Destination = inDestination
        
    '''
    inTime : DateTime
    inUpdatedTime : DateTime
    '''
    def SetNextTransitTime(self, inTime, inUpdatedTime):
        self._NextTransitTime = inTime
        self._LastNextTrainTimestamp = inUpdatedTime
        
    '''
    inSchedual : List<DateTime>
    inUpdatedTime : DateTime
    '''
    def SetSchedual(self, inSchedual, inUpdatedTime):
        self._TransitTimes = inSchedual
        self._LastTransitTimesTimestamp = inUpdatedTime
        
        
    def __repr__(self):
        schedList = ', '.join(self._TransitTimes)
        returnString = 'StopInformaton(Name: "%s", Type: "%s", Dest: "%s", NextSec: "%d", TStamp: "%d", Sched: "%s", TStamp: "%d")' \
            % (self._StopName, self._TransitSystem, self._Destination, self._NextTransitTime, self._LastNextTrainTimestamp, schedList, self._LastTransitTimesTimestamp)
            
        return returnString