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

label scene14:
    scene bg dormitory with fade

    show alexey dormitory at center_right
    with None
    show gleb normal at left_to_right
    with moveinleft

    g "Здорово, трудяга! Снова за своим кодом?"

    a "Привет, Глеб. Да готовлюсь, чтобы проект сдать завтра. А ты чего хочешь? Ты же никогда просто так не заходишь."

    g "Слушай, хватит уже себя мучить. Вон у тебя круги под глазами. Пошли лучше на тусу. Я знаю одно местечко — музыка, люди, полный кайф!"

    a "Глеб, я же сказал, не до этого сейчас. Проект важен, времени почти не осталось."

    g "Да брось, ты и так всё сделал. Одной ночи хватит, чтобы развеяться. Ты ведь знаешь, как классно будет!"

    a "Нет. Я не хочу опять валяться полдня без сил. Спасибо за предложение, но нет."

    g "Ну, смотри сам. Если передумаешь — знаешь, где меня найти."

    hide gleb
    with dissolve

    show igor student at left_to_right
    with moveinleft

    i "С кем ты тут разговаривал?"

    a "С Глебом. Он опять звал меня на тусовку, но я отказался."

    i "Глеб? Кто это?"

    show alexey surprise at center_right

    a "Ну как кто? Наш сосед. Он всегда тут тусуется."

    i "Алексей, ты что-то путаешь. В соседней комнате никто не живёт, там ремонт."

    a "Нет, подожди. Я же с ним говорил. Он был тут, минуту назад."

    i "Ладно, пойдём проверим."

    scene bg build with fade

    show alexey surprise at center_right
    with moveinright

    show igor student at left_to_right
    with moveinleft

    a "Этого не может быть. Я... я же видел его. Мы говорили."

    i "Алексей, я думаю, тебе стоит отдохнуть. В прошлый раз ты ходил в клуб с нашими знакомыми, и там не было Глеба."

    a "Но... Глеб... Он всегда появляется. Мы говорим."

    i "Ты уверен, что он существует? Может, это просто твоя усталость играет с тобой злую шутку?"

    show alexey dormitory at center_right

    a "Может, ты прав..."

    i "Слушай, давай сделаем так. Сегодня ты просто ложишься спать. Завтра мы заканчиваем проект, и всё станет проще. Окей?"

    scene bg black
    with fade

    return