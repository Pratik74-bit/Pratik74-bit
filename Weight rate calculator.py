#sum calculator by pratik using Tkinter library in python



from tkinter import *



root = Tk()
root.title("Pratik Calculators- Weight Rate Calculator")

root.geometry('310x290')
root['bg'] = 'black'



#for Weight
label_1=Label(root, text="WEIGHT RATE CALCULATOR",font=('Comic Sans MS Bold', 15), bg='black',fg='yellow')
label_1.grid(row=0,column=0,columnspan=2)


label_2=Label(root, text="Enter rate for 1kg:", font=('bold'), bg='black',fg='cyan')      #Enter rate for 1 kg
label_2.grid(row=2,column=0,columnspan=2) 

txt = Entry(root,width=20, bd=3)                         #entrybox for rate for 1kg
txt.grid(row=3,column=0,columnspan=2)



space_label = Label(root,text="  ",bg='black')   #this is space label used to create empty space
space_label.grid(row=4,column=0,columnspan=2)



enterlb1 = Label(root,text= "Enter Rate: ",font=('bold'), bg='black',fg='green')              #enter your Rate
enterlb1.grid(row=5, column=0)

rate_entry= Entry(root, width=10, bd=3)                        # entry bar for your rate 
rate_entry.grid(row=6,column=0)

enterlb2 = Label(root,text= "Enter Weight: ",font=('bold'), bg='black',fg='green')              #enter your Weight
enterlb2.grid(row=5, column=1)

weight_entry= Entry(root, width=10, bd=3)                        # entry bar for your Weight 
weight_entry.grid(row=6,column=1)



space_label = Label(root,text="   ",bg='black')
space_label.grid(row=7,column=0,columnspan=2)




def go1():
    
    

    Rg = float(txt.get()) / 1000   # Rate per 1 gram
    Wrs = 1000 / float(txt.get())  #weight of Rs 1 

    
    Weight = float (Wrs * float(rate_entry.get())) 

    result = Label(root,text="Weight (g):", bg='black',fg='white',font='bold')
    result.grid(row=9,column=0)

    result = Label(root,text= Weight, bg='black',fg='yellow',font='bold')
    result.grid(row=9,column=1)
      
def go2():
    
    

    Rg = float(txt.get()) / 1000   # Rate per 1 gram
    Wrs = 1000 / float(txt.get())  #weight of Rs 1 

    Rate = float (Rg * float(weight_entry.get())) 

    result = Label(root,text="Rate (Rs):", bg='black',fg='white',font='bold')
    result.grid(row=10,column=0)

    result = Label(root,text= Rate, bg='black',fg='yellow',font='bold')
    result.grid(row=10,column=1)

go_button1= Button(root,text='Calculate weight',bg='white',fg='black',command=go1)
go_button1.grid(row=8,column=0)

go_button2= Button(root,text='Calculate Rate',bg='white',fg='black',command=go2)
go_button2.grid(row=8,column=1)



root.mainloop()
