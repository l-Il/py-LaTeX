# Бета версия программы, автоматически создающей титульный лист с введёнными в консоль данными.

from datetime import datetime as time
import os
from tkinter import *
from pylatex import Command, Document, Figure, Foot, LargeText, LineBreak, MediumText, MiniPage, TextBlock, Package, PageStyle
from pylatex.utils import bold


class Title:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('350x450')
        self.root.title('Создать титульный лист:')
        # self.root.configure(background='#202020')

        # Конструктор окна приложения (GUI)
        self.status = Label(self.root, text='Введитe поля ниже и нажмите кнопку.')
        self.status.place(x=0, y=10, width=350, height=20)
        Label(self.root, text='Название отчёта:').place(x=0, y=40, width=100, height=20)
        self.entry1 = Entry(self.root)
        self.entry1.place(x=101, y=40, width=250, height=20)

        self.your_var = IntVar()
        self.your_var.set(0)
        Label(self.root, text='Ваш пол:').place(x=140, y=70, width=80, height=20)
        self.male = Radiobutton(self.root, text="Мужской", variable=self.your_var, value=0)
        self.male.place(x=140, y=90)
        self.female = Radiobutton(self.root, text="Женский", variable=self.your_var, value=1)
        self.female.place(x=140, y=110)
        self.var = IntVar()
        self.var.set(0)
        Label(self.root, text='Пол преподавателя:').place(x=220, y=130, width=140, height=20)
        self.male = Radiobutton(self.root, text="Мужской", variable=self.var, value=0)
        self.male.place(x=220, y=150)
        self.female = Radiobutton(self.root, text="Женский", variable=self.var, value=1)
        self.female.place(x=220, y=170)

        Label(self.root, text='Номер курса:').place(x=0, y=80, width=80, height=20)
        self.entry2 = Entry(self.root)
        self.entry2.place(x=81, y=80, width=20, height=20)
        Label(self.root, text='Группа: ').place(x=0, y=120, width=50, height=20)
        self.entry3 = Entry(self.root)
        self.entry3.place(x=51, y=120, width=70, height=20)
        Label(self.root, text='Шифр:').place(x=0, y=160, width=40, height=20)
        self.entry4 = Entry(self.root)
        self.entry4.place(x=41, y=160, width=50, height=20)
        Label(self.root, text='ФИО студента:').place(x=0, y=200, width=80, height=20)
        self.entry5 = Entry(self.root)
        self.entry5.place(x=81, y=200, width=270, height=20)
        Label(self.root, text='Фамилия И.О преподавателя:').place(x=0, y=240, width=170, height=20)
        self.entry6 = Entry(self.root)
        self.entry6.place(x=171, y=240, width=180, height=20)
        Button(self.root, text='Создать', command=self.create).place(x=145, y=280, width=60, height=20)
        self.root.mainloop()

    def create(self):
        try:
            self.status['text'] = 'Загрузка, подождите'
            self.root.update()
            # Настройки отступов, языка
            geometry_options = {"tmargin": "2cm", "lmargin": "3cm", "rmargin": "1.5cm", "bmargin": "2cm"}
            doc = Document(geometry_options=geometry_options)
            doc.packages.add(Package('grffile', options=['encoding', 'filenameencoding=utf8']))
            doc.packages.add(Package('babel', options=['russian']))

            # Вставляем логотип МИРЭА
            image_filename = os.path.join(os.path.dirname(__file__), 'логотип.png')
            with doc.create(Figure(position='h!')) as logo:
                logo.add_image(image_filename, width='80px')

            # Обложка
            doc.change_length(r"\TPHorizModule", "1mm")
            doc.change_length(r"\TPVertModule", "1mm")
            with doc.create(MiniPage(width=r"\textwidth")) as page:
                # Центральная часть обложки
                with page.create(TextBlock(180, 0, 0)):
                    page.append(Command('centering'))
                    page.append('МИНОБРНАУКИ РОССИИ\n')
                    page.append('Федеральное государственное бюджетное образовательное учреждение высшего образования\n')
                    page.append(MediumText(bold('«МИРЭА - Российский Технологический Университет»\n')))
                    page.append(LargeText(bold('РТУ МИРЭА\n')))
                    page.append(LineBreak())
                    page.append(MediumText(bold('Институт комплексной безопасности и специального приборостроения\n')))
                    page.append(LineBreak())
                    page.append('Кафедра КБ-8 «Информационное Противоборство»\n')
                    page.append(LineBreak())
                    page.append(LineBreak())
                    page.append(LineBreak())
                    page.append(LargeText('Отчёт\n'))
                    page.append(f'{str(self.entry1.get())}\n')

                # Правая часть обложки
                with page.create(TextBlock(80, 88, 120)):
                    if self.your_var.get() == 0:
                        page.append('Выполнил:\n')
                        page.append(f'Студент {str(self.entry2.get())} курса\n')
                    else:
                        page.append('Выполнила:\n')
                        page.append(f'Студентка {str(self.entry2.get())} курса\n')
                    page.append(f'Группа {str(self.entry3.get())}\n')
                    page.append(f'Шифр {str(self.entry4.get())}\n')
                    page.append(f'{str(self.entry5.get())}\n')
                    page.append(LineBreak())
                    page.append(LineBreak())
                    if self.var.get() == 0:
                        page.append('Проверил:\n')
                    else:
                        page.append('Проверила:\n')
                    page.append(f'{str(self.entry6.get())}\n')

            # Нижний колонтитул
            header = PageStyle("header")
            with header.create(Foot("C")):
                header.append(f'Москва, {time.now().timetuple().tm_year}\n')
            doc.preamble.append(header)
            doc.change_document_style("header")

            doc.generate_pdf("title", clean_tex=False)
            self.status['text'] = 'Готово!'

        except FileNotFoundError as e:
            self.status['text'] = str(e)


if __name__ == '__main__':
    _ = Title()
