'''
Sean Duane
Favorite.py
Created on Feb 13, 2013
'''

class FavoriteTypeEnum:
    '''
    Route - A collection of transit systems and stops
    Transit - An entire system, like "Subway"
    TransitSystem - A specific, like "Subway Red Line"
    Stop - A specific stop.
    '''
    Undefined, Route, Transit, TransitSystem, Stop = range(5)
    
class Favorite():
    _Routes = []
    _FavoriteType = FavoriteTypeEnum.Undefined

    '''
    inRoutes : List<Route>
    inFavoriteType : FavoriteTypeEnum
    '''
    def __init__(self, inRoutes, inFavoriteType):
        self._Routes = inRoutes
        self._FavoriteType = inFavoriteType