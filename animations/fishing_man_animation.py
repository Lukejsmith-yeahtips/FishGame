import time

class FishingManAnimation:
    def __init__(self):
        self.frames = [
            """
             ,-.
           O /   `.
             <\\/      `.
              |*        `.
             / \\          `.
            /  /            `>')3s,
             --------.                 ,'
            """,
            """
               ,
                 ,-.
               O /   `.
                 <\\/      `.
                  |*        `.
                 / \\          `.
                /  /            `>')3s,
                 --------.                 ,
                  /                  7
            """,
            """
               ,
                 ,-.
               O /   `.
                 <\\/      `.
                  |*        `.
                 / \\          `.
                /  /            `>')3s,
                 --------.                 ,
                  /                  7
            """,
            """
               ,
                 ,-.
               O /   `.
                 <\\/      `.
                  |*        `.
                 / \\          `.
                /  /            `>')3s,
                 --------.                 ,
                  /                  7
            """,
            """
               ,
                 ,-.
               O /   `.
                 <\\/      `.
                  |*        `.
                 / \\          `.
                /  /            `>')3s,
                 --------.                 ,
                  /                  7
            """
        ]
        self.current_frame = 0

    def animate(self):
        print(self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)

    def update(self):
        if self.is_casting:
            self.animate()
            time.sleep(0.5)  # You may need to adjust this depending on your game's frame rate
