image attic = im.Scale("locations/attic/attic.png", 1920, 1080)
#image closet = im.Scale

default first_visit_attic = True
default in_dark = False

default poster = False
default table = False
default closet = False
default bed = False

screen attic:
    if (closet and table) or debug:
        imagebutton:
            idle "arrow_down"
            xpos 950
            ypos 950
            action Jump("home")
    if not table:
        imagebutton:
            idle im.Scale("locations/attic/desk.png", 617.8125, 337.5)
            hover im.Scale("locations/attic/desk white.png", 617.8125, 337.5)
            xpos 485
            ypos 678
            action Call("puzzle_pieces", 1)
    if not closet:
        imagebutton:
            idle im.Scale("locations/attic/closet.png", 516.5625, 840)
            hover im.Scale("locations/attic/closet white.png", 516.5625, 840)
            xpos 1131
            ypos 239
            action Jump("tetris_start")
#     if not bed:
#         imagebutton:
#             idle im.Scale("bed.png", 460.3, 351.5)
#             xpos 46
#             ypos 724
#             action Jump("slide_block_puzzle")
    if not poster:
        imagebutton:
            idle im.Scale("locations/attic/poster.png", 261.5625, 618.75)
            hover im.Scale("locations/attic/poster white.png", 261.5625, 618.75)
            xpos 0
            ypos 200
            action Jump("poster")



label attic:
    scene attic
    $ puzzle = 2
    if first_visit_attic:
        mc "Нужно разложить свои вещи."
        $first_visit_attic = False
    elif after_take_book:
        $after_take_book = False
        "*Читает*"
        mc "Ого, уже вечер. Время так быстро пролетело."
#ADD добавить переход в тёмный
        $in_dark = True

    call screen attic


label attic_puzzle:
    "asdasda"
    #ADD TEXT тест после решения паззла с бумажками
    $table = True
    call screen attic

label attic_tetris:
    #ADD TEXT тест после решения тетриса
    $closet = True
    call screen attic

label attic_slide:
    #ADD TEXT тест после решения паззла с блоками
    $bed = True
    call screen attic

label poster:
    mc "О, это же поп-звезда Зухра Йолдыз. Не знал что в подростковом возрасте папе такое нравилось."
    mc "Внизу есть какая-то надпись… “Ай с тат. - месяц”. Постер вот-вот упадёт, нужно поправить."
    mc "Ой. *уголок плаката рвётся, в руке остался клочок бумаги с надписью*"
    mc "Видимо бумага от времени совсем испортилась, нужно быть аккуратнее. Если близко не подходить, то и не заметно. Думаю папа не заметит."
    $poster = True
    call screen attic

