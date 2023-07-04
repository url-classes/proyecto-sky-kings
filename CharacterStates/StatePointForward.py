from CharacterStates.CharacterState import CharacterState
from CharacterDecorator.SpriteCharacter import SpriteCharacter


class StatePointForward(CharacterState):
    def __init__(self, character: SpriteCharacter):
        self.character = character

    def set_character(self, character: SpriteCharacter):
        self.character = character

    def get_actual_frame(self):
        return self.character.frames[1][self.character.pose.current_pose]
