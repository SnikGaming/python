import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH = 640
HEIGHT = 480

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Tên của game
pygame.display.set_caption("Basketball Game")

# Tải ảnh cho rổ và bóng
basket_img = pygame.image.load("Screenshot 2023-03-30 000410.png")
ball_img = pygame.image.load("Screenshot 2023-03-30 000410.png")

# Khởi tạo vị trí ban đầu của rổ và bóng
basket_x = WIDTH // 2 - basket_img.get_width() // 2
basket_y = HEIGHT - basket_img.get_height()
ball_x = WIDTH // 2 - ball_img.get_width() // 2
ball_y = 0

# Vận tốc rơi xuống của bóng
ball_speed = .05

# Điểm số
score = 0

# Khởi tạo font chữ
font = pygame.font.Font(None, 36)

# Vòng lặp game
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật trạng thái của bóng
    ball_y += ball_speed

    # Kiểm tra nếu bóng chạm vào rổ
    if ball_y + ball_img.get_height() >= basket_y and \
            ball_x + ball_img.get_width() >= basket_x and \
            ball_x <= basket_x + basket_img.get_width():
        score += 1
        ball_x = random.randint(0, WIDTH - ball_img.get_width())
        ball_y = 0

    # Kiểm tra nếu bóng rơi xuống đất
    if ball_y + ball_img.get_height() >= HEIGHT:
        ball_x = random.randint(0, WIDTH - ball_img.get_width())
        ball_y = 0

    # Vẽ các thành phần của game lên màn hình
    screen.fill(WHITE)
    screen.blit(basket_img, (basket_x, basket_y))
    screen.blit(ball_img, (ball_x, ball_y))
    text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(text, (10, 10))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc game
pygame.quit()
