from config import Config


class Hud:
    hud_text1 = Config.font.render("0", True, Config.red, Config.black)
    hud_text2 = Config.font.render("0", True, Config.blue, Config.black)
    hud_text3 = Config.font.render("0", True, Config.yellow, Config.black)
    hud_text4 = Config.font.render("0", True, Config.purple, Config.black)
    hud_text1_rect = hud_text1.get_rect()
    hud_text2_rect = hud_text2.get_rect()
    hud_text3_rect = hud_text3.get_rect()
    hud_text4_rect = hud_text4.get_rect()
    hud_text1_rect.center = (40, 30)
    hud_text2_rect.center = (370, 30)
    hud_text3_rect.center = (740, 30)
    hud_text4_rect.center = (1110, 30)
    hd1 = [hud_text1, hud_text1_rect]
    hd2 = [hud_text2, hud_text2_rect]
    hd3 = [hud_text3, hud_text3_rect]
    hd4 = [hud_text4, hud_text4_rect]
    list_hud = [hd1, hd2, hd3, hd4]
