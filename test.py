from manim import *
from manim_physics import*
import numpy as np

class Test(SpaceScene):

 def construct(self):
    ground=Line(
            start=RIGHT*10+DOWN*3,end=LEFT*10+DOWN*3
        ) 
     
    p=ValueTracker(-2)
    
    
    
    
    pivot=Polygram(
        [[p.get_value()+1,-2.95,0],
        [p.get_value(),-2.3,0],
        [p.get_value()-1,-2.95,0]]
        )
    pivot.add_updater(lambda h:h.become(Polygram(
        [[p.get_value()+1,-2.95,0],
        [p.get_value(),-2.3,0],
        [p.get_value()-1,-2.95,0]]
        )))    

    bar=Rectangle(width=8,height=0.3).next_to(ground,UP,buff=2)
    
    self.make_rigid_body(bar,pivot,elasticity=0)
    self.make_static_body(ground)

    self.add(pivot,bar)   
    self.add(ground)
    self.play(p.animate.set_value(2))
    self.wait(6)
