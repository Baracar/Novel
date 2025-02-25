image book_shop = im.Scale("images/bg/book_shop.jpg", 1920, 1080)

default first_visit_shop = True
default after_take_book = False

screen book_shop:
    imagebutton:
        idle "arrow_right"
        xpos 1800
        ypos 500
        action Jump("street")
label book_shop:
    scene book_shop

    if first_visit_shop:
        $first_visit_shop = False
        book_seller "За всё это я не могу дать много - такого старья у меня на складе навалом. Так и быть, оставь здесь."
        book_seller "Только в кассе у меня почти нет мелочи, а терминал для оплаты безнала сейчас не работает."
        book_seller " Могу дать за всё это монету в 10 сум. Мало? Ну можешь взамен выбрать 1 любую книгу с этой полки."
        mc "*Любую? Тут на полке одна книга!*"
        $iremove("old_papers")
        $iclick("book_myth")
        $iclick("coin")
        $after_take_book = True

    call screen book_shop


