import turtle
import pandas

# Creation of the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# Uploading custom image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Extracting data from a .csv file using 'pandas'
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# List to store the guessed states
guessed_states = []

# While the "guessed_states" list has less than 50 values, this loop will continue until broken
while len(guessed_states) < 50:
    # Storing the guessed state in a variable called "answer_state"
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # If the person gives up and types "Exit", this code will run
    if answer_state == "Exit":
        # Creating a list named "missing_states" that will hold all of the states that the person missed out on.
        missing_states = []
        # For loop that will run through "all_states"
        for state in all_states:
            # If the state is not in "guessed_states", it will be saved to "missing_states"
            if state not in guessed_states:
                missing_states.append(state)
        # Creation of a .csv file with a list of all missing states        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # End of the code
        break
        # If the person guessing makes a correct guess, this code will run
    if answer_state in all_states:
        # Adding the guessed_state to the list, "guessed_states"
        guessed_states.append(answer_state)
        # Creation of a turtle that will be needed to put the guess on the map (image)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Getting information from the row using pandas. Used to obtain the x and y values of the guess
        state_data = data[data.state == answer_state]
        # Using a "turtle" to put the guess on the map (image)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
