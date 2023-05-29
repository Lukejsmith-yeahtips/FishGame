# fish_animation.py
import math

def calculate_body_movement(fish):
    # Calculate the fish's body movement based on speed and direction
    body_movement = math.sin(fish.direction) * fish.speed
    return body_movement

def calculate_fin_motion(fish):
    # Calculate the fin motion based on fish size and speed
    fin_motion = fish.size * fish.speed * 0.1
    return fin_motion

def calculate_tail_movement(fish):
    # Calculate the tail movement based on fish speed
    tail_movement = fish.speed * 0.2
    return tail_movement
