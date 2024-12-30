define ai = Character('Алексей (внутренний монолог)', color="#0b5466")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label scene5:

    scene bg room
    with fade

    show alexey normal at center_right
    with moveinright

    ai "Курсы, хакатоны... А вдруг ничего не получится? Да и времени у меня уже нет, чтобы снова начинать."

    ai "Но всё-таки... Как же было здорово, когда мы жили в общаге. В те дни казалось, что всё впереди. Всё было проще, легче. А сейчас только рутина и усталость."

    ai "Если бы можно было всё изменить... Вернуться туда, где ещё можно было начать заново."

    scene black with fade
    show text Text("Ты всегда можешь изменить будущее, но важно помнить, где ты потерял свой путь.", color="#FFFFFF", size=25, xalign=0.5, yalign=0.5)
    pause 5.0
    scene black with fade
    return

