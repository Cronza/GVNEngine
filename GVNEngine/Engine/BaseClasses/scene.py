from Engine.Utilities.yaml_reader import Reader
from Engine.BaseClasses.renderable_sprite import SpriteRenderable
from Engine.BaseClasses.renderable_group import RenderableGroup
from Engine.Actions.action_manager import ActionManager

class Scene:
    def __init__(self, scene_data_file, window, pygame_lib, settings, scene_manager):

        self.window = window
        self.pygame_lib = pygame_lib
        self.settings = settings
        self.scene_manager = scene_manager

        # Create a sprite group to store all renderables objects in the scene
        self.renderables_group = RenderableGroup()

        # Initialize an action manager for any reusable actions performed in any subclassed scene
        self.a_manager = ActionManager(self, settings)

        # Read in the active scene data
        self.scene_data = Reader.ReadAll(scene_data_file)

        self.LoadSceneData()

    def Update(self, input_events):
        self.renderables_group.Update()

    def Draw(self, base_screen_size, new_screen_size):
        print("*** REDRAWING SCENE ***")

        # Get a sprite scale multiplier in case the screen resolution has changed
        multiplier = self.CalculateScreenSizeMultiplier(base_screen_size, new_screen_size)

        # Sort the renderable elements by their z-order (Lowest to Highest)
        renderables = sorted(self.renderables_group.renderables.values(), key=lambda renderable: renderable.z_order)

        # Draw any renderables using the screen space multiplier to fit the new resolution
        for sprite in renderables:

            # TODO: Figure out a way to cache the rescale upon initial screen update so we don't recalculate every draw
            # Calculate the new sprite size and position based on the screen size multiplier
            new_size = self.CalculateSpriteSize(sprite.surface, multiplier)
            new_position = self.ConvertNormToScreen(tuple(sprite.position))

            # Allow the user to specify center coordinates, then convert them to the top-left coordinates
            # used by the renderer
            if sprite.center_align:
                new_position = self.GetCenterOffset(new_position, new_size)

            # The rect and surface are independent of eachother's location and position, so update the rect to match
            # the surface location and position
            sprite.UpdateRect(new_position)
            sprite.rect.w = new_size[0]
            sprite.rect.h = new_size[1]

            # Blit the renderable, upscaling or downscaling to the new size
            self.window.blit(self.pygame_lib.transform.smoothscale(sprite.surface, new_size), new_position)

    def SwitchScene(self, scene_file, scene_type):
        self.renderables_group.Clear()
        self.a_manager = None

        self.scene_manager.LoadScene(scene_file, scene_type)

    def LoadSceneData(self):
        """
        Read the scene yaml file, and prepare the scene by spawning object classes, storing scene values, etc. We
        can also use aliases in order to make specific action calls
        """
        # TODO: Create an aliases file so users can write their own

        # 'background' alias for loading the background sprite
        if 'background' in self.scene_data:
            bg_path = self.scene_data['background']
            print(f"Background specified -  Loading: {bg_path}")

            action_data = {
                'action': 'load_background',
                'sprite': bg_path
            }

        self.a_manager.PerformAction(action_data)

    def CalculateScreenSizeMultiplier(self, old_resolution, new_resolution):
        """
        Based on a source and target resolution,
        return a tuple of multipliers for the difference (Width & height)
        """
        final_resolution = []

        # Determine if the new resolution height is smaller or larger
        if old_resolution[0] < new_resolution[0]:
            final_resolution.append(new_resolution[0] / old_resolution[0])
        else:
            final_resolution.append(old_resolution[0] / new_resolution[0])

        if old_resolution[1] < new_resolution[1]:
            final_resolution.append(new_resolution[1] / old_resolution[1])
        else:
            final_resolution.append(old_resolution[1] / new_resolution[1])

        return tuple(final_resolution)

    def CalculateSpriteSize(self, sprite_surface, screen_multiplier):
        """ Based on a given surface and multiplier for the current resolution, return the resulting size tuple"""
        width = sprite_surface.get_width()
        height = sprite_surface.get_height()

        # Round each value as blitting doesn't support floats
        return tuple(
            [
                round(width * screen_multiplier[0]),
                round(height * screen_multiplier[1])
            ]
        )

    def ConvertNormToScreen(self, norm_value):
        """ Take the normalized object pos and convert it to relative screen space coordinates """
        screen_size = self.pygame_lib.display.get_surface().get_size()

        return (
            norm_value[0] * screen_size[0],
            norm_value[1] * screen_size[1]
        )

    def GetCenterOffset(self, pos, size):
        """
        Given size and position tuples representing the center point of a sprite,
        return the offset position for the top-left corner
        """
        return (
            round(pos[0] - size[0] / 2),
            round(pos[1] - size[1] / 2)
        )
