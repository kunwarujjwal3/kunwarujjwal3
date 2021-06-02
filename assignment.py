import json
import tkinter
from tkinter import *
import random
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []




def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="Slate gray",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="Slate gray",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Awesome!! Outstanding!!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better, Good work!!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Better luck next time !!")


def calc():
    global indexes, user_answer, answers
    f = open("score.txt", "a")
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)
    f.writelines('\n')
    f.writelines('YOUR SCORE IS:-')
    f.write(str(score))
    f.close()


ques = 1




def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:

        calc()


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="Slate gray",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="Slate gray",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="Slate gray",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="Slate gray",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="Slate gray",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Nepal Quiz Compitition")
root.geometry("700x600")
root.config(background="Slate gray")
root.resizable(0, 0)
img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image=img1,
    background="Slate gray",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="Quiz super star",
    font=("Comic sans MS", 24, "bold"),
    background="Slate gray",
)
labelimage.pack(pady=(50, 0))

labeltext = Label(
    root,
    text="Quiz Competition",
    font=("Comic sans MS", 24, "bold"),
    background="Slate gray",
)

labeltext.pack(pady=(0, 50))


img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Click Start if You Are ready",
    background="Slate gray",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 100))

lblRules = Label(
    root,
    text="You will get 20 seconds to solve 10 question so, think before you choose",
    width=100,
    font=("Times", 12),
    background="purple"
               "",
    foreground="#FACA2F",
)
lblRules.pack()



# Create an Exit  Button
Exitbtn = Button(root, text='EXIT', bg='silver', fg='black',
                 command=root.destroy)
Exitbtn.pack(side='bottom')
root.mainloop()