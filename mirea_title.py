# Бета версия программы, автоматически создающей титульный лист с введёнными в консоль данными.

from datetime import datetime as time
import os
from pylatex import Command, Document, Figure, Foot, LargeText, LineBreak, MediumText, MiniPage, TextBlock, Package, PageStyle
from pylatex.utils import bold


class Title():
    def __init__(self):
        pass


if __name__ == '__main__':

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
    doc.change_length("\TPHorizModule", "1mm")
    doc.change_length("\TPVertModule", "1mm")
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
            page.append(f'По: {input("Введите название отчёта: > ")}\n')

        # Правая часть обложки
        with page.create(TextBlock(80, 88, 120)):
            page.append('Выполнил:\n')
            page.append(f'Студент {input("Введите номер курса: > ")} курса\n')
            page.append(f'Группа {input("Введите свою группу: > ")}\n')
            page.append(f'Шифр {input("Введите свой шифр: > ")}\n')
            page.append(f'{input("Введите свои ФИО: > ")}\n')
            page.append(LineBreak())
            page.append(LineBreak())
            page.append('Проверил:\n')
            page.append(f'{input("Введите ФИО преподавателя: > ")}\n')

    # Нижний колонтитул
    header = PageStyle("header")
    with header.create(Foot("C")):
        header.append(f'Москва, {time.now().timetuple().tm_year}\n')
    doc.preamble.append(header)
    doc.change_document_style("header")

    doc.generate_pdf("title", clean_tex=False)
