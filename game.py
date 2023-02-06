import pygame.time

from config import Config
from arena_class import Arena
from tanques import Tank
from tanques import Ball
from hud import Hud
from combat_tank_colisao import collision_tank_or_ball
import keystrokes_and_joystick
import elements


class Game:
    def __init__(self):
        self.__number_of_tank = 0
        self.__bullet_list: list = [[], [], [], []]
        self.__list_of_tank = []
        self.__list_of_animation = []
        self.__list_of_sounds = []
        self.__arena = Arena()
        self.__counter = 0
        self.__hud = Hud
        self.__winner = -1
        self.loop = True
        self.loop_victory = True
        self.invisible_mode = False
        self.__respawn = False
        self.__joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    def menu(self):
        menu = True
        while menu:
            Config.screen.fill(Config.black)
            elements.draw_menu1("assets/arena1.png", "assets/arena2.png", Config.screen, Config.font)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.__arena.creat_arena("Arena_1")
                        Config.arena_color = Config.green
                        Config.obstacle_color = Config.gray
                        menu = False
                    if event.key == pygame.K_2:
                        self.__arena.creat_arena("Arena_2")
                        Config.arena_color = Config.orange
                        Config.obstacle_color = Config.yellow
                        menu = False
            pygame.display.flip()

        menu = True
        while menu:
            Config.screen.fill(Config.black)
            elements.draw_menu2(
                "assets/tank1.png", "assets/tank2.png", "assets/tank3.png", "assets/tank4.png", Config.screen,
                Config.font
            )
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        self.__number_of_tank = 2
                        menu = False
                    if event.key == pygame.K_3:
                        self.__number_of_tank = 3
                        menu = False
                    if event.key == pygame.K_4:
                        self.__number_of_tank = 4
                        menu = False
            pygame.display.flip()

        list_spawn_position = self.__arena.get_spawns()
        for a in range(self.__number_of_tank):
            archive = pygame.image.load(Config.list_name_archive_tank[a])
            x = list_spawn_position[a][0]
            y = list_spawn_position[a][1]
            tank = Tank(archive, Config.arena_color, x, y, 0, Config.speed_tank, 0, a)
            tank.t_rect = tank.get_photo().get_rect()
            tank.t_rect.center = (tank.get_x(), tank.get_y())
            self.__list_of_tank.append(tank)

    def actions(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
                self.loop_victory = False
            if event.type == pygame.KEYDOWN:
                keystrokes_and_joystick.keys_down(event, self.__list_of_tank, self, self.__counter)

            if event.type == pygame.KEYUP:
                keystrokes_and_joystick.keys_up(event, self.__list_of_tank)

            if event.type == pygame.JOYHATMOTION:
                keystrokes_and_joystick.hatdown(event, self.__list_of_tank)

            if event.type == pygame.JOYBUTTONDOWN:
                keystrokes_and_joystick.buttondown(event, self.__list_of_tank)

            if event.type == pygame.JOYBUTTONUP:
                keystrokes_and_joystick.buttonup(event, self.__list_of_tank)

    def set_time_and_screen(self):
        Config.screen.fill(Config.arena_color)
        self.__counter = pygame.time.get_ticks()

    def respawn(self) -> None:
        if self.__respawn:
            self.__list_of_tank = self.__list_of_animation.copy()
            self.__list_of_animation.clear()
            for tank in self.__list_of_tank:
                tank.respawn(Config.speed_tank)
                self.__respawn = False
            for b in self.__bullet_list:
                b.clear()

    def movement_tank(self):
        for tank in self.__list_of_tank:
            tank.t_rect = tank.get_photo().get_rect()
            tank.t_rect.center = (tank.get_x(), tank.get_y())
            tank.move(self.__counter, self.__list_of_sounds[tank.get_id()])
            tank.spin_right()
            tank.spin_left()

    def collision_tank(self):
        self.__collision_tank_obstacles()
        self.__collision_tank_walls()

    def __collision_tank_obstacles(self):
        for tank in self.__list_of_tank:

            for obstacle in self.__arena.get_obstacles():
                x_obstacle_position = obstacle.get_x()
                y_obstacle_position = obstacle.get_y()
                w = obstacle.get_w()
                h = obstacle.get_h()

                if tank.t_rect.colliderect(obstacle.get_rect()):  # collision tank with obstacles
                    vector = tank.get_vector()
                    pos = collision_tank_or_ball(
                        tank.get_x(), tank.get_y(), vector[0], vector[1], x_obstacle_position,
                        y_obstacle_position, w, h, 0)
                    if tank.get_x() != pos[0][0]:
                        tank.set_x(pos[0][0])
                    if tank.get_y() != pos[0][1]:
                        tank.set_y(pos[0][1])

    def __collision_tank_walls(self):
        for tank in self.__list_of_tank:
            if tank.t_rect.colliderect(self.__arena.get_walls()[0]):
                tank.set_y(tank.get_y() + abs(tank.get_vector()[1]))
            if tank.t_rect.colliderect(self.__arena.get_walls()[1]):
                tank.set_y(tank.get_y() - abs(tank.get_vector()[1]))
            if tank.t_rect.colliderect(self.__arena.get_walls()[2]):
                tank.set_x(tank.get_x() - abs(tank.get_vector()[0]))
            if tank.t_rect.colliderect(self.__arena.get_walls()[3]):
                tank.set_x(tank.get_x() + abs(tank.get_vector()[0]))

    def collision_bullet(self):
        self.__collision_bullet_obstacles()
        self.__collision_bullet_walls()

    def __collision_bullet_walls(self):
        for b in self.__bullet_list:
            for bullet in b:
                bullet.move()
                bullet.rect.center = (bullet.x_position, bullet.y_position)
                if bullet.rect.colliderect(self.__arena.get_walls()[0]) or \
                        bullet.rect.colliderect(self.__arena.get_walls()[1]):
                    bullet.speed_y *= -1
                    bullet.life -= 1
                    Config.bounce_ball.play()
                if bullet.rect.colliderect(self.__arena.get_walls()[2]) or \
                        bullet.rect.colliderect(self.__arena.get_walls()[3]):
                    bullet.speed_x *= -1
                    bullet.life -= 1
                    Config.bounce_ball.play()

    def __collision_bullet_obstacles(self):
        for obstacle in self.__arena.get_obstacles():
            x_obstacle_position = obstacle.get_x()
            y_obstacle_position = obstacle.get_y()
            w = obstacle.get_w()
            h = obstacle.get_h()
            for b in self.__bullet_list:
                for bullet in b:
                    if bullet.rect.colliderect(obstacle.get_rect()):
                        Config.bounce_ball.play()
                        bullet.life -= 1
                        pos = collision_tank_or_ball(
                            bullet.x_position, bullet.y_position, bullet.speed_x, bullet.speed_y, x_obstacle_position,
                            y_obstacle_position, w, h, 1)
                        bullet.x_position = pos[0][0]
                        bullet.y_position = pos[0][1]
                        bullet.speed_x = pos[1][0]
                        bullet.speed_y = pos[1][1]
                    if bullet.life <= 0:
                        b.remove(bullet)

    def shoot(self):
        for tank in self.__list_of_tank:
            if tank.get_shoot():
                if self.__counter - tank.get_time_to_recharge() > Config.recharge_time * 1000:
                    archive = pygame.image.load(Config.list_name_archive_ball[tank.get_id()])
                    bullet = Ball(
                        archive, tank.get_x(), tank.get_y(), Config.speed_ball * tank.get_vector()[0],
                        Config.speed_ball * tank.get_vector()[1], Config.life_ball, tank.get_id())
                    self.__bullet_list[tank.get_id()].append(bullet)
                    tank.set_time_to_recharge()
                    Config.shoot_sound.play()
                tank.set_shoot(False)

    def collision_tank_bullet(self):
        for b in self.__bullet_list:
            for bullet in b:
                for tank in self.__list_of_tank:
                    if bullet.get_id() != tank.get_id():
                        if bullet.rect.colliderect(tank.t_rect):
                            self.__ad_point(bullet.get_id())
                            self.__bullet_list[tank.get_id()].clear()
                            b.remove(bullet)
                            tank.set_time_of_animation()
                            self.__list_of_animation.append(tank)
                            self.__list_of_tank.remove(tank)
                            Config.tank_explode.play()
                            break

    def __ad_point(self, ide):
        for tank in self.__list_of_tank:
            if ide == tank.get_id():
                tank.ad_point()

    def animation_death(self):
        for tank in self.__list_of_animation:
            tank.spin_death(self.__counter, Config.screen, tank.t_rect)

    def draw_elements(self):
        self.__tank()
        self.__draw_wall()
        self.__draw_obstacles()
        self.__draw_hud()
        self.__draw_bullet()

    def __tank(self):
        for tank in self.__list_of_tank:
            if not self.invisible_mode:
                Config.screen.blit(tank.get_photo(), tank.t_rect)
            if self.invisible_mode:
                pygame.draw.rect(Config.screen, Config.arena_color, tank.t_rect)

    def __draw_wall(self):
        self.__arena.draw_walls(Config.screen, Config.obstacle_color)

    def __draw_obstacles(self):
        self.__arena.draw_obstacles(Config.screen, Config.obstacle_color)

    def __draw_hud(self):
        for tank in self.__list_of_tank:
            self.__hud.list_hud[tank.get_id()][0] = Config.font_hud.render(str(tank.get_point()), True, Config.list_of_color[tank.get_id()])
            Config.screen.blit(self.__hud.list_hud[tank.get_id()][0], self.__hud.list_hud[tank.get_id()][1])
            if tank.get_point() >= Config.point_victory:
                if self.__winner == -1:
                    self.__winner = tank.get_id()
                if self.__counter - self.__list_of_animation[len(self.__list_of_animation) - 1].get_time_of_animation() > Config.animation_time * 1000:
                    self.loop = False
        for tank in self.__list_of_animation:
            self.__hud.list_hud[tank.get_id()][0] = Config.font_hud.render(str(tank.get_point()), True, Config.list_of_color[tank.get_id()])
            Config.screen.blit(self.__hud.list_hud[tank.get_id()][0], self.__hud.list_hud[tank.get_id()][1])
        if (len(self.__list_of_tank) == 1 and
                self.__counter - self.__list_of_animation[self.__number_of_tank - 2].get_time_of_animation() > Config.animation_time * 1000):
            self.__list_of_animation.append(self.__list_of_tank[0])
            self.__list_of_tank.clear()
            self.__respawn = True

    def __draw_bullet(self):
        for b in self.__bullet_list:
            for bullet in b:
                Config.screen.blit(bullet.photo, bullet.rect)

    def victory(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop_victory = False
            Config.screen.fill(Config.black)
            elements.victory_texts(Config.font_hud, Config.size_screen, self.__winner, Config.screen)

    def set_sounds(self):
        for s in range(self.__number_of_tank):
            self.__list_of_sounds.append(pygame.mixer.Sound("assets/tank-walking.wav"))

    def set_invisible(self, tf):
        self.invisible_mode = tf







