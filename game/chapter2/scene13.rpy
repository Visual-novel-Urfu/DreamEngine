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

label scene13:
    scene black with fade
    show text Text("Пятница", color="#FFFFFF", size=30, xalign=0.5, yalign=0.5)
    pause 2.0
    hide text with fade

    call screen characteristics
    with fade

    $ points = 10
    $ fatigue = fatigue - 4
    $ fatigue_buffer = fatigue

    scene bg classroom with fade

    show alexandr normal at left_to_right
    with moveinleft

    "Пятница прошла как обычно, ничего интересного"

    scene black with fade
    show text Text("Суббота", color="#FFFFFF", size=30, xalign=0.5, yalign=0.5)
    pause 2.0
    hide text with fade

    call screen characteristics
    with fade

    $ points = 10
    $ fatigue = fatigue + 4

    scene bg dormitory with fade

    show alexey dormitory at right_position
    show igor student at center_position
    show kristina normal at left_position

    i "Ну что, хостим на каком-нибудь бесплатном сервере или арендуем что-то посерьёзнее?"

    a "Бесплатный вариант может не потянуть, если будет большая нагрузка. У нас же предусмотрена база данных для заданий и уведомлений. Лучше взять что-то надёжное."

    k "Тогда я предлагаю использовать сервис, который я знаю. У них дешёвый тариф, а для хакатонов они иногда дают бесплатные кредиты."

    i "Отлично. Алексей, ты можешь всё настроить?"

    a "Да, это не проблема. У меня есть готовый скрипт для развертывания, осталось только подключить базу данных и домен."

    k "Пока ты занимаешься этим, я ещё раз проверю, как выглядит наш сайт на разных устройствах."

    i "А я подготовлю текст для описания проекта на странице хакатона. Там же нужно указать, что у нас есть?"

    k "Да. Напиши что-то вроде: “Удобный инструмент для студентов, позволяющий организовать учебные задания, следить за дедлайнами и получать напоминания”."

    i "Уже пишу."

    scene bg black with fade
    scene bg dormitory with fade

    show alexey dormitory at right_position
    show igor student at center_position
    show kristina normal at left_position

    a "Всё, сервер работает. Вот адрес: taskmanager.edu. Попробуйте зайти."

    k "Выглядит идеально. Осталось только убедиться, что ничего не сломается завтра."

    i "Я написал текст и загрузил его на платформу. Теперь осталось дождаться начала."

    a "Ну что, ребята, мы готовы. Завтра покажем, на что способны."

    k "Только, пожалуйста, выспитесь. Мы должны быть в форме, если жюри захочет задать вопросы."

    hide kristina
    with dissolve

    hide igor
    with dissolve

    scene bg black
    with fade

    return