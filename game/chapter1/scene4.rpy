
define a = Character('Алексей', color="#0e819e")
define i = Character('Игорь', color="#ff1900")
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

label scene4:

    scene bg street
    with fade

    show alexey normal at center_right
    with moveinright

    show igor home at left_to_right
    with moveinleft

    i "Ладно, Лёха, я побегу. Но ты не теряйся. Если что, пиши – номер у тебя ведь остался?"

    a "Да, остался."

    i "Отлично. Давай, удачи тебе. И думай!"

    hide igor
    with dissolve

    ai "А может, он прав? Я ведь всё ещё могу попробовать. Хотя бы начать с чего-то простого. Но хватит ли мне сил? Или это будет очередной провал?"

    ai "Нет. Если я ничего не сделаю, то так и останусь на этом заводе. Нужно хотя бы попробовать."

    hide alexey
    with dissolve

    scene bg black
    with fade

    return