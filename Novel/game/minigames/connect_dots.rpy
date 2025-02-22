init python:
    class LineDisplay(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(LineDisplay, self).__init__(*args, **kwargs)

        def render(self, width, height, st, at):
            screen = renpy.Render(640, 480)
            can=im.load_surface("images/blankcanvas.png")

            x= len(list_lines)
            y=0
            while y<x:
                pygame.draw.line(can,(0,0,255),list_lines[y][0], list_lines[y][1], 3)
                y += 1


            screen.blit(can,(0,0))
            renpy.redraw(self, 0)
            return screen

    def inCircle(pointX, pointY,gX,gY,distance):
        xDist = pointX-gX
        xDist=math.fabs(xDist)
        yDist = pointY-gY
        yDist=math.fabs(yDist)
        xyDist = (xDist*xDist)+(yDist*yDist)
        if distance >= math.sqrt(xyDist):
            return True
        else:
            return False