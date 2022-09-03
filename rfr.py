from manim import *
import numpy as np


class Reflection(Scene):
    

    def creating(self):
        ax=Axes(x_range=[-30,30],x_length=50)
        lines1=self.lines1=VGroup(*[Line(start=ax.c2p(0,4.2),
                                       end=ax.c2p(0,-4.5),
                                       color=BLUE),
                                 Line(start=ax.c2p(-10,0),
                                      end=ax.c2p(10,0),
                                      color= BLUE)

        ]
        )
        up=ax.plot(lambda x :x== 0)
        down=ax.plot(lambda x :x== 0).shift(DOWN * 8)
        area=ax.get_area(up,[-30,30],bounded_graph=down,color=GREY_BROWN,opacity=0.5)
        nmtex=Tex("Normal Line").next_to(lines1,UP,buff=0.1).set_color(BLACK)
        self.add(area)
        self.add(nmtex)

        self.add(lines1)
    
    def dotmoving(self):
        ax=Axes(x_range=[-30,30],x_length=50)
        path1 = VMobject().set_color(BLACK)
        dot1 = Dot(color=BLACK).move_to(ax.c2p(-3,5))
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path(path1):
            previous_path = path1.copy()
            previous_path.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path)
        path1.add_updater(update_path)
        dl=DashedLine(start=ax.c2p(0,0),end=ax.c2p(3,-5),color=BLUE)
        self.add(path1)
        self.play(Create(dot1))
        self.play(dot1.animate.move_to(ax.c2p(0,0)),run_time=2,rate_function=linear)
        self.wait()
        self.play(Create(dl),run_time=2)
        self.play(dot1.animate.move_to(ax.c2p(2,-5)),run_time=2,rate_function=linear)

    def construct(self):
        
        rotation_centre=LEFT
        self.creating()
        self.dotmoving()