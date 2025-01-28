image house = im.Scale("images/bg/house.jpg", 1920, 1080)

default first_visit_home = True
default street_open = False

screen home:
    imagebutton:
        idle "arrow_up"
        xpos 950
        ypos 50
        action Jump("attic")
    if first_visit_attic:
        imagebutton:
            idle "arrow_left"
            xpos 50
            ypos 500
            action Jump("not_kitchen")
    else:
        imagebutton:
            idle "arrow_left"
            xpos 50
            ypos 500
            action Jump("kitchen")
    if street_open:
        imagebutton:
            idle "arrow_down"
            xpos 950
            ypos 950
            action Jump("street")
label home:
    scene room

    if first_visit_home:
        #$first_visit_street = False
        father "Какой ужас! Представляешь, грузовик с нашими вещами поехал на другой конец города! В транспортной компании сказали, что теперь он приедет только завтра."
        father "Ну ничего страшного, тут всё есть. Я вижу, у тебя с собой какие-то вещи, можешь разложить их на чердаке. Там была моя комната. Когда освоишься, приходи на кухню."
        $first_visit_home = False



    call screen home



label not_kitchen:
    mc "{i}Думаю сначала схожу на чердак, оставлю вещи.{/i}"
    call screen home


