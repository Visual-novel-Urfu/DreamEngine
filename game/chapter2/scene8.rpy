define ac = Character('Александр Сильвестрович', color="#0e819e")
define a = Character('Алексей', color="#0e819e")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label scene8:
    scene bg classroom with fade

    show alexandr normal at left_to_right
    with None

    show alexey student at center_right
    with moveinright

    ac "Алексей, останьтесь на минуту."

    ac "Вы довольно внимательно слушали сегодня. Но мне почему-то кажется, что вы не всегда прилагаете нужные усилия."

    a "Не знаю… Просто иногда кажется, что у меня не получается так быстро разбираться, как у других."

    ac "Это нормально. Но у вас есть потенциал. Кстати, я слышал, что уже сейчас проходит хакатон. Вы как, участвуете?"

    a "Да, мы с Игорем в одной команде."

    ac "С Игорем это хорошо. Очень умный человек. Советую вам сосредоточиться на практическом применении знаний."

    ac "Например, если вы делаете сайт, то подумайте, как можно адаптировать и оптимизировать ваш продукт для мобильных устройств. Это может быть очень полезно."

    hide alexey
    with dissolve

    scene bg black
    with fade

    return

