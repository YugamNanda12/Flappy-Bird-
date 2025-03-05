import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3
BIRD_X = 50

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 250)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load Bird Image
bird_img = pygame.image.load("bird.png")  # Ensure you have a bird image or replace it
bird_img = pygame.transform.scale(bird_img, (40, 30))  # Resize

# Bird Properties
bird_y = HEIGHT // 2
bird_velocity = 0

# Pipes
pipes = []
pipe_heights = [random.randint(150, 400) for _ in range(3)]
for i in range(3):
    pipes.append([WIDTH + i * 200, pipe_heights[i]])

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLUE)  # Background color
    pygame.time.delay(30)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGTH

    # Bird Movement
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Pipe Movement
    for pipe in pipes:
        pipe[0] -= PIPE_SPEED
        if pipe[0] < -PIPE_WIDTH:
            pipe[0] = WIDTH
            pipe[1] = random.randint(150, 400)
            score += 1  # Increment score when pipe resets

    # Collision Detection
    for pipe in pipes:
        if (BIRD_X + 40 > pipe[0] and BIRD_X < pipe[0] + PIPE_WIDTH):
            if bird_y < pipe[1] or bird_y + 30 > pipe[1] + PIPE_GAP:
                running = False  # Game Over

    if bird_y >= HEIGHT - 30 or bird_y <= 0:
        running = False  # Game Over if bird hits ground or top

    # Draw Bird
    screen.blit(bird_img, (BIRD_X, bird_y))

    # Draw Pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))  # Top Pipe
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP))  # Bottom Pipe

    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)  # Maintain FPS

pygame.quit()
