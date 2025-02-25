import tkinter as tk
import random

window = tk.Tk()
window.title("TicTacToe")
window.geometry("500x500")

squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Result = tk.Label(window, text='', font=("Arial", 20))

def FindBestMove():
    
    for i in range(1, 10):
        if buttons[i-1]['text'] == '':
            buttons[i-1].config(text='O')
            if CheckWin() == 'O':  
                return i
            buttons[i-1].config(text='')  

    
    for i in range(1, 10):
        if buttons[i-1]['text'] == '':
            buttons[i-1].config(text='X')
            if CheckWin() == 'X':  
                buttons[i-1].config(text='')  
                return i
            buttons[i-1].config(text='')

    if buttons[4]['text']=='':
        return 5

    return random.choice(squares)


def CheckWin():
    
    if btn1['text'] == btn2['text'] == btn3['text'] != '':
        return btn1['text']
    elif btn4['text'] == btn5['text'] == btn6['text'] != '':
        return btn4['text']
    elif btn7['text'] == btn8['text'] == btn9['text'] != '':
        return btn7['text']
    elif btn1['text'] == btn4['text'] == btn7['text'] != '':
        return btn1['text']
    elif btn2['text'] == btn5['text'] == btn8['text'] != '':
        return btn2['text']
    elif btn3['text'] == btn6['text'] == btn9['text'] != '':
        return btn3['text']
    elif btn1['text'] == btn5['text'] == btn9['text'] != '':
        return btn1['text']
    elif btn3['text'] == btn5['text'] == btn7['text'] != '':
        return btn3['text']
    return None

def GamePlay(butt, number):
    butt.config(text='X', state="disabled")
    global squares
    squares.remove(number)

    winner = CheckWin()
    if winner == 'X':
        Result.config(text='You win!')
        Result.pack()
        DisableButtons()
        return

    if squares:
        opponent_move = FindBestMove()
        squares.remove(opponent_move)
        buttons[opponent_move-1].config(text='O', state="disabled")

        winner = CheckWin()
        if winner == 'O':
            Result.config(text='Computer wins!')
            Result.pack()
            DisableButtons()

def DisableButtons():
    for btn in buttons:
        btn.config(state="disabled")

def RestartGame():
    global squares
    squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for btn in buttons:
        btn.config(text='', state="normal")
    Result.config(text='')

# Кнопки для игрового поля
btn1 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn1, 1))
btn1.place(x=120, y=100)
btn2 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn2, 2))
btn2.place(x=200, y=100)
btn3 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn3, 3))
btn3.place(x=280, y=100)
btn4 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn4, 4))
btn4.place(x=120, y=185)
btn5 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn5, 5))
btn5.place(x=200, y=185)
btn6 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn6, 6))
btn6.place(x=280, y=185)
btn7 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn7, 7))
btn7.place(x=120, y=270)
btn8 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn8, 8))
btn8.place(x=200, y=270)
btn9 = tk.Button(window, width=10, height=5, command=lambda: GamePlay(btn9, 9))
btn9.place(x=280, y=270)


buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]


restart_btn = tk.Button(window, text="Restart", width=10, height=2, command=RestartGame)
restart_btn.place(x=200, y=380)

window.mainloop()