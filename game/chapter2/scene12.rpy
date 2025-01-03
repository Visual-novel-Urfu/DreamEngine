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
    xzoom -1.0

label scene12:
    scene black with fade
    show text Text("Среда", color="#FFFFFF", size=30, xalign=0.5, yalign=0.5)
    pause 2.0
    hide text with fade

    call screen characteristics
    with fade

    $ points = 10
    $ fatigue = fatigue - 4

    scene bg classroom with fade

    show alexandr normal at left_to_right
    with moveinleft

    "Среда прошла как обычно, ничего интересного"

    scene black with fade
    show text Text("Четверг", color="#FFFFFF", size=30, xalign=0.5, yalign=0.5)
    pause 2.0
    hide text with fade

    call screen characteristics
    with fade

    $ points = 10
    $ fatigue = fatigue + 4
    $ fatigue_buffer = fatigue

    scene bg dormitory with fade

    show alexey dormitory at right_position
    show igor student at center_position
    show kristina normal at left_position

    i "Итак, у нас есть прототип сайта для управления учебными заданиями. Что сделано: я добавил возможность создавать списки заданий, задавать дедлайны и помечать их статус."

    i "Алексей, как у тебя с интеграцией?"

    a "Каркас готов. Функции работают, но интерфейс всё ещё пустой. Вот, смотри."

    k "Это... ну, функционально, но скучно. Мы же хотим, чтобы этим было удобно пользоваться, верно?"

    i "Вот именно. И тут как раз нужна ты, Кристина. Что у тебя с дизайном?"

    k "Я накидала несколько вариантов. Вот, смотрите."

    k "Я подумала, что нужно разделить задания по предметам. Пользователь сможет добавлять задачи, ставить приоритеты и следить за прогрессом в статистике."

    a "Это круто. Особенно календарь — с ним будет проще не упускать дедлайны."

    i "Да, и это впишется в нашу идею. Алексей, сможешь всё это натянуть на сайт?"

    a "Смогу, но мне нужно пару дней. Вёрстка — это не мой конёк."

    k "Я помогу. Давайте сделаем так: я завершу макет до конца дня, а завтра начнём интеграцию."

    k "А ты что будешь делать?"

    i "Я работаю над функцией уведомлений. Пользователь сможет получать напоминания о ближайших дедлайнах."

    i "Это нужно ещё протестировать, но я думаю, к концу недели всё будет готово."

    a "Хорошо. Значит, на сегодня у нас задачи такие: я доделаю основные элементы, Кристина заканчивает дизайн, Игорь занимается уведомлениями."

    a "Кстати, у меня ещё идея: что если добавить раздел с советами по тайм-менеджменту? Типа короткие рекомендации, как организовать учебу."

    k "Звучит неплохо. Это можно сделать в виде подсказок на главной странице."

    i "Или встроить в статистику. Например, если у пользователя слишком много заданий с пропущенными дедлайнами, показывать уведомление: “Сократи количество задач” или что-то в этом духе."

    a "Да, это отлично. Тогда добавим в план."

    scene bg black
    with fade

    return