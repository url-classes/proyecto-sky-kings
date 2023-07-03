from CharacterStates.CharacterState import CharacterState
from CharacterDecorator.Character import Character


class StateNeutral(CharacterState):
    def __init__(self, character: Character):
        self.character = character

    def set_character(self, character: Character):
        self.character = character

    def get_actual_frame(self):
        return self.character.frames[0][self.character.pose.current_pose]
