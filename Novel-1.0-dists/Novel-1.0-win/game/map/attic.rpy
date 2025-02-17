image attic = im.Scale("images/bg/attic.jpg", 1920, 1080)

default first_visit_attic = True
default heap_game = True
default poster = False
default table = False
default closet = False

screen attic:
    if closet and table:
        imagebutton:
            idle "arrow_down"
            xpos 950
            ypos 950
            action Jump("home")
    if not table:
        imagebutton:
            idle "table.jpg"
            xpos 25
            ypos 570
            action Jump("table")
    if not closet:
        imagebutton:
            idle "closet.png"
            xpos 1550
            ypos 670
            action Jump("closet")
    if not poster:
        imagebutton:
            idle "poster.png"
            xpos 1550
            ypos 170
            action Jump("poster")



label attic:
    scene attic
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

label poster:
    mc "О, это же поп-звезда Зухра Йолдыз. Не знал что в подростковом возрасте папе такое нравилось."
    mc "Внизу есть какая-то надпись… “Ай с тат. - месяц”. Постер вот-вот упадёт, нужно поправить."
    mc "Ой. *уголок плаката рвётся, в руке остался клочок бумаги с надписью*"
    mc "Видимо бумага от времени совсем испортилась, нужно быть аккуратнее. Если близко не подходить, то и не заметно. Думаю папа не заметит."
    $poster = True
    call screen attic

