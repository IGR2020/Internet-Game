import pygame as pg, random, os
pg.mixer.init()
sounds, assets, objects, item_size, run, window, crush_sound, total_items_placed = [pg.mixer.Sound("assets/sounds/break1.ogg"), pg.mixer.Sound("assets/sounds/place1.ogg")], {}, [], 32, True, pg.display.set_mode((450, 750), pg.RESIZABLE), pg.mixer.Sound("assets/sounds/crush.mp3"), 0
window_width, window_height = window.get_size()
for file in os.listdir("assets/items"):
    assets[file.replace(".png", "")] = pg.transform.scale2x(pg.image.load(f"assets/items/{file}"))
pg.font.init()
def blit_text(win, text, pos, colour=(0, 0, 0), size=30, font="arialblack"):
    text = str(text)
    x, y = pos
    font_style = pg.font.SysFont(font, size)
    text_surface = font_style.render(text, True, colour)
    win.blit(text_surface, (x, y))
class Item(pg.Rect):
    def __init__(self, x, y, name) -> None:
        self.name = name
        super().__init__(x, y, item_size, item_size)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: run = False
        if event.type == pg.MOUSEBUTTONDOWN: 
            objects.append(Item(*pg.mouse.get_pos(), random.choice(list(assets.keys()))))
            random.choice(sounds).play()
            total_items_placed += 1
        if event.type == pg.VIDEORESIZE: window_width, window_height = event.dict["size"]
    window.fill((30, 30, 30))
    for obj in objects:
        if obj.bottom < window_height: obj.y += 2
        for obj2 in objects:
            if obj.colliderect(obj2) and id(obj) != id(obj2):
                objects.remove(obj2)
                crush_sound.play()
        window.blit(assets[obj.name], obj)
    blit_text(window, f"Total Items Placed: {total_items_placed}", (0, 0), (255, 255, 255), 30)
    pg.display.update()
pg.quit()