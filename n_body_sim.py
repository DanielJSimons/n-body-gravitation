import pygame
import itertools
import random
from n_body_sim.body import Body

pygame.init()
WINDOW_SIZE = (1000, 1000)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
CLOCK = pygame.time.Clock()

BACKGROUND = pygame.Surface(WINDOW_SIZE)
BACKGROUND.fill("Black")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(500, 500))

G = 1  # adjustable parameter

body_group = pygame.sprite.Group()
BODYCOUNT = 20

for i in range(BODYCOUNT):
    if i == 1:
        body_group.add(Body(80,34, (400, 400), "White", -0.15, 0.1))
        body_group.add(Body(40, 20, (600,600), "Yellow", 0.15, -0.1))
        body_group.add(Body(8, 6, (500,500), "Red", 0.3, -0.15))
    """ 
    if i == 1:
        body_group.add(Body(40, 20, (500, 700), "Yellow", 0.02, 0.02))
        body_group.add(Body(80,34, (500, 300), "White", 0.02, 0.02))
        body_group.add(Body(8, 6, (400, 400), "Red", 0.02, 0.02))
    """  
    """
    else:
        if i %2 ==0:
            body_group.add(Body(1, 6, (random.randrange(150, 850), random.randrange(150, 850)), "Royal Blue", 0, 0))
        if i %2 !=0:
            body_group.add(Body(2, 8, (random.randrange(150, 850), random.randrange(150, 850)), "Forest Green", 0, 0))
    """
# Create a surface for drawing the tracks
track_surface = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)

# Set the initial time and duration for the timer
start_time = pygame.time.get_ticks()
timer_duration = 5000  # 5 seconds

pygame.font.init()  # Initialize the font module
timer_font = pygame.font.Font(None, 48)  # Define the font and size for the timer text

# Define the rectangle parameters
rect_pos = (20, 10)  # Position of the top-left corner of the rectangle
rect_size = (400, 60)  # Width and height of the rectangle
rect_color = pygame.Color("White")  # Color of the rectangle
rect_thickness = 2  # Thickness of the rectangle outline

max_track_points = 800  # Maximum number of track points per body

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    WINDOW.blit(BACKGROUND, BACKGROUND_RECT)

    body_group.draw(WINDOW)

    for body, otherbody in itertools.combinations(body_group, 2):
        body.gravitate(otherbody)
        otherbody.gravitate(body)
        body.animate()
        otherbody.animate()

        # Append current position to track points
        body.track_points.append((round(body.x_pos), round(body.y_pos)))

        # Limit the number of track points
        if len(body.track_points) > max_track_points:
            body.track_points = body.track_points[-max_track_points:]

        # Append current position to track points
        otherbody.track_points.append((round(otherbody.x_pos), round(otherbody.y_pos)))

        # Limit the number of track points
        if len(otherbody.track_points) > max_track_points:
            otherbody.track_points = otherbody.track_points[-max_track_points:]

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Draw track lines on the track surface
    track_surface.fill((0, 0, 0, 0))  # Clear the track surface with a transparent color
    for body in body_group:
        # Get the RGB values of the body color
        r, g, b, _ = pygame.Color(body.image.get_at((body.radius, body.radius)))

        # Decrease the alpha value for each track point
        for i in range(len(body.track_points)):
            alpha = 0 + int(255 * (i / len(body.track_points)))

            # Create a new color with the adjusted alpha value
            track_color = (r, g, b, alpha)

            pygame.draw.circle(track_surface, track_color, body.track_points[i], 1)

    timer_text = timer_font.render(f"Time Elapsed (s): {elapsed_time / 1000:.2f}", True, pygame.Color("white"))
    WINDOW.blit(timer_text, (35, 25))

    pygame.draw.rect(WINDOW, rect_color, (*rect_pos, *rect_size), rect_thickness)
    
    WINDOW.blit(track_surface, (0, 0))  # Blit the track surface onto the window

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
