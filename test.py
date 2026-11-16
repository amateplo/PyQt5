from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QButtonGroup
from random import shuffle, choice

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []

questions_list.append(
    Question('Государствеенный язык Бразилии' , 'португальский', 'Немецкий', 'Итальянаский', 'Английский')
)
questions_list.append(
    Question('Государственный язык португалии', 'Португальский', 'Английский', 'Испанский','Французкий')
)
questions_list.append(
    Question('Вкакой стране находятся пирамиды Гизы?', 'Египет', 'Бразилия', 'Китай','Мексика')
)
questions_list.append(
    Question('Какой национальный символ изобраен на флаге Канады?', 'Дубовый лист', 'Кленовый лист', 'Пальмовая ветвь','Цветущач сакура')
)
questions_list.append(
    Question('Какой город является столицей Франции?', 'Берлин', 'Мадрид', 'Париж','Рим')
)
questions_list.append(
    Question('Самая большая страна по площади?', 'Китай', 'США', 'Россия','Канада')
)
questions_list.append(
    Question('В какой стране находится Эйфелева башня?', 'Италия', 'Франция', 'Испания','Германия')
)
questions_list.append(
    Question('Столица какой страны является Токио?', 'Китай', 'Южная Корея', 'Япония','Таиланд')
)
questions_list.append(
    Question('Какая страна имеет форму, напоминающаую сапог?', 'Греция', 'Италия', 'Чили','Индия')
)
questions_list.append(
    Question('Какое животное является национальм символом Австралии?', 'Панда', 'Медведь', 'Кенгуру','Тигр')
)
questions_list.append(
    Question('Какая страна является самой густонаселенной в мире?', 'США', 'Китай', 'Япония','Индия')
)





app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
text = QLabel('Здесь должен быть текст')
main_win.resize(600, 400)

Buttons = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Вариант1')
answer2 = QRadioButton('Вариант2')
answer3 = QRadioButton('Вариант3')
answer4 = QRadioButton('Вариант4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

buttonan = QPushButton('Ответить')

Ansgroupbox = QGroupBox('Результат теста')
result = QLabel('Прав ты или не прав')
correct = QLabel('Верно/неверно!')

Resbox = QGroupBox('')
result2 = QLabel('')
correct2 = QLabel('Дано верных ответов:')

total = QLabel('')


h1line = QHBoxLayout()#вопрос
h2line = QHBoxLayout()#ответы
h3line = QHBoxLayout()
h2line.addWidget(Buttons)
h3line.addStretch(1)
h3line.addWidget(buttonan, stretch=2)
h3line.addStretch(1)
h2line.setSpacing(5)#кнопка
mainvline = QVBoxLayout()#глпаная лииния



v_line1 = QVBoxLayout()#первая вертикаль
v_line2 = QVBoxLayout()#вторая вертикаль
box_line = QHBoxLayout() #оснавная горизанталь

v_line1.addWidget(answer1)#кнопки на первой линиии
v_line1.addWidget(answer3)#кнопки на первой линиии
v_line2.addWidget(answer2)#кнопки на второй линии
v_line2.addWidget(answer4)#кнопки на второй линии

box_line.addLayout(v_line1)#линии лежащие в гуппе
box_line.addLayout(v_line2)#линии лежащие в гуппе

Buttons.setLayout(box_line)
#Ответы
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment=Qt.AlignCenter, stretch=2)
Ansgroupbox.setLayout(layout_res)

#Результаты
layout_res2 = QVBoxLayout()
layout_res2.addWidget(correct2, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res2.addWidget(total, alignment=Qt.AlignCenter, stretch=2)
Resbox.setLayout(layout_res2)
Ansgroupbox.hide()


h1line.addWidget(text, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))#текст на линии
h2line.addWidget(Buttons)#варанты ответов ана линии
h2line.addWidget(Ansgroupbox)#варанты ответов ана линии
h2line.addWidget(Resbox)
Resbox.hide()
Ansgroupbox.hide()#варанты ответов ана линии
#кнопка на линиие

mainvline.addLayout(h1line, stretch=2)#горизпнтпль лежит на главной линии
mainvline.addLayout(h2line, stretch=8)#горизпнтпль лежит на главной линии
mainvline.addStretch(1)#горизпнтпль лежит на главной линии
mainvline.addLayout(h3line, stretch=1)#горизпнтпль лежит на главной линии
mainvline.addStretch(1)
mainvline.setSpacing(5)

def show_question():
    Buttons.show()
    Ansgroupbox.hide()
    buttonan.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    Buttons.hide()
    Ansgroupbox.show()
    buttonan.setText('Следующий вопрос')

answers = [answer1, answer2, answer3, answer4]
def ask(q: Question):
    shuffle (answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    correct.setText(q.right_answer)
    show_question()
    
def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Верно")
        result.setStyleSheet ("color: MediumSpringGreen;")
        main_win.score += 1

    else: 
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            result.setStyleSheet ("color: red")
    print('Статистика \n Всего влпросов:'  ,main_win.total,' \n-Правильных ответов:', main_win.score)
    print('Рейтинг:', int(main_win.score/ main_win.total*100), '%')

def next_question():
    #main_win.cur_question += 1
    #if main_win.cur_question >= len(questions_list):
    #    main_win.cur_question = 0
    #q = questions_list[main_win.cur_question]
    if len(questions_list) != 0:
        q = choice(questions_list)
        main_win.total += 1
        ask(q)
        questions_list.remove(q)

def get_result():
    Buttons.hide()
    Ansgroupbox.hide()
    Resbox.show()
    text.setText('Результат')
    buttonan.hide()
    total.setText(str(main_win.score) + "из" + str(main_win.total))

def click_ok():
    if buttonan.text() == 'Ответить':
        check_answer()
    elif len(questions_list) == 0:
        get_result()
    else:
        next_question()

Buttons.setLayout(box_line)
main_win.setLayout(mainvline)

#Стили
main_win.setStyleSheet("background-color: PaleTurquoise; font-size: 24px")
buttonan.setStyleSheet("background-color: MediumAquamarine; font-weight:bold; border:2px solid DarkSlateGray")
text.setStyleSheet("font-weight:bold;")


main_win.cur_question = -1
buttonan.clicked.connect(click_ok)
main_win.score = 0
main_win.total = 0

next_question()



main_win.show()
app.exec_()
