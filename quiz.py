import tkinter as tk
from tkinter import StringVar

cyber = tk.Tk()
cyber.title("Quiz App")
cyber.geometry('500x500')
cyber.iconbitmap("logo.ico")
cyber.maxsize()
questions = ["What is the launch date for Chandrayaan 3 mission?",
             "The Chandrayaan 3 mission’s rover is known as",
             "The mission life of the Lander and Rover equal to",
             "Who is the director of the Chandrayaan 3 mission?",
             " How did Chandrayaan-2 welcomed Chandrayaan-3?"]
options = [
    ['24 July 2023', '04 July 2023', '14 July 2023', '13 July 2023', '14 July 2023'],
    ['Vikram', 'Pragyaan', 'Bheem', 'Dhruv', 'Pragyaan'],
    ['24 Earth Days', '16 Earth Days', '12 Earth Days', '14 Earth Days', '14 Earth Days'],
    ['Ritu Karidhal', 'Veeramuthuvel', 'M Vanitha ', 'K. Sivan', 'Ritu Karidhal'],
    ['Hello Buddy', 'Welcome Buddy!', 'Hi Buddy!', 'Hey Buddy!', 'Welcome Buddy!']]

frame = tk.Frame(cyber, padx=10, pady=10, bg='#fff')
question_label = tk.Label(frame, height=5, width=28, bg='dark orange', fg='#fff', font=('comic sans ms', 20), wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg='#fff', variable=v1, font=('comic sans ms', 20),
                         command=lambda: checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg='#fff', variable=v2, font=('comic sans ms', 20),
                         command=lambda: checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg='#fff', variable=v3, font=('comic sans ms', 20),
                         command=lambda: checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg='#fff', variable=v4, font=('comic sans ms', 20),
                         command=lambda: checkAnswer(option4))
button_next = tk.Button(frame, text='NEXT', bg='orange', font=('comic sans ms', 20), bd=12, width=20,
                        command=lambda: displayNextQuestion())

frame.pack(fill='both', expand='true')
question_label.grid(row=0, column=0)

option1.grid(sticky='W', row=1, column=0)
option2.grid(sticky='W', row=2, column=0)
option3.grid(sticky='W', row=3, column=0)
option4.grid(sticky='W', row=4, column=0)

button_next.grid(row=6, column=0)

index = 0
correct = 0

# create a function to disables radio buttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

#  create a function to check the selected answer
def checkAnswer(radio):
    global correct, index

    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct += 1

    index += 1
    disableButtons(('disable'))


# Create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'


    if index == len(options):
        question_label['text'] = str(correct) + '/' + str(len(options))
        button_next['text'] = 'Restart The Quiz'
        if correct >= len(options) / 2:
            question_label['bg'] = 'green'
        else:
            question_label['bg'] = 'red'

    else:
        question_label['text'] = questions[index]
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'




displayNextQuestion()
cyber.mainloop()
