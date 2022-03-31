from manim import *
import numpy as np 
from manim_physics import *
from colour import Color

class Interference(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(90 * DEGREES, 90 * DEGREES,zoom= 1)
        self.camera.background_color=BC

      

        w=LinearWave(
            wavelength=2,
            amplitude=0.2,
            x_range=[-5,5],
            y_range=[-10,10],
            checkerboard_colors=[BLUE,BLUE],
            stroke_width=0
        )
        

        wave1 = RadialWave(
                        np.array([5,0,0]),
                        
                        
                        wavelength=2,
                        amplitude=0.2, # Two source of waves
                        
                        checkerboard_colors=[BLUE,BLUE],
                        stroke_width=0,
                        x_range=[5,15],
                        y_range=[-10,10]
                    )
        wave2 = RadialWave(
                        np.array([5,-6.7,0]),
                        
                        
                        wavelength=2,
                        amplitude=0.2, # Two source of waves
                        
                        checkerboard_colors=[BLUE,BLUE],
                        stroke_width=0,
                        x_range=[5,15],
                        y_range=[-10,10]
                    )
        wave3 = RadialWave(
                        np.array([5,3.4,0]),
                        np.array([5,-6.7,0]),
                        
                        
                        wavelength=2,
                        amplitude=0.2, # Two source of waves
                        
                        checkerboard_colors=[BLUE,BLUE],
                        stroke_width=0,
                        x_range=[5,15],
                        y_range=[-10,10]
                    )


        l1=Line3D(
            stroke_width=15,
            start=np.array([5,-10,0]),
            end=np.array([5,-0.5,0]),
            color=BLACK
        )
        l2=Line3D(
            stroke_width=15,
            start=np.array([5,10,0]),
            end=np.array([5,0.5,0]),
            color=BLACK
        )

        l3=Line3D(
            stroke_width=15,
            start=np.array([5,-10,0]),
            end=np.array([5,-7.2,0]),
            color=BLACK
        )
        l4=Line3D(
            stroke_width=15,
            start=np.array([5,-6.2,0]),
            end=np.array([5,2.9,0]),
            color=BLACK
        )
        l5=Line3D(
            stroke_width=15,
            start=np.array([5,3.9,0]),
            end=np.array([5,10,0]),
            color=BLACK
        )
        l6=Line3D(
            stroke_width=15,
            start=np.array([5,10,0]),
            end=np.array([5,-6.7,0]),
            color=BLACK
        )
        l7=Line3D(
            stroke_width=15,
            start=np.array([5,-0.5,0]),
            end=np.array([5,0.5,0]),
            color=BLACK
        )
        fridge1=Line3D(
            stroke_width=15,
            start=np.array([-5,-10,0]),
            end=np.array([15,-10,0]),
            color=AC
        )
        fridge2=Line3D(
            stroke_width=15,
            start=np.array([15,-10,0]),
            end=np.array([15,10,0]),
            color=AC
        )
        fridge3=Line3D(
            stroke_width=15,
            start=np.array([15,10,0]),
            end=np.array([-5,10,0]),
            color=AC
        )
        fridge4=Line3D(
            stroke_width=15,
            start=np.array([-5,10,0]),
            end=np.array([-5,-10,0]),
            color=AC
        )
        fridge=VGroup(fridge1,fridge2,fridge3,fridge4)
        
        self.play(Write(w))
        self.wait(2)
        
        w.start_wave()
        
        self.move_camera(60 * DEGREES,-45 * DEGREES,zoom=0.5,run_time=4)
        self.add(l1,l2,l7)
        self.play(Create(fridge1),run_time=0.5)
        self.play(Create(fridge2),run_time=0.5)
        self.play(Create(fridge3),run_time=0.5)
        self.play(Create(fridge4),run_time=0.5)
        self.wait(3)
        self.move_camera(60 * DEGREES,180 * DEGREES,zoom=0.5,run_time=4)
        self.wait(3)
        self.play(Uncreate(l7))
        wave1.start_wave()
        self.play(Create(wave1))
        self.move_camera(40 * DEGREES,
                         180 * DEGREES,
                         zoom=0.5,
                         frame_center=np.array([5,0,0]),
                         run_time=4)
        self.move_camera(20 * DEGREES,
                         180 * DEGREES,
                         zoom=0.5,
                         frame_center=np.array([5,0,0]),
                         run_time=4)
        self.wait(10)
        wave2.start_wave()
        wave1.stop_wave()
        w.stop_wave()
        self.wait(1.5)
        self.play(Uncreate(l1),run_time=0.5)
        self.play(Uncreate(l2),run_time=0.5)
        self.play(Create(l3))
        self.play(Create(l6))
        w.start_wave()
        self.play(ReplacementTransform(wave1,wave2))
        self.move_camera(40 * DEGREES,
                         180 * DEGREES,
                         zoom=0.5,
                         frame_center=np.array([5,0,0]),
                         run_time=4)
        self.wait(4)
        w.stop_wave()
        self.play(Uncreate(l6),run_time=0.5)
        self.play(Create(l4),run_time=0.5)
        self.play(Create(l5),run_time=0.5)
        wave3.start_wave()
        w.start_wave()
        self.play(ReplacementTransform(wave2,wave3))
        self.wait(4)
        self.move_camera(40 * DEGREES,
                         180 * DEGREES,
                         zoom=0.3,
                         frame_center=np.array([5,0,0]),
                         run_time=3)
        self.move_camera(40 * DEGREES,
                         180 * DEGREES,
                         zoom=0.6,
                         frame_center=np.array([5,0,0]),
                         run_time=3)
        self.move_camera(40 * DEGREES,
                         150 * DEGREES,
                         zoom=0.5,
                         frame_center=np.array([5,0,0]),
                         run_time=4)                 
        self.move_camera(40 * DEGREES,
                         210 * DEGREES,
                         zoom=0.6,
                         frame_center=np.array([5,0,0]),
                         run_time=8)
        self.wait(6)




        



        




        

        