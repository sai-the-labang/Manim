from manim import *
from manim_physics import *
import numpy as np


class Wave(Scene):
      def blue(self):
            ax=Axes(x_range=[-1,13],y_range=[-2,2])
            rec=SurroundingRectangle(ax,color=WHITE)
            box=VGroup(ax,rec)
            t,k=ValueTracker(1),ValueTracker(1)
            rect=Rectangle(height=3,width=10,fill_color=["#5a3ed5","#3685c3","#36ceba",
                                                                     "#36ce4f","#d9cf2c","#9cd234","#e65736"],fill_opacity=1
                                                                     ).rotate(PI,axis=OUT)
            tex=Tex("400nm","700nm",font_size=25)
            tex2=Tex("Electromagnetic Spectrum",font_size=35)
            tex[0].add_updater(lambda h:h.next_to(rect,DOWN+LEFT))
            tex[1].add_updater(lambda h:h.next_to(rect,DOWN+RIGHT))
            tex2.set_color(["#e65736","#9cd234","#d9cf2c","#36ce4f","#36ceba","#3685c3","#5a3ed5"])
            tex2.add_updater(lambda h:h.next_to(rect,DOWN))

            sin=ax.plot(lambda x :np.sin(t.get_value()*x)*k.get_value(),
                                                        color=WHITE)

            
            sin.add_updater(lambda r:r.become(ax.plot(lambda x :np.sin(t.get_value()*x)*k.get_value(),
                                                        color=WHITE)))

            c1=Circle(radius=2,stroke_opacity=0,fill_opacity=1,
                      fill_color="#29c643"
            )                                            
            c2=Circle(radius=2,stroke_opacity=0,fill_opacity=0.75,
                      fill_color="#29c643"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)  
            c3=Circle(radius=2,stroke_opacity=0,fill_opacity=0.75,
                      fill_color="#2943c6"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            c4=Circle(radius=2,stroke_opacity=0,fill_opacity=0.75,
                      fill_color="#c62929"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            c5=Circle(radius=2,stroke_opacity=0,fill_opacity=0.75,
                      fill_color="#29c643"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            c6=Circle(radius=2,stroke_opacity=0,fill_opacity=1,
                      fill_color="#02fd2b"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            c7=Circle(radius=2,stroke_opacity=0,fill_opacity=1,
                      fill_color="#4f02fd"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            c8=Circle(radius=2,stroke_opacity=0,fill_opacity=1,
                      fill_color="#fd0202"
            ).shift(UP*2+LEFT*3.7).set_scale(0.8)
            self.play(Create(rec))
            self.play(Create(ax))
            self.play(Create(sin))
            
            self.wait()
            self.play(box.animate.shift(RIGHT*3.5+UP*2).scale(0.5))
            self.play(Create(rect),Create(tex),Create(tex2))
            self.play(rect.animate.shift(DOWN*2).scale(0.7))
            self.play(Create(c1))
            self.play(c1.animate.shift(UP*2+LEFT*3.7).set_scale(0.8))
            
            
            self.play(ReplacementTransform(c2,c3),t.animate.set_value(5),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c3,c4),t.animate.set_value(0.4),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c4,c5),t.animate.set_value(1),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c5,c6),k.animate.set_value(2),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c6,c5),k.animate.set_value(1),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c5,c6),k.animate.set_value(2),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c6,c7),t.animate.set_value(5),run_time=3)
            self.wait()
            self.play(ReplacementTransform(c7,c8),t.animate.set_value(0.4),run_time=3)
            self.wait()
            

            
            
      def construct(self):
            
            self.blue()    