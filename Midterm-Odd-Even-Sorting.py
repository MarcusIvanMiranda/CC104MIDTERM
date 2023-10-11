from tkinter import *

odds = []
evens = []

def store():
    nums = num.get()
    entry.delete(0, 'end')

    if nums % 2 != 0:  # Odd number
        if len(odds) < 9 and nums not in odds:
            odds.append(nums)
            odd_labels[len(odds) - 1].config(text=nums)
            warning.config(text='')
        else:
            warning.config(text='Odd Slot Full' if len(odds) >= 9 else 'Number Entered')
    else:  # Even number
        if len(evens) < 9 and nums not in evens:
            evens.append(nums)
            even_labels[len(evens) - 1].config(text=nums)
            warning.config(text='')
        else:
            warning.config(text='Even Slot Full' if len(evens) >= 9 else 'Number Entered')

wow = Tk()
wow.title("Odd Even Separator")
wow.geometry("800x500+300+100")

label_instruction = Label(wow, text='Enter a Number', font=('arial', 10, 'bold'))
label_instruction.place(x=350, y=10)

num = IntVar()
entry = Entry(wow, textvariable=num, font=('arial', 10, 'bold'), justify='center')
entry.delete(0, 'end')
entry.place(x=330, y=30)

button_store = Button(wow, width=17, text='Store', font=('arial', 10, 'bold'), command=store)
button_store.place(x=330, y=60)

label_odd = Label(wow, text='Odd Numbers', font=('arial', 10, 'bold'))
label_odd.place(x=105, y=150)

label_even = Label(wow, text='Even Numbers', font=('arial', 10, 'bold'))
label_even.place(x=595, y=150)

odd_labels = []
even_labels = []

for i in range(3):
    for j in range(3):
        odd_label = Label(wow, width=3, bd=3, bg='white', relief='solid', font=('arial', 20, 'bold'))
        odd_label.place(x=50 + 70 * j, y=200 + 70 * i)
        odd_labels.append(odd_label)

for i in range(3):
    for j in range(3):
        even_label = Label(wow, width=3, bd=3, bg='white', relief='solid', font=('arial', 20, 'bold'))
        even_label.place(x=550 + 70 * j, y=200 + 70 * i)
        even_labels.append(even_label)

warning = Label(wow, text='', fg='red', font=('arial', 10, 'bold'))
warning.config(anchor='center')
warning.place(x=350, y=250)

wow.mainloop()

print(f'Odd: {odds}')
print(f'Even: {evens}')