image kitchen = im.Scale("locations/kitchen/bg.png", 1920, 1080)

default first_visit_kitchen = True

screen kitchen:
    imagebutton:
        idle "arrow_right"
        xpos 1800
        ypos 500
        action Jump("home")
label kitchen:
    scene kitchen
    if first_visit_kitchen:
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
        hide father normal
        $first_visit_home = False

    $street_open = True

    call screen kitchen
