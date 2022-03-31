from manim import *
import numpy as np 

class Consndes(MovingCameraScene):
    def construct(self):
        self.camera.background_color=BC
        self.camera.frame.save_state()

        title=Tex()
        ax=Axes(x_range=[0,8.1,1],
                y_range=[-3.1,3.1,1],
                tips=False
                
                
                ).set_color("#5e5031")

        sin=ax.plot(lambda x: np.sin(x),
                              x_range=[0,8],
                              color=BLUE
                        
                    )
        cos=ax.plot(lambda x: np.cos(x),

                              x_range=[0,8],
                              color=PURPLE
                              
                    )
        sc=ax.plot(lambda x: np.cos(x)+np.sin(x),
                              x_range=[0,8],
                              color=BLACK
                              
                  )
        labs=MathTex("sin(x)",
                color=BLUE
        ).move_to(UR *1.5)    

        labc=MathTex("cos(x)",
                color=PURPLE
        ).move_to(UR *1.5)  

        labsc=MathTex("sin(x)+cos(x)",
                color=BLACK
        ).move_to(UR * 1.5) 


        self.add(VGroup(ax,sin,cos,sc))
        self.wait()
        self.play(Transform(sin,sc),Transform(cos,sc))    
        self.wait()