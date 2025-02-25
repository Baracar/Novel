image kitchen = im.Scale("locations/kitchen/bg.png", 1920, 1080)

default first_visit_kitchen = True
default fridge = False
default dirty_cup = False
default milk_jar = False

screen kitchen:
    imagebutton:
        idle "arrow_right"
        xpos 1800
        ypos 500
        action Jump("home")
    if not fridge:
        imagebutton:
            idle im.Scale("locations/kitchen/refrigerator.png", 416, 774.5625)
            hover im.Scale("locations/kitchen/refrigerator white.png", 416, 774.5625)
            xpos 97
            ypos 306
            action Call("puzzle_pieces", "fridge")
    if not dirty_cup:
        imagebutton:
            idle im.Scale("locations/kitchen/dirty cup.png", 100, 100)
            hover im.Scale("locations/kitchen/dirty cup white.png", 100, 100)
            xpos 1585
            ypos 540
            action Call("dirty_cup")
    if not milk_jar:
        imagebutton:
            idle im.Scale("locations/kitchen/milk jar.png", 177, 150.1875)
            hover im.Scale("locations/kitchen/milk jar white.png", 177, 150.1875)
            xpos 1353
            ypos 721
            action Call("milk_jar")


label kitchen:
    scene kitchen
    if first_visit_kitchen:
        $first_visit_kitchen = False
        show father normal
        father "Ну и шуточки у тебя. Если хотел кофе с молоком, мог бы себе сделать отдельно, не обязательно было в мой подмешивать."
        mc "О чём ты? Я даже не заходил ещё на кухню."
        father "Хочешь сказать, у нас в доме приведение?"
        mc "Не думаю. Но было бы интересно!"
        father "Что-то мой сотовый здесь перестал ловить. Я не смог дозвониться до транспортной компании."
        mc "У меня тоже. Пойду на улицу, проверю там."
        father "Тогда возьми с собой стопку макулатуры из старых газет и книг и отнеси их в букинистику. Может газеты подойдут для архива."
        father "А книги… Эти уже много раз прочитаны, не думаю, что мы будем их читать ещё раз."
        father "Может кому-нибудь они пригодятся."
        $iclick("old_papers")
        hide father normal
#         $first_visit_home = False

    $street_open = True

    call screen kitchen

label puzzle_fridge:
    #ADD TEXT тест после решения паззла в холодильнике
    $iclick("kefir")
    $fridge = True
    call screen kitchen

label dirty_cup:
    #ADD TEXT тест после подбора кружки
    $dirty_cup = True
    $iclick("dirty_cup")
    call screen kitchen

label milk_jar:
    #ADD TEXT тест после подбора молочника
    $milk_jar = True
    $iclick("milk_jar")
    call screen kitchen