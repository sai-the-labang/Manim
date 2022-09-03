from manim import*

class Intro(Scene):
    def welcome(self):
        color=[BLUE,RED,GREEN,GREY,WHITE,PINK,ORANGE]
        wel=Text(
              "ကြိုဆိုပါတယ်",font="Myanmar Text",color=WHITE
        )
        self.play(Write(wel))







    def construct(self):
        self.welcome()
        self.wait()