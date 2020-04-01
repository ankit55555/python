
from tkinter import*
import sqlite3
from tkinter import messagebox

window = Tk()
window.title("ONLINE VOTING SYSTEM")
window.geometry('1500x500')

conn=sqlite3.connect('data.db')
c=conn.cursor() 

#c.execute("CREATE TABLE data(firstname text,lastname text,rollno integer,idnumber integer)")



name1=StringVar()
id1=StringVar()
age1=StringVar()
v=IntVar()



l=Label(window,text="****VOTING****",font=("Adobe Fan Heiti Std",20),bg="black",fg="light green")
l.grid(row=0,column=0,pady=15,columnspan=2)

l=Label(window,text="Please Enter correct Details below.",font=('',15))
l.grid(row=1,column=0,pady=10,columnspan=2)

  
def clear():
    name.delete(0,END)
    id_number.delete(0,END)
    age.delete(0,END)

def check():
    global a
    global v
    a=int(a.get())
    if(a<=18):
        messagebox.showerror("Error", "you are not eighteen")
    else:
        
        messagebox.showinfo("vote", "thanks")

        
        sub1=name1.get()
        sub2=int(id1.get())
        sub3=a
        
        if v.get()==1 :
            sub4="Congress"
        elif v.get()==2 :
            sub4="BJP"
        elif v.get()==3 :
            sub4="Shivsena"
        elif v.get()==4 :
            sub4="AAP"
        
        conn=sqlite3.connect('data.db')
        c=conn.cursor() 
        c.execute("CREATE TABLE IF NOT EXISTS data(Name text NOT NULL,ID  int NOT NULL,Age int NOT NULL,Party text NOT NULL)")
        conn.commit()
        conn.close()

        conn=sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("INSERT INTO data (Name,ID,Age,Party) \
            VALUES (?,?,?,?)",(sub1,sub2,sub3,sub4));
        conn.commit()
        conn.close()        
        
        
    
    

        
    
a=StringVar()
name=Entry(window,width=30,textvariable=name1)
name.grid(column=1,row=2,ipadx=20,pady=5)
id_number=Entry(window,width=30,textvariable=id1)
id_number.grid(column=1,row=3,ipadx=20,pady=5)
#age = Spinbox(window, from_=0, to=100, width=28,command=agee)
#age.grid(column=1,row=3,pady=5,ipadx=20)
age=Entry(window,textvariable=a,width=30)
age.grid(column=1,row=4,ipadx=20,pady=5)


name_label=Label(window,text="ENTER NAME:",font=("Adobe Fan Heiti Std",10))
name_label.grid(column=0,row=2,pady=5)
id_label=Label(window,text="ENTER ID NOS:",font=("Adobe Fan Heiti Std",10))
id_label.grid(column=0,row=3,pady=5)
age_label=Label(window,text="ENTER AGE:",font=("Adobe Fan Heiti Std",10))
age_label.grid(column=0,row=4,pady=5)


l=Label(window,text="Please select your option below.",font=('',15))
l.grid(row=5,column=0,pady=10,columnspan=2)

congress_label=Label(window,text="CONGRESS:").grid(column=0,row=6)
bjp_label=Label(window,text="BJP:").grid(column=0,row=7)
shiv_label=Label(window,text="SHIV SENA:").grid(column=0,row=8)
aap_label=Label(window,text="AAP:").grid(column=0,row=9)

congress_radio=Radiobutton(window,value=1,variable=v)
congress_radio.grid(column=1,row=6,pady=5)

bjp_radio=Radiobutton(window,value=2,variable=v)
bjp_radio.grid(column=1,row=7,pady=2)

shiv_radio=Radiobutton(window,value=3,variable=v)
shiv_radio.grid(column=1,row=8,pady=2)

aap_radio=Radiobutton(window,value=4,variable=v)
aap_radio.grid(column=1,row=9,pady=2,padx=10)

vote_button=Button(window,text="VOTE..!",width=40,font=("arial bold",10),bg="red",fg="white",command=check)
vote_button.grid(row=10,column=0,ipadx=20,pady=10,padx=10,columnspan=2)
reset_button=Button(window,text="CLEAR INFO",width=20,font=("arial bold",10),bg="yellow",command=clear)
reset_button.grid(row=11,column=0,ipadx=20,pady=10,padx=10,columnspan=2)

#reset_button=Button(window,text="CLEAR INFO",width=20,font=("arial bold",10),bg="yellow",command=clear)
#reset_button.grid(row=0,column=4,ipadx=20,pady=10,padx=10)



conn.commit()

#print(c.fetchall())

conn.close()


window.mainloop()


