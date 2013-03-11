'''
Created on Mar 10, 2013

@author: Greg
'''

from xml.etree.cElementTree import ElementTree

class SyncProject:
    
    __PROJECT_ROOT_NODE_NAME = "project"
    __PROJECT_SETTINGS_NODE_NAME = "settings"
    __PROJECT_TRACKS_NODE_NAME = "tracks"
    __PROJECT_TRACK_NODE_NAME = "track"
    
    @classmethod
    def load(cls, filename):
        project_root = ElementTree().parse(filename)
        settings_node = project_root.find(cls.__PROJECT_SETTINGS_NODE_NAME)
        tracks_node = project_root.find(cls.__PROJECT_TRACKS_NODE_NAME)
        track_nodes = tracks_node.findall(cls.__PROJECT_TRACK_NODE_NAME)
        for node in track_nodes:
            print node
        