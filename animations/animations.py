import random
import time
import os

class FishingManAnimation:
    def __init__(self):
        self.frames = [
            """
             ,-.
           O / .
             <\\/ .
             |* .
             / \\ .
             / / '>)3s,
             --------. ,'
            """
        ]

class FishAnimation:
    def __init__(self):
        self.frames = [
            """
              ><(((('>
            """,
            """
              ><(((('>
            """
        ]

def animate_fishing_man_fish():
    fishing_man_frames = FishingManAnimation().frames

    fish_frames = FishAnimation().frames

    columns, lines = os.get_terminal_size()
    fishing_man_width = len(max(fishing_man_frames[0].split('\n'), key=len))
    fishing_man_height = len(fishing_man_frames[0].split('\n'))
    fish_width = len(max(fish_frames[0].split('\n'), key=len))
    fish_height = len(fish_frames[0].split('\n'))

    if columns < max(fishing_man_width, fish_width) or lines < max(fishing_man_height, fish_height):
        print("Your terminal window is too small for this animation. Please increase its size.")
        return

    fishing_man_position = [random.randint(0, columns-fishing_man_width), random.randint(0, lines-fishing_man_height)]
    fish_position = [random.randint(0, columns-fish_width), random.randint(0, lines-fish_height)]

    while True:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Ensure the fishing man and fish are always within the terminal window
        fishing_man_position[0] = min(max(fishing_man_position[0], 0), columns-fishing_man_width)
        fishing_man_position[1] = min(max(fishing_man_position[1], 0), lines-fishing_man_height)
        fish_position[0] = min(max(fish_position[0], 0), columns-fish_width)
        fish_position[1] = min(max(fish_position[1], 0), lines-fish_height)

        # Fishing man chases the fish with some random chance to move or not
        if random.random() < 0.75:  # 75% chance to move towards the fish
            if fishing_man_position[0] < fish_position[0]: fishing_man_position[0] += 1
            if fishing_man_position[0] > fish_position[0]: fishing_man_position[0] -= 1
            if fishing_man_position[1] < fish_position[1]: fishing_man_position[1] += 1
            if fishing_man_position[1] > fish_position[1]: fishing_man_position[1] -= 1

        # Fish moves randomly
        fish_position[0] += random.randint(-1, 1)
        fish_position[1] += random.randint(-1, 1)

        # Check if the fishing man caught the fish
        if fishing_man_position == fish_position:
            print("YOU WON!")
            time.sleep(2)
            return True

        # Print the fishing man and fish
        for i, line in enumerate(fishing_man_frames[0].split('\n')):
            print(" " * fishing_man_position[0] + line + " " * (columns-fishing_man_position[0]-fishing_man_width))
            if i < len(fish_frames[0].split('\n')):
                print(" " * fish_position[0] + fish_frames[0].split('\n')[i])

        time.sleep(0.1)
        fish_frames = fish_frames[::-1]
