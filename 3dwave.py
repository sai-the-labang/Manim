from manim import *
import numpy as np 

class Waves(ThreeDScene):
    def construct(self):
 
     self.set_camera_orientation(theta=-35 * DEGREES,phi=70 * DEGREES)
     ax=ThreeDAxes()
     pc=ax.get_parametric_curve(lambda x:np.array([np.sin(x),np.cos(x),x]))
     sin=ax.plot(lambda x: np.sin(x))

     
     self.add(ax,pc)
     self.play(self.begin_ambient_camera_rotation(2 *PI))

