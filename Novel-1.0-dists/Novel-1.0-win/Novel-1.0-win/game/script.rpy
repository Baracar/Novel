#персонажи
define mc = Character('Вы', color="#c8ffc8")
define father = Character('Отец', color="#008000")
define book_sealer = Character('Продавец книг', color="#8b00ff")

#спрайты гг
image mc_neutral = "mc/mc_neutral.png"

#фоны
image house = "bg/house.jpg"
image room = "bg/room.jpg"
image lake = "bg/lake.jpg"

#переменные
default location = 'home'

#старотовая позиция
label start:
    scene house
    jump street













    "Вы прибываете в домик, который стал вашим новым жилищем. Все вокруг кажется каким-то давно забытым, как будто время здесь остановилось."

    show mc_neutral
    with dissolve
    mc "Давно я тут не был..."

    scene room
    show mc_neutral
    with dissolve
  
    "Старые фотографии, запах сырости, и телевизор, который кажется отображает лишь кусочек прошлого. Но вам нужно привыкнуть к этому новому месту."
    mc "Чем бы сперва заняться: убраться дома или проведать окресности?"

    menu:
        "Навести порядок.":
            jump clean
        "Прогуляться.":
            $location = 'home'
            call screen idleScreen
    return

label clean:
    "Вы решаете разобраться с вещами в доме, чтобы сделать его более уютным. Начнем с того, чтобы найти место для своих вещей и, возможно, немного привести в порядок кухню."

    while len(found_items) < 3:
        call screen trash


## уборка
screen trash:
    # Носки
    if "носки" not in found_items:
        imagebutton:
            idle "trash/socks.png"
            xpos 100
            ypos 800
            action Function(found_item, "носки")  

    # Мусор
    if "мусор" not in found_items:
        imagebutton:
            idle "trash/garbage.png"
            xpos 1500
            ypos 750
            action Function(found_item, "мусор")  

    # Плесень
    if "плесень" not in found_items:
        imagebutton:
            idle "trash/mold.png"
            xpos 1200
            ypos 400
            action Function(found_item, "плесень")  

    text "Найдите все предметы!" xpos 10 ypos 10


    


init python:
    found_items = []

    def found_item(item_name):
        if item_name not in found_items:
            found_items.append(item_name)
            renpy.notify(f"Вы убрали {item_name}")
        
        # Если все 3 предмета найдены
        if len(found_items) == 3:
            renpy.notify("Вы закончили уборку! Дома теперь куда уютнее!")
            renpy.jump("work_in_progress")






## озеро
label lake:
    $ lakeVisited = True
    scene house
    show mc_neutral
    mc "Лучше схожу на прогулку, интересно, как многое тут успело измениться."
    "Вы решаете покинуть домик и прогуляться по окрестностям. Ведь, может быть, что-то интересное или полезное окажется неподалеку."
    "Вы выходите на улицу и направляетесь к парку с озером, который находится неподалеку от вашего нового дома"
    scene lake
    show mc_neutral

    $location = 'lake'
    call screen idleScreen

default homeVisited = True
label homeSecond:
    scene room
    "Вы снова дома"
    $location = 'home'
    call screen idleScreen


default lakeVisited = False
label lakeSecond:
    scene lake
    "Вы снова на озере"
    $location = 'lake'
    call screen idleScreen


label work_in_progress:
    "В разработке."
    return