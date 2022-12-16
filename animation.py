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
            if event.type == pygame.MOUSEBUTTONUP:
                Point.AMPLITUDE = 50
                Point.START_TIME = time.time()

        draw()


def update_freq():
    while True:
        Point.ANG_FREQ = float(input('Update angle frequency: '))
        
if __name__ == '__main__':
    while True:
        is_decr =  input('Should oscillation be decreasing? y/n ').upper() 
        if is_decr.upper() not in ['Y', 'N']:
            print('please answer y (yes) or n (no)')
        else:
            Point.IS_DECR = True if is_decr.upper() == 'Y' else False
            break
    main()