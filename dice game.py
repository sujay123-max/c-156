from tkinter import*
from PIL import ImageTk, Image
import random
root=Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background="yellow2")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))

player1 = Label(root,text = "Player 1",  bg = "royal blue", fg = "white")
player1.place(relx=0.1,rely=0.3,anchor = CENTER)

player2 = Label(root,text = "Player 2",  bg = "royal blue", fg = "white")
player2.place(relx=0.9,rely=0.3,anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1,rely = 0.4,anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9,rely = 0.4,anchor = CENTER)

random_dice_label = Label(root,bg = "chocolate1",fg = "white")
random_dice_label.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_score=0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_dice_label["text"] = "Player 1 dice random number : " + str(random_no)
    player1_score=player1_score+ random_no
    player1_score_label["text"]=str(player1_score)
    
    player_1_btn=Button(root,image=img,command=player1)
    player_1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)
    
    player2_score=0
def player2():
    global player2_score
    random_no = random.randint(1,6)
    random_dice_label["text"] = "Player 2 dice random number : " + str(random_no2)
    player2_score=player2_score+ random_no2
    player2_score_label["text"]=str(player2_score)
    
    player2__btn=Button(root,image=img,command=player2)
    player2_btn.place(relx=0.9,rely=0.6,anchor=CENTER)
    

root.mainloop()