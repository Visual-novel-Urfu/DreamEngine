define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")
define k = Character('Кристина', color="#1e90ff")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label scene15:
    scene bg dormitory with fade

    show alexey normal at center_right

    a "Всё, ребята. Мы сделали это. Проект отправлен."

    k "Даже не верится, что мы уложились. И знаете что? Я думаю, у нас есть шансы на победу."

    i "Или хотя бы на призовое место. Мы реально постарались. Алексей, спасибо, что затащил всю техническую часть."

    a "Без вас я бы точно не справился. Дизайн и текст тоже на высоте."

    k " А теперь давайте выспимся. Завтра объявят результаты, но я уже горжусь нашей работой."

    scene bg black
    with fade

    return