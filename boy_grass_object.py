from pico2d import *
import random   


# Game object class here

class Grass:
    def __init__(self):
        self.iamge = load_image('grass.png')
    def draw(self):
        self.iamge.draw(400, 30)
    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('animation_sheet.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(3, 6)
        self.image = load_image('ball41x41.png')
        self.frame_width = random.randint(self.image.w, self.image.w + 10)
        self.frame_hight = random.randint(self.image.h, self.image.h + 10)
    def update(self):
        if self.y < 580:
            self.y += self.frame
        else:
            while self.y >= 570:
                self.y -= 2
        self.y = max(50, min(self.y, 580))
    def draw(self):
        width = self.frame_width
        hight = self.frame_hight
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y, width, hight)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
        global running
        running = True

        global world
        world = []
        grass = Grass()
        world.append(grass)

        team = [Boy() for i in range(11)]
        world += team

        bollon = [Ball() for i in range(20)]
        world += bollon
def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
