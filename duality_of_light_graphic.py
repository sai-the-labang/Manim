from manim import *
import random
from manim_physics import*
from colour import Color

class Graphic(MovingCameraScene):
    def construct(self):
        self.camera.background_color=BC
        self.camera.frame.move_to(np.array([1900,0,0])).scale(10)
        self.camera.frame.save_state()
        
        self.ages()
    def ages(self):
        ax1=Axes(
            x_range=[0,2000],y_range=[-1,1],x_length=700
         ).set_scale(0.5).move_to(RIGHT*4+DOWN)
        
        home="D:\picture footages"
        nt=ImageMobject(f"{home}\\gettyimages-90733811.jpg").move_to(ax1.c2p(1643,5))
        ch=ImageMobject(f"{home}\\Christiaan_Huygens-painting-099aedfef46c44d894328dab890d2942.jpeg").move_to(ax1.c2p(1629,-4))
        ty=ImageMobject(f"{home}\\Thomas_Young_by_Briggs.jpg").move_to(ax1.c2p(1800,5))
        jcm=ImageMobject(f"{home}\\GettyImages-525524956-5c739b2846e0fb0001076317.jpg").move_to(ax1.c2p(1860,-5)).scale(1.6)
        mp=ImageMobject(f"{home}\\Max_Planck_1933.jpg").move_to(ax1.c2p(1900,5)).scale(0.5)
        ae=ImageMobject(f"{home}\\gettyimages-3091504.jpg").move_to(ax1.c2p(1915,-5))

        nt2=nt.copy().scale(10)
        
        tnt=Tex("Issac Newton","(1643-1727)",font_size=200,color=BLACK)
        tch=Tex("Christiaan Huygens","(1629-1695)",font_size=200,color=BLACK)
        tty=Tex("Thomas Young","(1773-1829)",font_size=200,color=BLACK)
        tjcm=Tex("James Clerk Maxwell","(1831-1879)",font_size=200,color=BLACK)
        tmp=Tex("Max Planck","(1858-1947)",font_size=200,color=BLACK)
        tae=Tex("Albert Einstein","(1879-1955)",font_size=200,color=BLACK)

        tnt[0].next_to(nt,DOWN*2)
        tch[0].next_to(ch,DOWN*2)
        tty[0].next_to(ty,DOWN*2)
        tjcm[0].next_to(jcm,DOWN*2)
        tmp[0].next_to(mp,DOWN*2)
        tae[0].next_to(ae,DOWN*2)

        line_to_scientists=VGroup()
        line1=DashedLine(color=BLACK,stroke_width=60,start=ax1.c2p(1629,0),end=ch.get_top())
        line2=DashedLine(color=BLACK,stroke_width=60,start=ax1.c2p(1860,0),end=jcm.get_top())
        line3=DashedLine(color=BLACK,stroke_width=60,start=ax1.c2p(1915,0),end=ae.get_top())
        line_to_scientists.add(line1,line2,line3)
        
        names_and_age=VGroup(tnt,tch,tty,tjcm,tmp,tae)
        for d in names_and_age:
            d[1].next_to(d[0],DOWN)

        
        
        
        
        l1=Line(
            start=ax1.c2p(0,0),end=ax1.c2p(2000,0),stroke_width=50,stroke_color=AC
            )
        n=VGroup()
        t=VGroup()
        for number in np.arange(0,2000,50):
                nb=Tex(number,font_size=200,color=AC)
                nb.move_to(ax1.c2p(number,1))
                tips=Line(
                    start=ax1.c2p(number,-0.5),end=ax1.c2p(number,0.5),stroke_width=40,stroke_color=AC
                )
                n.add(nb)
                t.add(tips)
        timeline=VGroup(n,t,l1)
        
        
        
        
        self.add(timeline)
        self.add(nt,ch,ty,jcm,mp,ae)
        self.add(names_and_age,line_to_scientists)
       
        
        
        
        self.play(self.camera.frame.animate.move_to(nt).scale(0.5),run_time=3)
        self.wait()
        self.play(self.camera.frame.animate.move_to(ch),
        ty.animate.set_opacity(0.2),tty.animate.set_opacity(0.2),

        run_time=1
        )
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(ty),
        ty.animate.set_opacity(1),tty.animate.set_opacity(1),
        jcm.animate.set_opacity(0.2),tjcm.animate.set_opacity(0.2),
        mp.animate.set_opacity(0.2),tmp.animate.set_opacity(0.2),
        run_time=1
        )
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(jcm),
        jcm.animate.set_opacity(1),tjcm.animate.set_opacity(1),
        mp.animate.set_opacity(0.2),tmp.animate.set_opacity(0.2),
        ae.animate.set_opacity(0.2),tae.animate.set_opacity(0.2),
        run_time=1
        )
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(mp),
        mp.animate.set_opacity(1),tmp.animate.set_opacity(1),
        ty.animate.set_opacity(0.2),tty.animate.set_opacity(0.2),
        run_time=1
        )
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(ae),
        ae.animate.set_opacity(1),tae.animate.set_opacity(1),
        mp.animate.set_opacity(0.2),tmp.animate.set_opacity(0.2),
        jcm.animate.set_opacity(0.2),tjcm.animate.set_opacity(0.2),
        run_time=1
        )
        self.wait(4)
        
        self.wait()
        