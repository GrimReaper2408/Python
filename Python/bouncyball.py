import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Spinning Hexagon")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Physics constants
GRAVITY = 1.2
FRICTION = 0.99
BALL_RADIUS = 25
HEXAGON_RADIUS = 350
ROTATION_SPEED = 1.0

# Ball properties
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [5, -10]  # Initial velocity

# Hexagon properties
hexagon_angle = 0  # Current rotation angle

def rotate_point(point, angle, center):
    """Rotate a point around a center by a given angle."""
    x, y = point
    cx, cy = center
    dx = x - cx
    dy = y - cy
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_new = dx * cos_theta - dy * sin_theta + cx
    y_new = dx * sin_theta + dy * cos_theta + cy
    return (x_new, y_new)

def get_hexagon_points(center, radius, angle):
    """Get the vertices of a hexagon centered at `center` with a given radius and rotation angle."""
    points = []
    for i in range(6):
        theta = math.radians(60 * i) + angle
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)
        points.append((x, y))
    return points

def point_line_distance(point, line_start, line_end):
    """Calculate the distance between a point and a line segment."""
    px, py = point
    x1, y1 = line_start
    x2, y2 = line_end
    dx, dy = x2 - x1, y2 - y1
    segment_length_squared = dx * dx + dy * dy
    if segment_length_squared == 0:
        return math.hypot(px - x1, py - y1)
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / segment_length_squared))
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy
    return math.hypot(px - closest_x, py - closest_y)

def reflect_ball(ball_pos, ball_vel, line_start, line_end):
    """Reflect the ball's velocity off a line segment."""
    x1, y1 = line_start
    x2, y2 = line_end
    dx, dy = x2 - x1, y2 - y1
    normal = (-dy, dx)
    normal_length = math.hypot(normal[0], normal[1])
    normal = (normal[0] / normal_length, normal[1] / normal_length)
    dot = ball_vel[0] * normal[0] + ball_vel[1] * normal[1]
    ball_vel[0] -= 2 * dot * normal[0]
    ball_vel[1] -= 2 * dot * normal[1]

def update_ball(ball_pos, ball_vel, hexagon_points):
    """Update the ball's position and velocity, handling collisions with the hexagon."""
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    ball_vel[1] += GRAVITY  # Apply gravity
    ball_vel[0] *= FRICTION  # Apply friction
    ball_vel[1] *= FRICTION

    # Check for collisions with hexagon walls
    for i in range(6):
        start = hexagon_points[i]
        end = hexagon_points[(i + 1) % 6]
        distance = point_line_distance(ball_pos, start, end)
        if distance <= BALL_RADIUS:
            reflect_ball(ball_pos, ball_vel, start, end)
            # Move the ball out of the wall to prevent sticking
            dx = end[0] - start[0]
            dy = end[1] - start[1]
            normal = (-dy, dx)
            normal_length = math.hypot(normal[0], normal[1])
            normal = (normal[0] / normal_length, normal[1] / normal_length)
            ball_pos[0] += normal[0] * (BALL_RADIUS - distance)
            ball_pos[1] += normal[1] * (BALL_RADIUS - distance)

def draw_hexagon(screen, points):
    """Draw the hexagon on the screen."""
    pygame.draw.polygon(screen, BLACK, points, 2)

def draw_ball(screen, pos):
    """Draw the ball on the screen."""
    pygame.draw.circle(screen, RED, (int(pos[0]), int(pos[1])), BALL_RADIUS)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update hexagon rotation
    hexagon_angle += ROTATION_SPEED
    hexagon_points = get_hexagon_points((WIDTH // 2, HEIGHT // 2), HEXAGON_RADIUS, hexagon_angle)

    # Update ball position and velocity
    update_ball(ball_pos, ball_vel, hexagon_points)

    # Draw everything
    screen.fill(WHITE)
    draw_hexagon(screen, hexagon_points)
    draw_ball(screen, ball_pos)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()  # Ensure the program exits cleanly in IDLE