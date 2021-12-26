import pygame
from PIL import Image, ImageDraw


def custom_cube(screen):
    width, height = 850, 450
    style_cube, color1, color2 = None, None, None
    main_cube = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    styles = {"style1.png": (width * 0.15, height * 0.05), "style2.png": (width * 0.15, height * 0.225),
              "style3.png": (width * 0.15, height * 0.4), "style4.png": (width * 0.15, height * 0.575)}

    customize_screen = screen

    for name, coords in styles.items():
        sprite = pygame.sprite.Sprite(all_sprites)
        if name != "style4.png":
            sprite.image = load_image(name, None)
        else:
            sprite.image = load_image(name, (255, 0, 0))
        sprite.image = pygame.transform.scale(sprite.image, (70, 70))
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x, sprite.rect.y = styles[name]

    image = load_image("colors.png", -1)
    for i in range(2):
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = image
        sprite.image = pygame.transform.scale(sprite.image, (200, 100))

        sprite.rect = sprite.image.get_rect()
        if i == 0:
            sprite.rect.x = 625
            sprite.rect.y = 40
        else:
            sprite.rect.x = 625
            sprite.rect.y = 180

    pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
    pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
    pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                     (width * 0.75, height * 0.82),
                     width=2)
    pygame.draw.polygon(customize_screen, (245, 50, 255), ((width * 0.02, height * 0.1),
                                                           (width * 0.07, height * 0.05),
                                                           (width * 0.07, height * 0.15)))

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos[0], event.pos[1]
                if 625 <= x <= 825 and 40 <= y <= 140:
                    c = customize_screen.get_at(event.pos)
                    color1 = c[0], c[1], c[2]
                if 625 <= x <= 825 and 180 <= y <= 280:
                    c = customize_screen.get_at(event.pos)
                    color2 = c[0], c[1], c[2]

                if 127 <= x <= 197 and 22 <= y <= 92:
                    style_cube = 1
                if 127 <= x <= 197 and 101 <= y <= 171:
                    style_cube = 2
                if 127 <= x <= 197 and 180 <= y <= 250:
                    style_cube = 3
                if 127 <= x <= 197 and 258 <= y <= 328:
                    style_cube = 4

            sprite = pygame.sprite.Sprite(main_cube)

            with open('color_cube.txt', encoding='utf8', mode="r") as f:
                text = f.readline()

            text = text.split(";")
            style, c1, c2 = int(text[0]), text[1], text[2]
            c1 = c1[1:-1]
            c2 = c2[1:-1]

            c1 = tuple(int(item) for item in c1.split(', '))
            c2 = tuple(int(item) for item in c2.split(', '))

            if style_cube is not None:
                style = style_cube

            if color1 is not None:
                c1 = color1

            if color2 is not None:
                c2 = color2

            draw_cube(style, c1, c2)
            if style != 4:
                cube_image = load_image("cube.png", None)
            else:
                cube_image = load_image("cube.png", "white")

            sprite.image = cube_image
            sprite.image = pygame.transform.scale(sprite.image, (150, 150))

            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = 350, 240

            pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
            pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
            pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                             (width * 0.75, height * 0.82), width=2)
            pygame.draw.polygon(customize_screen, (245, 50, 255), ((width * 0.02, height * 0.1),
                                                                   (width * 0.07, height * 0.05),
                                                                   (width * 0.07, height * 0.15)))

        main_cube.draw(customize_screen)
        main_cube = pygame.sprite.Group()
        all_sprites.draw(customize_screen)
        pygame.display.flip()
    pygame.quit()


def draw_cube(style_cube, color1, color2):

    width, height = 200, 200
    pic = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(pic)
    if style_cube == 1:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.225, height * 0.225), (width * 0.775, int(height * 0.775))), "black")

        drawer.rectangle(((width * 0.275, height * 0.275), (width * 0.725, int(height * 0.725))), (127, 127, 127))

        drawer.rectangle(((width * 0.375, height * 0.375), (width * 0.625, int(height * 0.625))), "black")
        drawer.rectangle(((width * 0.425, height * 0.425), (width * 0.575, int(height * 0.575))), color2)
    elif style_cube == 2:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.14, height * 0.19), (width * 0.36, int(height * 0.41))), "black")
        drawer.rectangle(((width * 0.175, height * 0.225), (width * 0.325, int(height * 0.375))), color2)

        drawer.rectangle(((width * 0.64, height * 0.19), (width * 0.86, int(height * 0.41))), "black")
        drawer.rectangle(((width * 0.675, height * 0.225), (width * 0.825, int(height * 0.375))), color2)

        drawer.rectangle(((width * 0.09, height * 0.69), (width * 0.91, int(height * 0.86))), "black")
        drawer.rectangle(((width * 0.125, height * 0.725), (width * 0.875, int(height * 0.825))), color2)
    elif style_cube == 3:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.24, height * 0.14), (width * 0.46, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.275, height * 0.175), (width * 0.425, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.54, height * 0.14), (width * 0.76, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.575, height * 0.175), (width * 0.725, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.14, height * 0.49), (width * 0.86, int(height * 0.71))), "black")
        drawer.rectangle(((width * 0.175, height * 0.525), (width * 0.825, int(height * 0.675))), color2)
    elif style_cube == 4:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.24, height * 0.14), (width * 0.46, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.275, height * 0.175), (width * 0.425, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.54, height * 0.14), (width * 0.76, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.575, height * 0.175), (width * 0.725, int(height * 0.325))), color2)
        drawer.line(((0, height * 0.67), (width, height * 0.67)), "black", width=10)

        drawer.rectangle(((width * 0.29, height * 0.49), (width * 0.47, height * 0.7)), "black")
        drawer.rectangle(((width * 0.53, height * 0.49), (width * 0.71, height * 0.7)), "black")

        drawer.rectangle(((width * 0.325, height * 0.525), (width * 0.435, height * 0.8)), "white")
        drawer.rectangle(((width * 0.565, height * 0.525), (width * 0.675, height * 0.8)), "white")

        drawer.rectangle(((0, height * 0.7), (width, height * 0.8)), "white")
        drawer.rectangle(((0, height * 0.8), (width, height * 0.85)), "black")
    text = ";".join([str(style_cube), str(color1), str(color2)])

    with open('color_cube.txt', encoding='utf8', mode="w") as f:
        f.write(text)

    pic.save("images\cube.png")
    return pic

