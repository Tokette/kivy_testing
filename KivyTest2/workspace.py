'''
Created on Mar 10, 2013

@author: Greg
'''

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
from syncproject import SyncProject

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
class WorkspaceDialog(FloatLayout):
    show_load_dialog = ObjectProperty(None)
    show_new_dialog = ObjectProperty(None)

class Workspace(Widget):
    
    _popup = None
    
    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.show_init_dialog()
        
    def show_init_dialog(self):
        if self._popup is not None:
            self._popup.dismiss()
            
        content = WorkspaceDialog(show_load_dialog=self.show_load, show_new_dialog=self.show_new)
        self._popup = Popup(title="Open A Workspace", content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self._popup.open()
    
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        if self._popup is not None:
            self._popup.dismiss()
            
        content = LoadDialog(load=self.load, cancel=self.show_init_dialog)
        self._popup = Popup(title="Open An Existing Workspace", content=content, size_hint=(0.9, 0.9), auto_dismiss=False)
        self._popup.open()
        
    def show_new(self):
        if self._popup is not None:
            self._popup.dismiss()
            
        content = SaveDialog(save=self.create, cancel=self.show_init_dialog)
        self._popup = Popup(title="Create A New Workspace", content=content, size_hint=(0.9, 0.9), auto_dismiss=False)
        self._popup.open()
        
    def load(self, path, filenames):
        '''
        if len(filenames) > 0:
            filename = os.path.join(str(path), str(filenames[0]))
            print "Load %s" % filename
            SyncProject.load(filename) 
        '''
        self._popup.dismiss()
            
        
    def create(self, path, filename):
        print "Create %s" % os.path.join(str(path), str(filename))