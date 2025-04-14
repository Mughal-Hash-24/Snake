import pygame, random

pygame.init()
clock = pygame.time.Clock()

win_res = (800, 600)

window = pygame.display.set_mode(win_res)

snake_x = 150
snake_y = 150
size = 25
snak_vel = 3

score = 0

moving_left = False
moving_right = True
moving_up = False
moving_down = False

bg_color = (150, 220, 255)

foods = []
def Foods():
    food_x = random.randint(100, 700)
    food_y = random.randint(100, 500)
    food = pygame.Rect(food_x, food_y, 25, 25)
    foods.append(food)

font = pygame.font.SysFont("Arial", 45)
def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])


def draw_snake(window, color, snk_list, size):
    for x,y in snk_list:
        pygame.draw.rect(window, (0,155,0), [x, y, size, size])

Foods()

snk_list = []
snk_length = 1

def restart_game():
    global snake_x, snake_y, moving_left, moving_right, moving_up, moving_down, snk_list, snk_length, score, game_over, foods

    snake_x = 150
    snake_y = 150
    snk_length = 1
    score = 0
    moving_left = False
    moving_right = True
    moving_up = False
    moving_down = False
    snk_list = []
    foods = []
    Foods()
    game_over = False

restart_game()

running = True

while running:
    if game_over:
        window.fill(bg_color)
        score_screen("Game Over! Press Enter to restart", (0,0,0),120, win_res[1]/2-30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart_game()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not moving_down:
                    moving_up = True
                    moving_down = False
                    moving_left = False
                    moving_right = False

                if event.key == pygame.K_DOWN and not moving_up:
                    moving_up = False
                    moving_down = True
                    moving_left = False
                    moving_right = False

                if event.key == pygame.K_RIGHT and not moving_left:
                    moving_up = False
                    moving_down = False
                    moving_left = False
                    moving_right = True

                if event.key == pygame.K_LEFT and not moving_right:
                    moving_up = False
                    moving_down = False
                    moving_left = True
                    moving_right = False

        bg = pygame.draw.rect(window, bg_color, [0,0,800,600])

        snake = pygame.draw.rect(window, (0,155,0), [snake_x, snake_y, size, size])

        if moving_down:
            snake_y += snak_vel
        elif moving_left:
            snake_x -= snak_vel
        elif moving_right:
            snake_x += snak_vel
        elif moving_up:
            snake_y -= snak_vel

        for snack in foods.copy():
            if snake.colliderect(snack):
                foods.remove(snack)
                Foods()
                score += 10
                snk_length += 10

        score_screen("Score: "+str(score), (0,0,0), 5, 5)

        for snack in foods:
            pygame.draw.rect(window, (255, 0, 0), snack)

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_length:
            del snk_list[0]

        draw_snake(window, (0,155,0), snk_list, size)

        if snake_x < 0 or snake_x > win_res[0]:
            game_over = True

        if snake_y < 0 or snake_y > win_res[1]:
            game_over = True

        if head in snk_list[:-1]:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()