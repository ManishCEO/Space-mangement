import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import pymysql



def adddata():
    if fi.get()=='' or la.get()=='' or lm.get()=='' or ed.get()=='' or option1.get()=='' or og.get()=='' or mc.get()=='' or cd.get()=='' or md.get()=='' or ad.get()=='' or dp.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='manish123@')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        try:
            query='use userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table emprecord(id int auto_increment primary key not null,firstname varchar(50),lastname varchar(50),immediateManager varchar(50),emailid varchar(100),empstd varchar(50),organization varchar(50),mucode varchar(50),division varchar(50),workmode varchar(50),adminname varchar(50),departmentmanager varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from emprecord where emailid=%s'
        
        mycursor.execute(query,(ed.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','EmailID already exits')
        
        else:
            query='insert into emprecord(firstname,lastname,immediateManager,emailid,empstd,organization,mucode,division,workmode,adminname,departmentmanager)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(fi.get(),la.get(),lm.get(),ed.get(),option1.get(),og.get(),mc.get(),cd.get(),md.get(),ad.get(),dp.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful')


      
        




root = ctk.CTk()


root.title("CBRE_KEYISGHT")
root.geometry("1920x1080-10+0+10")
ctk.set_appearance_mode("system")

tabview=ctk.CTkTabview(master=root,width=1300,height=700)
tabview.place(x=300,y=75)

t1=tabview.add("Add New Emplyoee")
t2=tabview.add("Workstation Assign")
tabview.set("Workstation Assign")



logo = ctk.CTkLabel(root,text="KEYSIGHT SPACE DATA MANAGEMENT",anchor="center",text_color="RED",corner_radius=40,height=50,width=200,font=('Abadi',50,'bold'))
logo.pack(padx=5,pady=5)


Frame= ctk.CTkFrame(root,width=7000,height=3,fg_color='white')
Frame.pack(padx=0,pady=0)

first = ctk.CTkLabel(master=t1,text="First Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
#first.place(x=350,y=150)
first.place(x=50,y=37)

fi= Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color="black",font=('Aptos Narrow',15))
#Entry.place(x=450,y=145)
Entry.place(x=155,y=35)

last = ctk.CTkLabel(master=t1,text="Last Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
last.place(x=450,y=37)

la=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=560,y=35)


lmanager = ctk.CTkLabel(master=t1,text="Immediate Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
lmanager.place(x=860,y=37)

lm=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=1020,y=35)


Email = ctk.CTkLabel(master=t1,text="Email ID",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
Email.place(x=50,y=120)

ed=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=155,y=115)

Std = ctk.CTkLabel(master=t1,text="Emp Std",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
Std.place(x=450,y=120)


#Entry = ctk.CTkEntry(root,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
#Entry.place(x=850,y=245)


Emp = ["FTE","NKW","ETW","INTERN"]
option1 = ctk.CTkOptionMenu(master=t1, values=Emp,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
option1.place(x=560,y=115)
option1.set(" ")

org = ctk.CTkLabel(master=t1,text="Organization",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
org.place(x=860,y=120)

og=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=1020,y=115)

MU = ctk.CTkLabel(master=t1,text="MU_Code",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
MU.place(x=50,y=205)

mc=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=155,y=200)

code = ctk.CTkLabel(master=t1,text="Division Code",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
code.place(x=450,y=205)

cd=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=565,y=200)

mode = ctk.CTkLabel(master=t1,text="Work mode",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
mode.place(x=860,y=205)

#Entry = ctk.CTkEntry(root,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
#Entry.place(x=1300,y=345)
mode = ["Work For Home","Office","Visitor Village"]
md=code = ctk.CTkOptionMenu(master=t1, values=mode,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
code.place(x=1020,y=200)
code.set(" ")



admin = ctk.CTkLabel(master=t1,text="Admin Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
admin.place(x=450,y=295)

ad=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=565,y=290)

deptm = ctk.CTkLabel(master=t1,text="Department Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
deptm.place(x=860,y=295)

dp=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=1020,y=290)

Button = ctk.CTkButton(master=t1, text="Add New Employee",height=35,corner_radius=15,font=('Aptos Narrow',15),command=adddata)
Button.place(x=1030,y=400)


#Workstation assign TAB Section
def fetchdata():
    
    e2=t2ed.get()
    
    if t2ed.get()=='':
        messagebox.showerror('Error','Email_ID Field is required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='manish123@',database='userdata')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        try:
            mycursor.execute("select * from emprecord where emailid = '"+ e2 +"'")
            r=mycursor.fetchall()
            for row in r:
                pass
            t2og.delete(0, END)
            t2og.insert(END, row[6])
            t2lm.delete(0, END)
            t2lm.insert(END, row[3])
            t2ad.delete(0, END)
            t2ad.insert(END, row[10])
            t2dp.delete(0, END)
            t2dp.insert(END, row[11])
            
            

        except Exception as e:
            print(e)
            con.rollback()
            con.close()

        
 

t2email = ctk.CTkLabel(master=t2,text="Email ID",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2email.place(x=430,y=75)

t2ed=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=270,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=520,y=70)

Button = ctk.CTkButton(master=t2, text="Fetch",height=35,corner_radius=15,font=('Aptos Narrow',15),command=fetchdata)
Button.place(x=800,y=70)


t2org = ctk.CTkLabel(master=t2,text="Organization",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2org.place(x=220,y=200)

t2og=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=350,y=195)


t2lmanager = ctk.CTkLabel(master=t2,text="Immediate Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2lmanager.place(x=710,y=200)

t2lm=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=900,y=195)



t2admin = ctk.CTkLabel(master=t2,text="Admin Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2admin.place(x=220,y=280)

t2ad=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=350,y=275)


t2deptm = ctk.CTkLabel(master=t2,text="Department Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2deptm.place(x=710,y=280)

t2dp=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
Entry.place(x=900,y=275)

t2floor = ctk.CTkLabel(master=t2,text="floor name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2floor.place(x=460,y=390)

name = ["Ground Floor","First Floor","Second Floor","Third Floor","Fourth Floor","Fifth Floor"]
floor = ctk.CTkOptionMenu(master=t2, values=name,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
floor.place(x=590,y=385)
floor.set(" ")



t2mode = ctk.CTkLabel(master=t2,text="Work Mode",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t2floor.place(x=460,y=390)


occpany = ctk.CTkLabel(master=t2,text="Occupancy",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
occpany.place(x=460,y=440)


#Entry = ctk.CTkEntry(root,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15))
#Entry.place(x=450,y=445)

option4 = ["Occupied","Vacant"]
occ = ctk.CTkOptionMenu(master=t2, values=option4,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
occ.place(x=590,y=435)
occ.set(" ")


seat = ctk.CTkLabel(master=t2,text="Seat Number",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
seat.place(x=460,y=490)

option5 = ["Seat number"]
set1 = ctk.CTkOptionMenu(master=t2, values=option5,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
set1.place(x=590,y=485)
set1.set(" ")


b1=Button = ctk.CTkButton(master=t2, text="Save Data",height=35,corner_radius=15,font=('Aptos Narrow',15))
Button.place(x=590,y=550)

root.mainloop()




