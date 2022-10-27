from helper import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(start_time):
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (50, HEIGHT//2), (WIDTH-50, HEIGHT//2))
    for p in POINTS:
        if p.start_time is None:
            p.start_time = time.time()
        p.move()
        pygame.draw.rect(WIN, BLACK, pygame.Rect(p.x, p.y, 3, 3))
    pygame.display.update()

def main():
    start_time = time.time()
    clock = pygame.time.Clock()
    clock.tick(60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw(start_time)




if __name__ == '__main__':
    main()