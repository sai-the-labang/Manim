from manim import *

import random
class Test(ThreeDScene):
    def construct(self):
        def wait_while_updating(duration=1):
            return Animation(Mobject(), run_time=duration)
        a = [Dot() for i in range(100)]
        self.add(*a)
        d=ValueTracker(1)
        while d==1:
          [a[i].add_updater(lambda m:m.shift(random.choice([UP,DOWN,LEFT,RIGHT,UL,UR,DL,DR,IN,OUT])*0.2).set_color(random.choice([BLUE,RED,GREEN,PURPLE,
          BLACK,WHITE,ORANGE,PINK])))for i in range (100)]
         

        
        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(zoom=0.4)
        self.wait(20)
        d.set_value(0)
        
        