import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

price_menu = {"Breakfast":15,"Lunch":18,"Dinner":22,"Drinks":8}

def restart_again():
    Cost.config(state="normal")
    Cost.delete(0,tk.END)             
    Cost.config(state="disabled")
                
    Tax.config(state="normal")
    Tax.delete(0,tk.END)
    Tax.config(state="disabled")

    Total.config(state="normal")
    Total.delete(0,tk.END)
    Total.config(state="disabled")

def sum_prices():
    if Breakfast.get():
        Breakfast_bill = int(Breakfast.get())*price_menu["Breakfast"]
    else:
        Breakfast_bill = 0

    if Lunch.get():
        Lunch_bill = int(Lunch.get())*price_menu["Lunch"]
    else:
        Lunch_bill = 0

    if Dinner.get():
        Dinner_bill = int(Dinner.get())*price_menu["Dinner"]
    else:
        Dinner_bill = 0

    if Drinks.get():
        Drinks_bill = int(Drinks.get())*price_menu["Drinks"]
    else:
        Drinks_bill = 0
        
    file = open("Data.txt")
    current_order = int(file.read())
    file.close()
    new_order = current_order+1
    
    Number.config(state="normal")
    Number.delete(0, tk.END)
    Number.insert(tk.END, str(new_order))
    Number.config(state="disabled")
    
    file = open("Data.txt","w")
    file.write(str(new_order))
    file.close()
    
    Total_cost = Breakfast_bill+Lunch_bill+Dinner_bill+Drinks_bill
    Total_tax = 30*Total_cost/100
    Total_bill = Total_cost+Total_tax
    
    restart_again()
    
    Cost.config(state="normal")
    Cost.insert(tk.END, Total_cost)
    Cost.config(state="disabled")

    Tax.config(state="normal")
    Tax.insert(tk.END, Total_tax)
    Tax.config(state="disabled")

    Total.config(state="normal")
    Total.insert(tk.END, Total_bill)
    Total.config(state="disabled")


def restart():
    Number.config(state="normal")
    Number.delete(0,tk.END)
    Number.config(state="disabled")
    
    Breakfast.delete(0,tk.END)
    
    Lunch.delete(0,tk.END)

    Dinner.delete(0,tk.END)
    
    Drinks.delete(0,tk.END)
    
    Cost.config(state="normal")
    Cost.delete(0,tk.END)             
    Cost.config(state="disabled")
                
    Tax.config(state="normal")
    Tax.delete(0,tk.END)
    Tax.config(state="disabled")

    Total.config(state="normal")
    Total.delete(0,tk.END)
    Total.config(state="disabled")
               
def show_prices():
    prices = Toplevel(resturaunt)
    prices.geometry("500x400")
    prices.title("-$-Prices-of-Each-Item-$-")
    prices.configure(bg="light green")

    price_title = tk.Label(prices, text="✰-$-Prices-$-✰",bg="light green",fg="dark green",font="Normal 20 bold")
    price_title.pack(pady=10)

    menu_outline = tk.Frame(prices, bd=8, bg="green", relief="ridge")
    menu_outline.pack(pady=10)

    menu = ttk.Treeview(menu_outline, column=("Column1","Column2"), show="headings")
    menu.pack()

    menu.heading("Column1", text="[:::] ITEM [:::]")
    menu.heading("Column2", text="$ PRICE $")

    item_costs = [("-o Breakfast meal o-","$15"),("C0D lunch meal C0D","$18"),("l> Dinner meal <l","$22"),("\_/ drinks \_/","$8")]

    for i in item_costs:
        menu.insert("","end",values=i)

    exit_price = tk.Button(prices, text="Exit ---->", bg="red", fg="brown",font=("Arial",18),width=20,command=prices.destroy)
    exit_price.pack(pady=20)

resturaunt = tk.Tk()
resturaunt.geometry("640x430")
resturaunt.title("Restaurant system")
resturaunt.configure(bg="tan")

label = tk.Label(text="✦-Restaurant Management System-✦",bg="tan",fg="brown",font="Normal 20 bold")
label.pack(pady=10)

label1 = tk.Label(text="Order nu -",bg="tan",fg="brown")
label1.place(x=50,y=70)

Number = tk.Entry()
Number.place(x=130,y=70)
Number.config(state="disabled")

label2 = tk.Label(text="Breakfast meal -",bg="tan",fg="brown")
label2.place(x=50,y=110)

Breakfast = tk.Entry()
Breakfast.place(x=175,y=110)

label3 = tk.Label(text="Lunch meal -",bg="tan",fg="brown")
label3.place(x=50,y=150)

Lunch = tk.Entry()
Lunch.place(x=150,y=150)

label3 = tk.Label(text="Dinner meal -",bg="tan",fg="brown")
label3.place(x=50,y=190)

Dinner = tk.Entry()
Dinner.place(x=155,y=190)

label4 = tk.Label(text="Drinks -",bg="tan",fg="brown")
label4.place(x=50,y=230)

Drinks = tk.Entry()
Drinks.place(x=110,y=230)

label5 = tk.Label(text="Cost - $",bg="tan",fg="brown")
label5.place(x=350,y=70)

Cost = tk.Entry()
Cost.place(x=408,y=70)
Cost.config(state="disabled")

label6 = tk.Label(text="Tax -",bg="tan",fg="brown")
label6.place(x=360,y=150)

Tax = tk.Entry()
Tax.place(x=400,y=150)
Tax.config(state="disabled")

label7 = tk.Label(text="Total -",bg="tan",fg="brown")
label7.place(x=330,y=230)

Total = tk.Entry()
Total.place(x=380,y=230)
Total.config(state="disabled")

Price_button = tk.Button(text="$-Price-$",highlightbackground="green",highlightcolor="dark green", highlightthickness=3,fg="dark green", font=("Arial",12), bg="light green",command=show_prices)

Price_button.place(x=30,y=280)

Total_button = tk.Button(text="<-- Total -->",highlightbackground="dark blue",highlightcolor="dark blue", highlightthickness=3,fg="dark blue", font=("Arial",12), bg="light blue",command=sum_prices)

Total_button.place(x=145,y=280)

Restart_button = tk.Button(text="o Restart o",highlightbackground="purple",highlightcolor="purple", highlightthickness=3,fg="purple", font=("Arial",12), bg="violet",command=restart)

Restart_button.place(x=290,y=280)

Exit_button = tk.Button(text="X Exit -->",highlightbackground="brown",highlightcolor="brown", highlightthickness=3,fg="brown", font=("Arial",12), bg="red",command=resturaunt.destroy)

Exit_button.place(x=420,y=280)

resturaunt.mainloop()