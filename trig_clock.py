import sys
import pygame
import time
import math

# Set up constants
BRIGHTBLUE = (0, 50, 255)
WHITE = (255, 255, 255)
DARKRED = (128, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

HOUR_HAND_COLOR = DARKRED
MINUTE_HAND_COLOR = RED
SECOND_HAND_COLOR = YELLOW
NUMBER_BOX_COLOR = BRIGHTBLUE
BACKGROUND_COLOR = WHITE

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2

CLOCK_NUM_SIZE = 40
CLOCK_RADIUS = 200
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Trig Clock')
font = pygame.font.Font(pygame.font.get_default_font(), 26)
clock = pygame.time.Clock()

# Pre-render clock numbers
clock_numbers = [font.render(f'{i}', True, BACKGROUND_COLOR, NUMBER_BOX_COLOR)
                 for i in [12] + list(range(1, 12))]


def get_tick_position(tick, stretch=1.0, origin_x=CENTER_X, origin_y=CENTER_Y):
    """Return the x, y position on the circle for a given tick (0-59)."""
    tick %= 60
    angle = 2 * math.pi * (tick / 60.0)
    x = math.sin(angle) * stretch + origin_x
    y = -math.cos(angle) * stretch + origin_y  # Pygame y-axis goes down
    return x, y


def draw_clock_face():
    """Draw the clock face numbers and boxes."""
    for i, num_surf in enumerate(clock_numbers):
        tick = i * 5
        center = get_tick_position(tick, CLOCK_RADIUS)

        num_rect = num_surf.get_rect(center=center)
        box_rect = pygame.Rect(0, 0, CLOCK_NUM_SIZE, CLOCK_NUM_SIZE)
        box_rect.center = center

        pygame.draw.rect(screen, NUMBER_BOX_COLOR, box_rect)
        screen.blit(num_surf, num_rect)


def draw_hand(tick_value, stretch, color, width):
    """Draw a clock hand."""
    end_x, end_y = get_tick_position(tick_value, stretch)
    pygame.draw.line(screen, color, (CENTER_X, CENTER_Y), (end_x, end_y), width)


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    draw_clock_face()

    now = time.localtime()
    now_hour = now.tm_hour % 12
    now_minute = now.tm_min
    now_second = now.tm_sec + time.time() % 1  # Smooth second hand

    # Calculate positions
    hour_tick = now_hour * 5 + (now_minute * 5 / 60.0)
    minute_tick = now_minute + (now_second / 60.0)
    second_tick = now_second

    # Draw hands
    draw_hand(hour_tick, CLOCK_RADIUS * 0.6, HOUR_HAND_COLOR, 8)
    draw_hand(minute_tick, CLOCK_RADIUS * 0.8, MINUTE_HAND_COLOR, 6)
    draw_hand(second_tick, CLOCK_RADIUS * 0.8, SECOND_HAND_COLOR, 2)
    draw_hand(second_tick, -CLOCK_RADIUS * 0.2, SECOND_HAND_COLOR, 2)  # Tail of the second hand

    pygame.display.flip()
    clock.tick(FPS)
