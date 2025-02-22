image home = im.Scale("locations/home/bg.png", 1920, 1080)

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
    scene home

    if first_visit_home:
        #$first_visit_street = False
        show father normal
        father "Какой ужас! Представляешь, грузовик с нашими вещами поехал на другой конец города!"
        father "В транспортной компании сказали, что теперь он приедет только завтра."
        father "Ну ничего страшного, тут всё есть. Я вижу, у тебя с собой какие-то вещи, можешь разложить их на чердаке."
        father "Там была моя комната. Когда освоишься, приходи на кухню."
        hide father normal
        $first_visit_home = False
    elif after_take_book:
        mc "Думаю пойду наверх, почитаю книгу."
    elif in_dark:
        $in_dark = False
        father "Как хорошо, что я купил спички для газовой плиты. Есть чем зажечь свечи."
        "*стук в дверь*"
        father "Кто бы мог там быть, в такую-то погоду?"
        book_seller "Извините, я заработался в своей лавке и пропустил автобус. Мой телефон не ловит. Будьте добры, я закажу такси с вашего стационарного телефона? "
        father "Конечно."
        book_seller "Спасибо. *набирает номер* Здравствуйте, такси? Можно заказать по адресу… Из-за плохой погоды заказы не принимаете? До свидания. Что ж, пожалуй вернусь в лавку, пережду дождь там."
        father "Вы что! Оставайтесь у нас, если что постелим вам на полу. Я где-то видел в шкафах матрас и постельное бельё…"
        book_seller "Вы так добры!"
        father "Кстати, мы так и не представились. Я - Роберт, а это мой сын - …"
        book_seller "А меня… Су… нет, не так. Иясе…"
        father "Я плохо расслышал, вас зовут Ияс?"
        book_seller "А, да-да, меня зовут Ияс."
        $book_seller_name = "Ияс"
        father "Надеюсь вы не боитесь привидений. А то в доме постоянно случается что-то странное. Похоже придётся вызвать экзорцистов, или охотников на приведений."
        book_seller "Какое совпадение! Я являюсь дипломированным эспером! Могу помочь вам провести обряд очищения дома."


    call screen home



label not_kitchen:
    mc "{i}Думаю сначала схожу на чердак, оставлю вещи.{/i}"
    call screen home


