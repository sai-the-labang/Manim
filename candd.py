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

        

        self.play(DrawBorderThenFill(ax))

        self.play(Write(labs))
        self.play(Wiggle(labs))
        self.play(ReplacementTransform(labs,sin))

        self.play(Write(labc))
        self.play(Wiggle(labc))
        self.play(ReplacementTransform(labc,cos))
        self.wait(2)

        self.play(Write(labsc))
        self.play(Wiggle(labsc))
        self.play(ReplacementTransform(labsc,sc))
        self.play(Indicate(sc))

        self.play(self.camera.frame.animate.move_to(ax.c2p(PI/4,0)).scale(0.5))
        
        for k in [PI/4,5*PI/4,PI/2,2.6]:
            ls=DashedLine(start=ax.c2p(k,0),
                      end=ax.c2p(k,sin.underlying_function(k)),
                      color=BLUE
            )
            lc=DashedLine(start=ax.c2p(k,0),
                      end=ax.c2p(k,cos.underlying_function(k)),
                      color=PURPLE
            ).shift(RIGHT * 0.3)
        
            lsc=Line(
            start=ax.c2p(k,0),
            end=ax.c2p(k,sc.underlying_function(k)),
            color=BLACK
            )

            self.play(self.camera.frame.animate.move_to(ax.c2p(k,0)))
            def up(mob):
             mob.animate(run_time=0.5).move_to(ax.c2p(k,0))
    
            self.camera.frame.add_updater(up)

            d1=Dot().move_to(ax.c2p(k,sin.underlying_function(k)))
        
            self.play(FocusOn(d1))
            self.play(Create(ls))
            self.play(Create(lc))
            self.play(lc.animate.shift(LEFT * 0.3))

            if len(ls)==len(lc) and sin.underlying_function(k)>0 and cos.underlying_function(k)>0 :
              self.play(ls.animate.shift(UP * lc.get_length()))
              self.play(Create(lsc))
              self.play(Uncreate(ls))
              self.play(Uncreate(lc))
            elif len(ls)==len(lc) and sin.underlying_function(k)<0 and cos.underlying_function(k)<0 :
              self.play(ls.animate.shift(DOWN * lc.get_length()))   
              self.play(Create(lsc))
              self.play(Uncreate(ls))
              self.play(Uncreate(lc)) 
            
             
              
            elif sin.underlying_function(k)>0 and cos.underlying_function(k)<0 :
              self.play(ls.animate.shift(DOWN * lc.get_length())) 
              self.play(Create(lsc))
              self.remove(ls)
              self.remove(lc)
            else :
                self.play(Transform(ls,lsc))
        
        self.camera.frame.remove_updater(up)  
        self.play(Restore(self.camera.frame))
        
        self.wait()


       
