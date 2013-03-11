'''
Created on Mar 9, 2013

@author: Greg
'''

from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Timeline(Widget):
    
    def __init__(self, **kwargs):
        super(Timeline, self).__init__(**kwargs)
        
        popup = Popup(title='Test popup', content=Label(text='Hello world'),
              auto_dismiss=False)
        popup.open()
        
        
        