'''
Created on Feb 26, 2013

@author: MintyAnt
'''

class FavoritesSystem():
    _CurrentFavorite = None
    _Favorites = []

    '''
    Constructor
    '''
    def __init__(self):
        pass
    
    def Startup(self):
        # Jumpstart to a system if one is loaded up.
        if (self._CurrentFavorite != None):
            self.LoadCurrentFavorite()
        
    '''
    inNewFavorite : Favorite
    '''
    def SetCurrentFavorite(self, inNewFavorite):
        assert inNewFavorite in self._Favorites, "%r is not in %r" % (inNewFavorite, self._Favorites)
        __CurrentFavorite = inNewFavorite
        
    '''
    inNewFavorite : Favorite
    '''
    def AddFavorite(self, inNewFavorite):
        assert inNewFavorite in self._Favorites, "%r already in %r" % (inNewFavorite, self._Favorites)
        if (inNewFavorite not in self._Favorites):
            self._Favorites.append(inNewFavorite)
    
    '''
    inFavoriteToRemove : Favorite
    '''
    def RemoveFavorite(self, inFavoriteToRemove):
        if (inFavoriteToRemove in self._Favorites):
            self._Favorites.remove(inFavoriteToRemove)
            
    def LoadCurrentFavorite(self):
        assert self._CurrentFavorite == None
        self.LoadFavorite(self._CurrentFavorite)
        
    def LoadFavorite(self, inFavoriteToLoad):
        pass