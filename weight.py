from manim import*
from manim_physics import*
import numpy as np

home="D:\For Physics.bayta\Weightlessness"
class Intro(Scene):

    def newton_3rd_law(self):

        
        ground=Line(start=LEFT*10,end=RIGHT*10).shift(DOWN*2)  
        boy=SVGMobject(f"{home}\\1553709145.svg").next_to(ground,UP,buff=0)
        title=Title("Newton's 3rd Law")

        a1=Arrow(start=LEFT,end=LEFT+DOWN*2)
        F=Tex("F=mg").next_to(a1,DOWN*1.5)
        a2=Arrow(start=RIGHT+DOWN*2,end=RIGHT)
        Fs=MathTex("F_{s}=mg").next_to(a2,UP)
        action=VGroup(a1,F)
        reaction=VGroup(a2,Fs)
        
        
        Fsw=MathTex("F_{s}=weight",font_size=50).to_edge(RIGHT+UP,buff=2).set_color(GREEN)
        Fw=MathTex(r"F\not=weight",font_size=50).next_to(Fsw,DOWN).set_color(RED)
        

        action_tex=Tex("(action)").next_to(F,RIGHT)
        reaction_tex=Tex("(reaction)").next_to(Fs,RIGHT)

        at_and_rat=Tex("action","=reaction").next_to(boy,(UP+LEFT)*3)
        al=VGroup(boy,ground,title,action,reaction,Fsw,Fw,action_tex,reaction_tex,at_and_rat)

        self.play(Create(ground))
        self.play(Create(boy))
        self.play(Create(action))
        self.wait(4)
        self.play(Create(reaction)) 
        self.wait(4)
        self.play(Create(title))
        self.play(Create(action_tex))
        self.play(Create(reaction_tex))
        self.wait(5)
        self.play(ReplacementTransform(action_tex.copy(),at_and_rat[0]))
        self.wait()
        self.play(ReplacementTransform(reaction_tex.copy(),at_and_rat[1]))
        self.wait(5)
        self.play(ReplacementTransform(F.copy(),Fw))
        self.wait(4)
        self.play(ReplacementTransform(Fs.copy(),Fsw))
        self.wait(4)
        self.play(Indicate(Fsw,scale_factor=1.5),Indicate(Fw,scale_factor=1.5))
        self.wait()
        self.play(Uncreate(al))
        self.wait()
        
    def construct(self):
        self.newton_3rd_law()  

class Weight_Update(Scene):
    def weight_in_elevator(self):
        
        b=self.b=ValueTracker(-10)

        #Elevator#####################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-30,30],y_length=15
        ).shift(LEFT*4.5)
        
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)

        aclrtion_arrow=Arrow(
            start=ax2.c2p(-3,b.get_value()-2),end=ax2.c2p(-3,b.get_value()+2)
        ).set_color(RED)
        aclrtion_arrow.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(-3,b.get_value()-2),end=ax2.c2p(-3,b.get_value()+10)
        ).set_color(RED)))
        aclrtion_a=Tex(r"a").next_to(aclrtion_arrow,UP).set_color(RED)
        aclrtion_a.add_updater(lambda h:h.become(Tex(r"a").next_to(aclrtion_arrow,UP).set_color(RED)))
        aclrtion=VGroup(aclrtion_arrow,aclrtion_a)

        
        equpdate1=MathTex("F_{s}-mg=ma",font_size=40).next_to(head,RIGHT*5)
        equpdate2=MathTex("F_{s}=","m","(","g","+a)",font_size=40).next_to(equpdate1,DOWN)

        a1=Arrow(
            start=ax2.c2p(-1,b.get_value()+2),
            end=ax2.c2p(-1,b.get_value()-2)
        )
        a1.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(-1,b.get_value()+2),
            end=ax2.c2p(-1,b.get_value()-2)
        )))
        F=Tex("mg").next_to(a1,DOWN*1.5)
        F.add_updater(lambda h:h.become(Tex("mg").next_to(a1,DOWN*1.5)))

        a2=Arrow(
            start=ax2.c2p(1,b.get_value()-2),
            end=ax2.c2p(1,b.get_value()+2)
        )
        a2.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(1,b.get_value()-2),
            end=ax2.c2p(1,b.get_value()+2)
        )))
        Fs=MathTex("F_{s}").next_to(a2,UP)
        Fs.add_updater(lambda h:h.become(MathTex("F_{s}").next_to(a2,UP)))
        action=VGroup(a1,F)
        reaction=VGroup(a2,Fs)

        fs_weight=MathTex("F_{s}=","weight",font_size=50)
        fs_weight[1].set_color(BLUE)

        g_val=MathTex(r"g=9.8ms^{-2}").to_edge(UP+RIGHT,buff=2)

        self.play(Create(elvt))
        self.wait(3)
        self.play(Create(aclrtion))
        self.wait(3 )
        
        self.play(b.animate.set_value(30),run_time=1.5,rate_func=rate_functions.ease_in_cubic)
        b.set_value(-10)
        
        self.play(b.animate.set_value(30),run_time=1.5,rate_func=rate_functions.ease_in_cubic)
        b.set_value(-10)
        self.wait()
        
        self.play(Write(action))
        self.wait(3)
        self.play(Write(reaction))
        self.wait(6)
        
        self.play(Write(equpdate1))
        self.wait()
        self.play(Write(equpdate2))
        self.wait(5)
        self.play(Write(fs_weight))
        self.wait()
        self.play(fs_weight.animate.to_corner(RIGHT+DOWN))
        self.play(Create(g_val))
        self.play(Indicate(g_val,scale_factor=2))
        self.play(Indicate(equpdate2[1]))
        self.wait()
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait()
        self.play(Indicate(equpdate2[1],scale_factor=2),Indicate(aclrtion_a,scale_factor=2))
        self.wait()
        self.play(Indicate(equpdate2[1],scale_factor=2),Indicate(aclrtion_a,scale_factor=2))
        self.wait()
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait(2)
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait(2)
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait(2)
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait(2)
        self.play(b.animate.set_value(30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(-10)
        self.wait(2)
        self.remove(elvt,aclrtion,action,reaction,equpdate1,equpdate2,g_val,fs_weight)

    def weight_in_elevator2(self):
        b=self.b=ValueTracker(10)

        #Elevator#####################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-30,30],y_length=15
        ).shift(LEFT*4.5)
        
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)

        #action_and_reaction###################################################################################
        a1=Arrow(
            start=ax2.c2p(-1,b.get_value()+2),
            end=ax2.c2p(-1,b.get_value()-2)
        )
        a1.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(-1,b.get_value()+2),
            end=ax2.c2p(-1,b.get_value()-2)
        )))
        F=Tex("mg").next_to(a1,DOWN*1.5)
        F.add_updater(lambda h:h.become(Tex("mg").next_to(a1,DOWN*1.5)))

        a2=Arrow(
            start=ax2.c2p(1,b.get_value()-2),
            end=ax2.c2p(1,b.get_value()+2)
        )
        a2.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(1,b.get_value()-2),
            end=ax2.c2p(1,b.get_value()+2)
        )))
        Fs=MathTex("F_{s}").next_to(a2,UP)
        Fs.add_updater(lambda h:h.become(MathTex("F_{s}").next_to(a2,UP)))
        action=VGroup(a1,F)
        reaction=VGroup(a2,Fs)
        #weight_update#########################################################
        
        equpdate3=MathTex("ma=mg-F_{s}",font_size=40).next_to(head,RIGHT*5)
        equpdate4=MathTex("F_{s}=m(g","-","a",")",font_size=40).next_to(equpdate3,DOWN)

        #acceleration_arrow#################################################
        aclrtion_arrow2=Arrow(
            start=ax2.c2p(-3,b.get_value()+10),end=ax2.c2p(-3,b.get_value()-2)
        ).set_color(RED)
        aclrtion_arrow2.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(-3,b.get_value()+10),end=ax2.c2p(-3,b.get_value()-2)
        ).set_color(RED)))
        aclrtion_a2=Tex(r"a").next_to(aclrtion_arrow2,DOWN).set_color(RED)
        aclrtion_a2.add_updater(lambda h:h.become(Tex(r"a").next_to(aclrtion_arrow2,DOWN).set_color(RED)))
        aclrtion2=VGroup(aclrtion_arrow2,aclrtion_a2)


        self.play(Create(elvt))
        self.wait()
        self.play(Create(aclrtion2))
        self.wait()
        
        
        self.play(b.animate.set_value(-30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(10)
        self.wait()
        
        
        
        self.play(Write(action))
        self.play(Write(reaction))
        self.wait(3)
        
        self.play(Write(equpdate3))
        self.wait()
        self.play(Write(equpdate4))
        self.wait()
        self.play(Indicate(equpdate4[1],scale_factor=1.5))
        self.play(b.animate.set_value(-30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(10)
        self.wait()
        self.play(Indicate(equpdate4[2],scale_factor=2),Indicate(aclrtion_a2,scale_factor=2))
        self.wait()
        self.play(Indicate(equpdate4[2],scale_factor=2),Indicate(aclrtion_a2,scale_factor=2))
        self.wait()
        self.play(b.animate.set_value(-30),run_time=2,rate_func=rate_functions.ease_out_cubic)
        b.set_value(10)
        self.wait(5)
        self.remove(elvt,aclrtion2,action,reaction,equpdate3,equpdate4)
    
    def weight_gain_and_loss(self):
        c=self.c=ValueTracker(0)
        a=self.a=ValueTracker(0)
        b=self.b=ValueTracker(-10)
        #Graphs##################################################################################
        ax1=Axes(
            x_range=[0,50,4],
            y_range=[0,600,100],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
                

            },
            y_axis_config={
                "numbers_to_include":np.arange(0,600,100)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).shift(RIGHT*3)

        ax1_labels=ax1.get_axis_labels(
            Tex("time"),Tex("weight")
        )
        
        
        path1 = VMobject()
        dot1 = Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))
        dot1.add_updater(lambda h:h.become(Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))))
        
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path1(path1):
            previous_path1 = path1.copy()
            previous_path1.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path1)
        path1.add_updater(update_path1)
        graph=VGroup(ax1,path1,dot1,ax1_labels)

        path2=VMobject()
        path2.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path2(path2):
            previous_path2 = path2.copy()
            previous_path2.add_points_as_corners([dot1.get_center()])
            path2.become(previous_path2)
        path2.add_updater(update_path2)

        path3=VMobject()
        path3.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot1.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)

        path4=VMobject()
        path4.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path4(path4):
            previous_path4 = path4.copy()
            previous_path4.add_points_as_corners([dot1.get_center()])
            path4.become(previous_path4)
        path4.add_updater(update_path4)
  
        #Elevator##################################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-30,30],y_length=15
        ).shift(LEFT*4.5)
        
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)
        
        
        self.play(Create(elvt))
        self.play(Create(graph))
        self.wait(2)
        #Weight_gain
        self.play(b.animate.set_value(30),a.animate.set_value(-8),c.animate.set_value(10),run_time=3,rate_func=rate_functions.ease_in_cubic)
        
        self.remove(dot1,path1)
        b.set_value(-10)
        a.set_value(0)
        c.set_value(0)
        self.add(dot1,path2)
        #weight_gain
        self.play(b.animate.set_value(30),a.animate.set_value(-8),c.animate.set_value(10),run_time=3,rate_func=rate_functions.ease_in_cubic)
        self.remove(elvt,dot1,path2)
        
        #Weight_loss
        b.set_value(10)
        a.set_value(0)
        c.set_value(0)
        self.wait()
        self.play(Create(elvt))
        self.play(Create(dot1))
        self.add(path3)
        self.wait(4)
        self.play(b.animate.set_value(-30),a.animate.set_value(8),c.animate.set_value(10),run_time=3,rate_func=rate_functions.ease_in_cubic)
        self.remove(dot1,path3)
        
        #Weight_loss
        b.set_value(10)
        a.set_value(0)
        c.set_value(0)
        self.wait()
        self.add(dot1,path4)
        self.play(b.animate.set_value(-30),a.animate.set_value(8),c.animate.set_value(10),run_time=3,rate_func=rate_functions.ease_in_cubic)
        self.wait(3)
        self.play(Uncreate(graph))
        self.remove(path4)
        self.play(b.animate.set_value(0),run_time=2,rate_func=rate_functions.linear)
        self.wait(5)

    
    def construct(self):
        self.weight_in_elevator()
        self.weight_in_elevator2()
        self.weight_gain_and_loss()
        

class Weight_and_graph(Scene):
    def wt(self):
        a=self.a=ValueTracker(0)
        b=self.b=ValueTracker(10)
        c=self.c=ValueTracker(0)
  
        #Elevator#####################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-20,20],y_length=10
        ).shift(LEFT*4.5)
        
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)
        
        #Graphs##################################################################################
        ax1=Axes(
            x_range=[0,50,4],
            y_range=[0,600,100],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,600,100)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).to_corner(RIGHT+UP)

        ax1_labels=ax1.get_axis_labels(
            Tex("time"),Tex("weight")
        )
        
        
        path1 = VMobject()
        dot1 = Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))
        dot1.add_updater(lambda h:h.become(Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))))
        
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path1(path1):
            previous_path1 = path1.copy()
            previous_path1.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path1)
        path1.add_updater(update_path1)

        ax3=Axes(
            x_range=[0,50,4],
            y_range=[-10,10,2],
            x_length=8,
            y_length=6,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
                
            },
            y_axis_config={
                "numbers_to_include":np.arange(-10,10,2)
            },
            x_axis_config={
                "numbers_to_include":[]    
            }
        ).next_to(ax1,DOWN,buff=1)
        ax3_labels=ax3.get_axis_labels(
            Tex("time"),Tex("acceleration")
        )
        path2 = VMobject()
        dot2 = Dot().move_to(ax3.c2p(c.get_value(),a.get_value()))
        dot2.add_updater(lambda h:h.become(Dot().move_to(ax3.c2p(c.get_value(),a.get_value()))))
        
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        def update_path2(path2):
            previous_path2 = path2.copy()
            previous_path2.add_points_as_corners([dot2.get_center()])
            path2.become(previous_path2)
        path2.add_updater(update_path2)

        path3 = VMobject()
        path3.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot1.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)

        wt=VGroup(ax1,ax1_labels,path1,dot1)
        at=VGroup(ax3,ax3_labels,path2,dot2)

        #Equations
        eq1=MathTex("F_{s}=m(","g","+a)",font_size=40).next_to(ax1,DOWN*5)
        eq1help=Tex(r"$(a \rightarrow\ +   upward)$",font_size=30).next_to(eq1,RIGHT)
        eq1help.add_updater(
            lambda h:h.become(Tex(r"$(a \rightarrow\ +   upward)$",font_size=30).next_to(eq12,RIGHT))
        )
        eq2=MathTex("F_{s}=m(","g","-a)",font_size=40).next_to(eq1,DOWN*1.5)
        eq2help=Tex(r"$(a \rightarrow\ +   downward)$",font_size=30).next_to(eq2,RIGHT)
        eq2help.add_updater(
            lambda h:h.become(Tex(r"$(a \rightarrow\ +   downward)$",font_size=30).next_to(eq22,RIGHT))
        )
        eq12=MathTex(
            "Weight=m(","g","+","(",
            Integer(
                -a.get_value(),
                num_decimal_places=1,
                color=YELLOW
                ).set_color(YELLOW).get_value(),
            "))",
            font_size=40
        ).next_to(ax1,DOWN*5)

        eq12.add_updater(
            lambda h:h.become(
            MathTex("Weight=m(","g","+","(",
            Integer(
                -a.get_value(),
                num_decimal_places=1
                ).set_color(YELLOW).get_value(),
            "))",
            font_size=40
        ).next_to(ax1,DOWN*5)))

        eq22=MathTex(
            "Weight","=m(","g","-","(",
            Integer(
                a.get_value(),
                num_decimal_places=1,
                color=YELLOW
                ).get_value(),
            "))",
            font_size=40
        ).next_to(eq12,DOWN*1.5)
        eq22.add_updater(
            lambda h:h.become(MathTex(
                "Weight","=m(","g","-","(",
                Integer(
                    a.get_value(),
                    num_decimal_places=1
                    ).get_value(),
                "))",
                font_size=40
        ).next_to(eq12,DOWN*1.5)))
        
        #acceleration arrow
        aclrtion_arrow2=Arrow(
            start=ax2.c2p(-3,b.get_value()-2),end=ax2.c2p(-3,b.get_value()+10)
        ).set_color(RED)
        aclrtion_arrow2.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(-3,b.get_value()-2),end=ax2.c2p(-3,b.get_value()+10)
        ).set_color(RED)))
        aclrtion_a2=Tex(r"a").next_to(aclrtion_arrow2,UP).set_color(RED)
        aclrtion_a2.add_updater(lambda h:h.become(Tex(r"a").next_to(aclrtion_arrow2,UP).set_color(RED)))
        aclrtion2=VGroup(aclrtion_arrow2,aclrtion_a2)

        aclrtion_arrow3=Arrow(
            start=ax2.c2p(3,b.get_value()+2),end=ax2.c2p(3,b.get_value()-10)
        ).set_color(GREEN)
        aclrtion_arrow3.add_updater(lambda h:h.become(Arrow(
            start=ax2.c2p(3,b.get_value()+2),end=ax2.c2p(3,b.get_value()-10)
        ).set_color(GREEN)))
        aclrtion_a3=Tex(r"a").next_to(aclrtion_arrow3,DOWN).set_color(GREEN)
        aclrtion_a3.add_updater(lambda h:h.become(Tex(r"a").next_to(aclrtion_arrow3,DOWN).set_color(GREEN)))
        aclrtion3=VGroup(aclrtion_arrow3,aclrtion_a3)
        

        

        eq1s=VGroup(eq12,eq1help)
        eq2s=VGroup(eq22,eq2help)
        alleq=VGroup(eq1s,eq2s)
        rec=SurroundingRectangle(alleq,color=WHITE,buff=0.6)
        m_value=Tex("m=30kg",font_size=40).next_to(rec,LEFT*1.7)
        g_value=MathTex(r"g=9.8ms^{-2}",font_size=40).next_to(m_value,DOWN)
        
        #Just_showing_normal_elevator
        self.play(Create(elvt))
        self.play(b.animate.set_value(8),run_time=1.5,rate_func=rate_functions.ease_in_cubic)
        self.play(b.animate.set_value(-8),run_time=5,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(-10),run_time=1.5,rate_func=rate_functions.ease_out_cubic)
        self.wait()
        self.play(b.animate.set_value(-8),run_time=1.5,rate_func=rate_functions.ease_in_cubic)
        self.play(b.animate.set_value(8),run_time=5,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(10),run_time=1.5,rate_func=rate_functions.ease_out_cubic)

        #Writing_equation
        self.play(Write(eq1),Write(eq1help))
        
        self.wait(0.5)
        self.play(Write(eq2),Write(eq2help))
        
        self.play(Unwrite(eq1),Unwrite(eq2))
        self.play(Write(eq12),Write(eq22))
        self.play(Create(rec))
        self.play(Indicate(eq22,scale_factor=1.5))
        self.play(Indicate(eq12,scale_factor=1.5))
        self.wait(2)
        self.play(Indicate(eq1help,scale_factor=1.5))
        self.play(Indicate(eq2help,scale_factor=1.5))
        self.wait(3)
        self.play(Write(m_value))
        self.play(Write(g_value))
        self.wait(2)
        #Down
        self.play(Unwrite(eq1s))
        self.wait()
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            run_time=1.5
        )
        self.remove(aclrtion3)
        a.set_value(0)
        self.play(b.animate.set_value(-8),run_time=5,rate_func=rate_functions.linear)
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            run_time=1.5
        )
        a.set_value(0)
        self.remove(aclrtion2)
        
        self.wait()
        
        #Up
        self.play(Write(eq1s),Unwrite(eq2s))
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(-8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            run_time=1.5
        )
        a.set_value(0)
        self.remove(aclrtion2)
        
        self.play(b.animate.set_value(8),run_time=5,rate_func=rate_functions.linear)
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(10),
            a.animate(rate_func=rate_functions.linear).set_vlaue(-6),
            run_time=1.5
        )
        a.set_value(0)
        self.remove(aclrtion3)
        
        #Elvator_with_graph
        self.play(Create(wt))
        self.wait(2)
        
        #Down
        self.play(Unwrite(eq1s),Write(eq2s))
        self.wait()
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(3),run_time=1.5
        )
        self.remove(aclrtion3)
        a.set_value(0)

        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(-8),       
            c.animate(rate_func=rate_functions.linear).set_value(13),
            run_time=5
        )        
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(16),
            run_time=1.5
        )
        self.remove(aclrtion2)
        a.set_value(0)
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(19),
            run_time=1.5
        )
        
        #Up
        self.play(Write(eq1s),Unwrite(eq2s),run_time=0.5)
        self.wait()
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(-8),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(22),
            run_time=1.5
        )
        a.set_value(0)
        self.remove(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(8),       
            c.animate(rate_func=rate_functions.linear).set_value(32),
            run_time=5
        ) 
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(10),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(35),
            run_time=1.5
        )
        self.remove(aclrtion3)
        a.set_value(0)  
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(38),
            run_time=1.5
        )
        self.wait()
        self.remove(path1,dot1)
        self.wait()
        self.add(path3)
        c.set_value(0)
        self.play(Create(dot1))
 
        #Down
        self.play(Write(eq2s),Unwrite(eq1s),run_time=0.5)
        self.wait()
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(3),run_time=1.5
        )

        a.set_value(0)
        self.remove(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(-8),       
            c.animate(rate_func=rate_functions.linear).set_value(13),
            run_time=5
        )        
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(16),
            run_time=1.5
        )
        self.remove(aclrtion2)
        a.set_value(0)
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(19),
            run_time=1.5
        )

        #Up
        self.play(Write(eq1s),Unwrite(eq2s),run_time=0.5)
        self.wait()
        self.add(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(-8),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(22),
            run_time=1.5
        )
        a.set_value(0)
        self.remove(aclrtion2)
        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(8),       
            c.animate(rate_func=rate_functions.linear).set_value(32),
            run_time=5
        ) 
        self.add(aclrtion3)
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(10),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(35),
            run_time=1.5
        )
        self.remove(aclrtion3)
        a.set_value(0)
        self.play(eq2s.animate.set_opacity(0.3),eq1s.animate.set_opacity(0.3),run_time=0.5)  
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(38),
            run_time=1.5
        )
        self.wait()
        
    def construct(self):
        self.wt()

class a_and_v(Scene):
    def why_acceleration(self):
        b=self.b=ValueTracker(10)
        a=self.a=ValueTracker()
        c=self.c=ValueTracker()
        
        #elevator
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-20,20],y_length=10
        ).shift(LEFT*4.5)
        
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)
        
        #graph
        ax1=Axes(
            x_range=[0,50,4],
            y_range=[0,600,100],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,600,100)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).to_corner(RIGHT+UP)

        ax1_labels=ax1.get_axis_labels(
            Tex("time"),Tex("weight")
        )
        
        
        path1 = VMobject()
        dot1 = Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))
        dot1.add_updater(lambda h:h.become(Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))))
        
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path1(path1):
            previous_path1 = path1.copy()
            previous_path1.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path1)
        path1.add_updater(update_path1)
        wt=VGroup(ax1,ax1_labels,path1,dot1)

        #a_and_v
        ax3=Axes(
            x_range=[0,50,4],
            y_range=[0,600,100],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,600,100)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).to_corner(RIGHT+UP)
        
        #Equation
        eq1=MathTex("F_{s}=m(","g","-(","a","))",font_size=60).next_to(ax1,DOWN*5)
        
        a_val=Integer(a.get_value()).set_color(YELLOW)
        a_val.add_updater(lambda h: h.become(Integer(a.get_value()).set_color(YELLOW)))
        
        eq2=MathTex(
            "F_{s}","=m(","g","-","(",
            Integer(a.get_value(),
            num_decimal_places=1,
            color=YELLOW
            ).get_value(),
            "))",
            font_size=60
        ).next_to(ax1,DOWN*5)
        eq22=MathTex(
            "Weight","=m(","g","-","(",
            Integer(
                a.get_value(),
                num_decimal_places=1,
                color=YELLOW
                ).get_value(),
            "))",
            font_size=60
        ).next_to(ax1,DOWN*5)
        eq22.add_updater(
            lambda h:h.become(MathTex(
                "Weight","=m(","g","-","(",
                Integer(
                    a.get_value(),
                    num_decimal_places=1
                    ).get_value(),
                "))",
                font_size=60
        ).next_to(ax1,DOWN*5)))
        

        eq3=MathTex(
            "Weight=m(","g","+","(",
            Integer(
                -a.get_value(),
                num_decimal_places=1,
                color=YELLOW
                ).set_color(YELLOW).get_value(),
            "))",
            font_size=60
        ).next_to(ax1,DOWN*5)

        eq3.add_updater(
            lambda h:h.become(
            MathTex("Weight=m(","g","+","(",
            Integer(
                -a.get_value(),
                num_decimal_places=1
                ).set_color(YELLOW).get_value(),
            "))",
            font_size=60
        ).next_to(ax1,DOWN*5)))

        #play
        self.play(Create(wt))
        self.play(Create(elvt))
        self.play(Create(eq1))
        self.wait(2)
        self.remove(eq1)
        self.play(Create(eq2))
        self.wait()
        self.play(ReplacementTransform(eq2,eq22))
        self.wait()

        #Down
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(3),run_time=1.5
        )

        a.set_value(0)

        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(-8),       
            c.animate(rate_func=rate_functions.linear).set_value(13),
            run_time=5
        )        

        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(16),
            run_time=1.5
        )
        a.set_value(0)
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(19),
            run_time=1.5
        )
        
        
        #Up
        self.remove(eq22)
        self.play(Create(eq3))
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(-8),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.linear).set_value(22),
            run_time=1.5
        )
        a.set_value(0)

        self.play(
            b.animate(rate_func=rate_functions.linear).set_value(8),       
            c.animate(rate_func=rate_functions.linear).set_value(32),
            run_time=5
        ) 
        self.play(
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(10),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.linear).set_value(35),
            run_time=1.5
        )
        a.set_value(0)  
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(38),
            run_time=1.5
        )
        self.play(Uncreate(eq3),Uncreate(wt))
        self.wait(2)
        self.play(Uncreate(elvt))

       #anv
        v_axis=Axes(
            x_range=[0,20,2],y_range=[0,12,2],
            x_length=8,y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,12,2)
                
            },
            x_axis_config={
                "numbers_to_include":np.arange(0,20,2)
                
            }
        ).to_corner(RIGHT+UP)
        v_axis_labels=v_axis.get_axis_labels(
            Tex("time"),Tex("velocity")
        )
        
        
        v_graph1= v_axis.plot_parametric_curve(
              lambda t: np.array([
                t,t**2
            ]),t_range=[0,3]
           )
        v_graph2= v_axis.plot_parametric_curve(
              lambda t: np.array([
                t,9
            ]),t_range=[3,12]
           ) 
        v_graph3= v_axis.plot_parametric_curve(
              lambda t: np.array([
                t,-(t-12)*(t-12)+9
            ]),t_range=[12,15]
           )
        #dot 1
        dot=Dot().move_to(v_axis.c2p(0,0)) 
        path=VMobject()
        path.set_points_as_corners([dot.get_center(),dot.get_center()])
        def update_path(path):
            previous_path=path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        #dot 2
        dot2=Dot().move_to(v_axis.c2p(0,0)) 
        path2=VMobject()
        path2.set_points_as_corners([dot2.get_center(),dot2.get_center()])
        def update_path2(path2):
            previous_path2=path2.copy()
            previous_path2.add_points_as_corners([dot2.get_center()])
            path2.become(previous_path2)

        path2.add_updater(update_path2)     
        v_graphs=VGroup(
            *[
                v_graph1,v_graph2,v_graph3
            ]
        ) 
        v_graph=VGroup(v_axis,dot,path,v_axis_labels)
        v_tex=MathTex("v=",font_size=50).next_to(v_axis,DOWN*3) 
        v_val=Integer(number=c.get_value(),num_decimal_places=0).set_color(BLUE).next_to(v_tex,RIGHT)
        v_val.add_updater(lambda h:h.become(Integer(number=c.get_value(),num_decimal_places=0).set_color(BLUE).next_to(v_tex,RIGHT)))

        a_tex=MathTex("a=",font_size=50).next_to(v_tex,DOWN*2) 
        a_val=Integer(number=a.get_value(),num_decimal_places=0).set_color(RED).next_to(a_tex,RIGHT)
        a_val.add_updater(lambda h:h.become(Integer(number=a.get_value(),num_decimal_places=0).set_color(RED).next_to(a_tex,RIGHT)))

        
        #derivative of a and v
        acceleration=VGroup(a_tex,a_val)
        vt=VGroup(v_tex,v_val)
        
        text1=Tex(r"$\frac{\partial v}{\partial t} \rightarrow\ $","a",font_size=90)
        text1[1].set_color(YELLOW)
        text2=Tex(r"$\frac{\partial v}{\partial t} = $","a",font_size=90).next_to(text1,DOWN)
        text2[1].set_color(YELLOW)

        vlct=Tex(r"$v = t^2$",font_size=60)
        ac=Tex(r"$a=2t$",font_size=60).next_to(vlct,DOWN*2)
        
        ax5=Axes(
            x_range=[0,10],y_range=[0,20,4],
            x_length=8,y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,20,4)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).to_corner(RIGHT+UP)
        ax5_labels=ax5.get_axis_labels(
             Tex("time"),Tex("velocity")
        )
        velocity=ax5.plot(lambda t :t*t,x_range=[0,3],color=BLUE)


        ax6=Axes(
            x_range=[0,10],y_range=[0,10,2],
            x_length=8,y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
            },
            y_axis_config={
                "numbers_to_include":np.arange(0,10,2)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).next_to(ax5,DOWN)
        ax6_labels=ax6.get_axis_labels(
             Tex("time"),Tex("acceleration")
        )
        accelerations=ax6.plot(lambda t :2*t,x_range=[0,3],color=RED)
        
        av=VGroup(ax5,ax5_labels,ax6,ax6_labels)

        self.play(Write(text1))
        self.wait(3)
        self.play(Write(text2),text1.animate.set_opacity(0.5))
        self.wait(4)
        self.play(Unwrite(text1),Unwrite(text2))
        self.wait()
        self.play(Create(vlct))
        self.wait(2)
        self.play(Create(ac))
        self.wait(3)
        self.play(vlct.animate.next_to(ax5,LEFT*2),ac.animate.next_to(ax6,LEFT*2))
        self.play(Create(av))
        self.wait()
        self.play(Write(velocity),Write(accelerations),run_time=5,rate_func=rate_functions.linear)
        self.remove(velocity,accelerations)
        self.play(Write(velocity),Write(accelerations),run_time=5,rate_func=rate_functions.linear)
        self.play(Unwrite(velocity),Unwrite(accelerations))
    
        self.play(Uncreate(vlct),Uncreate(ac))
        self.wait()
        self.play(Uncreate(av))

        #c is velocity value in this case
        c.set_value(0)
        self.play(Create(elvt),Create(v_graph))
        
        self.play(Create(acceleration),Create(vt))
        
        #first time
        self.play(Indicate(v_axis_labels))
        b.set_value(10)
        self.wait(4)
        self.play(Indicate(v_tex,scale_factor=1.5))
        self.play(Indicate(a_tex,scale_factor=1.5))
        self.wait(2)
        self.play(
            MoveAlongPath(dot,v_graph1,rate_func=rate_functions.linear),
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.ease_in_quad).set_value(9),
            run_time=2
        )
        a.set_value(0)
        self.play(
            MoveAlongPath(dot,v_graph2),
            b.animate.set_value(-8),
            run_time=8,rate_func=rate_functions.linear
        )
        self.play(
            MoveAlongPath(dot,v_graph3,rate_func=rate_functions.linear),
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.ease_in_quad).set_value(0),
            run_time=2
        )
        self.play(a.animate.set_value(0),run_time=0.1)
        self.wait(2)
        self.remove(path,dot)
        
        #second time
        self.play(Create(dot2))
        self.add(path2)
        
        self.play(b.animate.set_value(10))
        self.play(
            MoveAlongPath(dot,v_graph1,rate_func=rate_functions.linear),
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(8),
            a.animate(rate_func=rate_functions.linear).set_value(6),
            c.animate(rate_func=rate_functions.ease_in_quad).set_value(9),
            run_time=2
        )
        a.set_value(0)
        self.play(
            MoveAlongPath(dot,v_graph2),
            b.animate.set_value(-8),
            run_time=8,rate_func=rate_functions.linear
        )
        self.play(
            MoveAlongPath(dot,v_graph3,rate_func=rate_functions.linear),
            b.animate(rate_func=rate_functions.ease_out_cubic).set_value(-10),
            a.animate(rate_func=rate_functions.linear).set_value(-6),
            c.animate(rate_func=rate_functions.ease_in_quad).set_value(0),
            run_time=2
        )

        

    def construct(self):
       self.why_acceleration()
       


class Weight(Scene):
    

    def elevator(self):
        a=self.a=ValueTracker(0)
        b=self.b=ValueTracker(10)
        
        ##########____Graph____################################################################################################################
        ax1=Axes(
            x_range=[0,520],y_range=[-1,1],x_length=4.5
        ).set_scale(0.5).move_to(RIGHT*3+DOWN)

        l1=Line(
            start=ax1.c2p(0,0),end=ax1.c2p(620,0)
            )
        n=VGroup()
        t=VGroup()
        for number in np.arange(0,601,100):
                nb=Tex(number,"N",font_size=25)
                nb.move_to(ax1.c2p(number,0.1))
                tips=Line(
                    start=ax1.c2p(number,-0.03),end=ax1.c2p(number,0.03)
                )
                n.add(nb)
                t.add(tips)
        dot=Dot(color="#0a2acc"  
            ).move_to(ax1.c2p(30*(a.get_value()+9.8),0))
        dot.add_updater(lambda t:t.become(Dot(color="#0a2acc"

            ).move_to(ax1.c2p(30*(a.get_value()+9.8),0))))
        
            
        weight_scale=VGroup(l1,*n,dot,*t)
        rec1=SurroundingRectangle(weight_scale,color=WHITE,buff=0.4)
        #######____numbers_____#######################################################################################################################
        
        mg=Tex("weight","=").next_to(rec1,UP,buff=1)
        mgnumber=Integer(30*(a.get_value()+9.8)).next_to(mg,RIGHT).set_color("#0a2acc")
        N=Tex("N").next_to(mgnumber,RIGHT)
        N.add_updater(lambda u: u.become(Tex("N").next_to(mgnumber,RIGHT)))
        
        
        mgnumber.add_updater(lambda h:h.become(Integer(30*(a.get_value()+9.8)).next_to(mg,RIGHT).set_color("#0a2acc")))
        mg.add_updater(lambda t:t.become(Tex("weight","=").next_to(rec1,UP,buff=1)))
        box1=VGroup(mg,mgnumber,N)
        rec2=SurroundingRectangle(box1,buff=0.5,color=WHITE)
        #####___elevator______###########################################################################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-20,20],y_length=10
        ).shift(LEFT*2)
        elvt=VGroup()
        head=SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5)))
        rec3=SurroundingRectangle(head,color=WHITE,buff=1)
        rec3.add_updater(lambda h:h.become(SurroundingRectangle(head,color=WHITE,buff=1)))
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt.add(head,rec3,dotline1,dotline2)

        self.add(weight_scale,rec1)
        self.add(mg,rec2,mgnumber,N)
        self.add(elvt)
        self.play(b.animate.set_value(8),a.animate.set_value(-4),run_time=1,rate_func=rate_functions.ease_in_cubic)
        a.set_value(0)
        self.play(b.animate.set_value(-10),run_time=5,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(-8),a.animate.set_value(4),run_time=1,rate_func=rate_functions.ease_in_cubic)
        a.set_value(0)
        self.play(b.animate.set_value(10),run_time=5,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(8),a.animate.set_value(-4),run_time=1,rate_func=rate_functions.ease_in_cubic)
        a.set_value(0)
        self.play(b.animate.set_value(-10),run_time=5,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(-8),a.animate.set_value(4),run_time=1,rate_func=rate_functions.ease_in_cubic)
        a.set_value(0)
        self.play(b.animate.set_value(10),run_time=5,rate_func=rate_functions.linear)

        self.play(b.animate.set_value(10),a.animate.set_value(9.8),run_time=3,rate_func=rate_functions.ease_out_cubic)
        self.play(b.animate.set_value(-10),a.animate.set_value(-9.8),run_time=3,rate_func=rate_functions.ease_out_cubic)
        self.play(b.animate.set_value(10),a.animate.set_value(9.8),run_time=3,rate_func=rate_functions.ease_out_cubic)
        self.play(a.animate.set_value(0))
        self.wait()
        self.play(b.animate.set_value(-10),run_time=4,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(10),run_time=4,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(-10),run_time=4,rate_func=rate_functions.linear)
        self.play(b.animate.set_value(-10),a.animate.set_value(-9.8),run_time=5,rate_func=rate_functions.wiggle)
        self.play(b.animate.set_value(10),a.animate.set_value(9.8),run_time=5,rate_func=rate_functions.wiggle)
        self.play(b.animate.set_value(-10),a.animate.set_value(-9.8),run_time=5,rate_func=rate_functions.wiggle)

    def construct(self):
        self.elevator()

class Zero_weight(SpaceScene):
    def zero(self):
        c=self.c=ValueTracker(0)
        a=self.a=ValueTracker(0.0)
        b=self.b=ValueTracker(0.00)
        
        #Elevator##################################################################################
        ax2=self.ax2=Axes(
            x_range=[-10,10],y_range=[-30,30],y_length=15
        ).shift(LEFT*4.5)
        
        head=VGroup(SVGMobject(f"{home}\\1553709145.svg")).move_to(ax2.c2p(0,b.get_value())).scale(0.5)
        head.add_updater(lambda t:t.become(VGroup(SVGMobject(f"{home}\\1553709145.svg").move_to(ax2.c2p(0,b.get_value())).scale(0.5))))
        rec3=Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)
        rec3.add_updater(lambda h:h.become(Rectangle(height=2.5,width=2,color=WHITE).move_to(head,DOWN)))

        
        dotline1=DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())
        dotline1.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,20),end=rec3.get_top())))
        dotline2=DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())
        dotline2.add_updater(lambda h:h.become(DashedLine(start=ax2.c2p(0,-20),end=rec3.get_bottom())))
        elvt=VGroup(head,rec3,dotline1,dotline2)

        ground = Line(ax2.c2p(-20, -11), ax2.c2p(20, -11))

        #Graphs##################################################################################
        ax1=Axes(
            x_range=[0,50,4],
            y_range=[0,600,100],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers":True,
                "font_size": 20,
                "include_tip":True,
                

            },
            y_axis_config={
                "numbers_to_include":np.arange(0,600,100)
                
            },
            x_axis_config={
                "numbers_to_include":[]
                
            }
        ).shift(RIGHT*3+UP)

        ax1_labels=ax1.get_axis_labels(
            Tex("time"),Tex("weight")
        )
        
        
        path1 = VMobject()
        dot1 = Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))
        dot1.add_updater(lambda h:h.become(Dot().move_to(ax1.c2p(c.get_value(),30*(9.8-a.get_value())))))
        
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path1(path1):
            previous_path1 = path1.copy()
            previous_path1.add_points_as_corners([dot1.get_center()])
            path1.become(previous_path1)
        path1.add_updater(update_path1)
        graph=VGroup(ax1,path1,dot1,ax1_labels)

        path2=VMobject()
        path2.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path2(path2):
            previous_path2 = path2.copy()
            previous_path2.add_points_as_corners([dot1.get_center()])
            path2.become(previous_path2)
        path2.add_updater(update_path2)

        path3=VMobject()
        path3.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot1.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)

        path4=VMobject()
        path4.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path4(path4):
            previous_path4 = path4.copy()
            previous_path4.add_points_as_corners([dot1.get_center()])
            path4.become(previous_path4)
        path4.add_updater(update_path4)
        graph=VGroup(ax1,path1,dot1,ax1_labels)
        
        path5=VMobject()
        path5.set_points_as_corners([dot1.get_center(),dot1.get_center()])
        def update_path5(path5):
            previous_path5=path5.copy()
            previous_path5.add_points_as_corners([dot1.get_center()])
            path5.become(previous_path5)
        path5.add_updater(update_path5)   
       
        #equtaion
        eq22=MathTex(
            "Weight","=m(","9.8","-","(",
            DecimalNumber(
                a.get_value(),
                num_decimal_places=1,
                color=YELLOW
                ).get_value(),
            "))",
            font_size=40
        ).next_to(ax1,DOWN*1.5)
        eq22.add_updater(
            lambda h:h.become(MathTex(
                "Weight","=m(","9.8","-","(",
                DecimalNumber(
                    a.get_value(),
                    num_decimal_places=1,
                    color=YELLOW
                    ).get_value(),
                "))",
                font_size=40
        ).next_to(ax1,DOWN*1.5)))

        

        b.set_value(10)
     
        self.add(elvt,graph)  
        self.add(ground)
        self.play(Write(eq22))
        self.wait(9)
        
        self.play(Uncreate(dotline1),Uncreate(dotline2))
        self.make_static_body(ground)
        self.wait()
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(10),run_time=1.2
        )
        a.set_value(9.8)
        
        
        self.play(
            b.animate(rate_func=rate_functions.ease_in_cubic).set_value(-9),
            c.animate(rate_func=rate_functions.linear).set_value(15),
            run_time=0.6
        )
        a.set_value(0)
        self.make_rigid_body(head,elasticity=0.001,
        density=5,
        friction=0.8)
        rec3.clear_updaters()
        self.play(
            c.animate(rate_func=rate_functions.linear).set_value(40),run_time=3
        )
        
    def construct(self):
            self.zero()
        
        
