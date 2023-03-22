from tkinter import*
from tkinter import messagebox

window = Tk()
def show_total_charge():
    choice = selected.get()
    if choice == 1:
        daytime = entNum.get()
        a = 0.07*int(daytime)
        messagebox.showinfo(title="Total Charges", message="Your total charges = ${:.2f}".format(a))
    elif choice == 2:
        evening = entNum.get()
        b = 0.12*int(evening)
        messagebox.showinfo(title="Total Charges", message="Your total charges = ${:.2f}".format(b))
    elif choice == 3:
        off_peak = entNum.get()
        c = 0.05*int(off_peak)
        messagebox.showinfo(title="Total Charges", message="Your total charges = ${:.2f}".format(c))

Label(window, text="Enter the number of minutes:").grid(row=3, column=0, padx=(30,0), sticky=E)
entNum = StringVar()
minute = Entry(window, width=15, textvariable=entNum)
minute.grid(row=3, column=1, padx=(0, 30), sticky=W)

selected = IntVar()
r1 = Radiobutton(window, text="Daytime (6:00am - 5:59pm)", value=1, variable=selected)
r1.grid(row=0, column=0, columnspan=2)
r2 = Radiobutton(window, text="Evening (6:00pm - 11:59pm)", value=2,  variable=selected)
r2.grid(row=1, column=0, columnspan=2)
r3 = Radiobutton(window, text="Off-Peak (12:00am - 5:59am)", value=3, variable=selected)
r3.grid(row=2, column=0, columnspan=2)

button1 = Button(window, text="Display Charges", command=show_total_charge)
button1.grid(row=4, column=0, padx=(75, 0), pady=(0, 20), sticky=E)
button2 = Button(window, text="Quit", command=window.destroy)
button2.grid(row=4, column=1, padx=(0, 75), pady=(0, 20), sticky=W)
window.mainloop()

