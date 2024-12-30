define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")
define k = Character('Кристина', color="#1e90ff")

transform left_position:
    xalign 0.2
    yalign 1.1
    zoom 0.8

transform center_position:
    xalign 0.5
    yalign 1.1
    zoom 0.8

transform right_position:
    xalign 0.8
    yalign 1.1
    zoom 0.8

label scene15:
    scene bg dormitory with fade

    show alexey normal at right_position
    show igor normal at center_position
    show kristina normal at left_position

    a "Всё, ребята. Мы сделали это. Проект отправлен."

    k "Даже не верится, что мы уложились. И знаете что? Я думаю, у нас есть шансы на победу."

    i "Или хотя бы на призовое место. Мы реально постарались. Алексей, спасибо, что затащил всю техническую часть."

    a "Без вас я бы точно не справился. Дизайн и текст тоже на высоте."

    k " А теперь давайте выспимся. Завтра объявят результаты, но я уже горжусь нашей работой."

    scene bg black
    with fade

    return