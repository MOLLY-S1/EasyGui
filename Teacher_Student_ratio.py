
import easygui

while True:
    school = easygui.enterbox("Enter School Name: ", "School Name")

    max_class = easygui.integerbox("Enter the maximum number of children allowed "
                                 "per class: Must be a number between 10 and 30",
                                 "Maximum Class Size",
                                 upperbound=30, lowerbound=10)
    roll = easygui.integerbox(f"What is the total number of children at {school}\n"
                            f"Must be a number between 10 and 1400",
                            "Total School Roll", upperbound=1400, lowerbound=10)

    teachers_need = roll//max_class
    teacher_at_school = easygui.integerbox(f"How many teachers at {school}:\n"
                                         f"Must be a number between 1 and 120",
                                         "Actual Number of Teachers at School",
                                         upperbound=120, lowerbound=1)

    if teachers_need > teacher_at_school:
        easygui.msgbox(f"You do not have enough teachers:\n"
                       f"You need {teachers_need - teacher_at_school} "
                       f" more teachers", "Under Staffed")


    elif teacher_at_school == teachers_need:
        easygui.msgbox("You have the perfect number of teachers!",
                       "Perfect Staffed")

    else:
        easygui.msgbox(f"You have enough teachers:\n"
                       f"You could do without "
                       f"{teacher_at_school - teachers_need}"
                       f" teachers", "Over Staffed")


    again = easygui.buttonbox(f"Do you want to perform another calculation\n"
                                , "Again?", choices= ['Yes', 'No'])
    if again == "No":
        break
easygui.msgbox("Goodbye", "Goodbye")
