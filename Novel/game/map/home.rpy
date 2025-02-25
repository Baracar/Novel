image home = im.Scale("locations/home/bg.png", 1920, 1080)

default first_visit_home = True
default street_open = False

default photo = False
default safe = False

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
    if not photo:
        imagebutton:
            idle im.Scale("locations/home/photo baby.png", 77, 56.53125)
            hover im.Scale("locations/home/photo baby white.png", 77, 56.53125)
            xpos 274
            ypos 188
            action Jump("tetris_start")
    if not photo:
        imagebutton:
            idle im.Scale("locations/home/safe.png", 140, 140.90625)
            hover im.Scale("locations/home/safe white.png", 140, 140.90625)
            xpos 672
            ypos 230
            action Jump("tetris_start")

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
        book_seller "Извините, я заработался в своей лавке и пропустил автобус. Мой телефон не ловит. "
        book_seller "Будьте добры, я закажу такси с вашего стационарного телефона? "
        father "Конечно."
        book_seller "Спасибо. *набирает номер* Здравствуйте, такси? Можно заказать по адресу… Из-за плохой погоды заказы не принимаете?"
        father "До свидания. Что ж, пожалуй вернусь в лавку, пережду дождь там."
        father "Вы что! Оставайтесь у нас, если что постелим вам на полу. Я где-то видел в шкафах матрас и постельное бельё…"
        book_seller "Вы так добры!"
        father "Кстати, мы так и не представились. Я - Роберт, а это мой сын - …"
        book_seller "А меня… Су… нет, не так. Иясе…"
        father "Я плохо расслышал, вас зовут Ияс?"
        book_seller "А, да-да, меня зовут Ияс."
        $book_seller_name = "Ияс"
        father "Надеюсь вы не боитесь привидений. А то в доме постоянно случается что-то странное. "
        father "Похоже придётся вызвать экзорцистов, или охотников на приведений."
        book_seller "Какое совпадение! Я являюсь дипломированным эспером! Могу помочь вам провести обряд очищения дома."
        father "Замечательно!"
        book_seller "Обряд проходит в виде суда над пэри. Роберт, как и в любом суде вам нужен адвокат. Думаю ваш сын с этим справится."
        father "Отлично."
        book_seller "Но и для пэри тоже нужен адвокат… Но у нас не хватает людей…"
        mc "Я могу с этим справиться."
        book_seller "Обычно так нельзя делать, но у нас дефицит в кандидатах. Вы сможете объективно рассмотреть дело с обеих сторон?"
        mc "Думаю что справлюсь."
        book_seller "Что-ж, приступим. Роберт, расскажите в общих чертах, что происходит."
        father "В этом доме жила моя мать. Недавно она умерла, и дом отошел по наследству моей семье."
        father "Вчера вечером я приехал сюда, чтобы утром встретить грузовик. "
        father "Приехал, разгрузил продукты в холодильник, выпил кефир перед сном и пошел спать."
        father "На утро пошел на кухню, взял чистую кружку со стола. "
        father "Кинул пару ложек кофе  и как только залил кипятком - зазвонил городской телефон. "
        father "Диспетчер сообщил, что водитель грузовика пропал."
        father "Затем пришёл сын. Я пошел на кухню за своим кофе, а там меня ждала мерзкая отрава - кофе с молоком!"
        father "У меня сильная непереносимость лактозы. Если не сын, то остается пенять на злой дух старой бабки!"
        book_seller "Я.. Всё понял… Хмм, да, похоже на проделки мистического существа. "
        book_seller "Дайте-ка вспомнить, на какое пэри это похоже… Совсем забыл название…"
        menu first_judge:
            "Кикимора?":
                book_seller "Похоже на её проделки. Но ведь покойная была татаркой? Думаю это другая сущность."
                jump first_judge
            "Домовой?":
                book_seller "Похоже на его дела. Но ведь в доме умерла эби, а не бабай. Думаю не он."
                jump first_judge
            "Шурале?":
                book_seller "Хм. Насколько я помню, это лесной дух, который щекочет заблудившихся в лесу путников до смерти. Не думаю."
                jump first_judge
            "Су Анасы?":
                book_seller "Бабушка же не утонула. Думаю это не подходит."
                jump first_judge
            "Бичура?":
                book_seller "Точно! Очень подходит!"
        mc "*Какой-то необразованный этот экзорцист…*"
        book_seller "Теперь задам вопросы к адвокату. Сейчас вы должны объяснить, почему это проделки Бичуры."
        book_seller "Почему Бичура налила молоко в чашку сыну?"
        menu judge1_1:
            "Любила молоко":
                mc "Она очень любила пить чай с молоком."
                mc "Она даже покупала деревенское молоко и пользовалась старинным молочником. Магазинное молоко презирала."
                book_seller "Да, но в самом молочнике молока нет."
                mc "Хм, действительно. Мне нужно подумать."
                jump judge1_1
            "Не знала об аллергии":
                mc "Как человек, который рос и долгое время жил в деревне, она не могла поверить, что на молоко может быть аллергия."
                mc "Добавить молоко в чай - жест заботы с её стороны."
                book_seller "Думаю звучит правдоподобно."
        book_seller "Роберт, были ли ещё какие-то странности, которые можно связать с нечистой силой?"
        father "Безусловно! Пэри разбушевался, и посреди лета нагрянула гроза!"
        father "А перед тем как вы пришли у нас отключилось электричество."
        father "Погодите-ка, если отключили электричество, то почему работает городской телефон?"
        father "Вот ещё одно доказательство потустороннего!"
        book_seller "Хорошо. Есть ли другие версии произошедшего?"
        mc "Думаю у этого всего есть логическое объяснение."
        book_seller "Хорошо, выслушаем. Роберт, расскажите ещё раз, как всё происходило."
        book_seller "А ты дай знать, если есть альтернативное объяснение."
        father "Итак."
        father "В этом доме жила моя мать. "
        father "Недавно она умерла, и дом отошел по наследству моей семье."
        father "Вчера вечером я приехал сюда, чтобы утром встретить грузовик."
        father "Приехал, разгрузил продукты в холодильник, выпил кефир перед сном и пошел спать."
        menu:
            "Объяснить":
                book_seller "Есть какие-то замечания?"
                mc "Да. Вы сразу пошли спать?"
                father "Да, всё именно так и было."
                mc "Посуду не помыли?"
                father "Э-э-э… Не помню. Думаю к делу не относится!"
                mc "Я иного мнения, но продолжайте рассказ."
            "Промолчать":
                mc "..."
        father "На утро пошел на кухню, взял чистую кружку со стола. "
        menu:
            "Объяснить":
                book_seller "Есть какие-то замечания?"
                mc "Да. Она точно была чистой?"
                father "Я конечно не вглядывался, но выглядела как чистая белая кружка. "
            "Промолчать":
                mc "..."
        father "Кинул пару ложек кофе, и как только залил кипятком - зазвонил городской телефон."
        father "Из-за Бичуры здесь не работает сотовая связь."
        father "Поэтому я дал компании грузоперевозки номер городского телефона."
        menu:
            "Объяснить":
                book_seller "Есть какие-то замечания?"
                mc "Да. Почему вы уверены, что это Бичура виновна в неполадках со связью?"
                father "Не вижу других причин для этого."
                mc "А я думаю причина в этом:"
                menu judge1_2:
                    "Местная газета":
                        mc "Здесь указано, что в связи с модернизацией сотовых вышек в центре города не будет работать сотовая связь."
                        book_seller "Выходит пэри тут не причём. "
                    "Книга “Мифология Казанских Татар”":
                        book_seller "Но это подтверждает теорию с пэри."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_2
                    "Счета за электричество":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_2
                    "Кусок плаката":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_2
            "Промолчать":
                mc "..."
        father "Диспетчер сообщил, что водитель грузовика пропал. "
        menu:
            "Объяснить":
                menu judge1_3:
                    "Местная газета":
                        mc "Здесь указано, что в связи с модернизацией сотовых вышек в центре города не будет работать сотовая связь."
                        mc "Водитель грузовика не смог позвонить и уточнить адрес, и уехал на другой конец города."
                        book_seller "Выходит пэри тут не причём."
                    "Книга “Мифология Казанских Татар”":
                        book_seller "Но это подтверждает теорию с пэри."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_3
                    "Счета за электричество":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_3
                    "Кусок плаката":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_3
            "Промолчать":
                mc "..."
        father "Затем пришёл сын."
        menu:
            "Возразить":
                book_seller "Это было не так?"
                mc "Нет, простите, ошибся. Продолжай, пап."
            "Промолчать":
                mc "..."
        father "Я пошел на кухню за своим кофе, а там меня ждала мерзкая отрава - кофе с молоком!"
        menu:
            "Объяснить":
                "(вставка другого экземпляра с головоломкой с сейфом)"
                "В случае верного ответа продолжить, в случае неверного: book_seller Это не имеет смысла."
            "Промолчать":
                mc "..."
        father "Сын сходил в вашу букинистику и отнес макулатуру."
        father "Затем до вечера сидел у себя в комнате."
        father "Я всё это время смотрел телевизор в зале."
        father "Затем пэри разбушевался, и посреди лета нагрянула гроза!"
        menu:
            "Возразить":
                menu judge1_4:
                    "Местная газета":
                        mc "В газете писали, что будет аномальная гроза."
                        book_seller "Значит пэри тут не причём - гроза не началась внезапно, раз синоптики предупреждали об этом."
                    "Книга “Мифология Казанских Татар”":
                        book_seller "Но это подтверждает теорию с пэри."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_4
                    "Счета за электричество":
                        book_seller "Думаю, это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_4
                    "Кусок плаката":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_4
            "Промолчать":
                mc "..."
        father "А перед тем как вы пришли у нас отключилось электричество."
        menu:
            "Возразить":
                menu judge1_5:
                    "Местная газета":
                        book_seller "Думаю, это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_5
                    "Книга “Мифология Казанских Татар”":
                        book_seller "Но это подтверждает теорию с пэри."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_5
                    "Счета за электричество":
                        mc "В почтовом ящике я нашел неоплаченные счета. Нам просто отключили за неуплату."
                        book_seller "Да, похоже пэри тут не причём."
                    "Кусок плаката":
                        book_seller "Это не относится к делу."
                        mc "Хм, действительно. Мне нужно подумать."
                        jump judge1_5
            "Промолчать":
                mc "..."
        father "Погодите-ка, если отключили электричество, то почему работает городской телефон?"
        father "Вот ещё одно доказательство потустороннего!"
        menu:
            "Возразить":
                mc "Городской телефон работает от электричества городской станции. "
            "Промолчать":
                mc "..."
         
        
#         Если есть хоть один неправильный ответ -
#         book_seller "Но ты не смог всё объяснить. "
#         book_seller "Роберт, расскажите ещё раз, как всё происходило. А ты дай знать, если есть альтернативное объяснение."


    call screen home

# label first_judge:
#     menu:


label not_kitchen:
    mc "{i}Думаю сначала схожу на чердак, оставлю вещи.{/i}"
    call screen home


