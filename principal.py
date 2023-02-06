from config import *
from game import Game
game = Game()
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
game.menu()
game.set_sounds()

while game.loop:
    game.actions()
    game.set_time_and_screen()
    game.respawn()
    game.movement_tank()
    game.collision_tank()
    game.collision_bullet()
    game.collision_tank_bullet()
    game.shoot()
    game.animation_death()
    game.draw_elements()
    pygame.display.flip()
    clock.tick(60)

while game.loop_victory:
    game.victory()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
