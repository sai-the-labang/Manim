from manim import * 
import numpy as np 
import random

class Wnp(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.camera.background_color=BC

        title=Text("Water Waves",font_size=50).shift(UP *3).set_scale(6).set_color(BLUE)
        
        ax=Axes(x_range=[-30,30],x_length=30).shift(DOWN* 5)    

        t=ValueTracker(1 * PI)

        sin=ax.plot(
            lambda x: np.sin(x+t.get_value()),
            x_range=[-30,30],
            color=BLUE
        ).shift(UP *6)

        sin.add_updater(lambda b:b.become(ax.plot(lambda x: np.sin(x+t.get_value()),
                                                            x_range=[-30,30],
                                                            color=BLUE)
        ).shift(UP *6))

        x0=ax.plot(lambda x: x==0)

        area=ax.get_area(sin,[-30,30],bounded_graph=x0,color=BLUE,opacity=2)
        area.add_updater(lambda i :i.become(ax.get_area(sin,[-30,30],bounded_graph=x0,color=BLUE,opacity=2)))

        

        
        
            
        dot=[always_redraw(lambda j=j :Dot(radius=0.05,color=BLACK).move_to(ax.c2p(j,sin.underlying_function(j))).shift(UP* 6))for j in np.arange(-30,30,1)]
        #paths########################################################
        path=VMobject()
        path.set_points_as_corners([dot[20].get_center(),dot[20].get_center()])
        def update_path(path):
            previous_path=path.copy()
            previous_path.add_points_as_corners([dot[20].get_center()])
            path.become(previous_path).set_color(GREY)
        ############################################################
        def cu(mob):
            mob.move_to(dot[20])

        
        
        self.play(FadeIn(sin,area))
        self.play(Write(title))
        self.wait(3)
        self.play(FadeIn(*dot))
        self.wait(2)
        
       
        self.play(t.animate.set_value(4 * PI),run_time=4,rate_function=wiggle)
        self.wait()
        
        self.play(t.animate.set_value(7 * PI),run_time=4,rate_function=wiggle)
        self.wait()
        self.play(self.camera.frame.animate.move_to(dot[20]).scale(0.5))
        self.add(path)
        self.wait()
        
        
        path.add_updater(update_path)
        self.play(t.animate.set_value(15 * PI),run_time=10,rate_function=wiggle)
        self.wait()
        self.play(Restore(self.camera.frame))
        self.wait()
        
        
        path2=VMobject()    
         
        path2.set_points_as_corners([dot[16].get_center(),dot[16].get_center()])
        def update_path2(path2):
              previous_path2=path2.copy()
              previous_path2.add_points_as_corners([dot[16].get_center()])
              path2.become(previous_path2).set_color(GREY)
       
        path2.add_updater(update_path2)
        self.add(path2)

        path3=VMobject()    
         
        path3.set_points_as_corners([dot[17].get_center(),dot[17].get_center()])
        def update_path3(path3):
              previous_path3=path3.copy()
              previous_path3.add_points_as_corners([dot[17].get_center()])
              path3.become(previous_path3).set_color(GREY)
       
        path3.add_updater(update_path3)
        self.add(path3)

        path4=VMobject() 

        path4.set_points_as_corners([dot[18].get_center(),dot[18].get_center()])
        def update_path4(path4):
              previous_path4=path4.copy()
              previous_path4.add_points_as_corners([dot[18].get_center()])
              path4.become(previous_path4).set_color(GREY)
       
        path4.add_updater(update_path4)
        self.add(path4)

        path5=VMobject() 

        path5.set_points_as_corners([dot[19].get_center(),dot[19].get_center()])
        def update_path5(path5):
              previous_path5=path5.copy()
              previous_path5.add_points_as_corners([dot[19].get_center()])
              path5.become(previous_path5).set_color(GREY)
       
        path5.add_updater(update_path5)
        self.add(path5)

        path6=VMobject() 

        path6.set_points_as_corners([dot[20].get_center(),dot[20].get_center()])
        def update_path6(path6):
              previous_path6=path6.copy()
              previous_path6.add_points_as_corners([dot[20].get_center()])
              path6.become(previous_path6).set_color(GREY)
       
        path6.add_updater(update_path6)
        self.add(path6)

        path7=VMobject() 

        path7.set_points_as_corners([dot[21].get_center(),dot[21].get_center()])
        def update_path7(path7):
              previous_path7=path7.copy()
              previous_path7.add_points_as_corners([dot[21].get_center()])
              path7.become(previous_path7).set_color(GREY)
       
        path7.add_updater(update_path7)
        self.add(path7)

        path8=VMobject() 

        path8.set_points_as_corners([dot[22].get_center(),dot[22].get_center()])
        def update_path8(path8):
              previous_path8=path8.copy()
              previous_path8.add_points_as_corners([dot[22].get_center()])
              path8.become(previous_path8).set_color(GREY)
       
        path8.add_updater(update_path8)
        self.add(path8)

        path9=VMobject() 

        path9.set_points_as_corners([dot[23].get_center(),dot[23].get_center()])
        def update_path9(path9):
              previous_path9=path9.copy()
              previous_path9.add_points_as_corners([dot[23].get_center()])
              path9.become(previous_path9).set_color(GREY)
       
        path9.add_updater(update_path9)
        self.add(path9)

        path10=VMobject() 

        path10.set_points_as_corners([dot[24].get_center(),dot[24].get_center()])
        def update_path10(path10):
              previous_path10=path10.copy()
              previous_path10.add_points_as_corners([dot[24].get_center()])
              path10.become(previous_path10).set_color(GREY)
       
        path10.add_updater(update_path10)
        self.add(path10)

        path11=VMobject() 

        path11.set_points_as_corners([dot[25].get_center(),dot[25].get_center()])
        def update_path11(path11):
              previous_path11=path11.copy()
              previous_path11.add_points_as_corners([dot[25].get_center()])
              path11.become(previous_path11).set_color(GREY)
       
        path11.add_updater(update_path11)
        self.add(path11)

        path12=VMobject() 

        path12.set_points_as_corners([dot[26].get_center(),dot[26].get_center()])
        def update_path12(path12):
              previous_path12=path12.copy()
              previous_path12.add_points_as_corners([dot[26].get_center()])
              path12.become(previous_path12).set_color(GREY)
       
        path12.add_updater(update_path12)
        self.add(path12)

        path13=VMobject() 

        path13.set_points_as_corners([dot[27].get_center(),dot[27].get_center()])
        def update_path13(path13):
              previous_path13=path13.copy()
              previous_path13.add_points_as_corners([dot[27].get_center()])
              path13.become(previous_path13).set_color(GREY)
       
        path13.add_updater(update_path13)
        self.add(path13)

        path14=VMobject() 

        path14.set_points_as_corners([dot[28].get_center(),dot[28].get_center()])
        def update_path14(path14):
              previous_path14=path14.copy()
              previous_path14.add_points_as_corners([dot[28].get_center()])
              path14.become(previous_path14).set_color(GREY)
       
        path14.add_updater(update_path14)
        self.add(path14)

        path15=VMobject() 

        path15.set_points_as_corners([dot[29].get_center(),dot[29].get_center()])
        def update_path15(path15):
              previous_path15=path15.copy()
              previous_path15.add_points_as_corners([dot[29].get_center()])
              path15.become(previous_path15).set_color(GREY)
       
        path15.add_updater(update_path15)
        self.add(path15)

        path16=VMobject() 

        path16.set_points_as_corners([dot[30].get_center(),dot[30].get_center()])
        def update_path16(path16):
              previous_path16=path16.copy()
              previous_path16.add_points_as_corners([dot[30].get_center()])
              path16.become(previous_path16).set_color(GREY)
       
        path16.add_updater(update_path16)
        self.add(path16)

        path17=VMobject() 

        path17.set_points_as_corners([dot[31].get_center(),dot[31].get_center()])
        def update_path17(path17):
              previous_path17=path17.copy()
              previous_path17.add_points_as_corners([dot[31].get_center()])
              path17.become(previous_path17).set_color(GREY)
       
        path17.add_updater(update_path17)
        self.add(path17)

        path18=VMobject() 

        path18.set_points_as_corners([dot[32].get_center(),dot[32].get_center()])
        def update_path18(path18):
              previous_path18=path18.copy()
              previous_path18.add_points_as_corners([dot[32].get_center()])
              path18.become(previous_path18).set_color(GREY)
       
        path18.add_updater(update_path18)
        self.add(path18)

        path19=VMobject() 

        path19.set_points_as_corners([dot[33].get_center(),dot[33].get_center()])
        def update_path19(path19):
              previous_path19=path19.copy()
              previous_path19.add_points_as_corners([dot[33].get_center()])
              path19.become(previous_path19).set_color(GREY)
       
        path19.add_updater(update_path19)
        self.add(path19)

        path20=VMobject() 

        path20.set_points_as_corners([dot[34].get_center(),dot[34].get_center()])
        def update_path20(path20):
              previous_path20=path20.copy()
              previous_path20.add_points_as_corners([dot[34].get_center()])
              path20.become(previous_path20).set_color(GREY)
       
        path20.add_updater(update_path20)
        self.add(path20)

        path21=VMobject() 

        path21.set_points_as_corners([dot[35].get_center(),dot[35].get_center()])
        def update_path21(path21):
              previous_path21=path21.copy()
              previous_path21.add_points_as_corners([dot[35].get_center()])
              path21.become(previous_path21).set_color(GREY)
       
        path21.add_updater(update_path21)
        self.add(path21)

        path22=VMobject() 

        path22.set_points_as_corners([dot[36].get_center(),dot[36].get_center()])
        def update_path22(path22):
              previous_path22=path22.copy()
              previous_path22.add_points_as_corners([dot[36].get_center()])
              path22.become(previous_path22).set_color(GREY)
       
        path22.add_updater(update_path22)
        self.add(path22)

        path23=VMobject() 

        path23.set_points_as_corners([dot[37].get_center(),dot[37].get_center()])
        def update_path23(path23):
              previous_path23=path23.copy()
              previous_path23.add_points_as_corners([dot[37].get_center()])
              path23.become(previous_path23).set_color(GREY)
       
        path23.add_updater(update_path23)
        self.add(path23)

        path24=VMobject() 

        path24.set_points_as_corners([dot[38].get_center(),dot[38].get_center()])
        def update_path24(path24):
              previous_path24=path24.copy()
              previous_path24.add_points_as_corners([dot[38].get_center()])
              path24.become(previous_path24).set_color(GREY)
       
        path24.add_updater(update_path24)
        self.add(path24)

        path25=VMobject() 

        path25.set_points_as_corners([dot[39].get_center(),dot[39].get_center()])
        def update_path25(path25):
              previous_path25=path25.copy()
              previous_path25.add_points_as_corners([dot[39].get_center()])
              path25.become(previous_path25).set_color(GREY)
       
        path25.add_updater(update_path25)
        self.add(path25)

        path26=VMobject() 

        path26.set_points_as_corners([dot[40].get_center(),dot[40].get_center()])
        def update_path26(path26):
              previous_path26=path26.copy()
              previous_path26.add_points_as_corners([dot[40].get_center()])
              path26.become(previous_path26).set_color(GREY)
       
        path26.add_updater(update_path26)
        self.add(path26)

        path27=VMobject() 

        path27.set_points_as_corners([dot[41].get_center(),dot[41].get_center()])
        def update_path27(path27):
              previous_path27=path27.copy()
              previous_path27.add_points_as_corners([dot[41].get_center()])
              path27.become(previous_path27).set_color(GREY)
       
        path27.add_updater(update_path27)
        self.add(path27)

        path28=VMobject() 

        path28.set_points_as_corners([dot[42].get_center(),dot[42].get_center()])
        def update_path28(path28):
              previous_path28=path28.copy()
              previous_path28.add_points_as_corners([dot[42].get_center()])
              path28.become(previous_path28).set_color(GREY)
       
        path28.add_updater(update_path28)
        self.add(path28)

        path29=VMobject() 

        path29.set_points_as_corners([dot[43].get_center(),dot[43].get_center()])
        def update_path29(path29):
              previous_path29=path29.copy()
              previous_path29.add_points_as_corners([dot[43].get_center()])
              path29.become(previous_path29).set_color(GREY)
       
        path29.add_updater(update_path29)
        self.add(path29)

        path30=VMobject() 

        path30.set_points_as_corners([dot[44].get_center(),dot[44].get_center()])
        def update_path30(path30):
              previous_path30=path30.copy()
              previous_path30.add_points_as_corners([dot[44].get_center()])
              path30.become(previous_path30).set_color(GREY)
       
        path30.add_updater(update_path30)
        self.add(path30)

        self.play(t.animate.set_value(30 * PI),run_time=10,rate_function=wiggle)
        self.wait()

        

        
