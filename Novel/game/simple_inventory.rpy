## КАК ПОЛЬЗОВАТЬСЯ:

# показать картинку id на экране в виде кликабельного спрайта по координатам x, y
# $ ishow("iposter", 111, 111)

# показать экран с кнопкой, которая показывает/прячет инвентарь
# show screen inventory_button

# всё. можно собирать предметы. их id (они же имена спрайтов) будут храниться в списке inventory

# в словарь items нужно добавить все имена предметов:
# items = {
    # "ipicture": _("Картина"),
    # "iposter": _("Постер")
# }

# если нужно сымитировать подбирание предмета iposter без клика по нему:
# $ iclick("iposter")

# переводим в action после возможной замены функции на свою
init 444 python:
    IClickSlot = renpy.curry(iclick_slot)

# можно написать свою функцию для обработки кликов по предметам
# init -4 python:
#     def iclick_slot(id):
#         renpy.notify(_("Это ") + items[id][0] + ".")
#     IClickSlot = renpy.curry(iclick_slot)

# можно добавить комментарии при собирании предметов, что вызывается из iclick(id):
init -4 python:
    def iclick_item(id):
        renpy.notify(_("Вы получили предмет: ") + items[id] + ".")

## НАСТРОЙКИ
init -5 python:
    # звук клика по предмету
    inventory_sound = None

    # папка с картинками для инвентаря
    ipath = "Items"

    # размеры слота в инвентаре
    slot_w = 200
    slot_h = 200

    # расстояние между слотами
    slot_spacing = 5

    # пустое место вокруг предметов в слотах
    slot_xpadding = 5
    slot_ypadding = 5

    # ширина окошка инвентаря
    iwidth = config.screen_width*8//10

init offset = -2

## СТИЛИ ДЛЯ ЭКРАНОВ И КОНОПОК ИНВЕНТАРЯ (МОЖНО МЕНЯТЬ)
# рамка экрана инвентаря
style inventory_main_frame is empty:
    # фон
    background Frame("#4448", 0, 0)

    # ширина
    xsize iwidth

    # положение
    align(.5, .0)

# рамка слота инвентаря
style inventory_frame is empty:
    # фон
    background Frame("#fff2", 0, 0)

    # размеры
    xysize(slot_w, slot_h)

## ДАЛЕЕ ЛУЧШЕ НИЧЕГО НЕ МЕНЯТЬ
init -5 python:
    # заглушка словаря названий для предметов
    # id - это ещё и спрайт
    items = {
        # "ipicture": _("Картина"),
        # "iposter": _("Постер")
    }

    # список id всех предметов в инвентаре
    inventory = [ ]

init -5:
    # для вывода предметов на локации
    transform pos(x, y, t=.25, b=.15):
        pos (x, y)

    # для реакции на наведение курсора
    transform hover_at(t=.25, b=.15):
        on idle:
            ease t matrixcolor BrightnessMatrix(0)

        # плавное подсвечивание при наведении
        on hover:
            ease t matrixcolor BrightnessMatrix(b)

# экран с кнопкой инвентаря
screen inventory_button:
    imagebutton idle "inventory_button" xalign 1. focus_mask True at hover_at action ToggleScreen()

# экран инвентаря
screen inventory:
    # рамочка для слотов
    frame:
        style "inventory_main_frame"

        style_prefix "inventory"

        # сетка с прокруткой
        vpgrid:
            rows 1
            scrollbars "horizontal"
            # убрать скроллбар, пока в нём нет нужды (но место под него останется)
            scrollbar_unscrollable "hide"
            mousewheel True
            draggable True
            pagekeys True

            if not inventory:
                hbox:
                    frame background None
                    null width slot_spacing

            # слоты
            for id in inventory:
                hbox:
                    frame:
                        # кликабельный предмет в слоте
                        imagebutton idle islot(id) at hover_at align(.5, .5) action IClickSlot(id) activate_sound  inventory_sound

                    null width slot_spacing

init -5 python:
    # вписываем миниатюры предметов в пределы слотов
    def islot(id):
        id = ipath + " " + id
        w, h = renpy.render(renpy.displayable(id), config.screen_width, config.screen_height, 0, 0).get_size()
        z = min((slot_w - slot_xpadding * 2) / w, (slot_h - slot_xpadding * 2) / h)
        if z >= 1.: return id
        return Transform(id, zoom=z)

    # показать/скрыть экран
    def toggle_screen(screen="inventory"):
        if renpy.get_screen(screen):
            renpy.hide_screen(screen)

        else:
            renpy.show_screen(screen)

        renpy.transition(dissolve)
        renpy.restart_interaction()

    ToggleScreen = renpy.curry(toggle_screen)

    # показать предмет на локации в виде кнопки
    def ishow(id, x=.5, y=.5):
        # показываем только те предметы, которых ещё нет в инвентаре
        if not id in inventory:
            # показываем в нужной позиции и с реакцией на наведение курсора
            renpy.show(id, what=ImageButton(id, clicked=IClick(id), focus_mask=True, activate_sound=inventory_sound), at_list=[ hover_at, pos(x, y) ])
            renpy.restart_interaction()

    # заглушка для комментариев при собирании предметов
    def iclick_item(id):
        pass

    # подобрать предмет с локации, поместить в инвентарь, если там ещё нет такого предмета
    def iclick(id):
        global inventory

        if not id in inventory: inventory.append(id)

        renpy.hide(id)
        renpy.transition(dissolve)
        renpy.restart_interaction()

        iclick_item(id)

    IClick = renpy.curry(iclick)

    def iremove(id):
        if id in inventory: inventory.remove(id)

    IRemove = renpy.curry(iremove)

    def icontains(id):
        return id in inventory

    IContains = renpy.curry(icontains)

    # клик по предмету в инвентаре
#     def iclick_slot(id):
#         pass

#     IClickSlot = renpy.curry(iclick_slot)
