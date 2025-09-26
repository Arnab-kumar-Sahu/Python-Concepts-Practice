import pygame
import sys
import random
import json
from pathlib import Path

# ----------------------
# Config
# ----------------------
CELL = 24
GRID_W, GRID_H = 24, 20   # total cells (columns, rows)
PADDING = 32               # outer margin for HUD spacing
WIN_W, WIN_H = GRID_W*CELL + PADDING*2, GRID_H*CELL + PADDING*2
FPS = 60
MOVE_MS_START = 140        # initial move interval (ms)
MOVE_MS_MIN = 700           # fastest speed
SPEEDUP_EVERY = 5          # speed up every X fruits

# Colors
BG1 = (22, 24, 28)
BG2 = (26, 28, 34)
GRID_LINE = (40, 44, 52)
SNAKE_HEAD = (82, 255, 168)
SNAKE_BODY = (0, 181, 124)
FOOD = (255, 108, 108)
TEXT = (230, 235, 245)
SUBTLE = (160, 170, 185)
ACCENT = (136, 192, 208)
WALL = (100, 100, 120)

SAVE_FILE = Path("snake_highscore.json")

# ----------------------
# Helpers
# ----------------------
Vec2 = pygame.math.Vector2

def grid_to_px(c, r):
    return (int(PADDING + c*CELL), int(PADDING + r*CELL), CELL, CELL)


def draw_cell(surface, c, r, color, radius=6):
    pygame.draw.rect(surface, color, grid_to_px(c, r), border_radius=radius)


def load_highscore():
    if SAVE_FILE.exists():
        try:
            data = json.loads(SAVE_FILE.read_text())
            return int(data.get("highscore", 0))
        except Exception:
            return 0
    return 0


def save_highscore(value):
    try:
        SAVE_FILE.write_text(json.dumps({"highscore": int(value)}))
    except Exception:
        pass

# ----------------------
# Game objects
# ----------------------
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        start = Vec2(GRID_W//2, GRID_H//2)
        self.body = [start, start-Vec2(1,0), start-Vec2(2,0)]
        self.dir = Vec2(1,0)
        self.pending = []  # buffered inputs
        self.grow_by = 0

    def head(self):
        return self.body[0]

    def turn(self, d):
        # prevent 180° turns
        if len(self.body) > 1 and self.body[0] + d == self.body[1]:
            return
        # ignore null
        if d.length_squared() == 0:
            return
        # buffer direction (processed per tick)
        self.pending.append(d)

    def step(self):
        # handle buffered turn (only the latest before movement)
        if self.pending:
            self.dir = self.pending[-1]
            self.pending.clear()
        new_head = self.head() + self.dir
        self.body.insert(0, new_head)
        if self.grow_by > 0:
            self.grow_by -= 1
        else:
            self.body.pop()

    def grow(self, n=1):
        self.grow_by += n

    def collided(self):
        h = self.head()
        # wall
        if not (0 <= h.x < GRID_W and 0 <= h.y < GRID_H):
            return True
        # self
        return any(h == seg for seg in self.body[1:])

    def draw(self, surf):
        # body
        for i, seg in enumerate(self.body):
            c = int(seg.x); r = int(seg.y)
            if i == 0:
                draw_cell(surf, c, r, SNAKE_HEAD, radius=8)
            else:
                draw_cell(surf, c, r, SNAKE_BODY, radius=8)


class Food:
    def __init__(self):
        self.pos = Vec2(0,0)
        self.relocate([])

    def relocate(self, forbidden):
        free = [(c, r) for c in range(GRID_W) for r in range(GRID_H)
                if Vec2(c, r) not in forbidden]
        if not free:
            self.pos = Vec2(-1,-1)
            return
        self.pos = Vec2(*random.choice(free))

    def draw(self, surf):
        draw_cell(surf, int(self.pos.x), int(self.pos.y), FOOD, radius=10)


# ----------------------
# Main game
# ----------------------
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake – Pygame Edition")
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Segoe UI", 22)
        self.font_big = pygame.font.SysFont("Segoe UI", 36, bold=True)
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.best = load_highscore()
        self.move_ms = MOVE_MS_START
        self.move_timer = 0
        self.paused = False
        self.game_over = False

    def update(self, dt):
        if self.game_over or self.paused:
            return
        self.move_timer += dt
        if self.move_timer >= self.move_ms:
            self.move_timer = 0
            self.snake.step()
            # eat
            if self.snake.head() == self.food.pos:
                self.score += 1
                self.snake.grow(1)
                self.food.relocate(self.snake.body)
                # speed up
                if self.score % SPEEDUP_EVERY == 0 and self.move_ms > MOVE_MS_MIN:
                    self.move_ms = max(MOVE_MS_MIN, self.move_ms - 5)
            # collisions
            if self.snake.collided():
                self.game_over = True
                if self.score > self.best:
                    self.best = self.score
                    save_highscore(self.best)

    def handle_input(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE,):
                    pygame.quit(); sys.exit()
                if e.key in (pygame.K_p, pygame.K_SPACE):
                    self.paused = not self.paused
                if e.key in (pygame.K_r,) and self.game_over:
                    self.reset()
                # directions
                if e.key in (pygame.K_a, pygame.K_LEFT):
                    self.snake.turn(Vec2(-1,0))
                elif e.key in (pygame.K_d, pygame.K_RIGHT):
                    self.snake.turn(Vec2(1,0))
                elif e.key in (pygame.K_w, pygame.K_UP):
                    self.snake.turn(Vec2(0,-1))
                elif e.key in (pygame.K_s, pygame.K_DOWN):
                    self.snake.turn(Vec2(0,1))

    def draw_grid(self):
        # Checkerboard background inside the padded playfield
        for r in range(GRID_H):
            for c in range(GRID_W):
                color = BG1 if (c + r) % 2 == 0 else BG2
                pygame.draw.rect(self.screen, color, grid_to_px(c, r), border_radius=8)
        # Outer frame
        pygame.draw.rect(self.screen, GRID_LINE,
                         (PADDING-4, PADDING-4, GRID_W*CELL+8, GRID_H*CELL+8),
                         border_radius=12, width=2)

    def draw_hud(self):
        # Top bar (score, best, speed)
        info = f"Score: {self.score}   Best: {self.best}   Speed: {int(1000/max(1,self.move_ms))} /s"
        text = self.font.render(info, True, TEXT)
        self.screen.blit(text, (PADDING, 6))
        # Hints
        hint = self.font.render("WASD / Arrows to move  •  Space/P to pause  •  R to restart", True, SUBTLE)
        self.screen.blit(hint, (PADDING, WIN_H - 28))

    def draw_overlay(self):
        if self.paused and not self.game_over:
            s = self.font_big.render("Paused", True, ACCENT)
            self.screen.blit(s, s.get_rect(center=(WIN_W//2, WIN_H//2)))
        if self.game_over:
            title = self.font_big.render("Game Over", True, (255, 120, 120))
            msg = self.font.render("Press R to restart • Esc to quit", True, TEXT)
            self.screen.blit(title, title.get_rect(center=(WIN_W//2, WIN_H//2 - 14)))
            self.screen.blit(msg, msg.get_rect(center=(WIN_W//2, WIN_H//2 + 18)))

    def draw(self):
        self.screen.fill((14, 16, 20))
        self.draw_grid()
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.draw_hud()
        self.draw_overlay()
        pygame.display.flip()

    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            self.handle_input()
            self.update(dt)
            self.draw()


if __name__ == "__main__":
    Game().run()
