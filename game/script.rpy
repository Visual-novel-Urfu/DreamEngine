default study = 0
default project = 0
default fatigue = 0

# Функция отображения меню
screen characteristics():
    frame:
        align (0.98, 0.02)
        padding (10, 10)
        background "#222831"
        xmaximum 200
        xminimum 150

        vbox:
            spacing 8
            text "Учёба: [study]" color "#4CAF50" size 20 bold True
            text "Проект: [project]" color "#2196F3" size 20 bold True
            text "Усталость: [fatigue]" color "#F44336" size 20 bold True

label start:
    call scene1
    call scene2
    call scene3
    call scene4
    call scene5
    call scene6
    call scene7
    call scene8
    call scene9
    call scene10
    call scene11
    call scene12
    call scene13
    call scene14
    call scene15
    return