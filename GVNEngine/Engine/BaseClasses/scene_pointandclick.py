from Engine.BaseClasses.scene import Scene
from Engine.BaseClasses.interactable import Interactable

class PointAndClickScene(Scene):
    def __init__(self, scene_data_file, window, pygame_lib, settings, scene_manager):

        super().__init__(scene_data_file, window, pygame_lib, settings, scene_manager)

    def Draw(self, base_screen_size, new_screen_size):

        # Draw both generics and interactive specifics using the parent's method
        super().Draw(base_screen_size, new_screen_size)

    def LoadSceneData(self):
        super().LoadSceneData()

        # Load any specified objects (Non-interactables)
        if 'objects' in self.scene_data:
            f_objects = self.scene_data['objects']

            for f_object in f_objects:
                f_object['action'] = 'load_sprite'
                self.a_manager.PerformAction(f_object)
        else:
            print('Scene file does not specify any objects')

        # Load any specified interactables
        if 'interactables' in self.scene_data:
            f_interactables = self.scene_data['interactables']

            for f_interactable in f_interactables:
                f_interactable['action'] = 'create_interactable'
                self.a_manager.PerformAction(f_interactable)
        else:
            print('Scene file does not specify any objects')
