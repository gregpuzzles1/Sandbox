import pygame
import random
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Canvas size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flower Generator")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

def random_color():
    return random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

def draw_flower1(surface, x, y, size):
    petals = random.randint(5, 8)
    radius = size
    color = random_color()
    for i in range(petals):
        angle = (2 * math.pi / petals) * i
        petal_x = x + math.cos(angle) * radius
        petal_y = y + math.sin(angle) * radius
        pygame.draw.ellipse(surface, color, (petal_x - size//4, petal_y - size//2, size//2, size))
    pygame.draw.circle(surface, (255, 255, 0), (x, y), size // 3)

def draw_flower2(surface, x, y, size):
    spikes = random.randint(6, 10)
    color = random_color()
    for i in range(spikes):
        angle = (2 * math.pi / spikes) * i
        end_x = x + math.cos(angle) * size
        end_y = y + math.sin(angle) * size
        pygame.draw.line(surface, color, (x, y), (end_x, end_y), 2)
    pygame.draw.circle(surface, (0, 0, 0), (x, y), size // 4)

def generate_flower(surface):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    size = random.randint(10, 30)
    flower_type = random.choice([draw_flower1, draw_flower2])
    flower_type(surface, x, y, size)

# Main loop
running = True
max_flowers = 300

try:
    while running:
        screen.fill(WHITE)
        flower_count = 0

        while flower_count < max_flowers:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            generate_flower(screen)
            flower_count += 1

            pygame.display.flip()
            clock.tick(60)

        # Wait before clearing screen and restarting
        pygame.time.wait(2000)  # 2 seconds pause before refreshing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

except Exception as e:
    print("An error occurred:", e)
    pygame.image.save(screen, "flower_garden_error_output.png")

finally:
    print("Cleaning up and quitting.")
    pygame.quit()
    sys.exit()
