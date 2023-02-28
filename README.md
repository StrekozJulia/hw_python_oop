# Модуль фитнес-трекера
Программный модуль для фитнес-трекера, который обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания.
Модуль является демонстрационной программой реализующей парадигму ООП.

### Выполняемые функции:
* принимать от блока датчиков информацию о прошедшей тренировке,
* определять вид тренировки,
* рассчитывать результаты тренировки,
* выводить информационное сообщение о результатах тренировки.

### Содержание информационного сообщения:
* тип тренировки (бег, ходьба или плавание);
* длительность тренировки;
* дистанция, которую преодолел пользователь, в километрах;
* средняя скорость на дистанции, в км/ч;
* расход энергии, в килокалориях.

### Реализованные классы:
* базовый класс Training;
* три дочерних класса: Running (RUN), SportsWalking (WLK), Swimming (SWM).

## Запуск модуля:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:StrekozJulia/hw_python_oop.git
cd hw_python_oop
```
2. Открыть файл homework.py в редакторе кода
3. Передать в модуль исходные данные в формате:
```
packages = [
        ('SWM', [<к-во гребков>, <время тренировки, ч>, <вес>, <длина бассейна>, <к-во бассейнов>]),
        ('RUN', [<к-во шагов>, <время тренировки, ч>, <вес>]),
        ('WLK', [<к-во шагов>, <время тренировки, ч>, <вес>, <рост>]),
    ]
```