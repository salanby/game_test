# core/state_manager.py

class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def switch_state(self, name):
        if name in self.states:
            self.current_state = self.states[name]

    def update(self, keys):
        if self.current_state:
            self.current_state.update(keys)

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
