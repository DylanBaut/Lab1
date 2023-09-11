from sense_hat import SenseHat
from time import sleep

sense=SenseHat()
sense.clear() ## to clear the LED matrix


blue= (0,0,255)
yellow= (255,255,0)
red=(255,0,0)
x=0
y=0
not_pressed = True
while not_pressed:
    sense.clear()
    sense.set_pixel(x,y, (250, 0, 0))
    for event in sense.stick.get_events():
        
        
        if event.action =="pressed":  ## check if the joystick was pressed

            if event.direction=="right":   ## to check for other directions use "up", "down", "left", "right"
                x= min(x+1,7)
            elif event.direction=="left":   ## to check for other directions use "up", "down", "left", "right"
                x=max(x-1, 0)
            elif event.direction=="down":   ## to check for other directions use "up", "down", "left", "right"
                y=min(y+1,7)
            elif event.direction=="up":   ## to check for other directions use "up", "down", "left", "right"
                y=max(y-1,0)
            elif event.direction=="middle":   ## to check for other directions use "up", "down", "left", "right"
                not_pressed = False
            print(x,y)
            
sense.clear()
# sense.show_letter("M",text_colour=(255,255,255))  ## white color text


