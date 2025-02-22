init python:
    def create_blocks():
        global block_sprites
        #Reset puzzle first
        for block in block_sprites:
            # Destroy each sprite in the sprites list.
            block.destroy()
        block_sprites = [] # Emptying the sprites list.
        block_SM.redraw(0) # Redraw the spritemanager to update it.
        # Create puzzle
        if current_puzzle == 1: # Puzzle 1
            #Row 1
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type ="sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 277
            block_sprites[-1].y = 87
            block_sprites[-1].initial_pos = [227, 87]

            block_sprites.append(block_SM.create(long_h_block))
            block_sprites[-1].type = "lh"
            block_sprites[-1].size = long_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 427
            block_sprites[-1].y = 87
            block_sprites[-1].initial_pos =[427, 87]

            #Row 2
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type = "sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 578
            block_sprites[-1].y = 237
            block_sprites[-1].initial_pos = [578, 237]
            #Row3
            block_sprites.append(block_SM.create(red_block))
            block_sprites[-1].type = "red"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x =277
            block_sprites[-1].y = 390
            block_sprites[-1].initial_pos = [277, 390]
            #Row4
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type = "sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 125
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos =[125, 540]

            block_sprites.append(block_SM.create(long_v_block))
            block_sprites[-1].type = "lv"
            block_sprites[-1].size = long_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 427
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos =[427, 540]

            block_sprites.append(block_SM.create(long_v_block))
            block_sprites[-1].type = "lv"
            block_sprites[-1].size = long_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 882
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos =[882, 540]
            #Row5
            block_sprites.append(block_SM.create(short_h_block))
            block_sprites[-1].type = "sh"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 578
            block_sprites[-1].y = 692
            block_sprites[-1].initial_pos =[578, 692]
            #Row 6
            block_sprites.append(block_SM.create(short_h_block))
            block_sprites[-1].type = "sh"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 125
            block_sprites[-1].y = 843
            block_sprites[-1].initial_pos =[125, 843]
            #Goal
            block_sprites.append(block_SM.create(goal))
            block_sprites[-1].type = "goal"
            block_sprites[-1].x = puzzle_frame_pos[0] + puzzle_frame_size[0] - 15
            block_sprites[-1].y = 390
            block_sprites[-1].size = [15, 151]

    def blocks_update(st):
        global current_puzzle
        for b1, block in enumerate(block_sprites):
            if block.type != "goal" and block.drag:
                offset = 2
                if block.type == "lv" or block.type == "sv":
                    distance = click_pos[1] - renpy.get_mouse_pos()[1]
                    block.y = block.initial_pos[1] - distance
                    for b2, block2 in enumerate(block_sprites):
                        if b1 !=b2:
                            if block2.type != "goal" and (block.x - offset > block2.x and block.x + offset < block2.x + block2.size[0] or block.x + block.size[0] + offset < block2.x + block2.size[0]
                            and block.x + block.size[0] - offset > block2.x):
                                if block.y < block2.y + block2.size[1] and block.y > block2.y:
                                    block.y = block2.y + block2.size[1]
                                    block.initial_pos[1] = block.y
                                    click_pos[1] = renpy.get_mouse_pos()[1]
                                elif block.y + block.size[1] > block2.y and block.y + block.size[1] < block2.y + block2.size[1]:
                                    block.y = block2.y - block.size[1]
                                    block.initial_pos[1] = block.y
                                    click_pos[1] = renpy.get_mouse_pos()[1]
                            elif block.y < puzzle_frame_pos[1] + 15:
                                block.y = puzzle_frame_pos[1] + 15
                                block.initial_pos[1] = block.y
                                click_pos[1] = renpy.get_mouse_pos()[1]
                            elif block.y + block.size[1] > (puzzle_frame_pos[1] + puzzle_frame_size[1]) - 15:
                                block.y = (puzzle_frame_pos[1] + puzzle_frame_size[1]) - block.size[1] - 15
                                block.initial_pos[1] = block.y
                                click_pos[1] = renpy.get_mouse_pos()[1]
                elif block.type == "lh" or block.type == "sh" or block.type == "red":
                    distance = click_pos[0] - renpy.get_mouse_pos()[0]
                    block.x = block.initial_pos[0] - distance
                    for b2, block2 in enumerate(block_sprites):
                        if b1 != b2:
                            if block2.type != "goal" and (block.y - offset > block2.y and block.y + offset < block2.y + block2.size[1] or block.y + block.size[1] + offset < block2.y + block2.size[1]
                            and block.y + block.size[1] - offset > block2.y):
                                if block.x < block2.x + block2.size[0] and block.x > block2.x:
                                    block.x = block2.x + block2.size[0]
                                    block.initial_pos[0] = block.x
                                    click_pos[0] = renpy.get_mouse_pos()[0]
                                elif block.x + block.size[0] > block2.x and block.x + block.size[0] < block2.x + block2.size[0]:
                                    block.x = block2.x - block.size[0]
                                    block.initial_pos[0] = block.x
                                    click_pos[0] = renpy.get_mouse_pos()[0]
                            elif block.x < puzzle_frame_pos[0] + 15:
                                block.x = puzzle_frame_pos[0] + 15
                                block.initial_pos[0] = block.x
                                click_pos[0] = renpy.get_mouse_pos()[0]
                            elif block.x + block.size[0] > (puzzle_frame_pos[0] + puzzle_frame_size[0]) - 15:
                                block.x = (puzzle_frame_pos[0] + puzzle_frame_size[0]) - block.size[0] - 15
                                block.initial_pos[0] = block.x
                                click_pos[0] = renpy.get_mouse_pos()[0]
                            if (block.type == "red" and block2.type == "goal") and block.x + block.size[0] == block2.x:
                                #current_puzzle = 2
                                renpy.jump("attic_slide")
                                return None
        return 0

    def blocks_events(event, x, y, st):
        global click_pos
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONDOWN:
        # Mouse button is down.
            if event.button == 1:
                # The left mouse button is down.
                for block in block_sprites:
                    if block.type != "goal" and block.x < x < block.x + block.size[0] and block.y < y < block.y + block.size[1]:
                        # Mouse is overlapping this block and the button is pressed down.
                        # Drag the block.
                        block.drag = True
                        click_pos = [x, y]
                        block_SM.redraw(0)
                        break
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            for block in block_sprites:
                if block.type != "goal" and block.drag:
                    block.drag = False
                    block.initial_pos = [block.x, block.y]
                    break

screen unblock_puzzle:
    image "slide_blocks/puzzle-bg.png"
    image "slide_blocks/puzzle-frame.png" pos puzzle_frame_pos
    add block_SM

# label solved_puzzle:
#     "I solved the puzzle!"
#     $bed = True
#     jump attic

label scene_1:
    #ADD TEXT тест перед решением паззла с блоками
    $create_blocks()
    call screen unblock_puzzle



label slide_block_puzzle:
    $block_SM = SpriteManager(update = blocks_update, event =blocks_events)
    $block_sprites = []
    $long_h_block = Image("slide_blocks/long-horizontal-block.png")
    $long_v_block = Image("slide_blocks/long-vertical-block.png")
    $short_h_block = Image("slide_blocks/short-horizontal-block.png")
    $short_v_block = Image("slide_blocks/short-vertical-block.png")
    $red_block = Image("slide_blocks/red-block.png")
    $goal = Image("slide_blocks/goal-vertical.png")
    $long_v_block_size =(151,454)
    $long_h_block_size =(454, 151)
    $short_v_block_size =(151,303)
    $short_h_block_size =(303,151)
    $puzzle_frame_size = (938, 938)
    $puzzle_frame_pos =(110,71)
    $current_puzzle = 1
    $click_pos = [0, 0]
    jump scene_1