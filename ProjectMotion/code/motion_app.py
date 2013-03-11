'''
Created on Mar 10, 2013

@author: MintyAnt
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from code import engine

# MotionApp kicks off the engine, who handles the duties from here on out.
class MotionApp(App):
    _Engine = None

    def build(self):
        screenManager = ScreenManager()

        self._Engine = engine.GetInstance()
        self._Engine.Initialize(screenManager)
        Clock.schedule_interval(self._Engine.Update, 1.0/30.0)
        return screenManager