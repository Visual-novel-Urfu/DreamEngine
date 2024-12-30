init python:
    def check_ending():
        if study >= 50 and project >= 50 and fatigue < 80:
            return "success"
        elif project >= 50 and study < 50:
            return "project_success"
        elif study >= 50 and project < 50:
            return "study_success"
        elif fatigue >= 80 or study < 50 or project < 50:
            return "failure"

label scene16:
    scene black with fade

    $ result = check_ending()

    if result == "success":
        show text Text("Алексей нашёл идеальный баланс между учёбой, проектом и отдыхом.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Он получил отличную оценку за контрольную по программированию, проект его команды занял первое место на хакатоне.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Усталость быстро прошла после пары выходных. Уверенность в себе и успехи мотивируют Алексея продолжать работать над собой и развиваться.", size=30, xalign=0.5, yalign=0.5) with fade

    elif result == "project_success":
        show text Text("Проект занял призовое место, и Алексей почувствовал себя профессионалом.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Однако в учёбе он провалил несколько заданий, и преподаватель дал ему строгий выговор.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Несмотря на успех в хакатоне, Алексей понимает, что ему придётся много работать, чтобы подтянуть учёбу.", size=30, xalign=0.5, yalign=0.5) with fade

    elif result == "study_success":
        show text Text("Алексей отлично справился с учёбой и получил похвалу от преподавателя, но их проект на хакатоне остался незамеченным.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Команда расстроилась, и Алексей почувствовал, что мог бы вложиться в работу больше.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Этот опыт заставляет его задуматься о своих приоритетах и времени.", size=30, xalign=0.5, yalign=0.5) with fade

    elif result == "failure":
        show text Text("Алексей не справился ни с учёбой, ни с проектом.", size=30, xalign=0.5, yalign=0.5)
        pause 5.0
        show text Text("Усталость, накопленная за неделю, привела к тому, что он не мог сосредоточиться ни на заданиях, ни на работе над проектом.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("В итоге его отчислили за неуспеваемость, и он вернулся на завод. Снова оказавшись в рутине, Алексей жалеет о потраченном времени.", size=30, xalign=0.5, yalign=0.5) with fade
        pause 5.0
        show text Text("Но начинает задумываться о том, как исправить свою жизнь.", size=30, xalign=0.5, yalign=0.5) with fade

    pause 5.0
    hide text with fade

    scene bg black with fade

    return
