from tkinter import*
import random
from tkinter import messagebox

root=Tk()

count=0
slideWords=' '
score=0
timeleft=60
miss=0

score=0
datashow=["apple","mango","banana","orange","grapes","cricket",
          "football","chess","carrom","ludo","hostel","hospital",
          "college","student","teacher","account",
          "programe","management","cable","network","operating",
          "system","analysis","stockmarket"
          ]

# time function implified
def time():
    global timeleft,score,miss
    if(timeleft>0):
        timeleft=timeleft-1
        timeleftcount.configure(text=timeleft)
        timeleftcount.after(1000,time)

    else:
        replaygame=messagebox.askretrycancel("notification",
                                             "forplay again hit retry button")
        if(replaygame==True):
            score=0
            timeleft=60
            
            miss=0
            timeleftcount.configure(text=timeleft)
            wordentry.configure(text=datashow[0])
            scorecount.configure(text=score)
        else:
            exit()



# function of entry the data

def startgame(event):
    global miss,score
    if(timeleft==60):
        time()
    #gamePlayDetail.configure(text="")
    if(wordentry.get()==word['text']):
        # print("matched")
        score=score+1
        scorecount.configure(text=score)
         # print("match",score)
       
    else:
        miss=miss+1
        print(" NOT MATCHED",wordentry.get(),miss)
        # print(wordentry.get())
        # print(miss)
    random.shuffle(datashow)
    word.configure(text=datashow[0])
            
    # print(wordentry.get())     it is used to print what user have write
    wordentry.delete(0,END)
    

# size of a screen
root.geometry("1000x800")
root["background"]="green"
root.minsize(500,800)
root.maxsize(1000,800)

# title
root.title("SPEED TESTOR")

# heading
blank=Label(root,font="freehand 20 bold",
              text="",
              bg="green")
blank.grid(row=0,column=15)

heading=Label(root,font="freehand 50 bold",text=
              "WELCOME TO TYPING SPEED GAME",
              bg="green")
heading.place(x=0,y=50)

# image insert
photo=PhotoImage(file="cl1.png")
paste_label=Label(image=photo,bg="green")
paste_label.place(x=350,y=150)

# word that is show and we have to write it

random.shuffle(datashow)

word=Label(root,text=datashow[0],font="freehand 50 bold",bg="green")
word.place(x=350,y=450)

# word that is going to written
wordentry=Entry(root,bg="white",justify="center",
                font="freehand 50 bold")
wordentry.place(x=100,y=550)
wordentry.focus_set()

#word count box show
wordcount=Label(root,text="WORDS",
                font="freehand 30 bold",bg="green")
wordcount.place(x=50,y=200)


# timerleft box show
timerLabel=Label(root,text="TIME LEFT",
                font="freehand 30 bold",bg="green")
timerLabel.place(x=750,y=200)

# score count
scorecount=Label(root,text=score,
                 font="freehand 30 bold",bg="green")
scorecount.place(x=100,y=300)

# timeleft count count
timeleftcount=Label(root,text=timeleft,
                 font="freehand 30 bold",bg="green")
timeleftcount.place(x=800,y=300)
                 
                


root.bind("<Return>",startgame)
root.mainloop()
