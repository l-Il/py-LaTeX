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
        self.root.configure(background='#202020')

        # Конструктор окна приложения (GUI)
        Label(self.root, text='Название отчёта:').place(x=0, y=0)
        self.entry1 = Entry(self.root)
        self.entry1.place(x=0, y=20, width=100, height=20)
        Label(self.root, text='Номер курса:').place(x=0, y=40)
        self.entry2 = Entry(self.root)
        self.entry2.place(x=85, y=40, width=100, height=20)
        Label(self.root, text='Группа: ').place(x=0, y=80)
        self.entry3 = Entry(self.root)
        self.entry3.place(x=55, y=80, width=100, height=20)
        Label(self.root, text='Шифр:').place(x=0, y=120)
        self.entry4 = Entry(self.root)
        self.entry4.place(x=45, y=120, width=50, height=20)
        Label(self.root, text='ФИО студента:').place(x=0, y=160)
        self.entry5 = Entry(self.root)
        self.entry5.place(x=90, y=160, width=100, height=20)
        Label(self.root, text='Фамилия И.О преподавателя:').place(x=0, y=200)
        self.entry6 = Entry(self.root)
        self.entry6.place(x=0, y=220, width=100, height=20)
        Button(self.root, text='Создать', command=self.create).place(x=150, y=280)
        self.root.mainloop()

    def create(self):
        try:
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
                    page.append('Выполнил:\n')
                    page.append(f'Студент {str(self.entry2.get())} курса\n')
                    page.append(f'Группа {str(self.entry3.get())}\n')
                    page.append(f'Шифр {str(self.entry4.get())}\n')
                    page.append(f'{str(self.entry5.get())}\n')
                    page.append(LineBreak())
                    page.append(LineBreak())
                    page.append('Проверил:\n')
                    page.append(f'{str(self.entry6.get())}\n')

            # Нижний колонтитул
            header = PageStyle("header")
            with header.create(Foot("C")):
                header.append(f'Москва, {time.now().timetuple().tm_year}\n')
            doc.preamble.append(header)
            doc.change_document_style("header")

            doc.generate_pdf("title", clean_tex=False)


        except Exception as e:
            print(e)


if __name__ == '__main__':
    _ = Title()
