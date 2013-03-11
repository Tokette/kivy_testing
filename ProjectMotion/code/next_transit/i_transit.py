'''
Created on Feb 13, 2013

@author: MintyAnt
'''
class ITransit():
    def TransitUpdate(self, inUpdatedTransitStop, inUpdatedTransitLine, inUpdatedTransitSystem):
        raise NotImplementedError("You must define this function.")