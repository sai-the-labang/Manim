from manim import*
import random 

class RandomDots(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(4)
        
        dots=VGroup(
            *[
                Dot(
                   0.36 
                ).move_to(np.array([random.randrange(-20,20),random.randrange(-12,12),0]))    for i in range(10)
            ]
        )
        rec=SurroundingRectangle(
            dots,buff=3,color=WHITE
        )
        
        self.add(rec)
        self.wait(2)
        
        
        
        
        
        
       
          
          
        dots1=dots[random.choice([0,1,2,3,4,5,6,7,8,9])]
        dots2=VGroup(*[])
        numbers2=[0,1,2,3,4,5,6,7,8,9]
        for i in range(2):
            
            random_number2=Integer(random.choice(numbers2))
            numbers2.remove(random_number2.get_value())
            dots2.add(dots[random_number2.get_value()])
        dots3=VGroup(*[])
        numbers3=[0,1,2,3,4,5,6,7,8,9]
        for i in range(3):
            
            random_number3=Integer(random.choice(numbers3))
            numbers3.remove(random_number3.get_value())
            dots3.add(dots[random_number3.get_value()])
        dots4=VGroup(*[])
        numbers4=[0,1,2,3,4,5,6,7,8,9]
        for i in range(4):
            
            random_number4=Integer(random.choice(numbers4))
            numbers4.remove(random_number4.get_value())
            dots4.add(dots[random_number4.get_value()])
        dots5=VGroup(*[])
        numbers5=[0,1,2,3,4,5,6,7,8,9]
        for i in range(5):
            
            random_number5=Integer(random.choice(numbers5))
            numbers5.remove(random_number5.get_value())
            dots5.add(dots[random_number5.get_value()])    
        dots6=VGroup(*[])
        numbers6=[0,1,2,3,4,5,6,7,8,9]
        for i in range(6):
            
            random_number6=Integer(random.choice(numbers6))
            numbers6.remove(random_number6.get_value())
            dots6.add(dots[random_number6.get_value()])
        dots7=VGroup(*[])
        numbers7=[0,1,2,3,4,5,6,7,8,9]
        for i in range(7):
            
            random_number7=Integer(random.choice(numbers7))
            numbers7.remove(random_number7.get_value())
            dots7.add(dots[random_number7.get_value()])
        dots8=VGroup(*[])
        numbers8=[0,1,2,3,4,5,6,7,8,9]
        for i in range(8):
            
            random_number8=Integer(random.choice(numbers8))
            numbers8.remove(random_number8.get_value())
            dots8.add(dots[random_number8.get_value()])
        dots9=VGroup(*[])
        numbers9=[0,1,2,3,4,5,6,7,8,9]
        for i in range(9):
            
            random_number9=Integer(random.choice(numbers9))
            numbers9.remove(random_number9.get_value())
            dots9.add(dots[random_number9.get_value()])
        dots10=VGroup(*[])
        numbers10=[0,1,2,3,4,5,6,7,8,9]
        for i in range(10):
        
            random_number10=Integer(random.choice(numbers10))
            numbers10.remove(random_number10.get_value())
            dots10.add(dots[random_number10.get_value()])
        


        all_dots_group=VGroup(
            *[
                dots1,dots2,dots3,dots4,dots5,dots6,dots7,dots8,dots9,dots10,
                
            ]
        )
        numbers_to_add=[0,1,2,3,4,5,6,7,8,9]
        for _ in range(10):
          number_to_add=Integer(random.choice(numbers_to_add))
          numbers_to_add.remove(number_to_add.get_value())
          to_be_added=all_dots_group[number_to_add.get_value()] 
                 
          self.play(
              FadeIn(to_be_added),run_time=0.1
          )
          self.wait(0.8)
          self.play(
              FadeOut(to_be_added),run_time=0.1
          )
          self.wait() 

class ChineseNumber(Scene):
    def construct(self):
        nums=Tex('一','二','三','四','五','六','七','八','九','十',tex_template=TexTemplateLibrary.ctex)        
        #self.play(Write(nums))
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)
                     
           
           
           

           
        

