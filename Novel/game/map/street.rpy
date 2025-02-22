image street = im.Scale("locations/street/bg.png", 1920, 1080)

default first_visit_street = 0

screen street:
    imagebutton:
        idle "arrow_up"
        xpos 950
        ypos 50
        action [SetLocalVariable(first_visit_street, False), Jump("home")]
    if first_visit_street > 1:
        imagebutton:
            idle "arrow_left"
            xpos 50
            ypos 500
            action Jump("book_shop")


label street:
    scene street

    show screen code_lock

    if first_visit_street == 0:
        mc "Странно, не видно грузовика с вещами. Наверно всё уже занесли."
        mc "Я здесь ни разу не был. В этом доме жил отец с родителями, пока не вырос."
        mc "Дедушки уже давно не стало, а бабушка умерла недавно и родители решили переехать в этот город обратно."
        mc "… Я всегда мечтал жить в центре города, но не так я себе это представлял…"
        $iclick("milk_jug")

    $first_visit_street = first_visit_street + 1

    call screen street

