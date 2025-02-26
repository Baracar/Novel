init:
# Items - картинка в инвентаре, Descr - картинка с описанием
    image Items milk_jar = Image("images/Items/milk_jar.png")
    image Descr milk_jar = Image("images/Items/info milk jar.png")
    image Items book_myth = Image("images/Items/myph_kzn_book.jpg")
    image Descr book_myth = Image("images/Items/info book.png")
    image Items photo_child = Image("images/Items/photo_baby.png")
    image Descr photo_child = Image("images/Items/photo_baby.png")
    image Items toy_car = Image("images/Items/toy_auto.png")
    image Descr toy_car = Image("images/Items/toy_auto.png")
    image Items bill_electricity = Image("images/Items/electricity_bill.png")
    image Descr bill_electricity = Image("images/Items/electricity_bill.png")
    image Items newspaper = Image("images/Items/newspaper.png")
    image Descr newspaper = Image("images/Items/info newspaper.png")
    image Items kefir = Image("images/Items/kefir_bottle.png")
    image Descr kefir = Image("images/Items/kefir_bottle.png")
    image Items poster_edge = Image("images/Items/poster_edge.png")
    image Descr poster_edge = Image("images/Items/poster_edge.png")
    image Items coin = Image("images/Items/coin.png")
    image Descr coin = Image("images/Items/coin.png")
    image Items old_papers = Image("images/Items/old_papers.png")
    image Descr old_papers = Image("images/Items/old_papers.png")
    image Items dirty_cup = Image("images/Items/dirty_cup.png")
    image Descr dirty_cup = Image("images/Items/dirty_cup.png")
    image Items child_craft = Image("images/Items/child_craft.jpg")
    image Descr child_craft = Image("images/Items/child_craft.jpg")
    image Items father_info = Image("images/Items/file_father.png")
    image Descr father_info = Image("images/Items/file_father.png")
    image Items grandma_info = Image("images/Items/file_abi.png")
    image Descr grandma_info = Image("images/Items/file_abi.png")

init python:
#     class item:
#         def __init__(self, name, image, desc):
#             self.name = name
#             self.image = image
#             self.desc = desc

    items = {
    "milk_jar": _("Молочник"),
    "book_myth": _("Книга \"Мифология Казанских татар\""),
    "photo_child": _("Фото ребёнка в костюме зайки"),
#     "toy_car": _("Старая игрушечная машинка"),
    "bill_electricity": _("Счета за электричество"),
    "newspaper": _("Свежая газета"),
    "kefir": _("Полупустая бутылка кефира"),
    "poster_edge": _("Кусок плаката"),
    "coin": _("Монета 10 сум"),
    "old_papers": _("Макулатура"),
    "dirty_cup": _("Грязная кружка"),
    "child_craft": _("Детская поделка"),
    "father_info": _("Папа"),
    "grandma_info": _("Эби")
    }

#     milk_jug = item("Молочник", "images/Items/milk_jug.png", "Глиняный кувшин в котором эби хранила молоко, купленное у соседки. Сейчас пустой.")
#     book_myth = item("книга \"Мифология Казанских татар\"", "images/Items/myph_kzn_book.png", " Бичура не причиняет никакого существенного вреда человеку ... беспокоит его ночью: кричит, играет, смеется, шутит, спящего перетаскивает с места на место; вещи, положенные в одно место, прячет в другое. ...Шурале -  Занимается тем, что сбивает одиноко идущих по лесу людей с пути, заманивает в глухие чащи; способен защекотать до смерти своими длинными пальцами. ...Су анасы представлялась красивой девушкой с длинными зеленоватыми волосами, которая сидела на берегу и золотым гребнем расчесывала свои волосы. ...Албасты — скитающаяся душа человека, умершего в результате несчастного случая и мученической смертью, или похороненного без соблюдения погребальных обрядов. Например, он может быть заблудшей душой или душой утопленника.")
#     photo_child = item("Фото ребёнка в костюме зайки", "images/Items/photo_baby.png", "Детское фото отца с надписью \"3ай\"")
#     toy_car = item("Старая игрушечная машинка", "images/Items/toy_auto.png", "Папина любимая детская игрушка, которую он думал, что безвозвратно потерял. Нашлась в сейфе.")
#     bill_electricity = item("Счета за электричество", "images/Items/electricity_bill.png", "Неоплаченные счета за электричество. Предупреждение об отключении за неуплату.")
#     newspaper = item("Свежая газета", "images/Items/newspaper.png", "Местная бесплатная газета. Дата выпуска: Вчера. На главной странице уведомление, что в связи с обновлением сотовых вышек пару дней в центре города временами не будет работать сотовая связь. Так же колонка с погодой: Завтра вечером ожидается гроза. Другая колонка: очевидцы сообщают, что статуи кота Казанского нет на постаменте!")
#     kefir = item("Полупустая бутылка кефира", "images/Items/kefir_bottle.png", "Куплена папой вчера. Любит пить кефир перед сном.")
#     poster_edge = item("Кусок плаката", "images/Items/poster_edge.png", "От руки написано \"Ай - с тат. месяц\"")
#     coin = item("Монета 10 сум", "images/Items/coin.png", "Монета в 10 сум")

    # все существующие в игре предметы с их названиями
#     items = {
#         "milk_jug": _(["Молочник", "images/Items/milk_jug.png", "Глиняный кувшин в котором эби хранила молоко, купленное у соседки. Сейчас пустой."]),
#         "book_myth": _(["Книга \"Мифология Казанских татар\"", "images/Items/myph_kzn_book.jpg", "Бичура не причиняет никакого существенного вреда человеку ... беспокоит его ночью: кричит, играет, смеется, шутит, спящего перетаскивает с места на место; вещи, положенные в одно место, прячет в другое. ...Шурале -  Занимается тем, что сбивает одиноко идущих по лесу людей с пути, заманивает в глухие чащи; способен защекотать до смерти своими длинными пальцами. ...Су анасы представлялась красивой девушкой с длинными зеленоватыми волосами, которая сидела на берегу и золотым гребнем расчесывала свои волосы. ...Албасты — скитающаяся душа человека, умершего в результате несчастного случая и мученической смертью, или похороненного без соблюдения погребальных обрядов. Например, он может быть заблудшей душой или душой утопленника."]),
#         "photo_child": _(["Фото ребёнка в костюме зайки", "images/Items/photo_baby.png", "Детское фото отца с надписью \"3ай\""]),
#         "toy_car": _(["Старая игрушечная машинка", "images/Items/toy_auto.png", "Папина любимая детская игрушка, которую он думал, что безвозвратно потерял. Нашлась в сейфе."]),
#         "bill_electricity": _(["Счета за электричество", "images/Items/electricity_bill.png", "Неоплаченные счета за электричество. Предупреждение об отключении за неуплату."]),
#         "newspaper": _(["Свежая газета", "images/Items/newspaper.png", "Местная бесплатная газета. Дата выпуска: Вчера. На главной странице уведомление, что в связи с обновлением сотовых вышек пару дней в центре города временами не будет работать сотовая связь. Так же колонка с погодой: Завтра вечером ожидается гроза. Другая колонка: очевидцы сообщают, что статуи кота Казанского нет на постаменте!"]),
#         "kefir": _(["Полупустая бутылка кефира", "images/Items/kefir_bottle.png", "Куплена папой вчера. Любит пить кефир перед сном."]),
#         "poster_edge": _(["Кусок плаката", "images/Items/poster_edge.png", "От руки написано \"Ай - с тат. месяц\""]),
#         "coin": _(["Монета 10 сум", "images/Items/coin.png", "Монета в 10 сум"]),
#         "father_info": _(["Папа", "images/Items/file_father.png", "Имя: Роберт. Дата рождения: 1 января 1980. Лактозная непереносимость. Не любит мыть посуду. С вечера приехал в дом. Должность: папа"]),
#         "grandma_info": _(["Эби", "images/Items/file_abi.png", "Энергичная эби, которая излишне опекала своего сына, делала уборку в его комнате по ночам. Выкидывала без спроса вещи, которые, по её мнению, ему больше не нужны. Не верила в аллергию на молоко и постоянного поила его чаем с молоком - от горла."])
#     }

    # заменим стандартный обработчик кликов по слотам на свой
    # вместо сообщения будем показывать постеры в центре экрана
    def iclick_slot(id):
        store.iclicked_id = "Descr " + id
#         store.item_desc = items[id][2]
        # нужно создать свой label или использовать уже готовый, как здесь
        renpy.call_in_new_context ("iclick_slot")



default iclicked_id = None

# показать предмет при клике по нему в слоте
label iclick_slot:
#     if not iclicked_id:
#         return

    window hide
    show screen description

    $ renpy.transition(dissolve)
    $ renpy.restart_interaction()

    pause

    $ renpy.transition(dissolve)
    return


screen description:
    modal True
#     text "[item_desc]" size 50 xalign 0.5 yalign 0.32
#     textbutton "Close" xalign 0.5 yalign 0.45 action Hide("description")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle iclicked_id
        action Hide("description")

#     class milk_jug:
#         name = "Молочник"
#         image = "images/Items/milk_jug.png"
#         desc = "Глиняный кувшин в котором эби хранила молоко, купленное у соседки. Сейчас пустой."














