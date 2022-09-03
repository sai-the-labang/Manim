from manim import *
home="D:\Randoledge\goblin"

class Goblin(MovingCameraScene):
    def construct(self):
        

        kobold=ImageMobject(f"{home}\\486px-kobold_artlibre_jnl.jpg").shift(UP*10+LEFT*10).scale(1.8)
        hobgoblin1=ImageMobject(f"{home}\\ca9f4009e10cb2569ca730ce69f91faa.jpg").next_to(kobold,RIGHT,buff=5).scale(2.5)
        hobgoblin2=ImageMobject(f"{home}\\index.jpg").scale(2.5).next_to(hobgoblin1,RIGHT,buff=0.1)
        knocker1=ImageMobject(f"{home}\\knocker 3.jpg").next_to(hobgoblin2,RIGHT,buff=5)
        knocker2=ImageMobject(f"{home}\\knocker.jpg").next_to(knocker1,RIGHT,buff=0.1)
        phooka1=ImageMobject(f"{home}\\phooka.jpg").scale(1.5).next_to(knocker2,RIGHT,buff=5)
        phooka2=ImageMobject(f"{home}\\phooka.jpeg").scale(1.5).next_to(phooka1,RIGHT,buff=0.1)
        bogey=ImageMobject(f"{home}\\e5356d469a0b6b6e2fac218dab763610--the-cheese-the-stick.jpg").scale(3.3).next_to(kobold,DOWN,buff=10)
        hogboon=ImageMobject(f"{home}\\oldmangob.jpg").next_to(bogey,RIGHT,buff=5)
        tengu1=ImageMobject(f"{home}\\tengu.jpg").scale(2.5).next_to(hogboon,RIGHT,buff=5)
        tengu2=ImageMobject(f"{home}\\tengu 2.jpg").next_to(tengu1,RIGHT,buff=0.1)
        kolksu1=ImageMobject(f"{home}\\kol ksu.jpg").scale(1.5).next_to(tengu2,RIGHT,buff=5)
        kolksu2=ImageMobject(f"{home}\\kol ksu2.jpg").scale(2.5).next_to(kolksu1,RIGHT,buff=0.1)

       #all=VGroup(*[
       #    kobold,hobgoblin1,hobgoblin2,
       #    hobgoblin2,knocker1,knocker2,
       #    phooka1,phooka2,bogey,
       #    hogboon,tengu1,tengu2,kolksu1,kolksu2
       #])
        
        hobs=[hobgoblin1,hobgoblin2]
        knocks=[knocker1,knocker2]
        phoos=[phooka1,phooka2]
        tens=[tengu1,tengu2]
        kols=[kolksu1,kolksu2]
        
        
        kotex=Tex("1.Kobold").next_to(kobold,DOWN,buff=0.8).scale(2)
        hobtex=Tex("2.Hobgoblin").next_to(hobgoblin1,DOWN,buff=0.8).shift(RIGHT*3).scale(2)
        knocktex=Tex("3.Knocker").next_to(knocker1,DOWN,buff=1).shift(RIGHT*3).scale(2)
        phootex=Tex("4.Phooka").next_to(phooka1,DOWN,buff=1).shift(RIGHT*3).scale(2)
        botex=Tex("5.Bogey").next_to(bogey,DOWN,buff=1).scale(2)
        hogtex=Tex("6.Hogboon").next_to(hogboon,DOWN,buff=1).scale(2.5)
        tentex=Tex("7.Tengu").next_to(tengu2,DOWN,buff=1).shift(LEFT*3).scale(2)
        koltex=Tex("8.Kol'Ksu").next_to(kolksu1,DOWN,buff=1).shift(RIGHT*3).scale(2)

        alltex=VGroup(*[kotex,hobtex,knocktex,phootex,botex,hogtex,tentex,koltex])


        self.camera.frame.move_to(knocktex).scale(5)
        self.camera.frame.save_state()



        
        self.add(kobold,hobgoblin1,hobgoblin2,
            hobgoblin2,knocker1,knocker2,
            phooka1,phooka2,bogey,
            hogboon,tengu1,tengu2,kolksu1,kolksu2,alltex)
        self.wait(3)

        self.play(
            self.camera.frame.animate.move_to(kobold).scale(0.3),

            kobold.animate.set_opacity(1),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(1),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )  
        self.wait(26)  

        self.play(
            self.camera.frame.animate.move_to(hobgoblin2.get_left()).scale(1),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(1),hobgoblin2.animate.set_opacity(1),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(1),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(13)

        self.play(
            self.camera.frame.animate.move_to(knocker2.get_left()).scale(1.3333),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(1),knocker2.animate.set_opacity(1),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(1),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(10)

        self.play(
            self.camera.frame.animate.move_to(phooka2.get_left()).scale(0.7),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(1),phooka2.animate.set_opacity(1),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(1),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(10)

        self.play(
            self.camera.frame.animate.move_to(bogey).scale(1),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(1),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(1),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(5)

        self.play(
            self.camera.frame.animate.move_to(hogboon).scale(1),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(1),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(1),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(9)

        self.play(
            self.camera.frame.animate.move_to(tengu2.get_left()).scale(1.333),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(1),tengu2.animate.set_opacity(1),
            kolksu1.animate.set_opacity(0.2),kolksu2.animate.set_opacity(0.2),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(1),koltex.animate.set_opacity(0.2),
            run_time=1
        )
        self.wait(13)

        self.play(
            self.camera.frame.animate.move_to(kolksu2.get_left()).scale(0.7),

            kobold.animate.set_opacity(0.2),hobgoblin1.animate.set_opacity(0.2),hobgoblin2.animate.set_opacity(0.2),
            knocker1.animate.set_opacity(0.2),knocker2.animate.set_opacity(0.2),
            phooka1.animate.set_opacity(0.2),phooka2.animate.set_opacity(0.2),bogey.animate.set_opacity(0.2),
            hogboon.animate.set_opacity(0.2),tengu1.animate.set_opacity(0.2),tengu2.animate.set_opacity(0.2),
            kolksu1.animate.set_opacity(1),kolksu2.animate.set_opacity(1),

            kotex.animate.set_opacity(0.2),hobtex.animate.set_opacity(0.2),knocktex.animate.set_opacity(0.2),phootex.animate.set_opacity(0.2),
            botex.animate.set_opacity(0.2),hogtex.animate.set_opacity(0.2),tentex.animate.set_opacity(0.2),koltex.animate.set_opacity(1),
            run_time=1
        )
        self.play(
            

            kobold.animate.set_opacity(1),hobgoblin1.animate.set_opacity(1),hobgoblin2.animate.set_opacity(1),
            knocker1.animate.set_opacity(1),knocker2.animate.set_opacity(1),
            phooka1.animate.set_opacity(1),phooka2.animate.set_opacity(1),bogey.animate.set_opacity(1),
            hogboon.animate.set_opacity(1),tengu1.animate.set_opacity(1),tengu2.animate.set_opacity(1),
            kolksu1.animate.set_opacity(1),kolksu2.animate.set_opacity(1),

            kotex.animate.set_opacity(1),hobtex.animate.set_opacity(1),knocktex.animate.set_opacity(1),phootex.animate.set_opacity(1),
            botex.animate.set_opacity(1),hogtex.animate.set_opacity(1),tentex.animate.set_opacity(1),koltex.animate.set_opacity(1),
            run_time=1
        )
        self.wait(13)
        self.play(Restore(self.camera.frame))
        self.wait(5)