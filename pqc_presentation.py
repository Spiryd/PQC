from manim import *  # or: from manimlib import *
import numpy as np  # for numerical calculations

from manim_slides import Slide


class PQC(Slide):
    def construct(self):
        # Title
        title = Text('PQC').scale(6)
        sub_title = Text("Securing Data in the Quantum Era").scale(2).next_to(title, DOWN)
        self.play(FadeIn(title, sub_title))
        self.next_slide()
        self.play(FadeOut(title, sub_title))
        # Fists Topic
        topic1_title = Text('Recent Developments & Current State Of Quantum Computing', font_size=60).to_edge(UP)
        biden_img = ImageMobject("JOEBIDENWAKEUP.jpg").scale(1.5)
        self.play(FadeIn(topic1_title, biden_img))
        self.next_slide()
        self.play(FadeOut(biden_img), run_time=1)
        values=[27, 65, 127, 433, 1125, 1386, 4158, 7500, 10000, 15000]
        quibit_chart = BarChart(
            values,
            bar_names=["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"],
            bar_colors=[BLUE, BLUE, BLUE, BLUE, BLUE, RED, RED, RED, RED, RED],
            y_range=[0, 15000, 5000],
            x_length=18,
            y_axis_config={"font_size": 40},
        )
        qchart_labels = quibit_chart.get_bar_labels(font_size=40)
        self.play(Create(quibit_chart), run_time=4)
        self.play(FadeIn(qchart_labels))
        self.next_slide()
        # Second Topic
        topic2_title = Text('What is PQC? Why Do We Care?', font_size=60).to_edge(UP)
        self.wipe(Group(quibit_chart, qchart_labels, topic1_title), topic2_title)
        self.next_slide()
        peter_img = ImageMobject("Peter.jpg").scale(.5)
        self.play(FadeIn(peter_img))
        self.next_slide()
        # Third Topic
        topic3_title = Text('Intro to Cryptographic Concepts', font_size=60).to_edge(UP)
        enigma_img = ImageMobject("Enigma.jpg")
        self.wipe(Group(peter_img, topic2_title), Group(topic3_title, enigma_img))
        self.next_slide()
        # Fourth Topic
        topic4_title = Text('Post Quantum Primitives', font_size=80).to_edge(UP)
        primitives_list = BulletedList(
            "Secret-key", "Code-based", "Multivariate-quadratic-equations", "Hash-based", "Lattice-based",
        ).scale(2)
        self.wipe(Group(topic3_title, enigma_img), Group(topic4_title, primitives_list))
        self.next_slide()
        self.play(primitives_list.animate.set_color_by_tex("Lattice-based", BLUE))
        self.next_slide()
        # Fifth Topic
        topic5_title = Text('Lattice-based Cryptography').scale(2)
        self.wipe(Group(topic4_title, primitives_list), topic5_title)
        self.next_slide()
        self.play(FadeOut(topic5_title))
        origin_dot = Dot(ORIGIN)
        v0_vec = np.array([2, 1, 0])
        v1_vec = np.array([-2, 2, 0])
        v0 = Arrow(ORIGIN, v0_vec, buff=0, color=RED)
        v1 = Arrow(ORIGIN, v1_vec, buff=0, color=BLUE)
        origin_label = MathTex("0").next_to(origin_dot, DOWN)
        v0_label = MathTex("v_0").next_to(v0.get_end(), UP)
        v0_label.color = RED
        v1_label = MathTex("v_1").next_to(v1.get_end(), UP)
        v1_label.color = BLUE
        self.play(Create(origin_dot), Create(origin_label), Create(v0), Create(v1), Create(v0_label), Create(v1_label))
        self.next_slide()
        current_location = v0_vec
        adding_vectors_example = [
            Arrow(current_location, (current_location + v0_vec), buff=0, color=RED_A),
            Arrow((current_location + v0_vec), (current_location + 2*v0_vec) , buff=0, color=RED_A),
            Arrow((current_location + 2*v0_vec), (current_location + 2*v0_vec + v1_vec), buff=0, color=BLUE_A),
        ]
        for arrow in adding_vectors_example:
            self.play(Create(arrow))
        end_point = Dot((current_location + 2*v0_vec + v1_vec))
        self.play(Create(end_point))
        self.next_slide()
        self.play(Uncreate(end_point), run_time=0.25)
        for arrow in adding_vectors_example[::-1]:
            self.play(FadeOut(arrow), run_time=0.25)
        self.next_slide()
        lattice = []
        for a in range(-10, 11):
            for b in range(-10, 11):
                lattice.append(Dot(a*v0_vec + b*v1_vec))
        self.play(Create(VGroup(*lattice)))
        self.next_slide()
        point_to_find = Dot(-3*v0_vec + 2*v1_vec + np.array([0, 0.25, 0]), color=GREEN)
        point_to_find_label = MathTex("c").next_to(point_to_find, UP)
        point_to_find_label.color = GREEN
        self.play(Create(point_to_find), Create(point_to_find_label))
        self.next_slide()
        private_vectors_to_c = [
            Arrow(v1_vec, 2*v1_vec, buff=0, color=BLUE_A),
            Arrow(2*v1_vec, 2*v1_vec - v0_vec, buff=0, color=RED_A),
            Arrow(2*v1_vec - v0_vec,  2*v1_vec - 2*v0_vec, buff=0, color=RED_A),
            Arrow(2*v1_vec - 2*v0_vec, 2*v1_vec - 3*v0_vec, buff=0, color=RED_A),
        ]
        for arrow in private_vectors_to_c:
            self.play(Create(arrow))
        self.next_slide()
        for arrow in private_vectors_to_c[::-1]:
            self.play(FadeOut(arrow), run_time=0.25)
        self.play(FadeOut(VGroup(v0, v0_label, v1, v1_label)))
        self.next_slide()
        w0_vec = np.array([2, 4, 0])
        w1_vec = np.array([4, 5, 0])
        w0 = Arrow(ORIGIN, w0_vec, buff=0, color=RED)
        w1 = Arrow(ORIGIN, w1_vec, buff=0, color=BLUE)
        w0_label = MathTex("w_0").next_to(w0.get_end(), UP)
        w0_label.color = RED
        w1_label = MathTex("w_1").next_to(w1.get_end(), UP)
        w1_label.color = BLUE
        self.play(Create(w0), Create(w1), Create(w0_label), Create(w1_label))
        self.next_slide()
        public_vectors_to_c = [
            Arrow(ORIGIN, -w1_vec, buff=0, color=BLUE_A),
            Arrow(-w1_vec, -w1_vec + w0_vec, buff=0, color=RED_A),
            Arrow(-w1_vec + w0_vec, -2*w1_vec + w0_vec, buff=0, color=BLUE_A),
            Arrow(-2*w1_vec + w0_vec, -2*w1_vec + 2*w0_vec, buff=0, color=RED_A),
            Arrow(-2*w1_vec + 2*w0_vec, -2*w1_vec + 3*w0_vec, buff=0, color=RED_A),
            Arrow(-2*w1_vec + 3*w0_vec, -3*w1_vec + 3*w0_vec, buff=0, color=BLUE_A),
            Arrow(-3*w1_vec + 3*w0_vec, -3*w1_vec + 4*w0_vec, buff=0, color=RED_A),
            Arrow(-3*w1_vec + 4*w0_vec, -4*w1_vec + 4*w0_vec, buff=0, color=BLUE_A),
            Arrow(-4*w1_vec + 4*w0_vec, -4*w1_vec + 5*w0_vec, buff=0, color=RED_A),
            Arrow(-4*w1_vec + 5*w0_vec, -5*w1_vec + 5*w0_vec, buff=0, color=BLUE_A),
            Arrow(-5*w1_vec + 5*w0_vec, -5*w1_vec + 6*w0_vec, buff=0, color=RED_A),
            Arrow(-5*w1_vec + 6*w0_vec, -6*w1_vec + 6*w0_vec, buff=0, color=BLUE_A),
            Arrow(-6*w1_vec + 6*w0_vec, -6*w1_vec + 7*w0_vec, buff=0, color=RED_A),
            Arrow(-6*w1_vec + 7*w0_vec, -7*w1_vec + 7*w0_vec, buff=0, color=BLUE_A),
            Arrow(-7*w1_vec + 7*w0_vec, -7*w1_vec + 8*w0_vec, buff=0, color=RED_A),
            Arrow(-7*w1_vec + 8*w0_vec, -7*w1_vec + 9*w0_vec, buff=0, color=RED_A),
        ]
        for arrow in public_vectors_to_c:
            self.play(Create(arrow), run_time=0.3)
        self.next_slide()
        # Final Slide
        final_title = Text('Thank You').scale(6)
        self.wipe(Group(w0, w0_label, w1, w1_label, VGroup(*lattice), VGroup(*public_vectors_to_c), point_to_find, point_to_find_label, origin_dot, origin_label), final_title)
        self.next_slide()
        