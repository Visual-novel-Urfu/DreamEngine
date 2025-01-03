
define a = Character('Алексей', color="#0e819e")
define ai = Character('Алексей (внутренний монолог)', color="#0b5466")
define m = Character('Мастер', color="#ff1900")

transform center_right:
    xalign 0.75
    yalign 1.1
    zoom 0.75
    xzoom -1.0

transform left_to_right:
    xalign 0.2
    zoom 0.8
    yalign 1.1

label scene1:

    scene bg factory
    with fade

    show master normal at left_to_right
    with moveinleft

    m "Алексей, подойди ко мне!"

    show alexey normal at center_right
    with moveinright

    m "Алексей, ты вообще понимаешь, где работаешь? Это завод, а не место для раздумий о высоком. У нас сроки, план, а ты не успеваешь."

    a "(молчит) …"

    m "Ты посмотри на остальных – они пашут, чтобы выполнить свою норму, а ты постоянно где-то витаешь. С коллегами у тебя тоже проблемы. Тебе готовы помочь, но ты сам всех сторонишься."

    m "Слушай, я тебя понимаю, всем тяжело. Но у нас тут не благотворительность. Если ты не соберёшься – пойдём к начальству. Поменяй своё отношение и жизнь легче будет. Это последнее предупреждение."

    a "Я вас понял"

    "Алексей молча выслушивает это, потом возвращается за своё место, далее он размышляет над своей жизнью и работает до конца смены."

    hide master normal
    with dissolve

    hide alexey normal
    with dissolve

    scene bg factory2
    with fade

    show alexey normal at center_right
    with dissolve

    ai "Когда я сюда попал? После универа, наверное. Вроде временно, чтобы деньги заработать... А уже задержался на пару лет."

    ai "Я ведь мог бы стать программистом. Не гением, но хотя бы кем-то."

    ai "Я ведь мог бы стать программистом. Не гением, но хотя бы кем-то. Даже пытался – пару курсов прошёл, лабораторные писал."

    ai "Но тогда мне было всё равно. Лень, друзья, тусовки... Да и зачем стараться, если экзамен и так сдашь?"

    ai "А теперь я сижу здесь, кручу гайки. И никакого кода. Никакой свободы. Одни станки, шум, пыль. Я сам закрыл себе двери."

    "Внезапно его размышления прерывает крик: “Смена окончена, можете идти!”. Обычно после этой фразы все рабочие быстро собираются и уходят домой, этот день не стал исключением."

    "Алексей ещё немного постоял возле своего места, чтобы ещё подумать и в конечном итоге присоединиться к остальным."

    hide alexey
    with dissolve

    return