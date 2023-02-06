from config import Config
import pygame


def draw_menu1(archive1, archive2, surface, font) -> None:
    image1 = pygame.image.load(archive1)
    image1_rect = image1.get_rect()
    image1_rect.center = (355, 350)
    surface.blit(image1, image1_rect)
    image2 = pygame.image.load(archive2)
    image2_rect = image2.get_rect()
    image2_rect.center = (1010, 350)
    surface.blit(image2, image2_rect)
    text = font.render("which arena will it be?", True, Config.white, Config.black)
    chose1 = font.render("1", True, Config.white, Config.black)
    chose2 = font.render("2", True, Config.white, Config.black)
    text_rect = text.get_rect()
    text_rect.center = (683, 100)
    surface.blit(text, text_rect)
    chose1_rect = chose1.get_rect()
    chose1_rect.center = (355, 183)
    surface.blit(chose1, chose1_rect)
    chose2_rect = chose2.get_rect()
    chose2_rect.center = (1010, 183)
    surface.blit(chose2, chose2_rect)


def draw_menu2(archive1, archive2, archive3, archive4, surface, font) -> None:
    list_archive = [archive1, archive2, archive3, archive4]
    x = 273
    for a in range(4):
        photo = pygame.image.load(list_archive[a])
        photo_rect = photo.get_rect()
        photo_rect.center = (x, 350)
        surface.blit(photo, photo_rect)
        x += 273
    text = font.render("how many players will play? min(2) max(4)", True, Config.white, Config.black)
    text_rect = text.get_rect()
    text_rect.center = (683, 100)
    surface.blit(text, text_rect)


def victory_texts(font, size, winner, surface):
    victory_text1 = font.render("player red win", True, Config.red, Config.black)
    victory_text2 = font.render("player blue win", True, Config.blue, Config.black)
    victory_text3 = font.render("player yellow win", True, Config.yellow, Config.black)
    victory_text4 = font.render("player purple win", True, Config.purple, Config.black)
    victory_text1_rect = victory_text1.get_rect()
    victory_text2_rect = victory_text2.get_rect()
    victory_text3_rect = victory_text3.get_rect()
    victory_text4_rect = victory_text4.get_rect()
    victory_text1_rect.center = (size[0]/2, 350)
    victory_text2_rect.center = (size[0]/2, 350)
    victory_text3_rect.center = (size[0]/2, 350)
    victory_text4_rect.center = (size[0]/2, 350)
    vc1 = (victory_text1, victory_text1_rect)
    vc2 = (victory_text2, victory_text2_rect)
    vc3 = (victory_text3, victory_text3_rect)
    vc4 = (victory_text4, victory_text4_rect)
    list_vic = [vc1, vc2, vc3, vc4]
    surface.blit(list_vic[winner][0], list_vic[winner][1])



