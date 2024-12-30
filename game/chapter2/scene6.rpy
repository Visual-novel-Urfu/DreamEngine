define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")
define ai = Character('Алексей (внутренний монолог)', color="#0b5466")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 1.0
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.2

label scene6:

    scene bg dormitory with fade

    show alexey surprise at center_right
    with moveinright

    show igor student at left_to_right
    with moveinleft

    i "Лёха, вставай, ну! Ты что, опять решил проспать? Пара через двадцать минут."

    a "Игорь?!"

    i "Ну да, Игорь. У тебя другие варианты есть?"

    a "Подожди... Как ты здесь? Мы же вчера сидели в кафе и каждый пошёл к себе домой! Мы закончили универ 5 лет назад, какие пары?"

    i "Ты что, издеваешься? А, ты, наверное, ещё от вечера не отошёл? Ну точно, ты же вчера опять пошёл на концерт! Собирайся, олух, а то опоздаем!"

    ai "Как это возможно? Это что – сон? Я был дома... Мы с Игорем встречались, говорили о прошлом. А теперь – я снова здесь? В общаге? В 2019 году? Это шутка?"

    i "Всё, давай, пошевеливайся! Пара через двадцать минут, а ты ещё даже не умывался. И не забудь: вечером соберёмся, будем продукт делать свой для хакатона. Ты в наше тиме, отказы не принимаю!"

    a "Хакатон... Сегодня?"

    i "Ага, сегодня! Так что лучше не тупи. Это шанс показать себя."

    ai "Если это сон – я не хочу просыпаться. Если это шанс – я не могу его упустить. В этот раз я сделаю всё иначе."

    a "Погнали, чего мы ждём!"

    scene black with fade
    show text Text("Понедельник", color="#FFFFFF", size=30, xalign=0.5, yalign=0.5)
    pause 2.0
    hide text with fade

    call screen characteristics
    with fade

    $ points = 10
    $ fatigue = fatigue + 4
    $ fatigue_buffer = fatigue
    return

