from bar import Bar
class HealthBar(Bar):
    def __init__(self, width, height):
        super().__init__(width, height, 100, (0, 255, 255))

    def decrease_health(self, amount):
        self.current_value -= amount
        if self.current_value < 0:
            self.current_value = 0

    def increase_health(self, amount):
        self.current_value += amount
        if self.current_value > self.max_value:
            self.current_value = self.max_value

    def get_percentage(self):
        return self.current_value / self.max_value * 100
