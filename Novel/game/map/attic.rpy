image attic = im.Scale("images/bg/attic.png", 1920, 1080)
#image closet = im.Scale

default first_visit_attic = True
default heap_game = True
default poster = False
default table = False
default closet = False
default bed = False

screen attic:
    if closet and table:
        imagebutton:
            idle "arrow_down"
            xpos 950
            ypos 950
            action Jump("home")
    if not table:
        imagebutton:
            idle im.Scale("table.png", 611.25, 286.875)
            xpos 490
            ypos 693
            action Call("puzzle_pieces", 2)
    if not closet:
        imagebutton:
            idle im.Scale("closet.png", 496.75, 838.125)
            xpos 1131
            ypos 239
            action Jump("tetris_start")
    if not bed:
        imagebutton:
            idle im.Scale("bed.png", 460.3, 351.5)
            xpos 46
            ypos 724
            action Jump("slide_block_puzzle")
#     if not poster:
#         imagebutton:
#             idle "poster.png"
#             xpos 1550
#             ypos 170
#             action Jump("poster")



label attic:
    scene attic
    $ puzzle = 2
    if first_visit_attic:
        mc "Нужно разложить свои вещи."
        $first_visit_attic = False

    call screen attic


label table:
    "Мини игра по раскладыванию вещей на столе"
    $table = True
    call screen attic

label closet:
    "Мини игра по раскладыванию вещей в шкафу"
    $closet = True
    call screen attic

label bed:
    "Мини игра по раскладыванию вещей в шкафу"
    $bed = True
    call screen attic

label poster:
    mc "О, это же поп-звезда Зухра Йолдыз. Не знал что в подростковом возрасте папе такое нравилось."
    mc "Внизу есть какая-то надпись… “Ай с тат. - месяц”. Постер вот-вот упадёт, нужно поправить."
    mc "Ой. *уголок плаката рвётся, в руке остался клочок бумаги с надписью*"
    mc "Видимо бумага от времени совсем испортилась, нужно быть аккуратнее. Если близко не подходить, то и не заметно. Думаю папа не заметит."
    $poster = True
    call screen attic

