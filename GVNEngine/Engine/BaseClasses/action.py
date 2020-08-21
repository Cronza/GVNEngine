class Action():
    def __init__(self, scene, action_data, a_manager):
        self.scene = scene
        self.action_data = action_data
        self.a_manager = a_manager
        self.active_transition = None
        self.complete = False

    def Start(self):
        pass

    def Update(self):
        pass