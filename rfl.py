from manim import *
from manim_physics import *



class Refraction(Scene):
    def construct(self):
        self.camera.background_color=BC
        rotation_centre=LEFT

        ax=Axes(x_range=[-30,30],x_length=50)
        l1=Line(start=ax.c2p(0,4.2),
                end=ax.c2p(0,-4.5),
                color=AC)
        l2=Line(start=ax.c2p(-10,0),
                end=ax.c2p(10,0),
                color= AC)
        l3=Line(start=ax.c2p(-5,5),
                end=ax.c2p(5,-5),
                color=AC)
        l4=Line(start=ax.c2p(5,5),
                end=ax.c2p(-5,-5),
                color=AC)
        l5=Line(start=ax.c2p(0,0),
                end=ax.c2p(0,-4.5),
                color=AC)
        nmtex=Tex("Normal Line").next_to(l1,UP,buff=0.1).set_color(BLACK)
        self.add(nmtex)
        self.add(l1,l2)
        
        up=ax.plot(lambda x :x== 0)
        down=ax.plot(lambda x :x== 0).shift(DOWN * 8)
        area=ax.get_area(up,[-30,30],bounded_graph=down,color=GREY_BROWN,opacity=0.5)
        self.add(area)

        path1 = VMobject().set_color(BLACK)
        dot1 = Dot(color=BLACK).move_to(ax.c2p(-3,5))
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path(path1):
            previous_path = path1.copy()
            previous_path.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path)
        path1.add_updater(update_path)

        self.add(dot1,path1)
        self.play(dot1.animate.move_to(ax.c2p(0,0)),run_time=2,rate_function=linear)
        self.wait()
        self.play(dot1.animate.move_to(ax.c2p(3,5)),run_time=2,rate_function=linear)
        self.wait()
        self.play(Uncreate(dot1),Uncreate(path1))
        self.wait()

        path2 = VMobject().set_color(BLACK)
        dot2 = Dot(color=BLACK).move_to(ax.c2p(-5,5))
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        def update_path(path2):
            previous_path = path2.copy()
            previous_path.add_points_as_corners([dot2.get_center()])
            path2.become(previous_path)
        path2.add_updater(update_path)

        l=Line(start=ax.c2p(-5,5),end=ax.c2p(0,0))
        l=Line(start=ax.c2p(0,0),end= ax.c2p(5,5))

        a1=Angle(l1,l3,radius=0.5,quadrant=(-1,-1),other_angle=False,color=BLACK)
        a2=Angle(l1,l4,radius=0.5,quadrant=(-1,-1),other_angle=True,color=BLACK)
        

        tex1 = MathTex(r"\theta",color=BLACK).move_to(
            Angle(
                l1, l3, radius=0.5 + 3 * SMALL_BUFF, other_angle=True,color=BLACK
            ).point_from_proportion(0.5)
        )

        tex2= MathTex(r"\theta",color=BLACK).move_to(
            Angle(
                l1, l4, radius=0.5 + 3 * SMALL_BUFF, other_angle=False,color=BLACK
            ).point_from_proportion(0.5)
        )
        
        self.add(dot2,path2)
        self.play(dot2.animate.move_to(ax.c2p(0,0)),run_time=2,rate_function=linear)
        self.wait()
        self.play(dot2.animate.move_to(ax.c2p(5,5)),run_time=2,rate_function=linear)
        
        self.play(Create(a1))
        self.play(Create(a2))
        self.play(Write(tex1))
        self.wait(3)
        self.play(Write(tex2))
        self.wait(2)
        

    
   
        






