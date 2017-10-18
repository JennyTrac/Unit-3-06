# Created by Jenny Trac
# Created on Oct 17 2017
# Program shows a man walking

import ui
import time
@ui.in_background

def walk_touch_up_inside(sender):
    # makes man start walking
    
    counter = 1
    
    while counter <= 10:
        
        # makes image appear
        walking_man = "Resources/walking_man" + str(counter) + ".BMP"
        view['walking_man_imageview'].image = ui.Image(walking_man)
        counter = counter + 1
        
        # makes image move
        view['walking_man_imageview'].x = view['walking_man_imageview'].x - counter
        
        # delay loop
        time.sleep(0.1)
        
        # if you want to repeat steps indefinitely, uncomment the following
        #if counter >= 10:
        #    counter = 1

view = ui.load_view()
view.present('sheet')
