from manim import*
import numpy as np
from manim_physics import*
home="D:\For Physics.bayta\Series\chapter 1\svg"
home2="D:\For Physics.bayta\Series\Svg"


class Intro(Scene):

  def construct(self):
    self.welcome()
    self.video_icons()
    self.aye_say()
    self.kbl()
    self.play(FadeOut(self.pppp))
    self.get_ready()

  def welcome(self):
    wel=Text("ကြိုဆိုပါတယ်",font="Myanmar Text",font_size=40)
    self.play(Write(wel),run_time=2)
    self.wait()
    self.play(Unwrite(wel))

  def video_icons(self):
    
    video_icons=self.video_icons=VGroup(*[
      SVGMobject(
        f"{home2}\\video-film-hand-drawn-symbol-svgrepo-com(1).svg"
      ) for i in range(10)
    ]).arrange(buff=0.6).scale(0.5).shift(UP*3).set_color(WHITE)
   #for i in range(10):
   #  c_video=video.copy()
   #  videos.add(c_video)
   #
   #videos.arrange_in_grid()
    self.play(DrawBorderThenFill(video_icons))
    self.play(Circumscribe(video_icons,time_width=3),run_time=3)
    self.wait()
  
  def aye_say(self):
    pppp=self.pppp=Text("သက်တောင့်သက်သာလေး \n\n         ထိုင်လိုက်ပါ",font="Myanmar Text")
    self.play(Write(pppp))
    self.wait()
    

  def kbl_angry(self):
    self.play(self.kbl_rec.animate.set_color(RED_E).scale(1.5),self.kbl.animate.scale(1.5))  
  
  def kbl_stop(self):
    self.play(self.kbl_rec.animate.set_color(WHITE).scale(0.75),self.kbl.animate.scale(0.75))

  def kbl_asking(self):
    self.play(self.kbl_rec.animate.set_color(GREEN_E).scale(1.5),self.kbl.animate.scale(1.5))  

  def kbl(self):
      kbl=self.kbl=SVGMobject(
        f"{home}\\vip-person-vip-svgrepo-com(1).svg"
      ).next_to(self.pppp,LEFT,buff=1).scale(0.3)
      kbl_rec=self.kbl_rec=SurroundingRectangle(kbl,color=WHITE,buff=0.3)
      kbls=self.kbls=VGroup(self.kbl,self.kbl_rec)
      self.play(Create(kbl),Create(kbl_rec))  
      self.wait()
      self.kbl_angry()
      self.wait()
      self.kbl_stop()
  
  def get_ready(self):
    floor=Line(start=np.array((-8,-2.5,0)),end=np.array((8,-2.5,0)))
    #self.play(Unwrite(self.pppp))
    self.wait()
    self.play(self.video_icons[0].animate.move_to([0,0,0]))
    self.wait()
    self.play(ReplacementTransform(self.video_icons[0],floor),FadeOut(self.video_icons[1:]))
    self.wait()






class Setup(Scene):
    def apply_force_right(self,mobject,force=10,distance=5,direction=RIGHT,color=BLUE,run_time=2):
          k=ValueTracker(0.0)
          
          initial_pos_dot=Dot(mobject.get_bottom(),radius=0.00001,color=WHITE)
          final_pos_dot=Dot(mobject.get_bottom(),radius=0.00001,color=WHITE)
          final_pos_dot.add_updater(
            lambda h:h.become(Dot(mobject.get_bottom(),radius=0.00001,color=WHITE))
          )
          line_for_brace=always_redraw(lambda :Line(
            start=initial_pos_dot,
            end=final_pos_dot,
          ))
        # Brace          
          distance_shower=self.distance_shower=Brace(
            line_for_brace
          )
          
          distance_shower.add_updater(
            lambda h:h.become(
              Brace(
            line_for_brace
          )
            )
          )
        # Number for distance
          num_for_distance=self.num_for_distance=DecimalNumber(
            k.get_value(),num_decimal_places=1
          ).next_to(distance_shower,DOWN)
          num_for_distance.add_updater(
            lambda h:h.become(
              DecimalNumber(
            k.get_value(),num_decimal_places=1
          ).next_to(distance_shower,DOWN)
            )
          )
          unit_for_distance=Tex("m").next_to(num_for_distance)
          unit_for_distance.add_updater(lambda h:h.become(
            Tex("m").next_to(num_for_distance)
          ))
          distance_value=VGroup(num_for_distance,unit_for_distance)
        # Arrow for Force
              
          a1=self.a1=Arrow(
            start=(mobject.get_critical_point(LEFT)),
            end=(mobject.get_critical_point(RIGHT)),
            color=color,max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=0.3

            ).shift(UP)
        # Number for Force
          num_for_force=self.num_for_force=Tex(
            force,"N").next_to(a1,LEFT).set_color(BLUE)
          num_for_force.add_updater(
            lambda h:h.become(
              Tex(
            force,"N").next_to(a1,LEFT).set_color(BLUE)
            )
          )   
        # Action
          self.add(a1)
          self.add(initial_pos_dot,final_pos_dot,line_for_brace,distance_value,num_for_force)
          self.add(distance_shower)   

          self.play(
           mobject.animate.shift(direction*force/4),
           a1.animate.shift(direction*force/4),
           k.animate.set_value(1*distance),
           run_time=run_time
          )
          self.remove(
            a1,
            
            initial_pos_dot,
            final_pos_dot,
            line_for_brace,
            
          )
        # force right simply
    def apply_force_right_simply(self,mobject,force=10,distance=5,direction=RIGHT,color=BLUE,run_time=2):

          a2=Arrow(
            start=(mobject.get_critical_point(LEFT)),
            end=(mobject.get_critical_point(RIGHT)),
            color=color,max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=0.3

            ).shift(UP)

          self.add(a2)
          self.play(
           mobject.animate.shift(direction*force/4),
           a2.animate.shift(direction*force/4),
           
           run_time=run_time
          )
          self.remove(a2)
        # force left simply
    def apply_force_left_simply(self,mobject,force=10,distance=5,direction=LEFT,color=BLUE,run_time=2):

          a3=Arrow(
            start=(mobject.get_critical_point(RIGHT)),
            end=(mobject.get_critical_point(LEFT)),
            color=color,max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=0.3

            ).shift(UP)
          self.add(a3)
          self.play(
           mobject.animate.shift(direction*force/4),
           a3.animate.shift(direction*force/4),
           
           run_time=run_time
          )
          self.remove(a3)
        # force up simply
    def apply_force_up_simply(self,mobject,force=10,distance=5,direction=UP,color=BLUE,run_time=2):

          a4=Arrow(
            start=(mobject.get_critical_point(DOWN)),
            end=(mobject.get_critical_point(UP)),
            color=color,max_stroke_width_to_length_ratio=20,
            max_tip_length_to_length_ratio=0.3

            ).shift(LEFT)
          self.add(a4)
          self.play(
           mobject.animate.shift(direction*force/4),
           a4.animate.shift(direction*force/4),
           
           run_time=run_time
          )    
          self.remove(a4)         
          

    def construct (self):
        self.kbl_and_floor()
        self.title()
        self.w_equals_fs()
        
    def title(self):
      title=Title("Work done and Power").set_color_by_gradient(BLUE,RED,GREEN,)
      self.play(Write(title))    
    def kbl_and_floor(self):
      pppp=Text("သက်တောင့်သက်သာလေး \n\n         ထိုင်လိုက်ပါ",font="Myanmar Text")
      kbl=SVGMobject(
        f"{home}\\vip-person-vip-svgrepo-com(1).svg"
      ).next_to(pppp,LEFT,buff=1).scale(0.3)
      rec=SurroundingRectangle(kbl,color=WHITE,buff=0.3)
      kbls=VGroup(kbl,rec)

      floor=Line(start=np.array((-8,-2.5,0)),end=np.array((8,-2.5,0)))

      self.add(kbl,rec,floor)
      self.play(kbls.animate.shift(UP*2+LEFT*1.2))

    def w_equals_fs(self):
        box=Rectangle(height=1,width=1).move_to(np.array((-4,-2,0)))
        

        stand=SVGMobject(f"{home}\\human-boy-person-man-svgrepo-com.svg").scale(0.35).set_color(
            WHITE
            ).next_to(
                box,LEFT*0.2
            ).shift(DOWN*0.15)
        push_right=SVGMobject(f"{home}\\boy-standing-on-one-leg-svgrepo-com.svg").scale(0.35).set_color(
            WHITE
            ).next_to(box,LEFT*0.05
            ).shift(DOWN*0.15).rotate(180*DEGREES,axis=UP)

        push_left=SVGMobject(f"{home}\\boy-standing-on-one-leg-svgrepo-com.svg").scale(0.35).set_color(
            WHITE
            ).next_to(box,RIGHT*0.05
            ).shift(DOWN*0.15)
        lift=SVGMobject(f"{home}\\boy-flexining-leg-and-with-arms-up-svgrepo-com.svg").scale(0.35).set_color(
            WHITE
            ).next_to(box,DOWN*0.000001
            )

        stand.add_updater(lambda h:h.next_to(box,LEFT*0.05).shift(DOWN*0.15))
        push_right.add_updater(lambda h:h.next_to(box,LEFT*0.05).shift(DOWN*0.15))
        push_left.add_updater(lambda h:h.next_to(box,RIGHT*0.05).shift(DOWN*0.15))
        lift.add_updater(lambda h:h.next_to(box,DOWN*0.000001))    

        
       #self.play(Create(stand))
       #self.play(ReplacementTransform(stand,push))
       #self.wait(2)
       #self.add(floor,box,stand)
       #self.remove(stand)
       #self.add(push)
       #self.apply_force_right(box)
       #self.remove(push)
       #stand.update()
       #self.add(stand)
       #self.wait(0.3)
       #self.remove(stand)
       #self.add(push)
       #self.apply_force_right(box)
       #self.remove(push)
       #stand.update()
       #self.add(stand)
       #self.wait()
        #self.add(push_left)

        work_done_eq=MathTex(
          "W","=","F","s"
        ).shift(UP*2,RIGHT*2)


        
        self.play(Create(box))
        self.play(Create(stand))
        self.wait()
        self.remove(stand)
        self.add(push_right)
        self.apply_force_up_simply(box)
       #self.apply_force_right(box)
       #self.remove(push_right)
       #stand.update()
       #self.add(stand)
       #self.wait()
       #self.add(work_done_eq)



