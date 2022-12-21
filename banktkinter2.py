from tkinter import *
from tkinter import *
import os
from tkinter import font
from typing import get_origin
#from PIL import ImageTk , Image

master=Tk()
master.title("banking app")
master.config(bg='light yellow')
def finish_reg():
    
    name =temp_name.get()
    age =temp_age.get()
    gender =temp_gender.get()
    password =temp_password.get()
    all_accounts =os.listdir()
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="all fields required *")
        return
    for name_check in all_accounts:
    	if(name==name_check):
    		notif.config(fg='red',text='already account exist** ');return
        else:
            new_file = open(name,'w')
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg='green',text='registeration completed successfully')
    

def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global all_accounts
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()



    register_screen= Toplevel(master)
    register_screen.title("register form")
    Label(register_screen,text="Bank register form",font=("calibri",14)).grid(row=0,column=0,columnspan=2,sticky=N)
    Label(register_screen,text="Name",font=("calibri",12)).grid(row=2,column=0,sticky=W)
    Label(register_screen,text="password",font=("calibri",12)).grid(row=3,column=0,sticky=W)
    Label(register_screen,text="gender",font=("calibri",12)).grid(row=4,column=0,sticky=W)
    Label(register_screen,text="age",font=("calibri",12)).grid(row=5,column=0,sticky=W)
    notif =Label(register_screen,font=("calibri",14))
    notif.grid(row=7,sticky=W)
    #Entry
    Entry(register_screen,textvariable=temp_name).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=3,column=1)
    Entry(register_screen,textvariable=temp_gender).grid(row=4,column=1)
    Entry(register_screen,textvariable=temp_age).grid(row=5,column=1)

    Button(register_screen,text=("register"),bg='green',width=8,command=finish_reg,font=("calibri",14)).grid(row=6,column=1,sticky=N,pady=5,padx=5)
    Button(register_screen,text=("Login"),bg='green',width=8,command=login,font=("calibri",14)).grid(row=7,column=1,sticky=N,pady=5,padx=5)

def main_screen():
    global login_username
    all_accounts=os.listdir()
    login_username = temp_login_username.get()
    login_password=temp_login_password.get()

    for name in all_accounts:
        if name==login_username:
            file = open(name,"r")
            file_data = file.read()
            file_data=file_data.split('\n')
            password=file_data[3]
            print(file_data)
            
            if login_password==password:
                login_screen.destroy()
                main_screen=Toplevel(master)
                main_screen.title("main screen")
                Label(main_screen,text="Welcome  "+name,font=("calibri",14),width=20).grid(row=0)
                Label(main_screen,text="select your option",font=("calibri",14),width=20).grid(row=1)
                Button(main_screen,text="personal details",font=("calibri",14),width=20,command=personal_details).grid(row=2,padx=5,pady=5)
                Button(main_screen,text="withdraw",font=("calibri",14),width=20,command=Withdraw).grid(row=4,padx=5,pady=5)
                Button(main_screen,text="deposit",font=("calibri",14),width=20,command=deposit).grid(row=3,padx=5,pady=5)
                return
            else:
                login_notif.config(fg="red",text="password in correct**")
                return
    login_notif.config(fg="red",text="  username not found!*")  


def personal_details():
    file=open(login_username,"r")
    file_data=file.read()
    user_details=file_data.split("\n")
    details_name=user_details[0]
    details_age=user_details[1]
    details_gender=user_details[2]
    details_password=user_details[3]
    details_balance=user_details[4]
    personal_details=Toplevel(master)
    personal_details.title("personal details")
    Label(personal_details,text="personal details",font=("calibri",14)).grid(row=0,sticky=W)
    Label(personal_details,text="Name :"+details_name,font=("calibri",14)).grid(row=1,sticky=W)
    Label(personal_details,text="Age :"+details_age,font=("calibri",14)).grid(row=2,sticky=W)
    Label(personal_details,text="Gender :"+details_gender,font=("calibri",14)).grid(row=3,sticky=W)
    Label(personal_details,text="Balance :"+details_balance,font=("calibri",14)).grid(row=4,sticky=W)



    
def deposit():
    #vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file =open(login_username,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #deposit screen
    deposit_screen=Toplevel(master)
    deposit_screen.title("Deposit")
    #Label
    Label(deposit_screen,text="Deposit",font=('calibri',12)).grid(row=0,sticky=N)
    current_balance_label =Label(deposit_screen,text="Current Balance :"+details_balance,font=('calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text='Amount :',font=('calibri',12)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,font=('calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    #entry
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
    #button
    Button(deposit_screen,text='Finish',font=('calibri',12),command=finish_deposit).grid(row=3,sticky=W)


def finish_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Amount is required :",fg="red")
        return
    if float(amount.get())<=0:
        deposit_notif.config(text='Negative currency is not accepted',fg='red')
        return
    file = open(login_username,"r+")
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance)+float(amount.get())
    file_data = file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance :"+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated ',fg='green')

def Withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file =open(login_username,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #deposit screen
    withdraw_screen=Toplevel(master)
    withdraw_screen.title("Withdraw")
    #Label
    Label(withdraw_screen,text="Withdraw",font=('calibri',12)).grid(row=0,sticky=N)
    current_balance_label =Label(withdraw_screen,text="Current Balance :"+details_balance,font=('calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen,text='Amount :',font=('calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=('calibri',12))
    withdraw_notif.grid(row=4,sticky=N,pady=5)
    #entry
    Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
    #button
    Button(withdraw_screen,text='Finish',font=('calibri',12),command=finish_withdraw).grid(row=3,sticky=W)


def finish_withdraw():
    if withdraw_amount.get()=="":
            withdraw_notif.config(text="Amount is required :",fg="red")
            return
    if float(withdraw_amount.get())<=0:
            withdraw_notif.config(text='Negative currency is not accepted',fg='red')
            return
    file = open(login_username,"r+")
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text="Insufficient Funds",fg='red')
        return
    updated_balance = current_balance
    updated_balance = float(updated_balance)-float(withdraw_amount.get())
    file_data = file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance :"+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated ',fg='green')     
                
            
    
    



def login():
    global temp_login_username
    global temp_login_password
    global login_notif
    temp_login_username=StringVar()
    temp_login_password=StringVar()
    global login_screen
    login_screen=Toplevel(master)
    login_screen.title("banking site")

    Label(login_screen,text='Enter your login details',fg='blue',font=('calibri',12)).grid(row=1,column=1,pady=10,padx=10,sticky=N)
    Label(login_screen,text='username',font=('calibri',12)).grid(row=2,column=0,)
    Label(login_screen,text='password',font=('calibri',12)).grid(row=3,column=0,)
    Entry(login_screen,textvariable=temp_login_username,width=20).grid(row=2,column=1)
    Entry(login_screen,textvariable=temp_login_password,width=20,show="*").grid(row=3,column=1)
    login_notif=Label(login_screen,font=("calibri",14))
    login_notif.grid(row=5,sticky=N)
    Button(login_screen,text='sign in',font=('calibri',14),fg='red',command=main_screen).grid(row=4,column=1)
    
    
    

Label(master,text = "This is Banking site",bg='light yellow' ,fg='orange',font=("Bold",16)).grid(row=1,column=1,pady=5,padx=5)
Label(master,text = "Using our bank is your safety",bg='light yellow',fg='orange',font=("calibri",14)).grid(row=2,column=1,padx=5,pady=5,sticky=N)

Button(master,text='login',font=("calibri",12),bg='light green',width=10,command=login).grid(row=4,column=1,)
Button(master,text='register',font=("calibri",12),bg='light green',width=10,command=register).grid(row=5,column=1)






master.mainloop()