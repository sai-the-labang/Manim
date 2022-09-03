from manim import*
import random




class ShowIncreasingSubsetsScene(Scene):
            def construct(self):
                p = VGroup(Dot(), Square(), Triangle()).arrange()
                self.add(p)
                self.play(DrawBorderThenFill(p))
                self.wait()
