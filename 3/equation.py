from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image as Img
from pyperclip import copy
from pylatex import Document, Alignat

textures = 'equation_textures.png'


class Abc:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('732x353')
        self.root.title('Оформление математических формул')
        self.root.config(bg='#202020')
        self.tablet = ttk.Notebook(self.root)
        self.a_tab = ttk.Frame(self.tablet)
        self.b_tab = ttk.Frame(self.tablet)
        self.c_tab = ttk.Frame(self.tablet)
        self.d_tab = ttk.Frame(self.tablet)
        self.e_tab = ttk.Frame(self.tablet)
        self.f_tab = ttk.Frame(self.tablet)
        self.tablet.add(self.a_tab, text="Math")
        self.tablet.add(self.b_tab, text="Greek")
        self.tablet.add(self.c_tab, text="Relations")
        self.tablet.add(self.d_tab, text="Logic")
        self.tablet.add(self.e_tab, text="Symbols")
        self.tablet.add(self.f_tab, text="Arrows")
        self.tablet.place(x=20, y=20, width=692, height=110)
        self.textbox = Text(self.root, relief=FLAT)
        self.textbox.place(x=20, y=142, width=692, height=170)
        self.status = Label(self.root, bg='#202020', fg='#FFFFFF', text='Введите название документа: ')
        self.status.place(x=430, y=313, width=200, height=20)
        self.entry = Entry(self.root)
        self.entry.place(x=630, y=313, width=60, height=20)
        self.img_cpy = ImageTk.PhotoImage(Img.open(textures).crop((526, 75, 542, 91)))
        self.img_nxt = ImageTk.PhotoImage(Img.open(textures).crop((543, 75, 559, 91)))
        self.img_clr = ImageTk.PhotoImage(Img.open(textures).crop((526, 92, 542, 108)))
        self.img_pdf = ImageTk.PhotoImage(Img.open(textures).crop((543, 92, 559, 108)))
        Button(self.root, image=self.img_cpy, command=lambda: copy(self.textbox.get(0.0, END))).place(x=20, y=313, width=20, height=20)
        Button(self.root, image=self.img_nxt, command=lambda: self.textbox.insert(END, r' \newline\ ')).place(x=44, y=313, width=20, height=20)
        Button(self.root, image=self.img_clr, command=lambda: self.textbox.delete(0.0, END)).place(x=68, y=313, width=20, height=20)
        Button(self.root, image=self.img_pdf, command=self.transform).place(x=692, y=313, width=20, height=20)

        self.i1_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 1, 37, 37)))
        self.i1_2 = ImageTk.PhotoImage(Img.open(textures).crop((38, 1, 74, 37)))
        self.i1_3 = ImageTk.PhotoImage(Img.open(textures).crop((75, 1, 111, 37)))
        self.i1_4 = ImageTk.PhotoImage(Img.open(textures).crop((112, 1, 148, 37)))
        self.i1_5 = ImageTk.PhotoImage(Img.open(textures).crop((149, 1, 185, 37)))
        self.i1_6 = ImageTk.PhotoImage(Img.open(textures).crop((186, 1, 222, 37)))
        self.i1_7 = ImageTk.PhotoImage(Img.open(textures).crop((223, 1, 259, 37)))
        self.i1_8 = ImageTk.PhotoImage(Img.open(textures).crop((260, 1, 296, 37)))
        self.i1_9 = ImageTk.PhotoImage(Img.open(textures).crop((297, 1, 333, 37)))
        self.i1_10 = ImageTk.PhotoImage(Img.open(textures).crop((334, 1, 370, 37)))
        self.i1_11 = ImageTk.PhotoImage(Img.open(textures).crop((371, 1, 407, 37)))
        self.i1_12 = ImageTk.PhotoImage(Img.open(textures).crop((408, 1, 444, 37)))
        self.i1_13 = ImageTk.PhotoImage(Img.open(textures).crop((445, 1, 481, 37)))
        self.i1_14 = ImageTk.PhotoImage(Img.open(textures).crop((482, 1, 518, 37)))
        self.i1_15 = ImageTk.PhotoImage(Img.open(textures).crop((519, 1, 555, 37)))
        self.i1_16 = ImageTk.PhotoImage(Img.open(textures).crop((556, 1, 589, 37)))
        self.i2_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 38, 37, 74)))
        self.i2_2 = ImageTk.PhotoImage(Img.open(textures).crop((38, 38, 74, 74)))
        self.i2_3 = ImageTk.PhotoImage(Img.open(textures).crop((75, 38, 111, 74)))
        self.i2_4 = ImageTk.PhotoImage(Img.open(textures).crop((112, 38, 148, 74)))
        self.i2_5 = ImageTk.PhotoImage(Img.open(textures).crop((149, 38, 185, 74)))
        self.i2_6 = ImageTk.PhotoImage(Img.open(textures).crop((186, 38, 222, 74)))
        self.i2_7 = ImageTk.PhotoImage(Img.open(textures).crop((223, 38, 259, 74)))
        self.i2_8 = ImageTk.PhotoImage(Img.open(textures).crop((260, 38, 296, 74)))
        self.i2_9 = ImageTk.PhotoImage(Img.open(textures).crop((297, 38, 333, 74)))
        self.i2_10 = ImageTk.PhotoImage(Img.open(textures).crop((334, 38, 370, 74)))
        self.i2_11 = ImageTk.PhotoImage(Img.open(textures).crop((371, 38, 407, 74)))
        self.i2_12 = ImageTk.PhotoImage(Img.open(textures).crop((408, 38, 444, 74)))
        self.i2_13 = ImageTk.PhotoImage(Img.open(textures).crop((445, 38, 481, 74)))
        self.i2_14 = ImageTk.PhotoImage(Img.open(textures).crop((482, 38, 518, 74)))
        self.i2_15 = ImageTk.PhotoImage(Img.open(textures).crop((519, 38, 555, 74)))
        self.i2_16 = ImageTk.PhotoImage(Img.open(textures).crop((556, 38, 589, 74)))
        self.i3_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 75, 25, 99)))
        self.i3_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 75, 50, 99)))
        self.i3_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 75, 75, 99)))
        self.i3_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 75, 100, 99)))
        self.i3_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 75, 125, 99)))
        self.i3_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 75, 150, 99)))
        self.i3_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 75, 175, 99)))
        self.i3_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 75, 200, 99)))
        self.i3_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 75, 225, 99)))
        self.i3_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 75, 250, 99)))
        self.i3_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 75, 275, 99)))
        self.i3_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 75, 300, 99)))
        self.i3_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 75, 325, 99)))
        self.i3_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 75, 350, 99)))
        self.i3_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 75, 375, 99)))
        self.i3_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 75, 400, 99)))
        self.i3_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 75, 425, 99)))
        self.i3_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 75, 450, 99)))
        self.i3_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 75, 475, 99)))
        self.i3_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 75, 500, 99)))
        self.i3_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 75, 525, 99)))
        self.i4_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 100, 25, 124)))
        self.i4_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 100, 50, 124)))
        self.i4_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 100, 75, 124)))
        self.i4_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 100, 100, 124)))
        self.i4_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 100, 125, 124)))
        self.i4_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 100, 150, 124)))
        self.i4_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 100, 175, 124)))
        self.i4_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 100, 200, 124)))
        self.i4_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 100, 225, 124)))
        self.i4_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 100, 250, 124)))
        self.i4_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 100, 275, 124)))
        self.i4_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 100, 300, 124)))
        self.i4_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 100, 325, 124)))
        self.i4_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 100, 350, 124)))
        self.i4_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 100, 375, 124)))
        self.i4_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 100, 400, 124)))
        self.i4_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 100, 425, 124)))
        self.i4_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 100, 450, 124)))
        self.i4_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 100, 475, 124)))
        self.i4_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 100, 500, 124)))
        self.i4_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 100, 525, 124)))
        self.i5_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 125, 25, 149)))
        self.i5_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 125, 50, 149)))
        self.i5_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 125, 75, 149)))
        self.i5_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 125, 100, 149)))
        self.i5_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 125, 125, 149)))
        self.i5_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 125, 150, 149)))
        self.i5_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 125, 175, 149)))
        self.i5_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 125, 200, 149)))
        self.i5_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 125, 225, 149)))
        self.i5_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 125, 250, 149)))
        self.i5_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 125, 275, 149)))
        self.i5_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 125, 300, 149)))
        self.i5_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 125, 325, 149)))
        self.i5_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 125, 350, 149)))
        self.i5_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 125, 375, 149)))
        self.i5_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 125, 400, 149)))
        self.i5_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 125, 425, 149)))
        self.i5_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 125, 450, 149)))
        self.i5_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 125, 475, 149)))
        self.i5_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 125, 500, 149)))
        self.i5_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 125, 525, 149)))
        self.i5_22 = ImageTk.PhotoImage(Img.open(textures).crop((526, 125, 550, 149)))
        self.i6_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 150, 25, 174)))
        self.i6_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 150, 50, 174)))
        self.i6_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 150, 75, 174)))
        self.i6_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 150, 100, 174)))
        self.i6_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 150, 125, 174)))
        self.i6_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 150, 150, 174)))
        self.i6_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 150, 175, 174)))
        self.i6_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 150, 200, 174)))
        self.i6_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 150, 225, 174)))
        self.i6_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 150, 250, 174)))
        self.i6_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 150, 275, 174)))
        self.i6_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 150, 300, 174)))
        self.i6_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 150, 325, 174)))
        self.i6_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 150, 350, 174)))
        self.i6_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 150, 375, 174)))
        self.i6_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 150, 400, 174)))
        self.i6_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 150, 425, 174)))
        self.i6_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 150, 450, 174)))
        self.i6_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 150, 475, 174)))
        self.i6_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 150, 500, 174)))
        self.i6_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 150, 525, 174)))
        self.i6_22 = ImageTk.PhotoImage(Img.open(textures).crop((526, 150, 550, 174)))
        self.i7_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 175, 25, 199)))
        self.i7_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 175, 50, 199)))
        self.i7_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 175, 75, 199)))
        self.i7_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 175, 100, 199)))
        self.i7_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 175, 125, 199)))
        self.i7_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 175, 150, 199)))
        self.i7_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 175, 175, 199)))
        self.i7_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 175, 200, 199)))
        self.i7_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 175, 225, 199)))
        self.i7_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 175, 250, 199)))
        self.i7_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 175, 275, 199)))
        self.i7_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 175, 300, 199)))
        self.i7_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 175, 325, 199)))
        self.i7_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 175, 350, 199)))
        self.i7_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 175, 375, 199)))
        self.i7_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 175, 400, 199)))
        self.i7_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 175, 425, 199)))
        self.i7_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 175, 450, 199)))
        self.i7_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 175, 475, 199)))
        self.i7_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 175, 500, 199)))
        self.i7_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 175, 525, 199)))
        self.i8_1 = ImageTk.PhotoImage(Img.open(textures).crop((1, 200, 25, 224)))
        self.i8_2 = ImageTk.PhotoImage(Img.open(textures).crop((26, 200, 50, 224)))
        self.i8_3 = ImageTk.PhotoImage(Img.open(textures).crop((51, 200, 75, 224)))
        self.i8_4 = ImageTk.PhotoImage(Img.open(textures).crop((76, 200, 100, 224)))
        self.i8_5 = ImageTk.PhotoImage(Img.open(textures).crop((101, 200, 125, 224)))
        self.i8_6 = ImageTk.PhotoImage(Img.open(textures).crop((126, 200, 150, 224)))
        self.i8_7 = ImageTk.PhotoImage(Img.open(textures).crop((151, 200, 175, 224)))
        self.i8_8 = ImageTk.PhotoImage(Img.open(textures).crop((176, 200, 200, 224)))
        self.i8_9 = ImageTk.PhotoImage(Img.open(textures).crop((201, 200, 225, 224)))
        self.i8_10 = ImageTk.PhotoImage(Img.open(textures).crop((226, 200, 250, 224)))
        self.i8_11 = ImageTk.PhotoImage(Img.open(textures).crop((251, 200, 275, 224)))
        self.i8_12 = ImageTk.PhotoImage(Img.open(textures).crop((276, 200, 300, 224)))
        self.i8_13 = ImageTk.PhotoImage(Img.open(textures).crop((301, 200, 325, 224)))
        self.i8_14 = ImageTk.PhotoImage(Img.open(textures).crop((326, 200, 350, 224)))
        self.i8_15 = ImageTk.PhotoImage(Img.open(textures).crop((351, 200, 375, 224)))
        self.i8_16 = ImageTk.PhotoImage(Img.open(textures).crop((376, 200, 400, 224)))
        self.i8_17 = ImageTk.PhotoImage(Img.open(textures).crop((401, 200, 425, 224)))
        self.i8_18 = ImageTk.PhotoImage(Img.open(textures).crop((426, 200, 450, 224)))
        self.i8_19 = ImageTk.PhotoImage(Img.open(textures).crop((451, 200, 475, 224)))
        self.i8_20 = ImageTk.PhotoImage(Img.open(textures).crop((476, 200, 500, 224)))
        self.i8_21 = ImageTk.PhotoImage(Img.open(textures).crop((501, 200, 525, 224)))

        self.buttons()
        self.root.mainloop()

    def buttons(self):

        Button(self.a_tab, image=self.i1_1, command=lambda: self.textbox.insert(END, r' \widetilde{ab} ')).place(x=2, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_2, command=lambda: self.textbox.insert(END, r' \overleftarrow{ba} ')).place(x=45, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_3, command=lambda: self.textbox.insert(END, r' \overline{ab} ')).place(x=88, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_4, command=lambda: self.textbox.insert(END, r' \overbrace{ab} ')).place(x=131, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_5, command=lambda: self.textbox.insert(END, r' \sqrt{ab} ')).place(x=174, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_6, command=lambda: self.textbox.insert(END, r" f' ")).place(x=217, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_7, command=lambda: self.textbox.insert(END, r' x^{k} ')).place(x=260, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_8, command=lambda: self.textbox.insert(END, r' \lim_{a \rightarrow b} ')).place(x=303, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_9, command=lambda: self.textbox.insert(END, r' \begin{bmatrix}a & b \\c & d \end{bmatrix} ')).place(x=346, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_10, command=lambda: self.textbox.insert(END, r' \big(a\big) ')).place(x=389, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_11, command=lambda: self.textbox.insert(END, r' \int_a^b x ')).place(x=432, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_12, command=lambda: self.textbox.insert(END, r' \sum_a^b x ')).place(x=475, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_13, command=lambda: self.textbox.insert(END, r' \prod_a^b x ')).place(x=518, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_14, command=lambda: self.textbox.insert(END, r' \bigcap_a^b x ')).place(x=561, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_15, command=lambda: self.textbox.insert(END, r' \bigvee_a^b x ')).place(x=604, y=2, width=40, height=40)
        Button(self.a_tab, image=self.i1_16, command=lambda: self.textbox.insert(END, r' \bigotimes ')).place(x=647, y=2, width=40, height=40)

        Button(self.a_tab, image=self.i2_1, command=lambda: self.textbox.insert(END, r' \widehat{ab} ')).place(x=2, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_2, command=lambda: self.textbox.insert(END, r' \overrightarrow{ab} ')).place(x=45, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_3, command=lambda: self.textbox.insert(END, r' \underline{ab} ')).place(x=88, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_4, command=lambda: self.textbox.insert(END, r' \underbrace{ab} ')).place(x=131, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_5, command=lambda: self.textbox.insert(END, r' \sqrt[n]{ab} ')).place(x=174, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_6, command=lambda: self.textbox.insert(END, r' \frac{a}{b} ')).place(x=217, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_7, command=lambda: self.textbox.insert(END, r' x_{k} ')).place(x=260, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_8, command=lambda: self.textbox.insert(END, r' \frac{\partial^nf}{\partial x^n} ')).place(x=303, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_9, command=lambda: self.textbox.insert(END, r' x =\begin{cases}a & x = 0\\b & x > 0\end{cases} ')).place(x=346, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_10, command=lambda: self.textbox.insert(END, r' \big\{a\big\} ')).place(x=389, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_11, command=lambda: self.textbox.insert(END, r' \oint_a^b x ')).place(x=432, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_12, command=lambda: self.textbox.insert(END, r' \bigsqcup_a^b x ')).place(x=475, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_13, command=lambda: self.textbox.insert(END, r' \coprod_a^b x ')).place(x=518, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_14, command=lambda: self.textbox.insert(END, r' \bigcup_a^b x ')).place(x=561, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_15, command=lambda: self.textbox.insert(END, r' \bigwedge_a^b x ')).place(x=604, y=45, width=40, height=40)
        Button(self.a_tab, image=self.i2_16, command=lambda: self.textbox.insert(END, r' \bigoplus ')).place(x=647, y=45, width=40, height=40)

        Button(self.b_tab, image=self.i3_1, command=lambda: self.textbox.insert(END, r' \alpha ')).place(x=2, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_2, command=lambda: self.textbox.insert(END, r' \beta ')).place(x=31, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_3, command=lambda: self.textbox.insert(END, r' \gamma ')).place(x=60, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_4, command=lambda: self.textbox.insert(END, r' \delta ')).place(x=89, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_5, command=lambda: self.textbox.insert(END, r' \epsilon ')).place(x=118, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_6, command=lambda: self.textbox.insert(END, r' \varepsilon ')).place(x=147, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_7, command=lambda: self.textbox.insert(END, r' \zeta ')).place(x=176, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_8, command=lambda: self.textbox.insert(END, r' \eta ')).place(x=205, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_9, command=lambda: self.textbox.insert(END, r' \theta ')).place(x=234, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_10, command=lambda: self.textbox.insert(END, r' \vartheta ')).place(x=263, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_11, command=lambda: self.textbox.insert(END, r' \gamma ')).place(x=292, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_12, command=lambda: self.textbox.insert(END, r' \kappa ')).place(x=321, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_13, command=lambda: self.textbox.insert(END, r' \lambda ')).place(x=350, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_14, command=lambda: self.textbox.insert(END, r' \mu ')).place(x=379, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_15, command=lambda: self.textbox.insert(END, r' \nu ')).place(x=408, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_16, command=lambda: self.textbox.insert(END, r' \Gamma ')).place(x=437, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_17, command=lambda: self.textbox.insert(END, r' \Delta ')).place(x=465, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_18, command=lambda: self.textbox.insert(END, r' \Theta ')).place(x=493, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_19, command=lambda: self.textbox.insert(END, r' \Lambda ')).place(x=521, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_20, command=lambda: self.textbox.insert(END, r' \Xi ')).place(x=549, y=2, width=26, height=26)
        Button(self.b_tab, image=self.i3_21, command=lambda: self.textbox.insert(END, r' \Pi ')).place(x=577, y=2, width=26, height=26)

        Button(self.b_tab, image=self.i4_1, command=lambda: self.textbox.insert(END, r' \xi ')).place(x=2, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_2, command=lambda: self.textbox.insert(END, r' o ')).place(x=31, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_3, command=lambda: self.textbox.insert(END, r' \pi ')).place(x=60, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_4, command=lambda: self.textbox.insert(END, r' \varpi ')).place(x=89, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_5, command=lambda: self.textbox.insert(END, r' \rho ')).place(x=118, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_6, command=lambda: self.textbox.insert(END, r' \varrho ')).place(x=147, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_7, command=lambda: self.textbox.insert(END, r' \sigma ')).place(x=176, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_8, command=lambda: self.textbox.insert(END, r' \varsigma ')).place(x=205, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_9, command=lambda: self.textbox.insert(END, r' \tau ')).place(x=234, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_10, command=lambda: self.textbox.insert(END, r' \upsilon ')).place(x=263, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_11, command=lambda: self.textbox.insert(END, r' \phi ')).place(x=292, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_12, command=lambda: self.textbox.insert(END, r' \varphi ')).place(x=321, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_13, command=lambda: self.textbox.insert(END, r' \chi ')).place(x=350, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_14, command=lambda: self.textbox.insert(END, r' \psi ')).place(x=379, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_15, command=lambda: self.textbox.insert(END, r' \omega ')).place(x=408, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_16, command=lambda: self.textbox.insert(END, r' \Sigma ')).place(x=437, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_17, command=lambda: self.textbox.insert(END, r' \Upsilon ')).place(x=465, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_18, command=lambda: self.textbox.insert(END, r' \Phi ')).place(x=493, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_19, command=lambda: self.textbox.insert(END, r' \Psi ')).place(x=521, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_20, command=lambda: self.textbox.insert(END, r' \Omega ')).place(x=549, y=31, width=26, height=26)
        Button(self.b_tab, image=self.i4_21, command=lambda: self.textbox.insert(END, r' \$ ')).place(x=577, y=31, width=26, height=26)
        
        Button(self.c_tab, image=self.i5_1, command=lambda: self.textbox.insert(END, r' \leq ')).place(x=2, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_2, command=lambda: self.textbox.insert(END, r' \prec ')).place(x=31, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_3, command=lambda: self.textbox.insert(END, r' \preceq ')).place(x=60, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_4, command=lambda: self.textbox.insert(END, r' \ll ')).place(x=89, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_5, command=lambda: self.textbox.insert(END, r' \subset ')).place(x=118, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_6, command=lambda: self.textbox.insert(END, r' \subseteq ')).place(x=147, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_7, command=lambda: self.textbox.insert(END, r' \sqsubset ')).place(x=176, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_8, command=lambda: self.textbox.insert(END, r' \sqsubseteq ')).place(x=205, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_9, command=lambda: self.textbox.insert(END, r' \in ')).place(x=234, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_10, command=lambda: self.textbox.insert(END, r' \vdash ')).place(x=263, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_11, command=lambda: self.textbox.insert(END, r' > ')).place(x=292, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_12, command=lambda: self.textbox.insert(END, r' \Join ')).place(x=321, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_13, command=lambda: self.textbox.insert(END, r' \smile ')).place(x=350, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_14, command=lambda: self.textbox.insert(END, r' \sim ')).place(x=379, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_15, command=lambda: self.textbox.insert(END, r' \asymp ')).place(x=408, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_16, command=lambda: self.textbox.insert(END, r' \equiv ')).place(x=437, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_17, command=lambda: self.textbox.insert(END, r' \mid ')).place(x=465, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_18, command=lambda: self.textbox.insert(END, r' \neq ')).place(x=493, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_19, command=lambda: self.textbox.insert(END, r' \perp ')).place(x=521, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_20, command=lambda: self.textbox.insert(END, r' : ')).place(x=549, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_21, command=lambda: self.textbox.insert(END, r' \rhd ')).place(x=577, y=2, width=26, height=26)
        Button(self.c_tab, image=self.i5_22, command=lambda: self.textbox.insert(END, r' \unrhd ')).place(x=605, y=2, width=26, height=26)

        Button(self.c_tab, image=self.i6_1, command=lambda: self.textbox.insert(END, r' \geq ')).place(x=2, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_2, command=lambda: self.textbox.insert(END, r' \succ ')).place(x=31, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_3, command=lambda: self.textbox.insert(END, r' \succeq ')).place(x=60, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_4, command=lambda: self.textbox.insert(END, r' \gg ')).place(x=89, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_5, command=lambda: self.textbox.insert(END, r' \supset ')).place(x=118, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_6, command=lambda: self.textbox.insert(END, r' \supseteq ')).place(x=147, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_7, command=lambda: self.textbox.insert(END, r' \sqsupset ')).place(x=176, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_8, command=lambda: self.textbox.insert(END, r' \sqsupseteq ')).place(x=205, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_9, command=lambda: self.textbox.insert(END, r' \ni ')).place(x=234, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_10, command=lambda: self.textbox.insert(END, r' \dashv ')).place(x=263, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_11, command=lambda: self.textbox.insert(END, r' < ')).place(x=292, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_12, command=lambda: self.textbox.insert(END, r' \bowtie ')).place(x=321, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_13, command=lambda: self.textbox.insert(END, r' \frown ')).place(x=350, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_14, command=lambda: self.textbox.insert(END, r' \simeq ')).place(x=379, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_15, command=lambda: self.textbox.insert(END, r' \approx ')).place(x=408, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_16, command=lambda: self.textbox.insert(END, r' \cong ')).place(x=437, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_17, command=lambda: self.textbox.insert(END, r' \parallel ')).place(x=465, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_18, command=lambda: self.textbox.insert(END, r' \doteq ')).place(x=493, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_19, command=lambda: self.textbox.insert(END, r' \models ')).place(x=521, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_20, command=lambda: self.textbox.insert(END, r' \propto ')).place(x=549, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_21, command=lambda: self.textbox.insert(END, r' \lhd ')).place(x=577, y=31, width=26, height=26)
        Button(self.c_tab, image=self.i6_22, command=lambda: self.textbox.insert(END, r' \unlhd ')).place(x=605, y=31, width=26, height=26)

        Button(self.d_tab, image=self.i7_1, command=lambda: self.textbox.insert(END, r' \hat{a} ')).place(x=2, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_2, command=lambda: self.textbox.insert(END, r' \acute{a} ')).place(x=31, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_3, command=lambda: self.textbox.insert(END, r' \bar{a} ')).place(x=60, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_4, command=lambda: self.textbox.insert(END, r' \dot{a} ')).place(x=89, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_5, command=lambda: self.textbox.insert(END, r' \breve{a} ')).place(x=118, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_6, command=lambda: self.textbox.insert(END, r' + ')).place(x=147, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_7, command=lambda: self.textbox.insert(END, r' \times ')).place(x=176, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_8, command=lambda: self.textbox.insert(END, r' \cap ')).place(x=205, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_9, command=lambda: self.textbox.insert(END, r' \cup ')).place(x=234, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_10, command=lambda: self.textbox.insert(END, r' \vee ')).place(x=263, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_11, command=lambda: self.textbox.insert(END, r' \setminus ')).place(x=292, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_12, command=lambda: self.textbox.insert(END, r' \bigtriangleup ')).place(x=321, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_13, command=lambda: self.textbox.insert(END, r' \triangleright ')).place(x=350, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_14, command=lambda: self.textbox.insert(END, r' \rhd ')).place(x=379, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_15, command=lambda: self.textbox.insert(END, r' \unrhd ')).place(x=408, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_16, command=lambda: self.textbox.insert(END, r' \oplus ')).place(x=437, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_17, command=lambda: self.textbox.insert(END, r' \otimes ')).place(x=465, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_18, command=lambda: self.textbox.insert(END, r' \odot ')).place(x=493, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_19, command=lambda: self.textbox.insert(END, r' \uplus ')).place(x=521, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_20, command=lambda: self.textbox.insert(END, r' \ast ')).place(x=549, y=2, width=26, height=26)
        Button(self.d_tab, image=self.i7_21, command=lambda: self.textbox.insert(END, r' \circ ')).place(x=577, y=2, width=26, height=26)

        Button(self.d_tab, image=self.i8_1, command=lambda: self.textbox.insert(END, r' \check{a} ')).place(x=2, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_2, command=lambda: self.textbox.insert(END, r' \grave{a} ')).place(x=31, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_3, command=lambda: self.textbox.insert(END, r' \vec{a} ')).place(x=60, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_4, command=lambda: self.textbox.insert(END, r' \ddot{a} ')).place(x=89, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_5, command=lambda: self.textbox.insert(END, r' \tilde{a} ')).place(x=118, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_6, command=lambda: self.textbox.insert(END, r' - ')).place(x=147, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_7, command=lambda: self.textbox.insert(END, r' \div ')).place(x=176, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_8, command=lambda: self.textbox.insert(END, r' \sqcup ')).place(x=205, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_9, command=lambda: self.textbox.insert(END, r' \sqcap ')).place(x=234, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_10, command=lambda: self.textbox.insert(END, r' \wedge ')).place(x=263, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_11, command=lambda: self.textbox.insert(END, r' \wr ')).place(x=292, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_12, command=lambda: self.textbox.insert(END, r' \bigtriangledown ')).place(x=321, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_13, command=lambda: self.textbox.insert(END, r' \triangleleft ')).place(x=350, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_14, command=lambda: self.textbox.insert(END, r' \lhd ')).place(x=379, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_15, command=lambda: self.textbox.insert(END, r' \unlhd ')).place(x=408, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_16, command=lambda: self.textbox.insert(END, r' \ominus ')).place(x=437, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_17, command=lambda: self.textbox.insert(END, r' \oslash ')).place(x=465, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_18, command=lambda: self.textbox.insert(END, r' \bigcirc ')).place(x=493, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_19, command=lambda: self.textbox.insert(END, r' \amalg ')).place(x=521, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_20, command=lambda: self.textbox.insert(END, r' \star ')).place(x=549, y=31, width=26, height=26)
        Button(self.d_tab, image=self.i8_21, command=lambda: self.textbox.insert(END, r' \bullet ')).place(x=577, y=31, width=26, height=26)

    def transform(self):
        try:
            self.status.config(text='Подождите...')
            self.root.update()
            geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
            doc = Document(geometry_options=geometry_options)
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(self.textbox.get(0.0, END))
            doc.generate_pdf(str(self.entry.get()), clean_tex=True)
            self.status.config(text='Готово.')
        except Exception as e:
            self.status.config(text=e)


if __name__ == '__main__':
    _ = Abc()
