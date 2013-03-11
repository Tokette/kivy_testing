'''
Sean Duane
Route.py
Created on Feb 13, 2013
'''

class Route():
    _Stops = []

    '''
    inStops : List<TransitStop>
    '''
    def __init__(self, inStops):
        self._Stops = inStops