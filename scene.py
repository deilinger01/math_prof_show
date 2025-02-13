from manim import *

class MyScene(Scene):
    """ conda activate eth-pfe-project """
    """ manim -ql scene.py MyScene """

    def construct(self):
        ''' constants '''
        square_size = 1.5   # size of square on screen
        depth = 8           # amount of generated triangle steps
        colors_4  = [RED_B, YELLOW_B, GREEN_B, BLUE_B]      # triangle group colors
        colors_8 = [RED_B, YELLOW_B, GREEN_B, BLUE_B, GOLD_B, PURPLE_B, PINK, LIGHT_BROWN] # single triangle colors inside group
        
        # Group containing the whole square with all its contents. Used to fade out the square later
        graph = Group()

        ''' Start Equation / Question '''
        question = MathTex(r"\sum_{n = 0}^{\infty} \frac{1}{2^{n+3}} \stackrel{?}{=} \frac{1}{4}")
        self.play(Write(question))
        self.wait(4)
        self.clear()

        ''' Create Square '''
        square = Square().set_stroke(color=WHITE).scale(square_size)
        graph.add(square)
        self.play(Create(square))
        self.wait()

        square_area = MathTex(r"A_{square} = 1")
        square_area.move_to([0, 2.5, 0])
        graph.add(square_area)
        self.play(Write(square_area))
        self.wait()

        ''' create subsquares with animation'''
        curr_square = square.copy().set_stroke(color=WHITE)
        for _ in range(depth):
            graph.add(curr_square)
            rs_square = curr_square.copy().rotate(45 * DEGREES).scale(1 / np.sqrt(2))
            self.play(Transform(curr_square, rs_square))
            curr_square = rs_square.copy()


        ''' Create Triangle '''
        # text to declare triangle areas. Will be animated step by step with the generation of the triangles
        area = MathTex(r"A_{\text{triangle}} =", 
                       r"\frac{1}{8}", 
                       r"+ \frac{1}{16}", 
                       r"+ \frac{1}{32}", 
                       r"+ \frac{1}{64}",
                       r"+ \frac{1}{128}"
                       r"+ \ldots",
                       r"= \sum_{n = 0}^{\infty} \frac{1}{2^{n+3}}",
                       r"= A_{\text{red}}")
        area.move_to([0, -3, 0])
        self.play(Write(area[0]))

        # biggest triangle
        triangle = Triangle()
        triangle.set_points_as_corners([square.get_corner(LEFT), square.get_corner(DL), square.get_corner(DOWN), square.get_corner(LEFT)])
        triangle.set_fill(colors_8[0], opacity=1)
        triangle.set_stroke(WHITE, opacity=1)
        self.play(Create(triangle))
        area[1].set_color(colors_8[0])
        self.play(Write(area[1]))
        group = Group(triangle)

        # Create subtriangles
        curr_triangle = triangle.copy()
        for i in range(1, depth):
            group.add(curr_triangle)
            rs_triangle = curr_triangle.copy()\
                .set_fill(colors_8[i], opacity=1)\
                .rotate(45 * DEGREES, about_point=curr_triangle.get_vertices()[0])\
                .scale(1/np.sqrt(2), about_point=curr_triangle.get_vertices()[0])\
                .shift((curr_triangle.get_vertices()[2] - curr_triangle.get_vertices()[0]) / 2)
            
            self.play(Transform(curr_triangle, rs_triangle))
            curr_triangle = rs_triangle.copy()
            # print the area of the triangle
            if(i < 5):
                area[i + 1].set_color(colors_8[i])
                self.play(Write(area[i + 1]))
                self.wait()
        self.wait()

        # add mathematical sum symbol
        self.play(Write(area[6]))
        self.wait()

        ''' create triangle groups '''
        # recolor triangles to group color
        for item in group:
            item.set_fill(colors_4[0])
        self.wait()
        self.play(Write(area[7]))

        self.wait()

        # simplify formula
        self.play(FadeOut(area[0:6]))

        A_red = MathTex(r"A_{\text{red}} =",
                        r"\sum_{n = 0}^{\infty} \frac{1}{2^{n+3}}",
                        r"= \frac{A_{square}}{4}",
                        r"= \frac{1}{4}")
        
        # print formula of single group area
        A_red.move_to([0,-3,0])
        self.play(FadeOut(area[6:8]), FadeIn(A_red[0:2]))
        self.wait()
        graph.add(group)

        # generate groups with transform
        new_group = group.copy()
        for i in range(1, 4):
            graph.add(new_group)
            rs_group = new_group.copy()\
                .rotate(90 * DEGREES, about_point=square.get_center())
            for item in rs_group:
                item.set_fill(colors_4[i], opacity=1)
                item.set_stroke(WHITE, opacity=1)
            self.play(Transform(new_group, rs_group))
            new_group = rs_group.copy()
        self.wait()

        # print formula of total group area
        self.play(Write(A_red[2:4]))
        self.wait()
        self.play(FadeOut(graph))

        self.play(FadeOut(A_red[0]))
        self.play(FadeOut(A_red[2]))

        
        ''' Solution to Equation / Question '''
        solution = MathTex(r"\sum_{n = 0}^{\infty} \frac{1}{2^{n+3}}", 
                           r"= \frac{1}{4}")
        solution.move_to([0,1,0])
        self.play(Transform(A_red[1], solution[0]))
        self.play(Transform(A_red[3], solution[1]))

        qed = MathTex(r"q.e.d")
        qed.move_to([0, -1,0])
        self.play(Write(qed))
        self.wait()