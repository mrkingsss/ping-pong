from pygame import *

#window size and background's color (rgb)
window = display.set_mode((600, 600))
back = (133, 5, 50)
window.fill(back)



#fps 

clock = time.Clock()

display.update()
clock.tick(60)
