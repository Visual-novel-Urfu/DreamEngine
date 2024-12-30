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

label scene10:

    scene bg dormitory with fade

    show alexey normal at right_position
    show igor home at center_position

    a "Думаешь, Кристина точно придёт?"

    i "Ты же сказал, что она согласилась. Расслабься, Алексей, она выглядит куда более организованной, чем мы с тобой."

    a "Просто странно как-то. Мы не общались несколько лет, а тут сразу просьба о помощи. Вдруг она подумает, что мы просто используем её?"

    i "Ну а что? Так и есть. Ты же понимаешь, на данный момент у нас есть рабочий функционал и некрасивая обёртка, которая, несмотря на все удобства, отталкивает от нашего продукта потенциальных пользователей."

    a "Красиво ты описал наш сайт."

    show kristina normal at left_position with moveinleft

    k "Привет! Надеюсь, я не рано?"

    a "Привет! Нет, всё вовремя. Проходи."

    i "Привет, я Игорь. Спасибо, что согласилась помочь."

    k "Приятно познакомиться. Ну, рассказывайте, что у вас за проект."

    a "Мы хотим сделать сайт для управления учебными заданиями. Что-то вроде трекера, но с акцентом на студентов: дедлайны, напоминания, статистика по предметам."

    i "Всё работает, но пока это просто набор страниц с текстом. Выглядит... как типичный студенческий проект."

    k "Поняла. А у вас есть какие-то примеры интерфейсов, которые вам нравятся?"

    a "Мы собрали несколько идей, но пока это скорее черновики."

    k "Ясно. Вы хотите что-то минималистичное или с яркими акцентами?"

    i "Главное, чтобы было понятно и удобно."

    k "Хорошо. Тогда я сделаю несколько макетов. Думаю, начнём с главной страницы и навигации."

    a "Это было бы здорово. Мы тебе очень благодарны."

    k "Ну, я ведь тоже студентка. Может, этот сайт и мне пригодится."

    i "Если выиграем, я лично распечатаю твоё имя большими буквами на главной странице."

    k "Договорились. Но сначала сделаем, чтобы всё работало."

    k "Тогда я скину вам первые макеты завтра. Если что-то не так, сразу пишите."

    a "Спасибо ещё раз. Если что, заходи."

    k "Удачи с кодом."

    i "Ну, теперь у нас есть шанс сделать что-то крутое."

    a "Да. И хорошо, что мы её позвали."

    scene bg black
    with fade

    return
