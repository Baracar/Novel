# screen idleScreen:
#     imagebutton:
#         idle "walking_feet.png"
#         xpos 50
#         ypos 800
#         action Jump("chooseLocMove")
#
# label chooseLocMove:
#     if location == 'home':
#         call screen homeLoc
#     if location == 'lake':
#         call screen lakeLoc
#         #jump home
#     if location == 'home':
#         call screen homeLoc
#
# screen homeLoc:
#     if lakeVisited == True:
#         imagebutton:
#             idle "arrow_left"
#             xpos 50
#             ypos 300
#             action Jump("lakeSecond")
#     else:
#         imagebutton:
#             idle "arrow_left"
#             xpos 50
#             ypos 300
#             action Jump("lake")
#
# screen lakeLoc:
#     imagebutton:
#         idle "arrow_right"
#         xpos 1350
#         ypos 300
#         action Jump("homeSecond")


#фоны
image room = im.Scale("images/bg/room.jpg", 1920, 1080)
image lake = im.Scale("images/bg/lake.jpg", 1920, 1080)