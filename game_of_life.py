import pygame
import numpy as np
import random

WIDHT = 1600
HEIGHT = 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 14, 71)


class Grid:
    def __init__(self, width, height, scale, offset) -> None:
        self.scale = scale
        self.columns = height//scale
        self.rows = width//scale
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)
        self.offset = offset

    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)

    def draw(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale

                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [
                                     x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [
                                     x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

    def Conway(self):
        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neightbors = self.get_neighbors(x, y)
                if state == 0 and neightbors == 3:
                    next[x][y] = 1
                elif state == 1 and (neightbors < 2 or neightbors > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next

    def get_neighbors(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

# pos, WIDHT, HEIGHT, scaler, offset


def get_mouse_pos(pos, scale):

    y, x = pos

    row = y // scale
    col = x // scale
    return row, col


def main():
    pygame.init()
    pygame.display.set_caption('Game of life')
    screen = pygame.display.set_mode((WIDHT, HEIGHT))
    clock = pygame.time.Clock()
    fps = 60
    scaler = 20
    start = False
    offset = 1
    grid = Grid(WIDHT, HEIGHT, scaler, offset)
    grid.random2d_array()
    run = True
    while run:
        clock.tick(fps)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # left
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, scaler)
                grid.grid_array[row][col] = 1

            elif pygame.mouse.get_pressed()[2]:  # right
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, scaler)
                grid.grid_array[row][col] = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start
                if event.key == pygame.K_r and not start:
                    grid.random2d_array()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_c and not start:
                    for i in range(grid.rows):
                        for j in range(grid.columns):
                            grid.grid_array[i][j] = 0
        if start:
            grid.Conway()
        grid.draw(off_color=WHITE, on_color=BLUE, surface=screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
