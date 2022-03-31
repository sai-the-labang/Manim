from manim import *
from manim_physics import *
import numpy as np


class Em(ThreeDScene):
       def em(self):
            te=Tex("Electric Field",color=BLUE).to_edge(UP+LEFT,buff=2)
            tm=Tex("Magnetic Field",color=YELLOW).to_edge(UP+RIGHT,buff=2.5)
            ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE, fill_color=BLUE, fill_opacity=0.7,stroke_opacity=0)
            ellipse_2 = Ellipse(width=2.0, height=4.0, color=YELLOW, fill_color=YELLOW, fill_opacity=0.7,stroke_opacity=0).rotate(PI/2)
            self.add(te,tm)
            self.play(Create(ellipse_1))
            self.play(Create(ellipse_2))
            self.wait(2)
            self.play(Uncreate(ellipse_1),Uncreate(ellipse_2),Uncreate(tm),Uncreate(te))
            self.wait()
            

       def emwave(self):
           self.set_camera_orientation(50 * DEGREES,-130 * DEGREES,zoom=2)
           ax2=ThreeDAxes()
           ax=ThreeDAxes(x_range=[-20,20],y_range=[-20,20],z_range=[-20,20])
           tem=Tex("Electro","magnetic"," Wave",font_size=30).shift(UP*2.5+LEFT)
           tem[0].set_color(BLUE)
           tem[1].set_color(YELLOW)
           
           h=self.h=ValueTracker(0)

           s1=ax.plot(lambda x: np.sin(x+self.h.get_value()),x_range=[-20,20],
                                          stroke_opacity=0,fill_color=YELLOW)
           a1=ax.get_area(s1,x_range=[-20,20],color=YELLOW)

           s1.add_updater(lambda t : t.become(ax.plot(lambda x: np.sin(x+self.h.get_value()),x_range=[-20,20],
                                          stroke_opacity=0,fill_color=YELLOW)))
           a1.add_updater(lambda t: t.become(ax.get_area(s1,x_range=[-20,20],color=YELLOW)))



           s2=ax.plot(lambda x: np.sin(x+self.h.get_value()+1.05*PI),x_range=[-20,20],
                                          stroke_opacity=0,fill_color=BLUE).rotate(PI/2,axis=RIGHT)
           a2=ax.get_area(s2,x_range=[-20,20],color=BLUE)

           s2.add_updater(lambda t: t.become(ax.plot(lambda x: np.sin(x+self.h.get_value()+1.05*PI),x_range=[-20,20],
                                          stroke_opacity=0,fill_color=BLUE).rotate(PI/2,axis=RIGHT)))
           a2.add_updater(lambda t: t.become(ax.get_area(s2,x_range=[-20,20],color=BLUE)))
           #########################################################################################################
           arrowse=self.arrowse=[always_redraw(lambda j=j : 
                                               Arrow(start=ax.c2p(j,0),
                                                     end=ax.c2p(j,s2.underlying_function(j)),
                                                     color=BLUE,stroke_width=20,max_stroke_width_to_length_ratio=30).rotate(PI/2,axis=RIGHT).shift(OUT)
                                                     
                                                     )
                                               for j in np.arange(-20,20,0.5)] 

                                             
           
           arrowsm=self.arrowsm=[always_redraw(lambda k=k : 
                                               Arrow(start=ax.c2p(k,0),
                                                     end=ax.c2p(k,s1.underlying_function(k)),
                                                     color=YELLOW,stroke_width=20,max_stroke_width_to_length_ratio=30).shift(OUT))
                                               for k in np.arange(-20,20,0.5)]
           

               
           
           self.add(tem) 
           self.add(*self.arrowse,*self.arrowsm,ax2)
           self.wait()                              
           
           self.begin_ambient_camera_rotation(rate=0.015)
           
           self.play(self.h.animate.set_value(-40),run_time=20,rate_func=rate_functions.linear)
           
           
           self.stop_ambient_camera_rotation()
           self.wait(2)
          
           

   
       def construct(self):
           self.em()
           self.emwave()
