import numpy as np  # Используем библиотеку NumPY
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Matrix, Alignat  # Импортируем нужные классы
from pylatex.utils import italic  # Импорт шрифта курсива

if __name__ == '__main__':  # Запуск программы
    # tmargin - верхний (top) отступ
    # lmargin - левый (left) отступ
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}

    # Переменной doc (для дальнейшего использования присваиваем класс Документ с настройками границ выше
    doc = Document(geometry_options=geometry_options)

    # Создаём секцию. Заголовок 1.
    with doc.create(Section('Simple things')):
        # Добавляем обычный текст
        doc.append('Some basic text, and even ')
        # Добавляем курсив
        doc.append(italic('italic bold. '))
        # Переход на следующую строку, и вывод символов
        doc.append('\nAnd some symbols: $&#{}')
        # Создаём многоуровневую секцию 1.1.
        with doc.create(Subsection('Math that is incorrect: ')):
            # Добавляем математическое выражение
            doc.append(Math(data=['2*3', '=', 9]))

        # Создаём многоуровневую секцию (теперь уже 1.2.)
        with doc.create(Subsection('Tables, or kinda:')):
            # Создаём таблицу ('ccc|c') создаёт 4 строчечную таблицу с границей после 3 колонки
            with doc.create(Tabular('ccc|c')) as table:
                # Добавляем верхнюю границу на всю таблицу
                table.add_hline()
                # Добавляем строку c этими значениями, указанными как tuple (верхний ряд)
                table.add_row(('first', 2, 'Greece', 666.2))
                # Указываем, какие элементы подчеркнуть (добавить границу снизу) (с какого по какой)
                table.add_hline(0, 2)
                # Добавляем пустую строку без значений в таблицу (2 ряд)
                table.add_empty_row()
                # Добавляем строку c этими значениями, указанными как tuple (нижний ряд)
                table.add_row((4, 5, 6, 7))

    # Указываем, что переменная а это матрица 3х1 и транспонируем её (получается 1х3)
    a = np.array([[100, 10, 20]]).T
    # Указываем, элементы матрицы "в лоб"
    M = np.matrix([[2, 3, 4],
                   [-1, 0, 1],
                   [0, 0, 2]])

    # Создаём секцию. Заголовок 2.
    with doc.create(Section('The fancy stuff')):
        # Создаём многоуровневую секцию 2.1.
        with doc.create(Subsection('Correct matrix equations')):
            # Добавляем математический пример, сначала 2 матрицы, потом их произведение
            doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

        # Создаём многоуровневую секцию 2.2.
        with doc.create(Subsection('Alignat math environment')):
            # Также можно добавить формулу через "Выравниватель"
            # numbering - Нумерация формул (1) (2) в разделе
            # escape - оставляет строчки "сырыми", если True
            with doc.create(Alignat(numbering=True, escape=False)) as agn:
                # Добавляем формулу
                # frac - дробь
                # \\ - перенос на след строчку (как \n в строках)
                agn.append(r'\frac{a}{b} = 0\\')
                # Добавляем формулу умножения матриц
                agn.extend([Matrix(M), Matrix(a), '=', Matrix(M * a)])

        # Создаём многоуровневую секцию 2.3.
        with doc.create(Subsection('Beautiful graphs')):
            # Создаём движок для графика (TikZ)
            with doc.create(TikZ()):
                # Создаём настройки для графика
                # width - ширина
                # height - высота
                # grid - сетка (major - основные, minor - все деления)
                plot_options = 'width=6cm, height=4cm, grid=major'
                # Создаём пустой график с осями
                with doc.create(Axis(options=plot_options)) as plot:
                    # Добавляем точки с помощью функции, выводя в легенду название
                    plot.append(Plot(name='Function', func='-x^5 - 242'))

                    # Создаём список координат
                    coordinates = [
                        (-4.77778, 2027.60977),
                        (-3.55556, 347.84069),
                        (-2.33333, 22.58953),
                        (-1.11111, -493.50066),
                        (0.11111, 46.66082),
                        (1.33333, -205.56286),
                        (2.55556, -341.40638),
                        (3.77778, -1169.24780),
                        (5.00000, -3269.56775),
                    ]
                    # Либо на график можно добавить точки вручную по координатам
                    plot.append(Plot(name='By hand', coordinates=coordinates))

    # В этой же директории создаём .pdf документ с настройками выше
    # С названием "example"
    # Выбираем НЕ удалять .tex файл
    doc.generate_pdf('example', clean_tex=False)
    # Выводим "статус" в консоль, о том, что программа отработала
    print('Готово!')
