import pygame as pg, random, os
class Player(pg.Rect):
    def __init__(self, x: int, y: int, move_left, move_right, idle): _, self.leftImage, self.rightImage, self.idleImage, self.x_vel, self.y_vel, self.image = super().__init__(x, y, item_size, item_size*2), move_left, move_right, idle, 0, 0, idle
    def display(self, window): window.blit(player_assets[self.image], self)
    def script(self):
        keys, self.x_vel = pg.key.get_pressed(), 0
        if keys[pg.K_a]: self.x_vel -= 2
        if keys[pg.K_d]: self.x_vel += 2
        self.x, self.y = self.x + self.x_vel, self.y + self.y_vel
        if self.x_vel > 0: self.image = self.rightImage
        elif self.x_vel < 0: self.image = self.leftImage
        else: self.image = self.idleImage
window, _, _ = pg.display.set_mode((450, 750), pg.RESIZABLE), pg.mixer.init(), pg.display.set_caption("Internet Game!")
sounds, assets, objects, item_size, run, slime_blocks, clock, slime_image, slime_sound, player_assets, oof_sound = [pg.mixer.Sound("assets/sounds/break1.ogg"), pg.mixer.Sound("assets/sounds/place1.ogg")], {}, [], 32, True, [], pg.time.Clock(), pg.transform.scale2x(pg.image.load("assets/other/Slime Block.png")), pg.mixer.Sound("assets/sounds/slime.ogg"), {}, pg.mixer.Sound("assets/sounds/oof.mp3")
for file in os.listdir("assets/items"): assets[file.replace(".png", "")] = pg.transform.scale2x(pg.image.load(f"assets/items/{file}"))
for file in os.listdir("assets/player"): player_assets[file.replace(".png", "")] = pg.transform.scale2x(pg.image.load(f"assets/player/{file}"))
window_width, window_height, player = window.get_width(), window.get_height(), Player(200, 750-item_size*2, "Stone Left", "Stone Right", "Stone Idle")
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
            if event.button == 3: slime_blocks.append(Item((x // item_size)*item_size, (y// item_size)*item_size, None)), slime_sound.play()
        if event.type == pg.VIDEORESIZE: window_width, window_height = event.dict["size"]
    window.fill((30, 30, 30)),  clock.tick(60), player.display(window), player.script()
    for obj in objects:
        if obj.bottom < window_height: obj.y_vel += 0.2 
        else: obj.y_vel = 0
        if player.colliderect(obj): oof_sound.play(), objects.remove(obj)
        obj.y , _ = obj.y + obj.y_vel, window.blit(assets[obj.name], obj)
    for slime in slime_blocks: 
        window.blit(slime_image, slime.topleft)
        for obj in objects: 
            if slime.colliderect(obj): obj.y_vel = -obj.y_vel * 0.7
    pg.display.update()
pg.quit()