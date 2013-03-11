'''
Created on Mar 5, 2013

@author: MintyAnt
'''

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

#Builder.load_file('./user_interface/widgets/OrangeLine.kv')
Builder.load_file('code/user_interface/widgets/OrangeLine.kv')

class OrangeLineWidget(Screen):
    
    def __init__(self, **kwargs):
        super(OrangeLineWidget, self).__init__(**kwargs)
        
        scrollView = ScrollView(size_hint=(1, 1))

        # add custom widget into that layout
        customWidget = OrangeLineGraphicWidget(height=1200, size_hint_y=None)
        #layout.bind(minimum_height=layout.setter('height'))

        scrollView.add_widget(customWidget)
        
        self.add_widget(scrollView)
        
    def Initialize(self, inWidgetArgs):
        pass
        
    def ChangeWidget(self, inWidgetName, inWidgetArgs):
        from code import engine
        engine.gEngineInstance.mUserInterface.ChangeWidget(inWidgetName, inWidgetArgs)
        
    def PreEnter(self):
        pass
    
class OrangeLineGraphicWidget(RelativeLayout):
    def ChangeWidget(self, inWidgetName, inWidgetArgs):
        from code import engine
        engine.gEngineInstance.mUserInterface.ChangeWidget(inWidgetName, inWidgetArgs)