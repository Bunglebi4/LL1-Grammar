import string


def language():
    global ch
    if (ch in string.ascii_letters) or (ch == '[') or (ch == '('):
        brackets_sentence()


def brackets_sentence():
    global ch
    if ch == "(":
        read()
        inner_bracket_sentence()
        if ch == ")":
            read()
            sign()
            brackets_sentence()
    elif ch == "[":
        read()
        inner_bracket_sentence()
        if ch == "]":
            read()
            sign()
            brackets_sentence()


def inner_bracket_sentence():
    global ch
    if (ch in string.ascii_letters) or (ch == '[') or (ch == '('):
        arifmetic()
        sign()
        inner_bracket_sentence()


def parenthesis():
    global ch
    if ch == "(":
        read()
        arifmetic()
        if ch == ")":
            read()
        else:
            raise ValueError
    else:
        raise ValueError


def square_bracket():
    global ch
    if ch == "[":
        read()
        arifmetic()
        if ch == "]":
            read()
        else:
            raise ValueError
    else:
        raise ValueError


def arifmetic():
    global ch
    if (ch in string.ascii_letters):
        letter()
        sign()
        tag()
    elif ch == "[":
        square_bracket()
        end_for_bracket()
    elif ch == "(":
        parenthesis()
        end_for_bracket()
    else:
        raise ValueError


def tag():
    global ch
    if (ch in string.ascii_letters):
        letter()
        end()
    elif ch == "[":
        square_bracket()
        end_for_bracket()
    elif ch == "(":
        parenthesis()
        end_for_bracket()
    else:
        raise ValueError


def end():
    global ch
    if ch in ("*", "/", "+", "-"):
        sign_for_letter()
        tag()


def end_for_bracket():
    global ch
    sign()
    if (ch in string.ascii_letters) or (ch == '[') or (ch == '('):
        tag()


def letter():
    global ch
    if ch in string.ascii_letters:
        read()
    else:
        raise ValueError


def sign():
    global ch
    if ch in ("+", "-", "*", "/"):
        read()


def sign_for_letter():
    global current_letter
    if ch in ("+", "-", "*", "/"):
        read()
    else:
        raise ValueError


def read():
    global input_string
    global ch
    global index
    if index + 1 < len(input_string):
        index += 1
        ch = input_string[index]


print("""

Бункевич Глеб гр. 1305
Вариант 4

Формулировка задания: 

Правильная скобочная запись арифметических выражений с двумя видами скобок. 
Друг за другом могут стоять не более двух скобок. 
Знак умножения между парами скобок может пропускаться.
Могут быть “лишние” скобки, но одна буква не может браться в скобки.

Пример. 	
Правильная запись: [((a+b)c*[[a-b+c*c]])]((a-b+c)[a((b+c))])
Неправильная запись [(a)([b-c*d]([a-b+c]/(a+b)*(c-d)))]

""")
while True:
    input_string = input("Введите строку: ")
    index = 0
    ch = input_string[index]
    try:
        language()
    except ValueError:
        print("Неправильная запись!")
    else:
        print("Правильная запись")