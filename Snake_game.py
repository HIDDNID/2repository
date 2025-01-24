import pygame
import sys
import random

# Настройки окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def change_direction(self, direction):
        if direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        elif direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        elif direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_position):
        if self.direction == "RIGHT":
            self.position[0] += CELL_SIZE
        elif self.direction == "LEFT":
            self.position[0] -= CELL_SIZE
        elif self.direction == "UP":
            self.position[1] -= CELL_SIZE
        elif self.direction == "DOWN":
            self.position[1] += CELL_SIZE

        self.body.insert(0, list(self.position))

        if abs(self.position[0] - food_position[0]) <= CELL_SIZE and abs(
                self.position[1] - food_position[1]) <= CELL_SIZE:
            return True
        else:
            self.body.pop()
            return False

    def draw(self, surface):
        for pos in self.body:
            pygame.draw.rect(surface, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        # Проверяем столкновение со стенами
        if self.position[0] > WINDOW_WIDTH or self.position[0] < 0:
            return True
        if self.position[1] > WINDOW_HEIGHT or self.position[1] < 0:
            return True

        # Проверяем столкновение с собственным телом
        for block in self.body[1:]:
            if self.position == block:
                return True

        return False


class Food:
    def __init__(self):
        self.position = [0, 0]
        self.randomize_position()

    def randomize_position(self):
        self.position[0] = int(CELL_SIZE * round(random.randrange(0, WINDOW_WIDTH // CELL_SIZE)))
        self.position[1] = int(CELL_SIZE * round(random.randrange(0, WINDOW_HEIGHT // CELL_SIZE)))

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")

        surface.fill(BLACK)

        if snake.move(food.position):
            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)

        if snake.check_collision():
            pygame.quit()
            sys.exit()

        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()