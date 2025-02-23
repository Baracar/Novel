screen drag_pieces():
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "dismiss" action NullAction()

    #add "images/present/fortune/floor.jpg"

    draggroup:

        drag:
            child "puzzle/attic/background.png"
            xpos field_x_pos ypos field_y_pos
            draggable False
            droppable False

        for place in places_list:
            drag:
                drag_name place["ind"]
                child place["img"]
                draggable False
                xpos (field_x_pos + place["x_pos"]) ypos (field_y_pos + place["y_pos"])

        for piece in pieces_list:
            drag:
                drag_name piece["ind"] # use "ind" as the name
                child piece["img"]
                dragged piece_dragged
                draggable can_move
                xpos piece["x_pos"] ypos piece["y_pos"]
                #mouse_drop True # try and see if it behave better


init python:
    def piece_dragged(drags, drop):
        if not drop:
            return

        if drop.drag_name == drags[0].drag_name:
            if abs(drags[0].x - drop.x) < 10 and abs(drags[0].y - drop.y) < 10:
                i = drags[0].drag_name # 'cause we used "ind" as a name of draggable piece
                drags[0].snap(drop.x, drop.y, delay=0.1)
                store.pieces_list[i]["placed"] = True
                store.pieces_list[i]["x_pos"] = drop.x
                store.pieces_list[i]["y_pos"] = drop.y
                drags[0].draggable = False # sets placed piece undraggable

                for piece in pieces_list:
                    if not piece["placed"]:
                        return

                return True

        return

label puzzle_pieces(number):
    $ can_move = False
    $ field_x_pos = 0
    $ field_y_pos = 0
    if number == 1:
    # list of pieces
        $ pieces_list =[
            {"ind":0, "img":"puzzle/attic/piece-1.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":1, "img":"puzzle/attic/piece-2.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":2, "img":"puzzle/attic/piece-3.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":3, "img":"puzzle/attic/piece-4.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":4, "img":"puzzle/attic/piece-5.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":5, "img":"puzzle/attic/piece-6.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":6, "img":"puzzle/attic/piece-7.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":7, "img":"puzzle/attic/piece-8.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":8, "img":"puzzle/attic/piece-9.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":9, "img":"puzzle/attic/piece-10.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":10, "img":"puzzle/attic/piece-11.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":11, "img":"puzzle/attic/piece-12.png", "x_pos":0, "y_pos":0, "placed": False},
            ]
        $ places_list = [
            {"ind":0, "img":"puzzle/attic/piece-1.png", "x_pos":500, "y_pos":50},
            {"ind":1, "img":"puzzle/attic/piece-2.png", "x_pos":736, "y_pos":50},
            {"ind":2, "img":"puzzle/attic/piece-3.png", "x_pos":925, "y_pos":50},
            {"ind":3, "img":"puzzle/attic/piece-4.png", "x_pos":500, "y_pos":217},
            {"ind":4, "img":"puzzle/attic/piece-5.png", "x_pos":658, "y_pos":318},
            {"ind":5, "img":"puzzle/attic/piece-6.png", "x_pos":700, "y_pos":488},
            {"ind":6, "img":"puzzle/attic/piece-7.png", "x_pos":796, "y_pos":538},
            {"ind":7, "img":"puzzle/attic/piece-8.png", "x_pos":500, "y_pos":584},
            {"ind":8, "img":"puzzle/attic/piece-9.png", "x_pos":776, "y_pos":773},
            {"ind":9, "img":"puzzle/attic/piece-10.png", "x_pos":500, "y_pos":817},
            {"ind":10, "img":"puzzle/attic/piece-11.png", "x_pos":743, "y_pos":958},
            {"ind":11, "img":"puzzle/attic/piece-12.png", "x_pos":921, "y_pos":888},
            ]
    elif number == 2:
        $ pieces_list =[
            {"ind":0, "img":"present/fortune/0_drag.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":1, "img":"present/fortune/1_drag.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":2, "img":"present/fortune/2_drag.png", "x_pos":0, "y_pos":0, "placed": False},
            ]
        $places_list = [
            {"ind":0, "img":"present/fortune/0_drop.png", "x_pos":762, "y_pos":746},
            {"ind":1, "img":"present/fortune/1_drop.png", "x_pos":752, "y_pos":0},
            {"ind":2, "img":"present/fortune/2_drop.png", "x_pos":966, "y_pos":502},
            ]


    # sets random coordinates for pieces
#     python:
#         for piece in pieces_list:
#             pieces_list[piece["ind"]]["x_pos"] = renpy.random.randint(10, 320)
#             pieces_list[piece["ind"]]["y_pos"] = renpy.random.randint(10, 720)

    show screen drag_pieces
    $ can_move = True
    #ADD TEXT тест во время решения бумажек
    pause
    $ can_move = False
    $ renpy.pause(1.0)
    hide screen drag_pieces
    if number == 1:
        call attic_puzzle
    else:
        call attic_puzzle

label drag_quit:
    $ can_move = False
    "so long...{w=1.0}{nw}"
    hide screen drag_drop_scr
    return