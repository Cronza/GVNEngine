import pygame
from pygame.locals import VIDEORESIZE
from Engine.Core.scene_manager import SceneManager
from Engine.Utilities.settings import Settings

class GVNEngine():
    def __init__(self):
        # Build a settings object to house engine & project settings
        self.settings = Settings()
        self.settings.EvaluateProjectSettings("Config/Game.yaml")

        # Configure the game based on project settings
        pygame.display.set_caption(self.settings.projectSettings['Game']['title'])

        # Declare the scene manager, but we'll initialize it during the game loop
        self.scene_manager = None

        # DEBUG TRIGGERS
        self.show_fps = False

    def Main(self):

        pygame.init()

        # Initialize the game window and clock
        window = pygame.display.set_mode(self.settings.active_resolution)
        clock = pygame.time.Clock()

        # Initialize the scene manager
        self.scene_manager = SceneManager(window, pygame, self.settings)

        # Start the game loop
        is_running = True
        while is_running is True:
            input_events = pygame.event.get()

            # Handle all system actions
            for event in input_events:
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    # Maximize
                    if event.key == pygame.K_1:
                        self.UpdateResolution(1, pygame.FULLSCREEN)
                        self.scene_manager.ResizeScene()
                    # Minimize
                    if event.key == pygame.K_2:
                        self.UpdateResolution(0)
                        self.scene_manager.ResizeScene()
                    # Exit
                    if event.key == pygame.K_ESCAPE:
                        is_running = False
                    if event.type == pygame.QUIT:
                        is_running = False
                    # Debug - FPS
                    if event.key == pygame.K_F3:
                        self.show_fps = not self.show_fps

            # Update scene logic. This drives the core game functionality
            self.scene_manager.active_scene.Update(input_events)

            # Debug Logging
            if self.show_fps:
                print(clock.get_fps())

            # Refresh any changes
            pygame.display.update()

            # Get the time in miliseconds converted to seconds since the last frame. Used to avoid frame dependency
            # on actions
            self.scene_manager.active_scene.delta_time = clock.tick(60) / 1000

    def UpdateResolution(self, new_size_index, flag=0):
        # Use the given, but always add HWSURFACE and DOUBLEBUF
        if not self.settings.resolution == new_size_index:
            self.settings.resolution = new_size_index
            pygame.display.set_mode(self.settings.resolution_options[new_size_index], flag)

            self.scene_manager.active_scene.Draw()


if __name__ == "__main__":
    engine = GVNEngine()
    engine.Main()
