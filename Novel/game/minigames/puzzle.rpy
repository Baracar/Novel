screen drag_pieces():
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "dismiss" action NullAction()

    #add "images/present/fortune/floor.jpg"

    draggroup:

        drag:
            child "images/present/fortune/square.jpg"
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

label puzzle_pieces:

    $ can_move = False
    $ field_x_pos = 0
    $ field_y_pos = 0
    # list of pieces
    $ pieces_list =[
        {"ind":0, "img":"present/fortune/0_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":1, "img":"present/fortune/1_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":2, "img":"present/fortune/2_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":3, "img":"present/fortune/3_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":4, "img":"present/fortune/4_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":5, "img":"present/fortune/5_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":6, "img":"present/fortune/6_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":7, "img":"present/fortune/7_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":8, "img":"present/fortune/8_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":9, "img":"present/fortune/9_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":10, "img":"present/fortune/10_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":11, "img":"present/fortune/11_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":12, "img":"present/fortune/12_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":13, "img":"present/fortune/13_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        {"ind":14, "img":"present/fortune/14_drag.png", "x_pos":0, "y_pos":0, "placed": False},
        ] # "ind" is an index of the item in the list, so we can use it later

    # list of corresponding places ("ind" value does matter)
    $ places_list = [
        {"ind":0, "img":"present/fortune/0_drop.png", "x_pos":762, "y_pos":746},
        {"ind":1, "img":"present/fortune/1_drop.png", "x_pos":752, "y_pos":0},
        {"ind":2, "img":"present/fortune/2_drop.png", "x_pos":966, "y_pos":502},
        {"ind":3, "img":"present/fortune/3_drop.png", "x_pos":759, "y_pos":571},
        {"ind":4, "img":"present/fortune/4_drop.png", "x_pos":982, "y_pos":336},
        {"ind":5, "img":"present/fortune/5_drop.png", "x_pos":986, "y_pos":199},
        {"ind":6, "img":"present/fortune/6_drop.png", "x_pos":750, "y_pos":143},
        {"ind":7, "img":"present/fortune/7_drop.png", "x_pos":1236, "y_pos":440},
        {"ind":8, "img":"present/fortune/8_drop.png", "x_pos":1112, "y_pos":176},
        {"ind":9, "img":"present/fortune/9_drop.png", "x_pos":1322, "y_pos":578},
        {"ind":10, "img":"present/fortune/10_drop.png", "x_pos":1605, "y_pos":652},
        {"ind":11, "img":"present/fortune/11_drop.png", "x_pos":1466, "y_pos":226},
        {"ind":12, "img":"present/fortune/12_drop.png", "x_pos":1620, "y_pos":0},
        {"ind":13, "img":"present/fortune/13_drop.png", "x_pos":1348, "y_pos":0},
        {"ind":14, "img":"present/fortune/14_drop.png", "x_pos":1222, "y_pos":0},
        ]

    # sets random coordinates for pieces
    python:
        for piece in pieces_list:
            pieces_list[piece["ind"]]["x_pos"] = renpy.random.randint(10, 320)
            pieces_list[piece["ind"]]["y_pos"] = renpy.random.randint(10, 720)

    show screen drag_pieces
    $ can_move = True
    "Place images."
    $ can_move = False
    $ renpy.pause(1.0)
    hide screen drag_pieces
    return

label drag_quit:
    $ can_move = False
    "so long...{w=1.0}{nw}"
    hide screen drag_drop_scr
    return