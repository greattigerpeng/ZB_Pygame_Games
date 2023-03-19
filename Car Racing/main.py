import pygame
pygame.init()

window = pygame.display.set_mode([800, 600])

bg_color = (30, 190, 30)
track_color = (120, 110, 110)
outline_color = (220, 220, 220)

car_rect = pygame.Rect(350, 80, 40, 30)
car_rect2 = pygame.Rect(350, 100, 40, 30)
car_rect3 = pygame.Rect(350, 120, 40, 30)
track_rect = pygame.Rect(50, 50, 700, 500)
inner_rect = pygame.Rect(150, 150, 500, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        car_rect.y -= 1
        pygame.time.wait(5)
    if key[pygame.K_DOWN]:
        car_rect.y += 1
        pygame.time.wait(5)
    if key[pygame.K_RIGHT]:
        car_rect.x += 1
        pygame.time.wait(5)
    if key[pygame.K_LEFT]:
        car_rect.x -= 1
        pygame.time.wait(5)
    if key[pygame.K_w]:
        car_rect2.y -= 1
        pygame.time.wait(5)
    if key[pygame.K_s]:
        car_rect2.y += 1
        pygame.time.wait(5)
    if key[pygame.K_d]:
        car_rect2.x += 1
        pygame.time.wait(5)
    if key[pygame.K_a]:
        car_rect2.x -= 1
        pygame.time.wait(5)
    if key[pygame.K_i]:
        car_rect3.y -= 1
        pygame.time.wait(5)
    if key[pygame.K_k]:
        car_rect3.y += 1
        pygame.time.wait(5)
    if key[pygame.K_l]:
        car_rect3.x += 1
        pygame.time.wait(5)
    if key[pygame.K_j]:
        car_rect3.x -= 1
        pygame.time.wait(5)

    window.fill(bg_color)
    pygame.draw.ellipse(window, track_color, track_rect)
    pygame.draw.ellipse(window, outline_color, track_rect, 5)
    pygame.draw.ellipse(window, bg_color, inner_rect)
    pygame.draw.ellipse(window, outline_color, inner_rect, 5)
    pygame.draw.line(window, outline_color, (400, 50), (400, 150), 10)
    pygame.draw.ellipse(window, (230, 0, 20), car_rect)
    pygame.draw.ellipse(window, (230, 230, 20), car_rect2)
    pygame.draw.ellipse(window, (0, 20, 230), car_rect3)
    pygame.draw.ellipse(window, (20, 0, 0), car_rect3, 3)
    pygame.draw.ellipse(window, (20, 0, 0), car_rect2, 3)
    pygame.draw.ellipse(window, (20, 0, 0), car_rect, 3)
    pygame.display.flip()
