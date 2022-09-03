from manim import*
class BraceExample(Scene):
            def construct(self):
                k=ValueTracker(-2)
                t=ValueTracker(3)
                s = Line(start=np.array([k,0,0]),end=np.array([t,0,0]))
                s.add_updater(lambda h:h.become(Line(start=np.array([k,0,0]),end=np.array([t,0,0]))))
                
                self.add(s)