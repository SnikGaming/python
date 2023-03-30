import pygame

# Khởi tạo Pygame
pygame.init()

# Màn hình
screen = pygame.display.set_mode((800, 600))

# Tên của game
pygame.display.set_caption("My Jumping Game")

# Tải ảnh cho nhân vật và nền
player_img = pygame.image.load("Screenshot 2023-03-30 000410.png")
background_img = pygame.image.load("Screenshot_20230126_085240.png")

# Khởi tạo vị trí ban đầu của nhân vật
player_x = 50
player_y = 500

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Cập nhật vị trí của nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_SPACE]:
        player_y -= 10

    # Vẽ các thành phần của game lên màn hình
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, (player_x, player_y))

    # Cập nhật màn hình
    pygame.display.update()
