# LL1-Grammar
КС грамматика удовлетворяющая LL1, написано на python
Бункевич Глеб гр. 1305
Вариант 4

Формулировка задания: 

Правильная скобочная запись арифметических выражений с двумя видами скобок. Друг за другом могут стоять не более двух скобок. Знак умножения между парами скобок может пропускаться. Могут быть “лишние” скобки, но одна буква не может браться в скобки.

Пример. 	Правильная запись: [((a+b)c*[[a-b+c*c]])]((a-b+c)[a((b+c))])
Неправильная запись [(a)([b-c*d]([a-b+c]/(a+b)*(c-d)))]

Рефлексия: 
Исходя из текста можно понять следующее: Язык необходим для записи арифметических выражений, в нем есть два вида скобок и стандартные операторы из арифметики(“+” “-” “*” “/”). Далее указано, что друг за другом могут стоять не более двух скобок, однако, вероятно имелось в виду, что друг за другом  могут стоять не более двух  одинаковой вложенности скобок, что следует из примера(в правильной записи встречается последовательность скобок “[((“, что не соответствует условию без указанного уточнения). Также, взять одну букву в скобки нельзя. Более того, для большего понимания стоит детально разобрать контрпример – выделенные желтым участки несут в себе следующие ошибки:
(a) является ошибкой, так как одна буква взята в скобки
([a-b+c]/(a+b)*(c-d))) является ошибкой, так как в конце стоит три скобки одного типа подряд.  


Пример 1. 

[(a+b)(b+c)](d+a)

Пример 2.

[[([a+c])]]

Пример 3. 

(a+b+c-d) 

Пример 4.

(([b-d]*[d+a])+f)
 
Пример 5. 

[a - b + c] 


Контрпример 1.
 
(((a + b)))

Пояснение: стоит более двух скобок одного типа подряд

Контрпример 2.

[[[a+b][b+a]]]

Пояснение: стоит более двух скобок одного типа подряд

Контрпример 3. 

(a)(b)
Пояснение: одна буква взята в скобки 

Контрпример 4. 

(b+a]

Пояснение: выражение закрывается разным типом скобок

Контрпример 5. 

	((a+b)  

Пояснение: есть одна незакрытая скобка 


Вопросы: 
1. В случае, если “*” не ставится между буквами, является ли это ошибкой? 



2. КС-грамматика языка


<язык> ::= <скобочное выражение> | ^
<скобочное выражение> ::= (<выражение внутри скобок>) <знак> <скобочное выражение> | [<выражение внутри скобок>] <знак> <скобочное выражение> | ^
<выражение внутри скобок> ::= <арифметическое выражение> <знак> <выражение внутри скобок> | ^
<к скб> ::= (<арифметическое выражение>)
<кв скб> ::= [<арифметическое выражение>]
<арифметическое выражение> ::= <буква><знак><тег> | <кв скб><конец для скб> | <кр скб> <конец для скб> 
<тег>::= <буква><конец> | <кв скб> <конец для скб> | <к скб > <конец для скб>
<Конец>= <знак для букв><тег>|^
<конец для скб> ::= <знак><тег> | ^
<знак> ::= ^ | * | - | / | +
<знак для букв> ::= * | + | - | /
<буква> ::= a | b| … | z



3. проверка примера


Пример:  [((a+b)c*[[a-b+c*c]])]
<язык>
<скобочное выражение> 
[<выражение внутри скобок>]
[(<арифметическое выражение>)]
[(<кр скб> <конец для скб> )]
[((<арифметическое выражение) <конец для скб> )]
[((<буква><знак для буквы><тег>) <конец для скб> )]
[((a+<буква><конец>) <конец для скб> )]
[((a+b>)<знак><тег> )]
[((a+b>)с<конец>)]
[((a+b>)с <знак для букв><тег>)]
[((a+b>)с*[<арифметическое выражение>])]
[((a+b>)с*[<кв скб>])] 
[((a+b>)с*[[<арифметическое выражение>]])] 
[((a+b>)с*[[a-<тег>]])] 
[((a+b>)с*[[a-<буква><конец>]])] 
[((a+b>)с*[[a-b+<тэг>]])]
[((a+b>)с*[[a-b+c*c]])]

4 задание. 


<язык> :
L(W1) = {a, b,..., z}
L(W2) = { [ }
L(W3) = { ( }
L(W4) = {+, - , *, ^} 
W1 and W2 and … and W4 == {}
<выражение внутри скобок> :
	L(W1) = {a, b,..., z}
L(W2) = {}
L(W3) = { [ }
L(W4) = { ( }
W1 and W2 and … and W4 == {}
<тег>
L(W1) = {a, b,..., z}
L(W2) = {(}
L(W3) = {[}
W1 and W2 and W3 == {}



