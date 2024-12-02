define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label chapter2:

    scene bg street
    with fade

    show alexey normal at center_right
    with moveinright

    "Алексей идёт по тёмной улице. Свет фонарей тусклый, машины проносятся мимо, прохожие торопятся по своим делам."

    "Он смотрит себе под ноги, руки в карманах, видимо, потерян в мыслях. Внезапно сзади слышится голос."

    i "Эй, Алексей?! Это ты?"

    show igor normal at left_to_right
    with moveinleft

    i "Игорь? Привет! Не ожидал тебя встретить."

    a "Ага. Завод рядом, туда и хожу каждый день."

    i "Завод? Ты серьёзно?"

    a "Ага. Ничего особенного, обычная работа. А ты что, тут по делам?"

    i "Да, у нас в офисе встреча была. Работаю недалеко, в «CodeCraft»."

    i "Слушай, может, зайдём куда-нибудь? Тут неподалёку кафе есть. Всё равно уже поздно, домой не торопишься?"

    a "Ну... ладно. Почему бы и нет."

    hide igor
    with dissolve

    hide alexey
    with dissolve

    return
