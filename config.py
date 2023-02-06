import pygame
pygame.init()


class Config:
    # colors
    black = (0, 0, 0)
    orange = (255, 157, 4)
    yellow = (218, 255, 7)
    white = (255, 255, 255)
    green = (57, 255, 29)
    red = (255, 0, 0)
    gray = (156, 156, 156)
    blue = (0, 0, 255)
    purple = (242, 51, 242)

    # config arena
    point_victory = 7
    recharge_time = 1.5
    animation_time = 2.5

    # config tank
    speed_angle_tank = 2.5  # max speed = 3
    speed_tank = 2.5  # max speed = 3

    # config ball
    life_ball = 4
    # the velocity of the ball is a multiplication of the velocity of the tank by a variable, the max must be 9
    speed_ball = 3
    time_visibility = 2  # if visible mode was activated
    limit_ball = 3

    # sounds
    pygame.mixer.init()
    shoot_sound = pygame.mixer.Sound("assets/tiger.wav")
    tank_explode = pygame.mixer.Sound("assets/tank_explode.wav")
    bounce_ball = pygame.mixer.Sound("assets/bounce_ball.wav")
    tank_walk = pygame.mixer.Sound("assets/tank-walking.wav")
    time_sound = tank_walk.get_length()

    size_screen = (1366, 720)
    screen = pygame.display.set_mode(size_screen)
    arena_color = 0
    obstacle_color = 0
    font = pygame.font.Font("assets/PressStart2P.ttf", 25)
    font_hud = pygame.font.Font("assets/PressStart2P.ttf", 45)
    list_name_archive_tank = ["assets/tank1.png", "assets/tank2.png", "assets/tank3.png", "assets/tank4.png"]
    list_name_archive_ball = ["assets/bala1.png", "assets/bala2.png", "assets/bala3.png", "assets/bala4.png"]
    list_of_color = [red, blue, yellow, purple]
    size_walls = 17
