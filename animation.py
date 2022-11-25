from helper import *
import threading

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw():
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (50, HEIGHT//2), (WIDTH-50, HEIGHT//2))
    for p in POINTS:
        if p.start_time is None:
            p.start_time = time.time()
        p.move()
        pygame.draw.rect(WIN, BLACK, pygame.Rect(p.x, p.y, 3, 3))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(30)
    
    t = threading.Thread(target=update_freq, daemon=True)
    t.start()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                run = False

        draw()


def update_freq():
    while True:
        Point.ANG_FREQ = float(input('Update angle frequency: '))
    
    # Point.ANG_FREQ += 0.0000001

if __name__ == '__main__':
    main()