class ScrollMap:
    def __init__(self):
        self.Scroll = 0
        self.max = 960

    def update_scroll(self, add_y: int):
        if self.Scroll <= self.max:
            self.Scroll = add_y

    def get_scroll(self):
        return self.Scroll
