from CharacterStates.CharacterPose import CharacterPose
from CharacterDecorator.Character import Character


class PoseStatic(CharacterPose):
    def __init__(self, character: Character, previous_pose: int = 0, current_pose: int = 0, delay: int = 5):
        self.character = character
        self.previous_pose = previous_pose
        self.current_pose = current_pose
        self.delay = delay

    def set_character(self, character: Character, prev_pose: int, curr_pose: int, delay: int = 5):
        self.character = character
        self.previous_pose = prev_pose
        self.current_pose = curr_pose
        self.delay = delay

    def move1(self, movement: list[int, int] | None = None):
        if movement is None:
            movement = [0, 0]
        if movement == [0, 0]:
            if self.current_pose == 0:
                self.current_pose = 1
                self.previous_pose = 0
            else:
                self.current_pose = 0
                self.previous_pose = 1

    def move(self):
        if self.delay <= 0:
            if self.current_pose == 0:
                self.current_pose = 1
                self.previous_pose = 0
            else:
                self.current_pose = 0
                self.previous_pose = 1

            self.delay = 5

        else:
            self.delay -= 1
