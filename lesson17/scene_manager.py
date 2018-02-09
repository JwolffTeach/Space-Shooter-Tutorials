import pygame

""" A class to manage scenes in the game """
class SceneManager():
    
    def __init__(self):
        self.scenes = {}
        self.scene = None
        
    def change_scene(self, scene):
        self.scene = scene
        print(scene)
    
    def add_scene(self, scene_key, scene_value):
        self.scenes[scene_key] = scene_value