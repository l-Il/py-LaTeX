# Бета версия программы, автоматически создающей титульный лист с введёнными в консоль данными.

from datetime import datetime as time
import os
from pylatex import Command, Document, Figure, Foot, LargeText, LineBreak, MediumText, MiniPage, TextBlock, Package, PageStyle
from pylatex.utils import bold

if __name__ == '__main__':

    # Настройки отступов, языка
    geometry_options = {"tmargin": "2cm", "lmargin": "3cm", "rmargin": "1.5cm", "bmargin": "2cm"}
    doc = Document(geometry_options=geometry_options)
    doc.packages.add(Package('grffile', options=['encoding', 'filenameencoding=utf8']))

    # Вставляем логотип МИРЭА
    image_filename = os.path.join(os.path.dirname(__file__), 'логотип.png')
    with doc.create(Figure(position='h!')) as logo:
        logo.add_image(image_filename, width='80px')

    # Нижний колонтитул
    header = PageStyle("header")
    with header.create(Foot("C")):
        header.append(f'Moscow, {time.now().timetuple().tm_year}\n')
    doc.preamble.append(header)
    doc.change_document_style("header")

    # Обложка
    doc.change_length("\TPHorizModule", "1mm")
    doc.change_length("\TPVertModule", "1mm")
    with doc.create(MiniPage(width=r"\textwidth")) as page:

        with page.create(TextBlock(180, 0, 0)):
            page.append(Command('centering'))
            page.append('MINOBRNAUKI ROSSII\n')
            page.append('Federalnoe gosudarstvennoe budgetnoe obrazovatelnoe ucherezdenie vishego obrazovania\n')
            page.append(MediumText(bold('<<MIREA - Rossiyski Texnologicheskiy Universitet\n')))
            page.append(LargeText(bold('RTU MIREA\n')))
            page.append(LineBreak())
            page.append(MediumText(bold('Institut complex bezopasnosti i special priborostroyenia\n')))
            page.append(LineBreak())
            page.append('Kafedra KB-8 <<Information Protivoborstvo>>\n')
            page.append(LineBreak())
            page.append(LineBreak())
            page.append(LineBreak())
            page.append(LargeText('Otchet\n'))
            page.append(f'po: {input("Введите название отчёта: > ")}\n')

        with page.create(TextBlock(80, 120, 120)):
            page.append('Vipolnil:\n')
            page.append(f'Student {input("Введите номер курса: > ")} kursa\n')
            page.append(f'Gruppa {input("Введите свою группу: > ")}\n')
            page.append(f'Shifr {input("Введите cвой шифр: > ")}\n')
            page.append(f'Student {input("Введите свои ФИО: > ")}\n')
            page.append('Proverila:\n')
            page.append(f'{input("Введите ФИО преподавателя: > ")}\n')

    doc.generate_pdf("title", clean_tex=False)
