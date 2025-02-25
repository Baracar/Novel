default safe_open = False

init python:
    numbl = 0
    numbc = 0
    numbr = 0

screen code_lock:
    modal True
    add "images/code_lock/cl_panel.png" align .5, .5 zoom 3

    imagebutton auto "images/code_lock/up_%s.png" focus_mask True xalign .336 yalign .365 action If(numbl < 9, SetVariable("numbl", numbl + 1), SetVariable("numbl", 0))
    add "images/code_lock/cl_%s.png"%(numbl) xalign .32 yalign .47 zoom 0.9
    imagebutton auto "images/code_lock/dwn_%s.png" focus_mask True xalign .336 yalign .59 action If(numbl > 0, SetVariable("numbl", numbl - 1), SetVariable("numbl", 9))

    imagebutton auto "images/code_lock/up_%s.png" focus_mask True xalign .427 yalign .365 action If(numbc < 9, SetVariable("numbc", numbc + 1), SetVariable("numbc", 0))
    add "images/code_lock/cl_%s.png"%(numbc) xalign .42 yalign .47 zoom 0.9
    imagebutton auto "images/code_lock/dwn_%s.png" focus_mask True xalign .427 yalign .59 action If(numbc > 0, SetVariable("numbc", numbc - 1), SetVariable("numbc", 9))

    imagebutton auto "images/code_lock/up_%s.png" focus_mask True xalign .518 yalign .365 action If(numbr < 9, SetVariable("numbr", numbr + 1), SetVariable("numbr", 0))
    add "images/code_lock/cl_%s.png"%(numbr) xalign .52 yalign .47 zoom 0.9
    imagebutton auto "images/code_lock/dwn_%s.png" focus_mask True xalign .518 yalign .59 action If(numbr > 0, SetVariable("numbr", numbr - 1), SetVariable("numbr", 9))

    textbutton "ENTER" yalign .61 xalign .656 action If(numbl == 1, If(numbc == 0, If(numbr == 3, [SetVariable("safe_open", True), Hide("code_lock"), Call("after_safe")])))#, Show("access_denied")), Show("access_denied")), Show("access_denied"))
    textbutton "CLOSE" yalign .31 xalign .656 action [Hide("code_lock"), Call("after_safe")]

screen access_denied:
    modal True
    text "Wrong Password!!!" size 50 xalign 0.5 yalign 0.32
    textbutton "Try Again" xalign 0.5 yalign 0.45 action Hide("access_denied")