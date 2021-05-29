from tkinter import *
window = Tk()
window.geometry("600x900+0+0")
window['bg'] = "red"
window.title("Pizza Hut")
label10=Label(window,text="PIZZA HUT",font="times 30 bold",bg='red')
label10.grid(row=0, column=100)
#---------------------MENU SECTION-------------

label1=Label(window,text="--------------------------MENU--------------------------",font="times 20 bold",bg='red')
label1.grid(row=5, column=100)

label2=Label(window,text="Triple chicken feast-MED pizza ----------------Rs 1345",font="times 19 italic",bg='red')
label2.grid(row=6, column=100)
label3=Label(window,text="Chicken Tikka pizza ------------------------------Rs 1245",font="times 19 italic italic",anchor="e",bg='red')
label3.grid(row=7, column=100)
label4=Label(window,text="Chicken Supreme-MED pizza ------------------Rs 1345",font="times 19 italic",bg='red')
label4.grid(row=8, column=100)
label5=Label(window,text="Malai Chicken Tikka -MED --------------------Rs 1245",font="times 19 italic",bg='red')
label5.grid(row=9, column=100)
label6=Label(window,text="Italian Chicken Feast-MED pizza-------------Rs 1245",font="times 19 italic",bg='red')
label6.grid(row=10, column=100)
label7=Label(window,text="Chicken Pepper Crunch pizza ----------------Rs 1245",font="times 19 italic",bg='red')
label7.grid(row=11, column=100)
label8=Label(window,text="Pepsi---------------------------------------------Rs 70",font="times 19 italic",bg='red')
label8.grid(row=12, column=100)
label9=Label(window,text="Dessert-choco Volcano-----------------------------Rs 299",font="times 19 italic",bg='red')
label9.grid(row=13, column=100)
label10=Label(window,text="------------------------------------------------------------",font="times 20 bold",bg='red')
label10.grid(row=13, column=100)
#--------------------Billing section----------------------------
label11=Label(window,text="SELECT YOUR CHOICE",font="times 20 bold",bg='red')
label11.grid(row=14, column=100)
label12=Label(window,text="Triple chicken feast-MED pizza",font="times 19 italic",bg='red')
label12.grid(row=15,column=100)
label13=Label(window,text="Chicken Tikka pizza",font="times 19 italic",bg='red')
label13.grid(row=17, column=100)
label14=Label(window,text="Chicken Supreme-MED pizza",font="times 19 italic",bg='red')
label14.grid(row=19, column=100)
label15=Label(window,text="Malai Chicken Tikka -MED ",font="times 19 italic",bg='red')
label15.grid(row=21, column=100)
label16=Label(window,text="Italian Chicken Feast-MED pizza",font="times 19 italic",bg='red')
label16.grid(row=23, column=100)
label17=Label(window,text="Chicken Pepper Crunch pizza",font="times 19 italic",bg='red')
label17.grid(row=25, column=100)
label18=Label(window,text="Pepsi",font="times 19 italic",bg='red')
label18.grid(row=21, column=100)
label19=Label(window,text="Dessert-choco Volcano",font="times 19 italic",bg='red')
label19.grid(row=22, column=100)

window.mainloop()





