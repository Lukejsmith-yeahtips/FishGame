# fish_bait_interaction.py
import math

def calculate_distance(fish, bait):
    # Calculate the distance between fish and bait
    distance = math.sqrt((fish.x - bait.x) ** 2 + (fish.y - bait.y) ** 2)
    return distance

def attract_fish(fish, bait):
    # Adjust fish's swimming pattern to simulate attraction towards the bait
    distance = calculate_distance(fish, bait)
    if distance <= fish.size * 2:
        fish.direction = math.atan2(bait.y - fish.y, bait.x - fish.x)
        fish.speed = random.uniform(*FISH_SPEED_RANGE)
