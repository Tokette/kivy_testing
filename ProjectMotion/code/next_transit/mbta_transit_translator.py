'''
Sean Duane
MBTATransitTranslator.py
Created on Feb 13, 2013
'''

import json
import urllib2
import warnings
from code import transit_manager
from code.next_transit.transit_translator import TransitTranslator
from code.structures.transit_system import TransitSystem
from code.structures.stop_information import StopInformation

class MBTATransitTranslator(TransitTranslator):
    '''
    Members
    '''

    '''
    Methods
    '''
    
    '''
    Constructor
    '''
    def __init__(self):
        TransitTranslator.__init__(self)
    
    '''
    inTransitStop : string
    inTransitLine : string (MUSt be lowercased)
    inTransitSystem : string
    '''
    def FetchTransitInfo(self, inTransitSystem, inTransitLine, inTransitStop):
        print ("Incoming args mbta transittranslator: %s, %s, %s") % (inTransitSystem, inTransitLine, inTransitStop)
        #@TODO Determine the system, pass to the appropriate function.
        # This jazz works differnet for the MBTA's subway, commuter rail, and bus.
        if (inTransitSystem.lower() == "subway"):
            self.FetchSubwayTransitInfo(inTransitSystem, inTransitLine, inTransitStop)
        elif (inTransitSystem.lower() == "bus"):
            self.FetchBusTransitInfo(inTransitSystem, inTransitLine, inTransitStop)
        elif (inTransitSystem.lower() == "commuterrail"):
            self.FetchBusTransitInfo(inTransitSystem, inTransitLine, inTransitStop)
        else:
            warnings.warn("Given commuter system %r is not one I (boston mbta) define" % inTransitSystem, Warning)
        
        # Inform the transit system we are complete with our stuff.
        self.mNextTransitSystem.NextTransitSystemTimeUpdated(inTransitSystem, inTransitLine, inTransitStop)
    
    '''
    Fetches info for the given subway.
    '''
    def FetchSubwayTransitInfo(self, inTransitSystem, inTransitLine, inTransitStop):
        #Construct a URL
        nextTransitURL = 'http://developer.mbta.com/lib/rthr/%s.json' % inTransitLine
        print (nextTransitURL)
        
        #@TODO split off to a thread.
        # Fetch the data
        results = urllib2.urlopen(nextTransitURL)
        #Convert from data to json
        jsonData = json.load(results)
        
        # We know what the system is at this point, so lets fetch it.
        #@TODO un-hard-code the "subway" shit
        subwayLine = transit_manager.gTransitManagerInstance.GetTransitLine(inTransitSystem, inTransitLine)
        
        #From here its pretty hardcoded, like any json junk.
        #Get the trips list
        tripList = jsonData["TripList"]
        
        # Cache out the current retrieved time
        currentRetrievalTime = tripList["CurrentTime"]
        print ("CurrentTime: %d", currentRetrievalTime)
        
        # Get the trips in this list
        trips = tripList["Trips"]
        
        # Go through each trip and store the data.
        for currentTrip in trips:
            tripID = currentTrip["TripID"]
            transitSystem = TransitSystem(tripID, inTransitSystem)
            
            destination = currentTrip["Destination"]
            direction = ""
            #@HACK fuckin idk just choose inbound or outbound
            inboundList = ["South Station", "Braintree", "Ashmont",
                           "Oak Grove", "Malden Center"]
            outboundList = ["Alewife", "Davis",
                            "Forest Hills", "Green Street"]
            if (destination in inboundList):
                direction = "inbound"
            else:
                direction = "outbound"
            
            predictions = currentTrip["Predictions"]
            for currentPrediction in predictions:
                # Fetch the current stops information.
                stopName = currentPrediction["Stop"]
                stopInfo = None
                
                #transitStop = TransitStop(currentPrediction["Stop"], transitSystem)
                if (subwayLine.has_key(stopName) 
                    and subwayLine[stopName].has_key(direction)
                    and subwayLine[stopName][direction].has_key(destination)):
                    stopInfo = subwayLine[stopName][direction][destination]
                else:
                    # Looks like we need to create a stop first.
                    stopInfo = StopInformation(stopName, transitSystem, destination)
                    
                    if (not subwayLine.has_key(stopName)):
                        subwayLine[stopName] = {}
                    if (not subwayLine[stopName].has_key(direction)):
                        subwayLine[stopName][direction] = {}
                        
                    subwayLine[stopName][direction][destination] = stopInfo
                
                # Set the appropriate information!
                stopInfo.SetNextTransitTime(currentPrediction["Seconds"], currentRetrievalTime)
                
        print ("r u rady 4 sum information overload!?")
        print (subwayLine)
        print (transit_manager.gTransitManagerInstance.GetTransitSystem("Subway"))
        
    
    '''
    Fetches info for the given commuter rail.
    '''
    def FetchCommuterTransitInfo(self, inTransitSystem, inTransitLine, inTransitStop):
        pass
    
    '''
    Fetches info for the given Bus.
    '''
    def FetchBusTransitInfo(self, inTransitSystem, inTransitLine, inTransitStop):
        pass
        