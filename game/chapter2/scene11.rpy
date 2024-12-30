define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")
define g = Character('Глеб', color="#1e90ff")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label scene11:

    scene bg dormitory with fade

    show alexey normal at center_right
    show igor home at left_to_right

    i " Я в магазин, что-нибудь тебе взять?"

    a "Нет, спасибо."

    i "Ладно, я быстро."

    hide igor
    with dissolve

    show gleb normal at left_to_right
    with moveinleft

    g "О, здорово, программист! Сидишь тут, значит?"

    a "Глеб, ты чего сюда зашёл?"

    g "Да мимо проходил, думал, загляну. У меня к тебе дело, дружище."

    g 'Сегодня ночью движ в "Лабиринте". Будет музыка, девочки, короче, кайф. Ты же не собираешься тут торчать, как обычно?'

    a "Эм… Не знаю, у меня дела."

    g "Дела, дела… Какие дела? Ты все время за компом сидишь. Живи хоть немного, пока можешь."

    g "Слушай, реально, тебе надо проветриться. Твой проект не убежит, завтра вернёшься к нему."

    menu:
        "Пойти с Глебом на вечеринку.":
            jump party_with_gleb

        "Остаться в комнате.":
            jump stay_in_room

label party_with_gleb:

    a "Ладно, уговорил. Только ненадолго."

    g "Вот это другой разговор! Ну что, пошли?"

    scene bg black
    with fade

    scene bg club
    with fade

    # случай

    return

label stay_in_room:

    a "Нет, Глеб, извини. У меня действительно много работы."

    g "Ну, как знаешь. Потом не жалуйся, что ничего не происходит в жизни."

    g "Ладно, не буду отвлекать. Если передумаешь — звони."

    hide gleb
    with dissolve

    scene bg black
    with fade

    return
