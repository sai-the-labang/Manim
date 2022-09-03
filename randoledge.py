from manim import*
import random




class Intro(Scene):
    def construct(self):

        random_postion=np.array([random.randrange(-9,9),random.randrange(-6,6),0])
        random_tex=VGroup(
            *[Tex("R").move_to(np.array([random.randrange(-9,9),random.randrange(-6,6),0])),
            Tex("a").move_to(np.array([random.randrange(-9,9),random.randrange(-6,6),0])),
            Tex("n").move_to(np.array([random.randrange(-9,9),random.randrange(-6,6),0])),
            Tex("d").move_to(np.array([random.randrange(-9,9),random.randrange(-6,6),0])),
            Tex("0").move_to(np.array([random.randrange(-9,9),random.randrange(-6,6),0])) ]
        )

        t1=Text("R a n d o",font="Georgia",font_size=30).move_to(np.array((-0.8,0,0)))
        t2=Text("l e d g e",font="Georgia",font_size=30).next_to(t1[4],RIGHT,buff=0.1)
        t12=VGroup(t1,t2)
        t3=Text("'Goblin 101'",font="Gabriola",font_size=40)
        t2.rotate(3*PI/4,about_point=t2[0].get_center())
        home="D:\Randoledge\Intro stuffs"

        st0=SVGMobject(f"{home}\\minotaur-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)

        st1=SVGMobject(f"{home}\\cross-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st2=SVGMobject(f"{home}\\double-integral-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st3=SVGMobject(f"{home}\\bouzouki-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st4=SVGMobject(f"{home}\\creep-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st5=SVGMobject(f"{home}\\flask-science-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st6=SVGMobject(f"{home}\\laptop-computer-coding-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st7=SVGMobject(f"{home}\\podcast-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st8=SVGMobject(f"{home}\\intersex-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st9=SVGMobject(f"{home}\\twitter-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st10=SVGMobject(f"{home}\\poker-cards-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st11=SVGMobject(f"{home}\\uprising-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st12=SVGMobject(f"{home}\\viking-helmet-svgrepo-com(1).svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st13=SVGMobject(f"{home}\\detective-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st14=SVGMobject(f"{home}\\omega-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st15=SVGMobject(f"{home}\\polis-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st16=SVGMobject(f"{home}\\pulse-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st17=SVGMobject(f"{home}\\science-svgrepo-com(1).svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st18=SVGMobject(f"{home}\\ghost-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st19=SVGMobject(f"{home}\\brain-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st20=SVGMobject(f"{home}\\sword-fill-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)

        st21=SVGMobject(f"{home}\\ufo-alien-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)
        st22=SVGMobject(f"{home}\\goblin-head-svgrepo-com.svg").set_color(WHITE).scale(0.3).next_to(t3,DOWN)
        st23=SVGMobject(f"{home}\\god-svgrepo-com.svg").set_color(WHITE).scale(0.2).next_to(t3,DOWN)

        stickers=VGroup(*[
            st1,st2,st3,st4,st5,
            st6,st7,st8,st9,st10,
            st11,st12,st13,st14,st15,
            st16,st17,st18,st19,st20
        ]
        )
        
        

       #self.play(
       #    ReplacementTransform(random_tex[0],t1[0]),
       #    ReplacementTransform(random_tex[1],t1[1]),
       #    ReplacementTransform(random_tex[2],t1[2]),
       #    ReplacementTransform(random_tex[3],t1[3]),
       #    ReplacementTransform(random_tex[4],t3),
       #)
        self.play(
            ReplacementTransform(random_tex,t1,lag_ratio=0.2)
        )
        self.wait(0.5)
        self.play(Create(st0),Write(t2))
        self.wait(0.3)
        self.remove(st0)
        randomed_stickers=VGroup(*[])
        random_numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        for i in range(17):
            number_to_add=Integer(random.choice(random_numbers))
            random_numbers.remove(number_to_add.get_value())
            randomed_stickers.add(stickers[number_to_add.get_value()])
            self.add(stickers[number_to_add.get_value()])
            self.play(t2.animate.rotate(7.941176470588235*DEGREES,about_point=t2[0].get_center(),axis=IN),run_time=0.18)
            self.remove(stickers[number_to_add.get_value()])

        self.add(st21)    
        self.wait(1)
        
        self.play(ReplacementTransform(t12,t3),ReplacementTransform(st21,st22))
        
        self.wait(2)
        self.play(FadeOut(t3),FadeOut(st22))

class Outro(Scene):
    def construct(self):
        presenter_tex=Text("presented by",font="Georgia",font_size=30).shift(LEFT*0.8)    
        presenter_name=Text("Saimuchi",font="MV Boli",font_size=30).next_to(presenter_tex,RIGHT).shift(UP*0.04)
        editor_tex=Text("edited by",font="Georgia",font_size=15).shift(DOWN*3+RIGHT*2)
        editor_name=Text("nawtorious",font="MV Boli",font_size=15).next_to(editor_tex,RIGHT*0.35)
        ty_tex=Text("Thanks for watching",font="Georgia",font_size=40)
        
        texts=VGroup(presenter_tex,presenter_name)
        self.play(Write(presenter_tex))
        self.wait(0.5)
        self.play(Write(presenter_name))
        self.wait(0.5)
        self.play(Write(editor_tex),Write(editor_name))
        self.wait(2)
        self.remove(editor_name,editor_tex)
        self.play(ReplacementTransform(texts,ty_tex))
        self.wait(2)



         