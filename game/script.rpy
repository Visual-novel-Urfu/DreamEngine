default study = 20
default project = 20
default fatigue = 10

default study_buffer = 20
default project_buffer = 20
default fatigue_buffer = 10
default points = 10

screen characteristics():
    frame:
        align (0.5, 0.5)
        padding (20, 20)
        background "#222831"
        xmaximum 300
        xminimum 200

        vbox:
            spacing 12
            text "Очки для распределения: [points]" color "#FFFFFF" size 20 bold True

            hbox:
                text "Учёба: [study]" color "#4CAF50" size 20 bold True
                textbutton "+" action If(points > 0 and project - 1 >= 0, [SetVariable("study", study + 3), SetVariable("points", points - 1), SetVariable("project", project - 1), SetVariable("fatigue", fatigue + 2)]) align (0.95, 0.5)
            hbox:
                text "Проект: [project]" color "#2196F3" size 20 bold True
                textbutton "+" action If(points > 0 and study - 1 >= 0, [SetVariable("project", project + 3), SetVariable("points", points - 1), SetVariable("study", study - 1), SetVariable("fatigue", fatigue + 2)]) align (0.95, 0.5)
            hbox:
                text "Усталость: [fatigue]" color "#F44336" size 20 bold True
                textbutton "+" action If(points > 0 and fatigue - 4 >= 0 and study - 2 >= 0 and project - 2 >= 0, [SetVariable("fatigue", fatigue - 4), SetVariable("points", points - 1), SetVariable("project", project - 2), SetVariable("study", study - 2)]) align (0.95, 0.5)

            textbutton "Сбросить" action [
                SetVariable("study", study_buffer),
                SetVariable("project", project_buffer),
                SetVariable("fatigue", fatigue_buffer),
                SetVariable("points", 10)
            ] align (0.5, 0.9)

    if points == 0:
        textbutton "Закончить" action [
            SetVariable("study_buffer", study),
            SetVariable("project_buffer", project),
            SetVariable("fatigue_buffer", fatigue),
            Return()
        ] align (0.5, 0.9)

label start:
    play music "minecraft.ogg"
    call scene1 from _call_scene1
    call scene2 from _call_scene2
    call scene3 from _call_scene3
    call scene4 from _call_scene4
    call scene5 from _call_scene5
    stop music
    play music "star_rail.ogg"
    call scene6 from _call_scene6
    call scene7 from _call_scene7
    call scene8 from _call_scene8
    call scene9 from _call_scene9
    call scene10 from _call_scene10
    call scene11 from _call_scene11
    call scene12 from _call_scene12
    call scene13 from _call_scene13
    call scene14 from _call_scene14
    call scene15 from _call_scene15
    call scene16 from _call_scene16
    call scene17 from _call_scene17
    return
