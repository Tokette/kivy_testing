'''
Created on Mar 7, 2013

@author: MintyAnt
'''
from code.next_transit.i_transit import ITransit
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import Screen

#Builder.load_file('./user_interface/widgets/TransitDisplay.kv')
Builder.load_file('code/user_interface/widgets/TransitDisplay.kv')

class TransitDisplayWidget(Screen, ITransit):
    _TransitSystem = ""
    _TransitLine = ""
    _TransitStop = ""
    _InboundScreen = ObjectProperty(None)
    _OutboundScreen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(TransitDisplayWidget, self).__init__(**kwargs)
        
        accord = Accordion()
        
        self._InboundScreen = TransitDisplayScreenWidget(title = "Inbound")
        accord.add_widget(self._InboundScreen)
        
        self._OutboundScreen = TransitDisplayScreenWidget(title = "Outbound")
        accord.add_widget(self._OutboundScreen)
        
        self.add_widget(accord)
        
        
    def PreEnter(self):
        pass
    
    def Initialize(self, inWidgetArgs):#, inTransitSystem, inTransitLine, inTransitStop):
        self._TransitSystem = inWidgetArgs[0]#inTransitSystem
        self._TransitLine = inWidgetArgs[1]#inTransitLine
        self._TransitStop = inWidgetArgs[2]#inTransitStop
        
        print ("My args are: %s, %s, %s") % (self._TransitSystem, self._TransitLine, self._TransitStop)
        
        # Register with a transit system if we havent registered already.
        from code import engine
        nextTransitSystem = engine.gEngineInstance.mNextTransitSystem
        nextTransitSystem.RegisterAsListener(self)
        nextTransitSystem.FetchNextTransitSystemTimes(self._TransitSystem, self._TransitLine, self._TransitStop)
        
        # Update the transit info
        self.UpdateTransitInfo();
        
    def UpdateTransitInfo(self):
        print ("Updating our transit information")
        
        # Updates all the UI with current data
        #inbound
        from code import engine
        inboundStopsInfo = engine.gEngineInstance.mTransitManager.GetTransitInfo( \
                        self._TransitSystem, self._TransitLine, self._TransitStop, "inbound")
        
        print ("Inbound object: %r") % inboundStopsInfo
        if (inboundStopsInfo != None):
            self._InboundScreen.mTransitTitle = self._TransitStop
            self._InboundScreen.mTransitDirection = "Inbound"
            
            newList = []
            for currentStopKey in inboundStopsInfo:
                currentStop = inboundStopsInfo[currentStopKey]
                transitTimeAsString = ("%d - %s") % (currentStop._NextTransitTime, currentStop._Destination)
                newList.append(transitTimeAsString)
                
            self._InboundScreen.mNextTransitList = newList
        
        #outbound
        outboundStopInfo = engine.gEngineInstance.mTransitManager.GetTransitInfo( \
                        self._TransitSystem, self._TransitLine, self._TransitStop, "outbound")
        if(outboundStopInfo != None):
        
            self._OutboundScreen.mTransitTitle = self._TransitStop
            self._OutboundScreen.mTransitDirection = "Outbound"
            
            newList = []
            for currentStopKey in outboundStopInfo:
                currentStop = outboundStopInfo[currentStopKey]
                transitTimeAsString = ("%d - %s") % (currentStop._NextTransitTime, currentStop._Destination)
                newList.append(transitTimeAsString)
                
            self._OutboundScreen.mNextTransitList = newList
            #self._OutboundScreen.mNextTransitList = outboundStopInfo._NextTransitTime
        
        
    def TransitUpdate(self, inUpdatedTransitSystem, inUpdatedTransitLine, inUpdatedTransitStop):
        print ("Transit update received for transit display")
        self.UpdateTransitInfo()

class TransitDisplayScreenWidget(AccordionItem):
    #mNextTransitList = NumericProperty(0)
    mTransitTitle = StringProperty()
    mTransitDirection = StringProperty()
    mNextTransitList = ListProperty([])
    
    def __init__(self, **kwargs):
        super(TransitDisplayScreenWidget, self).__init__(**kwargs)
        
class TransitDisplayWidgetApp(App):
    def build(self):
        return TransitDisplayWidget()

if __name__ in ('__main__', '__android__'):
    TransitDisplayWidgetApp().run()