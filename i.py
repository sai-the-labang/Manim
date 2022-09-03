from manim import *
from manim_physics import*
import numpy as np
import random


class ApplyForce(Animation):

    def __init__(self,mobject,force=2,direction=RIGHT,color=BLUE,**kwargs):
        super().__init__(mobject,**kwargs)
        
        self.force=force
        self.direction=direction
        self.color=color
    
    def begin(self):

        
         a1=Arrow(
           start=4*(self.mobject.get_center()-self.mobject.get_critical_point(self.direction)),
            end=1.2*(self.mobject.get_center()-self.mobject.get_critical_point(self.direction)),
            color=self.color,
            max_tip_length_to_length_ratio=1,
            tip_length=(self.mobject.get_height()+self.mobject.get_width())*0.2,
            max_stroke_width_to_length_ratio=100,
            stroke_width=(self.mobject.get_height()+self.mobject.get_width())*10,
            )
        
         
         self.a1=a1
        
         super().begin()    

    def clean_up_from_scene(self,scene:"Scene")->  None:
         super().clean_up_from_scene(scene) 
         scene.remove(self.a1)
         self.mobject.shift(self.direction*self.force)
               
    def interpolate_mobject(self,alpha):
        
            self.mobject.move_to(self.direction*self.force*alpha)
            
        


class Intro(SpaceScene):

    

    def apply_force(self,mobject,force=2,direction=RIGHT,color=BLUE,run_time=2):
          
            
        a1=Arrow(
            start=(mobject.get_critical_point(-direction)),
            end=(mobject.get_critical_point(direction)),
            color=color,
            max_tip_length_to_length_ratio=1,
            tip_length=(mobject.get_height()+mobject.get_width())*0.2,
            max_stroke_width_to_length_ratio=100,
            stroke_width=(mobject.get_height()+mobject.get_width())*10

            ).shift(-direction*mobject.get_width())
        self.add(a1)   

            
        
    
     
        self.play(
         mobject.animate.shift(direction*force),
         a1.animate.shift(direction*force),
         run_time=run_time
        )
        self.remove(a1)
    def random_boxes(self):
        force_values=["15N","20N","25N","30N","35N","40N","45N","50N"]
        force_labels=VGroup(*[Tex(random.choice(force_values))for i in range(20)])
        sq=VGroup(*[Square(side_length=1.6) for i in range(20)])
        sq.arrange_in_grid(4,5)
        floor=Line(
            start=[-8,-4,0],
            end=[8,-4,0]
        )
        self.add(floor)
        for square,force_label in zip(sq,force_labels):
            force_label.move_to(square.get_center())
            force_label.add_updater(lambda h,square=square:h.move_to(square.get_center()))
            
            
            
        
        self.add(sq)
        self.add(force_labels)
        for _ in range(3):
          numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
          random_numbers=VGroup()
        
          for i in range(20):

           random_number=Integer(random.choice(numbers))
           numbers.remove(random_number.get_value())
           random_numbers.add(random_number)
             
          

          
           
          self.play(
                    sq[random_numbers[1].get_value()].animate.move_to(sq[random_numbers[2].get_value()].get_center()),
                    sq[random_numbers[2].get_value()].animate.move_to(sq[random_numbers[3].get_value()].get_center()),
                    sq[random_numbers[3].get_value()].animate.move_to(sq[random_numbers[4].get_value()].get_center()),
                    sq[random_numbers[4].get_value()].animate.move_to(sq[random_numbers[5].get_value()].get_center()),
                    sq[random_numbers[5].get_value()].animate.move_to(sq[random_numbers[6].get_value()].get_center()),
                    sq[random_numbers[6].get_value()].animate.move_to(sq[random_numbers[7].get_value()].get_center()),
                    sq[random_numbers[7].get_value()].animate.move_to(sq[random_numbers[8].get_value()].get_center()),
                    sq[random_numbers[8].get_value()].animate.move_to(sq[random_numbers[9].get_value()].get_center()),
                    sq[random_numbers[9].get_value()].animate.move_to(sq[random_numbers[10].get_value()].get_center()),
                    sq[random_numbers[10].get_value()].animate.move_to(sq[random_numbers[11].get_value()].get_center()),
                    sq[random_numbers[11].get_value()].animate.move_to(sq[random_numbers[12].get_value()].get_center()),
                    sq[random_numbers[12].get_value()].animate.move_to(sq[random_numbers[13].get_value()].get_center()),
                    sq[random_numbers[13].get_value()].animate.move_to(sq[random_numbers[14].get_value()].get_center()),
                    sq[random_numbers[14].get_value()].animate.move_to(sq[random_numbers[15].get_value()].get_center()),
                    sq[random_numbers[15].get_value()].animate.move_to(sq[random_numbers[16].get_value()].get_center()),
                    sq[random_numbers[16].get_value()].animate.move_to(sq[random_numbers[17].get_value()].get_center()),
                    sq[random_numbers[17].get_value()].animate.move_to(sq[random_numbers[18].get_value()].get_center()),
                    sq[random_numbers[18].get_value()].animate.move_to(sq[random_numbers[19].get_value()].get_center()),
                    sq[random_numbers[19].get_value()].animate.move_to(sq[random_numbers[0].get_value()].get_center()),
                    sq[random_numbers[0].get_value()].animate.move_to(sq[random_numbers[1].get_value()].get_center()),
                    


                )

        self.play(
            sq.animate.shift(UP*20)
        )        
        self.make_static_body(floor)
        self.make_rigid_body(sq)     
        self.wait(10) 
    def random_forces(self):
        sq=VGroup(*[Square().move_to([random.randrange(-10,10),random.randrange(-8,8),0])for _ in range(10)])         
        def 
        self.add(sq)
    def construct(self):
        self.random_forces()

    