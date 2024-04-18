
from tkinter import *
from random import randint
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="plum1")
rock_img = PhotoImage(file="rock-user.png")
paper_img = PhotoImage(file="paper-user.png")
scissor_img = PhotoImage(file="scissors-user.png")
rock_img_comp = PhotoImage(file="rock.png")
paper_img_comp = PhotoImage(file="paper.png")
scissor_img_comp = PhotoImage(file="scissors.png")
user_label = Label(root, image=scissor_img, bg="plum1")
comp_label = Label(root, image=scissor_img_comp, bg="plum1")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)
playerScore = Label(root, text=0, font=100, bg="plum1", fg="gray4")
computerScore = Label(root, text=0, font=100, bg="plum1", fg="gray4")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)
user_indicator = Label(root, font=50, text="USER", bg="plum1", fg="gray4")
comp_indicator = Label(root, font=50, text="COMPUTER",bg="plum1", fg="gray4")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)
msg = Label(root, font=50, bg="plum1", fg="gray4")
msg.grid(row=3, column=2)
def updateMessage(x):
    msg['text'] = x
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)
rock = Button(root, width=20, height=2, text="ROCK",
              bg="light salmon", fg="gray4", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="peachpuff2", fg="gray4", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="oliveDrab1", fg="gray4", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
                 
instructions = """
Instructions:
1. Click on ROCK, PAPER, or SCISSOR to make your choice.
2. The computer will randomly select its choice.
3. The winner will be determined based on the choices made.
4. Have fun playing!
"""

instruction_label = Label(root, text=instructions, font=("Arial", 12), bg="plum1", fg="gray4", justify=LEFT)
instruction_label.grid(row=4, column=2, columnspan=3)

root.mainloop()
