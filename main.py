from tkinter import PhotoImage, messagebox as mb
import tkinter as tk
import json
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


with open("./saves/save.json", "r") as f:
    data = json.load(f)


root = tk.Tk()
Clicks = data["clicks"]
Total_clicks = data["total_clicks"]


def worker_cps():
    global Clicks
    global Total_clicks

    Clicks += round(data["cps"] / 10, 1)
    Total_clicks += round(data["cps"] / 10, 1)

    click_label.configure(text=f"Clicks: {Clicks}")
    worker_label.after(100, worker_cps)


def on_click():
    global Clicks
    global Total_clicks

    # The way the if statements are placed is for hierarchy.
    if data["quintuple_click"] == True:
        Clicks += 5; Total_clicks += 5
        click_label.configure(text=f"Clicks: {Clicks}")

    elif data["triple_click"] == True:
        Clicks += 3; Total_clicks += 3
        click_label.configure(text=f"Clicks: {Clicks}")

    elif data["double_click"] == True:
        Clicks += 2; Total_clicks += 2
        click_label.configure(text=f"Clicks: {Clicks}")
    
    else:
        Clicks += 1; Total_clicks += 1
        click_label.configure(text=f"Clicks: {Clicks}")


def click_upgrade(type: str):
    global Clicks

    if type == "double" and Clicks >= 75 and data["double_click"] == False:
        Clicks -= 75
        click_label.configure(text=f"Clicks: {Clicks}")
        double_button.configure(text="Double Click: [BOUGHT]")
        data["double_click"] = True

    elif type == "triple" and Clicks >= 225 and data["triple_click"] == False:
        Clicks -= 225
        click_label.configure(text=f"Clicks: {Clicks}")
        triple_button.configure(text="Triple Click: [BOUGHT]")
        data["triple_click"] = True

    elif type == "quintuple" and Clicks >= 1000 and data["quintuple_click"] == False:
        Clicks -= 1000
        click_label.configure(text=f"Clicks: {Clicks}")
        quintuple_button.configure(text="Quintuple Click: [BOUGHT]")
        data["quintuple_click"] = True

    else: 
        return


def buy_worker(type: str):
    global Clicks, Total_clicks

    if Clicks >= data[type]["price"]:
        Clicks -= round(data[type]["price"], 1)

        data[type]["price"] += round(data[type]["price"] * 0.2)
        data[type]["bought"] += 1

        data["cps"] += data[type]["cps"]

        if (type == "ui"):
            ui_button.configure(text=f"{data['ui']['name']} ({data['ui']['cps']} CPS) [{data['ui']['price']} Clicks] - {data['ui']['bought']}")
        elif (type == "lm"):
            lm_button.configure(text=f"{data['lm']['name']} ({data['lm']['cps']} CPS) [{data['lm']['price']} Clicks] - {data['lm']['bought']}")
        elif (type == "rm"):
            rm_button.configure(text=f"{data['rm']['name']} ({data['rm']['cps']} CPS) [{data['rm']['price']} Clicks] - {data['ui']['bought']}")
        elif (type == "auto"):
            auto_button.configure(text=f"{data['auto']['name']} ({data['auto']['cps']} CPS) [{data['auto']['price']} Clicks] - {data['auto']['bought']}")

        worker_label.configure(text=f"Worker CPS: {data['cps']}")




def leave_shop():
    root['background']="#4851e6"

    click_label.configure(text=f"Clicks: {Clicks}", bg="#4851e6")
    shop_button.configure(text="Enter Shop", command=render_shop1)
    click_button.configure(text="Click me", borderwidth=0, bg="#4851d7", fg="#4851e6", activebackground="#4851e6", activeforeground = "#4851e6", command=on_click, width=1100, height=1200, image=buttonclick)
    worker_label.configure(bg="#4851e6")


def render_shop1():
    root['background']='#eacb1c'

    click_label.configure(text=f"Clicks: {Clicks}", bg="#eacb1c")
    click_button.configure(text=" ", borderwidth=0, bg="#eacb1c", fg="#eacb1c", activebackground='#eacb1c', activeforeground='#eacb1c', width=1, height=1, image=buttonclick_yellow)
    shop_button.configure(text="Leave Shop", command=leave_shop, borderwidth=3)
    worker_label.configure(bg="#eacb1c")

    # Clicker upgrade section:
    blank_label_yellow.pack(pady=5)
    shop_click_label.pack(side="top", anchor="nw", padx=2, pady=5)

    double_button.pack(side="top", anchor="nw", padx=5, pady=3)
    triple_button.pack(side="top", anchor="nw", padx=5, pady=3)
    quintuple_button.pack(side="top", anchor="nw", padx=5, pady=3)

    # Buying workers section:
    shop_worker_label.pack(side="top", anchor="nw", padx=2, pady=5)

    ui_button.pack(side="top", anchor="nw", padx=5, pady=0)
    ui_button.configure(text=f"{data['ui']['name']} ({data['ui']['cps']} CPS) [{data['ui']['price']} Clicks] - {data['ui']['bought']}")

    lm_button.pack(side="top", anchor="nw", padx=5, pady=3)
    lm_button.configure(text=f"{data['lm']['name']} ({data['lm']['cps']} CPS) [{data['lm']['price']} Clicks] - {data['lm']['bought']}")

    rm_button.pack(side="top", anchor="nw", padx=5, pady=3)
    rm_button.configure(text=f"{data['rm']['name']} ({data['rm']['cps']} CPS) [{data['rm']['price']} Clicks] - {data['rm']['bought']}")

    auto_button.pack(side="top", anchor="nw", padx=5, pady=3)
    auto_button.configure(text=f"{data['auto']['name']} ({data['auto']['cps']} CPS) [{data['auto']['price']} Clicks] - {data['auto']['bought']}")

    shop_page2_button.pack(side="bottom", anchor="se", padx=2, pady=5)


def render_homescreen():
    click_label.pack(anchor="nw")
    worker_label.place(x=300)

    settings_button.place(x=7, y=30)
    shop_button.place(x=327, y=30)

    click_button.pack(anchor="center")


if __name__ == "__main__":
    root.title("Average Clicker Game [v2.0]")
    root.geometry("400x400")
    root.resizable(False, False)
    root.iconbitmap(resource_path('Assets/icon.ico'))
    root['background'] = "#4851e6"


    buttonclick = PhotoImage(file=resource_path('Assets/ClickButton.png'))
    buttonclick_blue = PhotoImage(file=resource_path("Assets/ClickButton_Blue.png"))
    buttonclick_yellow = PhotoImage(file=resource_path("Assets/ClickButton_Yellow.png"))

    blank_label_blue = tk.Label(text=" ", bg="#4851e6")
    blank_label_yellow = tk.Label(text=" ", bg="#eacb1c")

    click_label = tk.Label(text=f"Clicks: {data['clicks']}", fg="black", bg="#4851e6", font=("Helvetica",10))
    click_button = tk.Button(text="click me", width=1100, height=1200, borderwidth=0, command=on_click, 
                            bg="#4851d7", fg="#4851e6", 
                            activebackground="#4851e6", activeforeground="#4851e6", 
                            image=buttonclick)
  
    worker_label = tk.Label(text=f"Worker CPS: {data['cps']}", fg="black", bg="#4851e6", font=("Helvetica",10))
    shop_button = tk.Button(text="Enter Shop", command=render_shop1)
    settings_button = tk.Button(text="Settings")

    double_button = tk.Button(text="Double Click [75 Clicks]", command=lambda: click_upgrade(type="double"))
    triple_button = tk.Button(text="Triple Click [225 Clicks]", command=lambda: click_upgrade(type="triple"))
    quintuple_button = tk.Button(text="Quintuple Click [1000 Clicks]", command=lambda: click_upgrade(type="quintuple"))
    decuple_button = tk.Button(text="Decuple Click [10000 Clicks]", command=lambda: click_upgrade(type="decuple"))

    # Worker buttons (names shortened):
    ui_button = tk.Button(text=f"{data['ui']['name']} ({data['ui']['cps']} CPS) [{data['ui']['price']} Clicks] - {data['ui']['bought']}", command=lambda: buy_worker(type="ui"))
    lm_button = tk.Button(text=f"{data['lm']['name']} ({data['lm']['cps']} CPS) [{data['lm']['price']} Clicks] - {data['lm']['bought']}", command=lambda: buy_worker(type="lm"))
    rm_button = tk.Button(text=f"{data['rm']['name']} ({data['rm']['cps']} CPS) [{data['rm']['price']} Clicks] - {data['rm']['bought']}", command=lambda: buy_worker(type="rm"))
    auto_button = tk.Button(text=f"{data['auto']['name']} ({data['auto']['cps']} CPS) [{data['auto']['price']} Clicks] - {data['auto']['bought']}", command=lambda: buy_worker(type="auto"))

    ui_upgrade_button = tk.Button(text="Slightly Paid Intern (0.5 -> 1 DPS): [750 Clicks]")
    lm_upgrade_button = tk.Button(text="Logitech Super Light Mouse (2 -> 4.5 DPS): [3500 Clicks]")
    rm_upgrade_button = tk.Button(text="Razor Viper Mouse (5 -> 12.5 DPS): [12500 Clicks]")
    auto_upgrade_button = tk.Button(text="Semi-OP Autoclicker (15 -> 35 DPS): [35000 Clicks]")

    # Shop Buttons:
    shop_click_label = tk.Label(text="Clicker Upgrades: ", bg="#eacb1c", font=("Helvetica",10))
    shop_worker_label = tk.Label(text="Workers:", bg="#eacb1c", font=("Helvetica",10))
    shop_worker_upgrade_label = tk.Label(text="Worker Upgrades:", bg="#eacb1c", font=("Helvetica",10))

    shop_page2_button = tk.Button(text="Page 2 ->", font=("Helvetica",10))
    shop_page3_button = tk.Button(text="Page 3 ->", font=("Helvetica",10))

    save_label = tk.Label(text="Manual Save Game:", bg="#4851e6")
    save_button = tk.Button(text="Save Game Stats")

    other_label = tk.Label(text="Settings Other Features: ", bg="#4851e6")
    reset_button = tk.Button(text="Reset Stats", bg="red", fg="Black", activebackground="red", activeforeground="black")
    # credits_button = tk.Button(text="Game Credits")  <- Come back to fix.

    worker_cps()
    render_homescreen()
    
def close(bind): 
	root.destroy()

root.protocol("WM_DELETE_WINDOW")
root.bind("<Escape>", close)
root.mainloop()
