from kivy.app import App
from workspace import Workspace
    
    
class SyncToolApp(App):
    def build(self):
        return Workspace()
        


if __name__ == '__main__':
    SyncToolApp().run()