# bait_animation.py
import math

def generate_bait_motion(elapsed_time):
    # Generate motion pattern for the bait based on elapsed time
    amplitude = 20
    frequency = 0.01
    motion = amplitude * math.sin(elapsed_time * frequency)
    return motion
