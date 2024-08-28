import pygame as pg, random, os
pg.mixer.init()
sounds, assets, objects, item_size, run, window, slime_blocks, clock, slime_image, slime_sound = [pg.mixer.Sound("assets/sounds/break1.ogg"), pg.mixer.Sound("assets/sounds/place1.ogg")], {}, [], 32, True, pg.display.set_mode((450, 750), pg.RESIZABLE), [], pg.time.Clock(), pg.transform.scale2x(pg.image.load("assets/other/Slime Block.png")), pg.mixer.Sound("assets/sounds/slime.ogg")
window_width, window_height, = window.get_size()
pg.display.set_caption("Internet Game!")
pg.font.init()
for file in os.listdir("assets/items"): assets[file.replace(".png", "")] = pg.transform.scale2x(pg.image.load(f"assets/items/{file}"))
def blit_text(win, text, pos, colour=(0, 0, 0), size=30, font="arialblack"):
    text = str(text)
    x, y = pos
    font_style = pg.font.SysFont(font, size)
    text_surface = font_style.render(text, True, colour)
    win.blit(text_surface, (x, y))
class Item(pg.Rect):
    def __init__(self, x, y, name) -> None: self.name, self.y_vel, _ = name, 0, super().__init__(x, y, item_size, item_size)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: run = False
        if event.type == pg.MOUSEBUTTONDOWN: 
            x, y = pg.mouse.get_pos()
            if event.button != 3: 
                objects.append(Item(x, y, random.choice(list(assets.keys()))))
                random.choice(sounds).play()
            if event.button == 3: 
                slime_blocks.append(Item((x // item_size)*item_size
                (y// item_size)*item_size, None))
                slime_sound.play()
        if event.type == pg.VIDEORESIZE: window_width, window_height = event.dict["size"]
    window.fill((30, 30, 30)),  clock.tick(60)
    for obj in objects:
        if obj.bottom < window_height: obj.y_vel += 0.2 
        else: obj.y_vel = 0
        obj.y , _ = obj.y + obj.y_vel, window.blit(assets[obj.name], obj)
    for slime in slime_blocks: 
        window.blit(slime_image, slime.topleft)
        for obj in objects:
            if slime.colliderect(obj):
                obj.y_vel = -obj.y_vel * 0.7
    pg.display.update()
pg.quit()
