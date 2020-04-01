from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import sqlite3
import random

# Database 
with sqlite3.connect('ankit.db') as db:
    c = db.cursor()
try:
    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX  NOT NULL,mobile TEX NOT NULL);')
except:
    pass
db.commit()
db.close()
  


class main:
    def __init__(self,master): 
  
        self.master = master
        
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_reg=StringVar()
        self.n_mobile=StringVar()
        self.mobile11=StringVar()
        self.widgets()


    
    def login(self):
  
        with sqlite3.connect('ankit.db') as db:
            c = db.cursor()


        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        
        if result:
            self.track()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    
        
        with sqlite3.connect('ankit.db') as db:
            c = db.cursor()
        if self.n_username.get()!=' ' and self.n_password.get()!=' ' and self.n_mobile.get()!=' ':
            find_user = ('SELECT * FROM user WHERE username = ?')
            c.execute(find_user,[(self.n_username.get())])        

            if c.fetchall():
                    ms.showerror('Error!','Username Taken Try a Diffrent One.')
            else:
                    insert = 'INSERT INTO user(username,password,mobile) VALUES(?,?,?)'
                    c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.n_mobile.get())])
                    db.commit()

                    ms.showinfo('Success!','Account Created!')
                    self.log()
        else:
             ms.showerror('Error!','Please Enter the details.')
        
     
        
    def consignment(self):
        
       
        
        try:
            with sqlite3.connect('ankit.db') as db:
                c = db.cursor()


            #Find user If there is any take proper action
            find_user = ('SELECT * FROM user WHERE mobile= ?')
            c.execute(find_user,[(self.mobile11.get())])
            result = c.fetchall()

            if result:
                    self.track()
                    self.crff.pack_forget()
                    self.head['text'] = self.username.get() + '\n Your Product Details'
                    self.consi.pack()
            else:
                    ms.showerror('Oops!','Mobile Number Not Found.')
        except:
            ms.showerror('Oops!','Mobile Number Not Found.')
                
    
   
    def track1(self):
        self.consi.pack_forget()
        self.head['text'] = self.username.get() + '\n Track your Product'
        self.crff.pack()
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()
        
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    def track(self):
             self.logf.pack_forget()
             self.head['text'] = self.username.get() + '\n Track your Product'
            
             self.crff.pack()
           

  
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',20),pady = 10)
        self.head.pack()
        
    
        self.logf = Frame(self.master,padx =10,pady = 10)
        
        self.logf.configure(background='lightblue')
        #PhotoImage(self.logf,file = 'lpu_logo.png')
        Label(self.logf,text = 'Username: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 3,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 3,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',background='lightgrey',bd = 2 ,font = ('',13),padx=6,pady=6,command=self.login).grid(row=8,column=0)
        Button(self.logf,text = ' New user ',background='lightgrey',bd = 2 ,font = ('',13),padx=6,pady=6,command=self.cr).grid(row=8,column=1)
       
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 0)
        Label(self.crf,text = 'Username: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 3,font = ('',15)).grid(row=0,column=1)
        
        Label(self.crf,text = 'Password: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 3,font = ('',15),show = '*').grid(row=1,column=1)
        
        Label(self.crf,text = 'Reg No.: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_reg,bd = 3,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Gender: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        var = IntVar()
        R1 = Radiobutton(self.crf, text="Male", variable=var, value=1).grid(row=3,column=2)
        R2 = Radiobutton(self.crf, text="Female", variable=var, value=2 ).grid(row=3,column=1)
        Label(self.crf,text = 'Mobile No.: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_mobile,bd = 3,font = ('',15)).grid(row=4,column=1)
        
        Label(self.crf,text = 'Email Id: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,bd = 3,font = ('',15)).grid(row=5,column=1)
        
        
        
        Button(self.crf,text = 'Create Account',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.new_user).grid(row=11,column=0)
        Button(self.crf,text = 'Go to Login',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.log).grid(row=11,column=1)

    

        self.crff = Frame(self.master,padx =10,pady = 10)
        
      

        Label(self.crff,text = 'Registered  No: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crff,bd = 3,font = ('',15)).grid(row=0,column=1)
        Label(self.crff,text = 'Mobile no:',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crff,bd = 3,textvariable = self.mobile11,font = ('',15)).grid(row=1,column=1)
        Button(self.crff,text = 'Track',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.consignment).grid(row=4,column=0)

        self.consi = Frame(self.master,padx =10,pady = 10)
        
        Label(self.consi,text = ' Product ID:',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text =random.randint(565154,99994216) ,font = ('',13),pady=5,padx=5).grid(row=0,column=1)
        L = ['Bag','Colgate','shoe','Redme 2','Jeans','Parrot','Mac','Ipad','Pen','Book','shirt']
        f=random.randint(0,10)
        Label(self.consi,text = 'Product name: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text =L[f] ,font = ('',13),pady=5,padx=5).grid(row=1,column=1)
        Label(self.consi,text = 'Product Status: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Label(self.consi,text ='Pending' ,font = ('',13),pady=5,padx=5).grid(row=2,column=1)
        Label(self.consi,font = ('',13), text = 'Thanks for Exploring!').grid(row = 4, column = 0)
       
        Label(self.consi, text = 'Comments:',font = ('',13)).grid(row = 5, column = 0, padx = 5, sticky = 'sw')
        Entry(self.consi,bd = 3,font = ('',15)).grid(row=5,column=1)

        Button(self.consi,text = 'Back',background='lightgrey',bd = 2,font = ('',13),padx=6,pady=6,command=self.track1).grid(row=6,column=0)
    
        
        
        
        

if __name__ == '__main__':

    root = Tk()
    root.title('Track Consignment')
    root.geometry('800x750+300+300')
    main(root)
    
    canvas = Canvas(root)
    canvas.pack()
    canvas.config(width = 640, height = 380)

    line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
    canvas.itemconfigure(line, fill = '#1abc9c')
    print("Successful")
    canvas.coords(line, 0, 0, 320, 240, 640, 0)

    canvas.itemconfigure(line, smooth = True)
    canvas.itemconfigure(line, splinesteps = 5)
    canvas.itemconfigure(line, splinesteps = 100)
    canvas.delete(line)

    rect = canvas.create_rectangle(160, 120, 480, 360)
    canvas.itemconfigure(rect, fill = '#3498db')
    oval = canvas.create_oval(160, 120, 480, 360)
    arc = canvas.create_arc(160, 1, 480, 240)
    canvas.itemconfigure(arc, start = 0, extent = 180, fill = '#1abc9c')
    poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = '#95a5a6')
    text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

  
    root.mainloop()
    
