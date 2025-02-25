screen drag_pieces():
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "dismiss" action NullAction()

    add "puzzle/attic/background.png"

    draggroup:

        drag:
            child "puzzle/puzzle-frame.png"
            xpos field_x_pos - 6 ypos field_y_pos - 6
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
        delta = 50
        if drop.drag_name == drags[0].drag_name:
            if abs(drags[0].x - drop.x) < delta and abs(drags[0].y - drop.y) < delta:
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
    $ field_x_pos = 600
    $ field_y_pos = 25
    if number == "desk":
    # list of pieces
        $ pieces_list =[
            {"ind":0, "img":"puzzle/attic_desk/piece-1.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":1, "img":"puzzle/attic_desk/piece-2.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":2, "img":"puzzle/attic_desk/piece-3.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":3, "img":"puzzle/attic_desk/piece-4.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":4, "img":"puzzle/attic_desk/piece-5.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":5, "img":"puzzle/attic_desk/piece-6.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":6, "img":"puzzle/attic_desk/piece-7.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":7, "img":"puzzle/attic_desk/piece-8.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":8, "img":"puzzle/attic_desk/piece-9.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":9, "img":"puzzle/attic_desk/piece-10.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":10, "img":"puzzle/attic_desk/piece-11.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":11, "img":"puzzle/attic_desk/piece-12.png", "x_pos":0, "y_pos":0, "placed": False},
            ]
    elif number == "closet":
        $ pieces_list =[
            {"ind":0, "img":"puzzle/attic_closet/piece-1.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":1, "img":"puzzle/attic_closet/piece-2.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":2, "img":"puzzle/attic_closet/piece-3.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":3, "img":"puzzle/attic_closet/piece-4.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":4, "img":"puzzle/attic_closet/piece-5.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":5, "img":"puzzle/attic_closet/piece-6.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":6, "img":"puzzle/attic_closet/piece-7.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":7, "img":"puzzle/attic_closet/piece-8.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":8, "img":"puzzle/attic_closet/piece-9.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":9, "img":"puzzle/attic_closet/piece-10.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":10, "img":"puzzle/attic_closet/piece-11.png", "x_pos":0, "y_pos":0, "placed": False},
            {"ind":11, "img":"puzzle/attic_closet/piece-12.png", "x_pos":0, "y_pos":0, "placed": False},
            ]
    $ places_list = [
        {"ind":0, "img":"puzzle/empty.png", "x_pos":0, "y_pos":0},
        {"ind":1, "img":"puzzle/empty.png", "x_pos":236, "y_pos":0},
        {"ind":2, "img":"puzzle/empty.png", "x_pos":425, "y_pos":0},
        {"ind":3, "img":"puzzle/empty.png", "x_pos":0, "y_pos":167},
        {"ind":4, "img":"puzzle/empty.png", "x_pos":228, "y_pos":144},
        {"ind":5, "img":"puzzle/empty.png", "x_pos":173, "y_pos":318},
        {"ind":6, "img":"puzzle/empty.png", "x_pos":281, "y_pos":328},
        {"ind":7, "img":"puzzle/empty.png", "x_pos":0, "y_pos":534},
        {"ind":8, "img":"puzzle/empty.png", "x_pos":242, "y_pos":592},
        {"ind":9, "img":"puzzle/empty.png", "x_pos":0, "y_pos":766},
        {"ind":10, "img":"puzzle/empty.png", "x_pos":299, "y_pos":832},
        {"ind":11, "img":"puzzle/empty.png", "x_pos":531, "y_pos":692},
        ]


    # sets random coordinates for pieces
    python:
        for piece in pieces_list:
            if piece["ind"] % 2 == 0:
                pieces_list[piece["ind"]]["x_pos"] = renpy.random.randint(10, 250)
            else:
                pieces_list[piece["ind"]]["x_pos"] = renpy.random.randint(10, 250) + 1350
            pieces_list[piece["ind"]]["y_pos"] = renpy.random.randint(10, 720)

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