import pygame as pg
import pyperclip

# init pygame
HEIGHT = WIDTH = 1000
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SGA writer")
clock = pg.time.Clock()
pg.font.init() 
sga_font = pg.font.Font("sga.ttf", 30)
normal_font = pg.font.SysFont('Comic Sans MS', 20)

# functions

# vars
normal_text = ""
sga_text = ""
MAX_LINE_CHARS = 30
dictionary = {
pg.K_a:"ᖋ",
pg.K_b:"ʖ",
pg.K_c:"ᔮ",
pg.K_d:"⌥",
pg.K_e:"ᒷ",
pg.K_f:"⎓",
pg.K_g:"˧",
pg.K_h:"₸",
pg.K_i:"¦",
pg.K_j:"ⵗ",
pg.K_k:"ꖌ",
pg.K_l:"ꖎ",
pg.K_m:"ᒲ",
pg.K_n:"リ",
pg.K_o:"𝙹",
pg.K_p:"ⅱ",
pg.K_q:"⊐", 
pg.K_r:"∷",
pg.K_s:"ᓭ",
pg.K_t:"ᒣ",
pg.K_u:"⚍",
pg.K_v:"⍊",
pg.K_w:"∴",
pg.K_x:"ン",
pg.K_y:"॥",
pg.K_z:"ᙁ",
}
reverse_dictionary = {
"ᖋ":"a",
"ʖ":"b",
"ᔮ":"c",
"⌥":"d",
"ᒷ":"e",
"⎓":"f",
"˧":"g",
"₸":"h",
"¦":"i",
"ⵗ":"j",
"ꖌ":"k",
"ꖎ":"l",
"ᒲ":"m",
"リ":"n",
"𝙹":"o",
"ⅱ":"p",
"⊐":"q",
"∷":"r",
"ᓭ":"s",
"ᒣ":"t",
"⚍":"u",
"⍊":"v",
"∴":"w",
"ン":"x",
"॥":"y",
"ᙁ":"z",
}
special_chars = {
    pg.K_PERIOD: ".",
    pg.K_COMMA: ",",
    pg.K_MINUS: "-",
    pg.K_UNDERSCORE: "_",
    pg.K_PLUS: "+",
    pg.K_QUESTION: "?",
    pg.K_EXCLAIM: "!",
    pg.K_QUOTE: '"',
    pg.K_SLASH: "/",
    pg.K_COLON: ":",
    pg.K_ASTERISK: "*",
    pg.K_LEFTPAREN: "(",
    pg.K_RIGHTPAREN: ")",
    pg.K_KP_EQUALS: "=",
    pg.K_SPACE: " ",
    pg.K_RETURN: "\n",
    pg.K_0: "0",
    pg.K_1: "1",
    pg.K_2: "2",
    pg.K_3: "3",
    pg.K_4: "4",
    pg.K_5: "5",
    pg.K_6: "6",
    pg.K_7: "7",
    pg.K_8: "8",
    pg.K_9: "9",
}

# mainloop
running = True
while running:
    keys = pg.key.get_pressed()
    special_action = False
    # copy
    if keys[pg.K_F1]:
        pyperclip.copy(sga_text)
    # paste
    if keys[pg.K_F2]:
        sga_text += pyperclip.paste()
        normal_text += pyperclip.paste()
    # open
    # save
        
    ##### events and typing ######
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if special_action:
                continue
            # special chars
            if event.key in special_chars:
                sga_text += special_chars[event.key]
                normal_text += special_chars[event.key]
            # alphabet
            for k, v in dictionary.items():
                if event.key == k:
                    sga_text += v
                    normal_text += reverse_dictionary[v]
            # other
            if event.key == pg.K_BACKSPACE:
                sga_text = sga_text[:-1]
                normal_text = normal_text[:-1]
    # shift special chars
    #if not special_action:
    #    for x, y in special_chars.items():
    #        if keys[pg.K_LSHIFT] and keys[x]:
    #            sga_text += y
    #            normal_text += y
    ##############################
    
    # background
    screen.fill("Green")
    # options background
    option_size = WIDTH*(30 / 100) # width * percent = xcord
    option_left_cord = WIDTH-option_size
    option_rect = pg.Rect((option_left_cord, 0), (option_size, HEIGHT))
    pg.draw.rect(screen, (255,255,255), option_rect)
    # option text
    option_head = (normal_font.render("OPTIONS", False, (0,0,0)), (option_left_cord+100, 0))
    screen.blit(option_head[0], option_head[1])
    # display text
    text_cords = [0,0]
    for x in normal_text.split("\n"):
        for line in [x[i:i+MAX_LINE_CHARS] for i in range(0, len(x), MAX_LINE_CHARS)]:
            sga = sga_font.render(line, False, (0, 0, 0))
            normal = normal_font.render(line, False, (0, 0, 0))
            screen.blit(sga, text_cords)
            screen.blit(normal, (0, text_cords[1]+30))
            text_cords[1] += 60
    pg.display.flip()
    clock.tick(20)
