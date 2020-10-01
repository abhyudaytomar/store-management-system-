from tkinter import *
from tkinter import ttk
import mysql.connector as sqltor 
from datetime import date


#opening a connection to the database 
mycon = sqltor.connect(user="root",password="abcd",database="project",charset="utf8")

cursor = mycon.cursor()

root = Tk()
root.geometry("1200x1200")


def insert_user(username,password):
    cursor.execute("insert into users values('{}','{}');".format(username,password))

    confirm = Tk()
    Label(confirm, text="USER ADDED SUCESSFULLY", font=("arial","12")).pack()





def add_new_user():
    add_new_user_screen = Tk()
    add_new_user_screen.geometry("300x100")

    Label(add_new_user_screen, text="USERNAME:", font=("arial","12")).place(x=0,y=0)
    username = ttk.Entry(add_new_user_screen, font=("arial","12"))
    username.place(x=110,y=0)

    Label(add_new_user_screen, text="PASSWORD",font=("arial","12")).place(x=0,y=30)
    password = ttk.Entry(add_new_user_screen, font=("arial","12"))
    password.place(x=110,y=30)   

    Button(add_new_user_screen, text="ADD", font=("arial","12"), command= lambda: insert_user(username.get(),password.get())).place(x=240,y=60) 








def insert_into_stock(prod_no,prod_name,quantity,price,category,shelf):
    prod_no = int(prod_no)
    price = int(price)
    quantity = int(quantity)
    cursor.execute("insert into stock values({},'{}',{},{},'{}','{}')".format(prod_no,prod_name,quantity,price,category,shelf))
    mycon.commit()

    confirm = Tk()
    Label(confirm, text="product added sucessfully", font=("arial","13")).pack()



def add_product():
    add_product_screen = Tk()
    add_product_screen.geometry("400x280")

    Label(add_product_screen, text='PRODUCT NO :', font=("arial","12")).place(x=0,y=0)
    prod_no = ttk.Entry(add_product_screen, font=("arial","12"))
    prod_no.place(x=140,y=0)


    Label(add_product_screen, text="PRODUCT NAME :", font=("arial","12")).place(x=0,y=30)
    prod_name = ttk.Entry(add_product_screen, font=("arial","12"))
    prod_name.place(x=140,y=30)

    Label(add_product_screen, text="QUANTITY : ", font=("arial","12")).place(x=0,y=60)
    quantity = ttk.Entry(add_product_screen, font=("arial","12"))
    quantity.place(x=140,y=60)

    Label(add_product_screen, text="PRICE : ", font=("arial","12")).place(x=0,y=90)
    price = ttk.Entry(add_product_screen, font=("ariial","12"))
    price.place(x=140,y=90)

    Label(add_product_screen, text="CATEGORY", font=("arial,","12")).place(x=0,y=120)
    category = ttk.Entry(add_product_screen, font=("arial","12"))
    category.place(x=140,y=120)

    Label(add_product_screen, text="SHELF : ", font=("arial","12")).place(x=0,y=150)
    shelf = ttk.Entry(add_product_screen, font=("arial","12"))
    shelf.place(x=140,y=150)

    Button(add_product_screen, text="ADD PRODUCT", font=("arial","15"), command= lambda: insert_into_stock(prod_no.get(),prod_name.get(),quantity.get(),price.get(),category.get(),shelf.get())).place(x=230,y=220)




def print_bill(email,cust_name,bill_no):
    
    cursor.execute("select sum(amount) from bills_data where bill_no={}".format(bill_no))
    data = cursor.fetchall()
    for amt in data:
        total = amt
    print(amt)

    cursor.execute("select * from bills_data where bill_no={}".format(bill_no))
    data1 = cursor.fetchall()
    print(data1)


    print_bill_window = Tk()
    canvas = Canvas(print_bill_window,height=600,width=800)
    canvas.create_text(100,10, text="========================================================================================================================================================================================")
    canvas.create_text(300,30, font=("arial","12"), text="                             BILL NO : {}                                                                                                                        DATE : {}".format(bill_no,date.today()))
    canvas.create_text(300,40,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    canvas.create_text(300,70,font=("arial","12"), text="                               PRODUCT NAME                                      QUANTITY                          PRICE                                AMOUNT")

    x = 300
    y = 90
    for i in data1:
        bill_no,prod_no,prod_name,quantity,price,amount=i
        canvas.create_text(x,y,font=("arial","10"), text="                                    {}                                                       {}                                               {}                                               {} ".format(prod_name,quantity,price,amount))
        y=y+20
            

    canvas.create_text(300,y,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    canvas.create_text(300,y+20,font=("arial","12"), text="SEE YOU SOON {} !!!".format(cust_name))
    canvas.create_text(300,y+40,text="===============================================================================================================================")
    canvas.pack()
    print_bill_window.mainloop()

    


def add_to_bill(bill_no,date_today,add_product_by,product,prod_quantity,treeview_bill):

    if add_product_by == 0:
        cursor.execute("select prod_no,prod_name,price from stock where prod_no={}".format(product))
    
    elif add_product_by == 1:
        cursor.execute("select prod_no,prod_name,price from stock where prod_name='{}'".format(product))
    
    data = cursor.fetchall()
    
    for prod_no,prod_name,price in data:
        amount = price*int(prod_quantity)
        i = (prod_no,prod_name,price,prod_quantity,amount)
        cursor.execute("insert into bills_data values({},{},'{}',{},{},{})".format(bill_no,prod_no,prod_name,price,prod_quantity,amount))
        mycon.commit()

        treeview_bill.insert("","end",values=i)
  
    
    





def bill():
    bill_screen = Tk()
    bill_screen.geometry("1100x530")


   



    #bill number 
    cursor.execute("select max(bill_no) from bills_data")
    data =  cursor.fetchone()
    bill_no = data[0]+1

    Label(bill_screen, text="BILL NO : {}".format(bill_no), font=("arial","15")).place(x=15,y=15)

    #  date 
    date_today = date.today()
    Label(bill_screen,text="DATE : {}".format(date_today), font=("arial","15")).place(x=900,y=15)

    #name 
    Label(bill_screen, text="NAME : ", font=("arial","15")).place(x=15,y=55)
    cust_name = ttk.Entry(bill_screen,font=("arial","15"), width=25)
    cust_name.place(x=100,y=55)


    #email
    Label(bill_screen, text="E-mail : ", font=("arial",15)).place(x=620,y=55)
    email = ttk.Entry(bill_screen, font=("arial","15"), width=35)
    email.place(x=700,y=55)


    #add product by 
    Label(bill_screen, text="ADD PRODUCT BY : ", font=("arial","15")).place(x=15,y=100)    
    add_product_by = ttk.Combobox(bill_screen, values=["PRODUCT NO","PRODUCT NAME"], font=("arial","15"))
    add_product_by.place(x=210,y=100)


    #product
    product = ttk.Entry(bill_screen, font=("arial","15"))
    product.place(x=460,y=100)

    #product quantity
    Label(bill_screen, text="QUANTITY : ", font=("arial","15")).place(x=710,y=100)
    prod_quantity = ttk.Entry(bill_screen, font=("arial","15"), width=10)
    prod_quantity.place(x=820,y=100)



    treeview_bill = ttk.Treeview(bill_screen)
    treeview_bill["columns"] = ("1","2","3","4","5")
    treeview_bill["show"] = ("headings")

    treeview_bill.place(x=20,y=180)

    #column headings 
    treeview_bill.heading("1", text="PRODUCT NO")
    treeview_bill.heading("2", text="PRODUCT NAME")
    treeview_bill.heading("3", text="QUANTITY")
    treeview_bill.heading("4", text="PRICE")
    treeview_bill.heading("5", text="AMOUNT")

    #column properties 
    treeview_bill.column("1", width=190, anchor="c")
    treeview_bill.column("2", width=300, anchor="c")
    treeview_bill.column("3", width=190, anchor="c")
    treeview_bill.column("4", width=190, anchor="c")
    treeview_bill.column("5", width=190, anchor="c")




    


    Button(bill_screen, text="ADD", font=("arial","15"), command= lambda: add_to_bill(bill_no,date_today,add_product_by.current(),product.get(),prod_quantity.get(),treeview_bill)).place(x=970,y=100)
    Button(bill_screen, text="PRINT BILL", font=("arial","15"),command= lambda: print_bill(email.get(),cust_name.get(),bill_no)).place(x=960,y=460)
   





def delete(delete_by,del_info):

    if delete_by == 0:
        cursor.execute("delete * from stock where prod_no='{}';".format(del_info))
    
    elif delete_by == 1:
        cursor.execute("delete from stock where prod_name='{}';".format(del_info))

    mycon.commit()
    confirm_screen = Tk()
    Label(confirm_screen, text="PRODUCT DELETED SUCESSFULLY", font=("arial","12")).pack()





def delete_product():
    delete_product_screen = Tk()
    delete_product_screen.geometry("400x80")

    Label(delete_product_screen, text="DELETE BY :", font=("arial","12")).place(x=0,y=0)

    
    delete_by =  ttk.Combobox(delete_product_screen, values=["PRODUCT NO","PRODUCT NAME"])
    delete_by.place(x=105,y=0)

    del_info = Entry(delete_product_screen)
    del_info.place(x=250,y=0)

    Button(delete_product_screen, text="DELETE", font=("arial","12"), command= lambda: delete(del_info.get(),delete_by.current())).place(x=300,y=30)
    
    
      



def get_results(search_by,search_for):

    if search_by == 0:
        cursor.execute("select * from stock where prod_no='{}';".format(search_for))

    elif search_by == 1:
        cursor.execute("select * from stock where prod_name='{}';".format(search_for))

    elif search_by == 2:
        cursor.execute("select * from stock where category='{}';".format(search_for))

    data = cursor.fetchall()
    
    show_results=Tk()
    treeview = ttk.Treeview(show_results)
    treeview.pack()

    treeview["columns"] = ("1","2","3","4","5","6")
    treeview["show"] = ("headings")

    #column headings 
    treeview.heading("1", text="PRODUCT NO")
    treeview.heading("2", text="PRODUCT NAME")
    treeview.heading("3", text="QUANTITY")
    treeview.heading("4", text="PRICE")
    treeview.heading("5", text="CATEGORY")
    treeview.heading("6", text="SHELF")




    for i in data:
        treeview.insert("","end",values=i)

    
def search():
    search_screen = Tk()
    search_screen.geometry("500x200")

    Label(search_screen, text="SEARCH BY", font=("arial","15")).place(x=10,y=20)

    search_by = ttk.Combobox(search_screen, values=["product no","product name","category"])
    search_by.place(x=140,y=20)
    search_for = ttk.Entry(search_screen)
    search_for.place(x=290,y=20)
    ttk.Button(search_screen, text="SEARCH", command= lambda: get_results(search_by.current(),search_for.get())).place(x=350,y=80)
    
   

def view_stock():
    view_stock_screen = Tk()
    view_stock_screen.geometry("850x300")

    
    
    


    cursor.execute("select * from stock")
    data = cursor.fetchall()
    
    
    treeview = ttk.Treeview(view_stock_screen)
    treeview["columns"] = ("1","2","3","4","5","6")
    treeview["show"] = ("headings")
    treeview.place(x=20,y=20)

    #headings 
    treeview.heading("1", text="PRODUCT NO")
    treeview.heading("2", text="PRODUCT NAME")
    treeview.heading("3", text="QUANTITY")
    treeview.heading("4", text="PRICE")
    treeview.heading("5", text="CATEGORY")
    treeview.heading("6", text="SHELF")

    #column properties 
    treeview.column("1", width=100, anchor="c")
    treeview.column("2", width=300, anchor="c")
    treeview.column("3", width=100, anchor="c")
    treeview.column("4", width=100, anchor="c")
    treeview.column("5", width=100, anchor="c")
    treeview.column("6",width=100, anchor="c")



    #adding a scrollbar 
    scrollbar = Scrollbar(view_stock_screen)
    scrollbar.pack(side="right", fill="y")
    treeview.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command=treeview.yview)

    for i in data:
        treeview.insert("","end", values = i)




    






def authentication():
    USERNAME = str(username.get())
    PASSWORD = str(password.get())

    cursor.execute("select password from users where username='{}';".format(USERNAME))
    password1 = cursor.fetchone()


    if password1[0] == PASSWORD :
        root.destroy()
        

        main_screen = Tk()
        main_screen.geometry("1200x900")

        background_img = PhotoImage(file="images/background.png")
        background = Label(main_screen,image=background_img)
        background.pack()
        background.image = background_img

        
        Label(main_screen, text="DASHBOARD", font=("algerian","45","underline ")).place(x=440,y=20)
        

        Button(main_screen, text="VIEW STOCK", font=("arial","25"), width=20, command=view_stock).place(x=120,y=150)
        Button(main_screen,text="ADD PRODUCT", font=("arial","25"), width=20,  command=add_product).place(x=700,y=150)
        Button(main_screen, text="DELETE PRODUCT", font=("arial","25"), width=20, command=delete_product).place(x=120,y=300)    
        Button(main_screen, text="SEARCH", font=("arial","25"), width=20,  command=search).place(x=700,y=300)
        Button(main_screen, text="GENERATE BILL", font=("arial","25"), width=20, command=bill).place(x=120,y=450)
        Button(main_screen, text="ADD NEW USER", font=("arial","25"), width=20, command=add_new_user).place(x=700,y=450)


    else:
        pass





#images 
user_login_img = PhotoImage(file="images/user.png")
password_img = PhotoImage(file="images/password.png")
username_img = PhotoImage(file="images/username.png")
background_img = PhotoImage(file="images/background.png")



#login screen
background = Label(root,image=background_img)
background.pack()
background.image = background_img

login_frame = Frame(root, height=550, width=800, bg="yellow")
login_frame.place(relx=0.17,rely=0.1)

user_login = Label(login_frame, image=user_login_img, compound="center")
user_login.image = user_login_img
user_login.place(x=350,y=80)


user_name = Label(login_frame, text="USERNAME", font=(("arial","25")), image=username_img, compound="left", bg="yellow")
user_name.place(x=65,y=250)
user_name.image = username_img

pass_word = Label(login_frame, text="PASSWORD", font=(("arial","25")), image=password_img, compound="left", bg="yellow")
pass_word.place(x=60,y=350)
pass_word.image = password_img



username= ttk.Entry(login_frame, font=(("arial","28")))
username.place(x=340,y=260)
password = ttk.Entry(login_frame, font=(("arial","28")),show="*")
password.place(x=340,y=360)






Button(login_frame, text="LOGIN", font=(("arial","24")), width="10", command=authentication ).place(x=570,y=440)

root.mainloop()