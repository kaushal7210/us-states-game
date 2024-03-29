import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    state_name = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Write the name of State")
    answer_state = state_name.title()
    if state_name == "exit": 
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)

screen.exitonclick()
