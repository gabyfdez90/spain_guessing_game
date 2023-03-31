import turtle
import pandas


data = pandas.read_csv("autonomous_communities.csv")
communities_list = data.name.to_list()

screen = turtle.Screen()
screen.title("¿Conoces las Comunidades Autónomas?")
image = "spain_bg.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
score = 0

while len(correct_guesses) < 17:

    answer = screen.textinput(title=f"{len(correct_guesses)}/17 aciertos", 
                              prompt="Escribe el nombre de una C.A. o 'Fin' para terminar")
    answer_formatted = answer.title()

    if answer_formatted == "Fin":
        missing_answers = [state for state in communities_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_answers)
        states_missing = new_data.to_csv("answers_missing.csv")

        break

    if answer_formatted in communities_list and answer_formatted not in correct_guesses:
        correct_guesses.append(answer_formatted)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.name == answer_formatted]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_formatted, move=False, align='left', font=('Arial', 12, 'bold'))

    else:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/17 aciertos", 
                              prompt="Escribe el nombre de una C.A. o 'Fin' para terminar")