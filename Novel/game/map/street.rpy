image street = im.Scale("locations/street/bg.png", 1920, 1080)

default first_visit_street = 0
default mailbox = False

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
    if not mailbox:
        imagebutton:
            idle im.Scale("locations/street/mailbox.png", 100, 100)
            hover im.Scale("locations/street/mailbox white.png", 100, 100)
            xpos 1730
            ypos 680
            action Call("mailbox")


label street:
    scene street

    if first_visit_street == 0:
        mc "Странно, не видно грузовика с вещами. Наверно всё уже занесли."
        mc "Я здесь ни разу не был. В этом доме жил отец с родителями, пока не вырос."
        mc "Дедушки уже давно не стало, а бабушка умерла недавно и родители решили переехать в этот город обратно."
        mc "… Я всегда мечтал жить в центре города, но не так я себе это представлял…"

    $first_visit_street = first_visit_street + 1

    call screen street


label mailbox:
    if "old_papers" in inventory:
        mc "У меня сейчас заняты руки. В другой раз."
    else:
        $mailbox = True
        $iclick("bill_electricity")
        $iclick("newspaper")
    call screen street