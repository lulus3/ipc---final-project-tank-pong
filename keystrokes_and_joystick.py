import pygame


def keys_down(event, list_of_tank, game, counter):

    # if event.key == pygame.K_m and not game.invisible_mode:
    # game.set_invisible(True)
    # if event.key == pygame.K_n and game.invisible_mode:
    # game.set_invisible(False)

    for tank in list_of_tank:
        if tank.get_id() == 0:
            move_front = pygame.K_w
            spin_left = pygame.K_a
            spin_right = pygame.K_d
            shoot = pygame.K_s

        elif tank.get_id() == 1:
            move_front = pygame.K_UP
            spin_left = pygame.K_LEFT
            spin_right = pygame.K_RIGHT
            shoot = pygame.K_DOWN

        elif tank.get_id() == 2:
            move_front = pygame.K_t
            spin_left = pygame.K_f
            spin_right = pygame.K_h
            shoot = pygame.K_g

        elif tank.get_id() == 3:
            move_front = pygame.K_i
            spin_left = pygame.K_j
            spin_right = pygame.K_l
            shoot = pygame.K_k
        else:
            move_front = 0
            spin_right = 0
            spin_left = 0
            shoot = 0

        if event.key == move_front:
            tank.set_movement(True)
        if event.key == spin_right:
            tank.set_spin_r(True)
        if event.key == spin_left:
            tank.set_spin_l(True)
        if event.key == shoot:
            tank.set_shoot(True)


def keys_up(event, list_of_tank):
    for tank in list_of_tank:
        if tank.get_id() == 0:
            move_front = pygame.K_w
            spin_left = pygame.K_a
            spin_right = pygame.K_d

        elif tank.get_id() == 1:
            move_front = pygame.K_UP
            spin_left = pygame.K_LEFT
            spin_right = pygame.K_RIGHT

        elif tank.get_id() == 2:
            move_front = pygame.K_t
            spin_left = pygame.K_f
            spin_right = pygame.K_h

        elif tank.get_id() == 3:
            move_front = pygame.K_i
            spin_left = pygame.K_j
            spin_right = pygame.K_l
        else:
            move_front = 0
            spin_right = 0
            spin_left = 0

        if event.key == move_front:
            tank.set_movement(False)
        if event.key == spin_right:
            tank.set_spin_r(False)
        if event.key == spin_left:
            tank.set_spin_l(False)


def hatdown(event, list_of_tank):
    for tank in list_of_tank:
        if tank.get_id() == event.joy:
            if event.value[0] == 1:
                tank.set_spin_r(True)
            if event.value[0] == 0:
                tank.set_spin_r(False)
            if event.value[0] == -1:
                tank.set_spin_l(True)
            if event.value[0] == 0:
                tank.set_spin_l(False)


def buttondown(event, list_of_tank):
    for tank in list_of_tank:
        if tank.get_id() == event.joy:
            if event.button == 0:
                tank.set_shoot(True)
            if event.button == 1:
                tank.set_movement(True)


def buttonup(event, list_of_tank):
    for tank in list_of_tank:
        if tank.get_id() == event.joy:
            if event.button == 1:
                tank.set_movement(False)
