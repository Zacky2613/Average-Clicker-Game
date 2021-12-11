from tkinter import PhotoImage, font
from tkinter import messagebox as mb
from Saves.save import Clicks, Total_Clicks, Worker_CPS, Double_Click_Upgrade, Double_Click_var, Triple_Click_Upgrade, Triple_Click_var, Quintuple_Click_Upgrade, Quintuple_Click_var, Unpaid_Intern, Unpaid_Intern_Price, Unpaid_Intern_DPS, Unpaid_Intern_Name, Unpaid_Intern_Upgrade_var, Logitech_Mouse, Logitech_Mouse_Price, Logitech_Mouse_Name, Logitech_Mouse_DPS, Logitech_Mouse_Upgrade_var, Razor_Mouse, Razor_Mouse_Name, Razor_Mouse_Price, Razor_Mouse_DPS, Razor_Mouse_Upgrade_var, Autoclicker, Autoclicker_DPS, Autoclicker_Name, Autoclicker_Price, Autoclicker_Upgrade_var
import tkinter as tk
import os
import sys
import time


root = tk.Tk()


# IMPORTANT NONE GOOGY FUNCTIONS

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def Developer_Console():
	global Clicks

	Clicks += 9999999999
	click_label.configure(text=f"Clicks: {Clicks}")



def Reset_Stats():
	reset_stats_popup = mb.askquestion('Average Clicker Game', 'Are you sure you want to reset your stats? They cannot be recovered.')

	if reset_stats_popup == "yes":
		with open(resource_path("Saves/save.py"), "w") as f:
			f.write(f"Clicks = 0\nTotal_Clicks = 0\nWorker_CPS = 0\n\n\nDouble_Click_Upgrade = False\nDouble_Click_var = False\n\nTriple_Click_Upgrade = False\nTriple_Click_var = False\n\nQuintuple_Click_Upgrade = False\nQuintuple_Click_var = False\n\n\nUnpaid_Intern = 0\nUnpaid_Intern_Price = 10\nUnpaid_Intern_Name = 'Unpaid Intern'\nUnpaid_Intern_DPS = 0.5\nUnpaid_Intern_Upgrade_var = False\n\nLogitech_Mouse = 0\nLogitech_Mouse_Price = 25\nLogitech_Mouse_Name = 'Logitech Mouse'\nLogitech_Mouse_DPS = 2\nLogitech_Mouse_Upgrade_var = False\n\nRazor_Mouse = 0\nRazor_Mouse_Price = 75\nRazor_Mouse_Name = 'Razor Mouse'\nRazor_Mouse_DPS = 5\nRazor_Mouse_Upgrade_var = False\n\nAutoclicker = 0\nAutoclicker_Price = 175\nAutoclicker_Name = 'Off-Brand Autoclicker'\nAutoclicker_DPS = 15\nAutoclicker_Upgrade_var = False")
			f.close()
		
		root.destroy()
	else:
		return



def save_system():
	with open(resource_path("Saves/save.py"), "w") as f:
		f.write(f"Clicks = {Clicks}\nTotal_Clicks = {Total_Clicks}\nWorker_CPS = {Worker_CPS}\n\n\nDouble_Click_Upgrade = {Double_Click_Upgrade}\nDouble_Click_var = {Double_Click_var}\n\nTriple_Click_Upgrade = {Triple_Click_Upgrade}\nTriple_Click_var = {Triple_Click_var}\n\nQuintuple_Click_Upgrade = {Quintuple_Click_Upgrade}\nQuintuple_Click_var = {Quintuple_Click_var}\n\n\nUnpaid_Intern = {Unpaid_Intern}\nUnpaid_Intern_Price = {Unpaid_Intern_Price}\nUnpaid_Intern_Name = '{Unpaid_Intern_Name}'\nUnpaid_Intern_DPS = {Unpaid_Intern_DPS}\nUnpaid_Intern_Upgrade_var = {Unpaid_Intern_Upgrade_var}\n\nLogitech_Mouse = {Logitech_Mouse}\nLogitech_Mouse_Price = {Logitech_Mouse_Price}\nLogitech_Mouse_Name = '{Logitech_Mouse_Name}'\nLogitech_Mouse_DPS = {Logitech_Mouse_DPS}\nLogitech_Mouse_Upgrade_var = {Logitech_Mouse_Upgrade_var}\n\nRazor_Mouse = {Razor_Mouse}\nRazor_Mouse_Price = {Razor_Mouse_Price}\nRazor_Mouse_Name = '{Razor_Mouse_Name}'\nRazor_Mouse_DPS = {Razor_Mouse_DPS}\nRazor_Mouse_Upgrade_var = {Razor_Mouse_Upgrade_var}\n\nAutoclicker = {Autoclicker}\nAutoclicker_Price = {Autoclicker_Price}\nAutoclicker_Name = '{Autoclicker_Name}'\nAutoclicker_DPS = {Autoclicker_DPS}\nAutoclicker_Upgrade_var = {Autoclicker_Upgrade_var}")
		f.close()
	
	root.destroy()



# GOOGY / WINDOW FUNCTION


def Worker_func():
	global Clicks
	global Total_Clicks

	Clicks_worker_takeaway_temp = Worker_CPS / 10
	Clicks_worker_takeaway_temp = round(Clicks_worker_takeaway_temp, 1)

	Clicks += Clicks_worker_takeaway_temp
	Clicks = round(Clicks, 1)
	Total_Clicks += Clicks_worker_takeaway_temp
	Total_Clicks = round(Total_Clicks, 1)

	click_label.configure(text=f"Clicks: {Clicks}")
	Worker_label.after(100, Worker_func)
		



def on_click():
	global Clicks
	global Total_Clicks

	if Double_Click_Upgrade == False and Triple_Click_Upgrade == False:
		Clicks += 1
		Total_Clicks += 1
		click_label.configure(text=f"Clicks: {Clicks}")

	elif Double_Click_Upgrade == True and Double_Click_var == True:
		Clicks += 2
		Total_Clicks += 2
		click_label.configure(text=f"Clicks: {Clicks}")

	elif Triple_Click_Upgrade == True and Triple_Click_var == True:
		Clicks += 3
		Total_Clicks += 3
		click_label.configure(text=f"Clicks: {Clicks}")	

	elif Quintuple_Click_Upgrade == True and Quintuple_Click_var == True:
		Clicks += 5
		Total_Clicks += 5
		click_label.configure(text=f"Clicks: {Clicks}")	



def Double_Click_Upgrade_Item():
	global Shop_DoubleClick_Button
	global Double_Click_var
	global Double_Click_Upgrade
	global Clicks

	if Clicks >= 75 and Double_Click_Upgrade != True:

		Clicks -= 75
		click_label.configure(text=f"Clicks: {Clicks}")
		Shop_DoubleClick_Button.configure(text="Double Click: [BOUGHT]")
		Double_Click_Upgrade = True
		Double_Click_var = True

		if Triple_Click_Upgrade == True or Quintuple_Click_Upgrade == True:
			Double_Click_var = False

	else:
		return




def Triple_Click_Upgrade_Item():
	global Shop_TripleClick_Button
	global Triple_Click_var
	global Triple_Click_Upgrade
	global Double_Click_var
	global Clicks

	if Clicks >= 225 and Triple_Click_Upgrade != True:

		Clicks -= 225
		click_label.configure(text=f"Clicks: {Clicks}")
		Shop_TripleClick_Button.configure(text="Triple Click: [BOUGHT]")
		Triple_Click_Upgrade = True
		Triple_Click_var = True

		if Double_Click_var == True:
			Double_Click_var = False
		
	else:
		return




def Quintuple_Click_Upgrade_Item():
	global Shop_QuintupleClick_Button
	global Quintuple_Click_var
	global Quintuple_Click_Upgrade
	global Double_Click_var
	global Triple_Click_var
	global Clicks

	if Clicks >= 1000 and Quintuple_Click_Upgrade != True:

		Clicks -= 1000
		click_label.configure(text=f"Clicks: {Clicks}")
		Shop_QuintupleClick_Button.configure(text="Quintuple Click: [BOUGHT]")
		Quintuple_Click_Upgrade = True
		Quintuple_Click_var = True

		if Double_Click_var == True:
			Double_Click_var = False

		elif Triple_Click_var == True:
			Triple_Click_var = False

	else:
		return




def Unpaid_Intern_Worker():
	global Clicks
	global Worker_CPS
	global Unpaid_Intern_Price
	global Unpaid_Intern

	if Clicks >= Unpaid_Intern_Price:
		Clicks -= Unpaid_Intern_Price

		Clicks = round(Clicks, 1)
		click_label.configure(text=f"Clicks: {Clicks}")

		Unpaid_Intern_Price *= 1.2
		Unpaid_Intern_Price = round(Unpaid_Intern_Price, 1)
		Unpaid_Intern += 1

		Unpaid_Intern_Worker_Button.configure(text=f"{Unpaid_Intern_Name} ({Unpaid_Intern_DPS} DPS): [{Unpaid_Intern_Price} Clicks] - {Unpaid_Intern}")

		Worker_CPS += Unpaid_Intern_DPS
		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")




def Unpaid_Intern_Worker_Upgrade():
	global Clicks
	global Worker_CPS
	global Unpaid_Intern_Name
	global Unpaid_Intern_DPS
	global Unpaid_Intern_Worker_Upgrade_Button
	global Unpaid_Intern_Upgrade_var

	if Clicks >= 750 and Unpaid_Intern_Upgrade_var != True:
		Clicks -= 750

		click_label.configure(text=f"Clicks: {Clicks}")

		Old_Unpaid_Intern_Placeholder = Unpaid_Intern_DPS * Unpaid_Intern
		Worker_CPS -= Old_Unpaid_Intern_Placeholder

		Unpaid_Intern_DPS = 1
		New_Unpaid_Intern_Placeholder = Unpaid_Intern_DPS * Unpaid_Intern
		Worker_CPS += New_Unpaid_Intern_Placeholder

		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")

		Unpaid_Intern_Name = "Slightly Paid Intern"

		Unpaid_Intern_Worker_Upgrade_Button.configure(text=f"Slightly Paid Intern (0.5 -> 1 DPS): [BOUGHT]")
		
		Unpaid_Intern_Upgrade_var = True




def Logitech_Mouse_Worker():
	global Clicks
	global Worker_CPS
	global Logitech_Mouse_Price
	global Logitech_Mouse

	if Clicks >= Logitech_Mouse_Price:
		Clicks -= Logitech_Mouse_Price

		Clicks = round(Clicks, 1)
		click_label.configure(text=f"Clicks: {Clicks}")

		Logitech_Mouse_Price *= 1.2
		Logitech_Mouse_Price = round(Logitech_Mouse_Price, 1)
		Logitech_Mouse += 1

		Logitech_Mouse_Worker_Button.configure(text=f"{Logitech_Mouse_Name} ({Logitech_Mouse_DPS} DPS): [{Logitech_Mouse_Price} Clicks] - {Logitech_Mouse}")

		Worker_CPS += Logitech_Mouse_DPS
		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")




def Logitech_Mouse_Worker_Upgrade():
	global Clicks
	global Worker_CPS
	global Logitech_Mouse_Name
	global Logitech_Mouse_DPS
	global Logitech_Mouse_Worker_Upgrade_Button
	global Logitech_Mouse_Upgrade_var

	if Clicks >= 3500 and Logitech_Mouse_Upgrade_var != True:
		Clicks -= 3500

		click_label.configure(text=f"Clicks: {Clicks}")

		Old_Logitech_Mouse_Placeholder = Logitech_Mouse_DPS * Logitech_Mouse
		Worker_CPS -= Old_Logitech_Mouse_Placeholder

		Logitech_Mouse_DPS = 4.5
		New_Logitech_Mouse_Placeholder = Logitech_Mouse_DPS * Logitech_Mouse
		Worker_CPS += New_Logitech_Mouse_Placeholder

		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")

		Logitech_Mouse_Name = "Logitech Super Light Mouse"

		Logitech_Mouse_Worker_Upgrade_Button.configure(text=f"Logitech Super Light Mouse (2 -> 4.5 DPS): [BOUGHT]")

		Logitech_Mouse_Upgrade_var = True




def Razor_Mouse_Worker():
	global Clicks
	global Worker_CPS
	global Razor_Mouse_Price
	global Razor_Mouse

	if Clicks >= Razor_Mouse_Price:
		Clicks -= Razor_Mouse_Price

		Clicks = round(Clicks, 1)
		click_label.configure(text=f"Clicks: {Clicks}")

		Razor_Mouse_Price *= 1.2
		Razor_Mouse_Price = round(Razor_Mouse_Price, 1)
		Razor_Mouse += 1

		Razor_Mouse_Worker_Button.configure(text=f"{Razor_Mouse_Name} ({Razor_Mouse_DPS} DPS): [{Razor_Mouse_Price} Clicks] - {Razor_Mouse}")

		Worker_CPS += Razor_Mouse_DPS
		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")




def Razor_Mouse_Worker_Upgrade():
	global Clicks
	global Worker_CPS
	global Razor_Mouse_Name
	global Razor_Mouse_DPS
	global Razor_Mouse_Worker_Upgrade_Button
	global Razor_Mouse_Upgrade_var

	if Clicks >= 12500 and Razor_Mouse_Upgrade_var != True:
		Clicks -= 12500

		click_label.configure(text=f"Clicks: {Clicks}")

		Old_Razor_Mouse_Placeholder = Razor_Mouse_DPS * Razor_Mouse
		Worker_CPS -= Old_Razor_Mouse_Placeholder

		Razor_Mouse_DPS = 12.5
		New_Razor_Mouse_Placeholder = Razor_Mouse_DPS * Razor_Mouse
		Worker_CPS += New_Razor_Mouse_Placeholder

		Razor_Mouse_Name = "Razor Viper Mouse"

		Razor_Mouse_Worker_Upgrade_Button.configure(text=f"Razor Viper Mouse (5 -> 12.5): [BOUGHT]")

		Razor_Mouse_Upgrade_var = True

	


def Autoclicker_Worker():
	global Clicks
	global Worker_CPS
	global Autoclicker_Price
	global Autoclicker

	if Clicks >= Autoclicker_Price:
		Clicks -= Autoclicker_Price

		Clicks = round(Clicks, 1)
		click_label.configure(text=f"Clicks: {Clicks}")

		Autoclicker_Price *= 1.2
		Autoclicker_Price = round(Autoclicker_Price, 1)
		Autoclicker += 1

		Autoclicker_Worker_Button.configure(text=f"{Autoclicker_Name} ({Autoclicker_DPS} DPS): [{Autoclicker_Price} Clicks] - {Autoclicker}")

		Worker_CPS += Autoclicker_DPS
		Worker_label.configure(text=f"Worker CPS: {Worker_CPS}")




def Autoclicker_Worker_Upgrade():
	global Clicks
	global Worker_CPS
	global Autoclicker_Name
	global Autoclicker_DPS
	global Autoclicker_Worker_Upgrade_Button
	global Autoclicker_Upgrade_var

	if Clicks >= 35000 and Autoclicker_Upgrade_var != True:
		Clicks -= 35000

		click_label.configure(text=f"Clicks: {Clicks}")

		Old_Autoclicker_Placeholder = Autoclicker_DPS * Autoclicker
		Worker_CPS -= Old_Autoclicker_Placeholder

		Autoclicker_DPS = 35
		New_Autoclicker_Placeholder = Autoclicker_DPS * Autoclicker
		Worker_CPS += New_Autoclicker_Placeholder

		Autoclicker_Name = "Semi-OP Autoclicker"

		Autoclicker_Worker_Upgrade_Button.configure(text=f"Semi-OP Autoclicker (15 -> 35 DPS): [BOUGHT]")

		Autoclicker_Upgrade_var = True




def Total_Stats():
	reset_stats_button.pack_forget()
	Settings_button.pack_forget()

	Clicks_label = tk.Label(root, text=f"Clicks: {Clicks}")
	Total_Clicks_label = tk.Label(root, text=f"Total Clicks: {Total_Clicks}")
	Worker_CPS_label = tk.Label(root, text=f"Worker CPS: {Worker_CPS}")

	I_Dont_wanna_finish_this = tk.Label(root, text=f"Times I wanna die: To big can't be rendered") # I don't want to finish this to be completely honest.




def Credits():
	settings_other_label.pack_forget()
	settings_save_label.pack_forget()
	reset_stats_button.pack_forget()
	Save_Button.pack_forget()
	Stats_Button.pack_forget()
	Contact_label.pack_forget()
	Developer_Console_Button.pack_forget()
	Credits_Button.pack_forget()

	Credits_Button.pack(side="bottom", anchor="ne")
	Credits_Button.configure(text="Close Credits", command=Settings)

	Credits_Developer_label.pack(side="top")
	Credits_Programmer_label.pack(side="top")
	Blank_label.pack(side="top")
	Credits_Idea_label.pack(side="top")
	Credits_Madewith_label.pack(side="top")





def Settings_Close():
	click_label.configure(text=f"Clicks: {Clicks}", bg="#4851e6")
	Shop_button.configure(text = "Enter Shop", command = Shop)
	click_button.configure(text = "Click me", borderwidth=0, bg="#4851d7", fg="#4851e6", activebackground = '#4851e6', activeforeground = '#4851e6', command=on_click, width=250, height=270, image=ButtonClick_Image)
	Settings_button.configure(text = "Settings", borderwidth=2, bg="white", fg="black", command=Settings)
	settings_other_label.pack_forget()
	settings_save_label.pack_forget()
	reset_stats_button.pack_forget()
	Save_Button.pack_forget()
	Stats_Button.pack_forget()
	Contact_label.pack_forget()
	Developer_Console_Button.pack_forget()
	Credits_Button.pack_forget()
	Credits_Developer_label.pack_forget()
	Credits_Idea_label.pack_forget()
	Credits_Madewith_label.pack_forget()
	Credits_Programmer_label.pack_forget()
	Credits_Button.pack_forget()
	Credits_Madewith_label.pack_forget()
	Blank_label.pack_forget()




def Settings():
	click_button.configure(text = " ", borderwidth=0, bg="#eacb1c", fg="#eacb1c", activebackground = '#eacb1c', activeforeground = '#eacb1c', width=1, height=1, image=ButtonClicker_Blue_Image)
	Shop_button.configure(text = "Enter Shop", command = Shop, borderwidth=3)
	Settings_button.configure(text = "Leave Settings", borderwidth=2, command=Settings_Close)
	Credits_Developer_label.pack_forget()
	Credits_Idea_label.pack_forget()
	Credits_Madewith_label.pack_forget()
	Credits_Programmer_label.pack_forget()
	Credits_Button.pack_forget()
	Credits_Madewith_label.pack_forget()
	Blank_label.pack_forget()

	settings_save_label.pack(side="top", anchor="nw")

	reset_stats_button.pack(side="top", anchor="nw", pady=5, padx=5)
	Save_Button.pack(side="top", anchor="nw", pady=3, padx=5)

	settings_other_label.pack(side="top", anchor="nw", pady=10)

	Credits_Button.pack(side="top", anchor="nw", pady=3, padx=5)
	Credits_Button.configure(text="Game Credits", command=Credits)


	Contact_label.pack(side="bottom", anchor="nw")
	Developer_Console_Button.pack(side="bottom", anchor="nw")





def leave_Shop():

	root['background']='#4851e6'

	click_label.configure(text=f"Clicks: {Clicks}", bg="#4851e6")
	Shop_button.configure(text = "Enter Shop", command = Shop)
	click_button.configure(text = "Click me", borderwidth=0, bg="#4851d7", fg="#4851e6", activebackground = '#4851e6', activeforeground = '#4851e6', command=on_click, width=250, height=270, image=ButtonClick_Image)
	Settings_button.pack(anchor="ne", side="bottom", padx=5, pady=5)
	Settings_button.configure(text = "Settings", borderwidth=2, bg="white", fg="black", command=Settings)
	Worker_label.configure(bg="#4851e6")


	Shop_DoubleClick_Button.pack_forget()
	Shop_TripleClick_Button.pack_forget()
	Shop_QuintupleClick_Button.pack_forget()

	Shop_ClickUpgrade_Label.pack_forget()

	Unpaid_Intern_Worker_Button.pack_forget()
	Unpaid_Intern_Worker_Upgrade_Button.pack_forget()
	Logitech_Mouse_Worker_Button.pack_forget()
	Logitech_Mouse_Worker_Upgrade_Button.pack_forget()
	Razor_Mouse_Worker_Button.pack_forget()
	Razor_Mouse_Worker_Upgrade_Button.pack_forget()
	Autoclicker_Worker_Button.pack_forget()
	Autoclicker_Worker_Upgrade_Button.pack_forget()

	Shop_Page_2_Button.pack_forget()
	Shop_Page_3_Button.pack_forget()
	Previous_Shop_Page_2_Button.pack_forget()
	Previous_Shop_Page_3_Button.pack_forget()

	Shop_Worker_Upgrade_label.pack_forget()
	Shop_Worker_label.pack_forget()





def Shop_Page_3():
	Shop_Worker_label.pack_forget()
	Previous_Shop_Page_2_Button.pack_forget()
	Shop_Page_3_Button.pack_forget()
	Shop_Worker_Upgrade_label.pack_forget()

	Unpaid_Intern_Worker_Upgrade_Button.pack_forget()
	Logitech_Mouse_Worker_Upgrade_Button.pack_forget()


	Razor_Mouse_Worker_Button.pack_forget()
	Autoclicker_Worker_Button.pack_forget()
	reset_stats_button.pqack_forget()


	if Razor_Mouse_Upgrade_var == True:
		global Razor_Mouse_Worker_Upgrade_Button

		Razor_Mouse_Worker_Upgrade_Button = tk.Button(root, text="Razor Viper Mouse (5 -> 12.5 DPS): [BOUGHT]")

		Razor_Mouse_Worker_Upgrade_Button.pack_forget()
		Razor_Mouse_Worker_Upgrade_Button.configure(text="Razor Viper Mouse (5 -> 12.5 DPS): [BOUGHT]")


	if Autoclicker_Upgrade_var == True:
		global Autoclicker_Worker_Upgrade_Button

		Autoclicker_Worker_Upgrade_Button = tk.Button(root, text=f"Semi-OP Autoclicker (15 -> 35 DPS): [BOUGHT]")

		Autoclicker_Worker_Upgrade_Button.pack_forget()
		Autoclicker_Worker_Upgrade_Button.configure(text=f"Semi-OP Autoclicker (15 -> 35 DPS): [BOUGHT]")


	Shop_Worker_Upgrade_label.pack(side="top", anchor="nw", pady=0, padx=5)

	Razor_Mouse_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)
	Autoclicker_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)

	Previous_Shop_Page_3_Button.pack(side="bottom", anchor="ne")



def Shop_Page_2():

	Shop_DoubleClick_Button.pack_forget()
	Shop_TripleClick_Button.pack_forget()
	Shop_QuintupleClick_Button.pack_forget()

	Shop_ClickUpgrade_Label.pack_forget()
	Shop_Worker_label.pack_forget()
	Shop_Worker_Upgrade_label.pack_forget()
	
	Unpaid_Intern_Worker_Button.pack_forget()
	Logitech_Mouse_Worker_Button.pack_forget()
	Razor_Mouse_Worker_Button.pack_forget()
	Autoclicker_Worker_Button.pack_forget()

	Previous_Shop_Page_3_Button.pack_forget()	
	Shop_Page_2_Button.pack_forget()
	Shop_Page_3_Button.pack_forget()

	# Yeah, that's a lot of pack_forget()...

	if Unpaid_Intern_Upgrade_var == True:
		global Unpaid_Intern_Worker_Upgrade_Button	

		Unpaid_Intern_Worker_Upgrade_Button = tk.Button(root, text=f"Slightly Paid Intern (0.5 -> 1 DPS): [BOUGHT]", command=Unpaid_Intern_Worker_Upgrade)

		Unpaid_Intern_Worker_Upgrade_Button.pack_forget()
		Unpaid_Intern_Worker_Upgrade_Button.configure(text=f"Slightly Paid Intern (0.5 -> 1 DPS): [BOUGHT]")
	else:
		Unpaid_Intern_Worker_Upgrade_Button.pack_forget()


	if Logitech_Mouse_Upgrade_var == True:
		global Logitech_Mouse_Worker_Upgrade_Button

		Logitech_Mouse_Worker_Upgrade_Button = tk.Button(root, text=f"Logitech Super Light Mouse (2 -> 4.5 DPS): [BOUGHT]", command = Logitech_Mouse_Worker_Upgrade)

		Logitech_Mouse_Worker_Upgrade_Button.pack_forget()
		Logitech_Mouse_Worker_Upgrade_Button.configure(text=f"Logitech Super Light Mouse (2 -> 4.5 DPS): [BOUGHT]")

	
	if Razor_Mouse_Upgrade_var == True:
		global Razor_Mouse_Worker_Upgrade_Button

		Razor_Mouse_Worker_Upgrade_Button = tk.Button(root, text="Razor Viper Mouse (5 -> 12.5 DPS): [BOUGHT]")

		Razor_Mouse_Worker_Upgrade_Button.pack_forget()
		Razor_Mouse_Worker_Upgrade_Button.configure(text="Razor Viper Mouse (5 -> 12.5 DPS): [BOUGHT]")


	if Autoclicker_Upgrade_var == True:
		global Autoclicker_Worker_Upgrade_Button

		Autoclicker_Worker_Upgrade_Button = tk.Button(root, text=f"Semi-OP Autoclicker (15 -> 35 DPS): [BOUGHT]")

		Autoclicker_Worker_Upgrade_Button.pack_forget()
		Autoclicker_Worker_Upgrade_Button.configure(text=f"Semi-OP Autoclicker (15 -> 35 DPS): [BOUGHT]")


	Previous_Shop_Page_2_Button.pack(side="bottom", anchor="ne")

	Shop_Worker_Upgrade_label.pack(side="top", anchor="nw", pady=10, padx=5)

	Unpaid_Intern_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)
	Logitech_Mouse_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)
	Razor_Mouse_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)
	Autoclicker_Worker_Upgrade_Button.pack(side="top", anchor="nw", padx=3, pady=3)




def Shop():

	reset_stats_button.pack_forget()
	Developer_Console_Button.pack_forget()
	Settings_button.pack_forget()

	Shop_Worker_label.pack_forget()
	Previous_Shop_Page_2_Button.pack_forget()
	Shop_Page_3_Button.pack_forget()
	Shop_Worker_Upgrade_label.pack_forget()

	Unpaid_Intern_Worker_Upgrade_Button.pack_forget()
	Logitech_Mouse_Worker_Upgrade_Button.pack_forget()
	Razor_Mouse_Worker_Upgrade_Button.pack_forget()
	Autoclicker_Worker_Upgrade_Button.pack_forget()

	Razor_Mouse_Worker_Button.pack_forget()
	Autoclicker_Worker_Button.pack_forget()

	settings_other_label.pack_forget()
	settings_save_label.pack_forget()
	reset_stats_button.pack_forget()
	Save_Button.pack_forget()
	Stats_Button.pack_forget()
	Contact_label.pack_forget()
	Developer_Console_Button.pack_forget()
	Credits_Button.pack_forget()

	Credits_Developer_label.pack_forget()
	Credits_Idea_label.pack_forget()
	Credits_Madewith_label.pack_forget()
	Credits_Programmer_label.pack_forget()
	Credits_Button.pack_forget()
	Credits_Madewith_label.pack_forget()
	Blank_label.pack_forget()

	root['background']='#eacb1c'

	click_label.configure(text =f"Clicks: {Clicks}", bg="#eacb1c")
	click_button.configure(text = " ", borderwidth=0, bg="#eacb1c", fg="#eacb1c", activebackground = '#eacb1c', activeforeground = '#eacb1c', width=1, height=1, image=ButtonClicker_Yellow_Image)
	Shop_button.configure(text = "Leave Shop", command = leave_Shop, borderwidth=3)
	Worker_label.configure(bg="#eacb1c")
 

	if Double_Click_Upgrade == True:
		global Shop_DoubleClick_Button 

		Shop_DoubleClick_Button = tk.Button(root, text="Double Click: [BOUGHT]", command=Double_Click_Upgrade_Item) 

		Shop_DoubleClick_Button.pack_forget()
		Shop_DoubleClick_Button.configure(text="Double Click: [BOUGHT]")

	else:
		Shop_DoubleClick_Button.pack_forget()


	if Triple_Click_Upgrade == True:
		global Shop_TripleClick_Button

		Shop_TripleClick_Button = tk.Button(root, text="Triple Click: [BOUGHT]", command=Triple_Click_Upgrade_Item)

		Shop_TripleClick_Button.pack_forget()
		Shop_TripleClick_Button.configure(text="Triple Click: [BOUGHT]")
	else:
		Shop_TripleClick_Button.pack_forget()


	if Quintuple_Click_Upgrade == True:
		global Shop_QuintupleClick_Button

		Shop_QuintupleClick_Button = tk.Button(root, text="Quintuple Click: [BOUGHT]", command=Quintuple_Click_Upgrade_Item)

		Shop_QuintupleClick_Button.pack_forget()
		Shop_QuintupleClick_Button.configure(text="Quintuple Click: [BOUGHT]")
	else:
		Shop_QuintupleClick_Button.pack_forget()


	Shop_ClickUpgrade_Label.pack(side="top", anchor="nw", pady=0, padx=5)

	Shop_DoubleClick_Button.pack(side="top", anchor="nw", pady=3, padx=5)
	Shop_TripleClick_Button.pack(side="top", anchor="nw", pady=3, padx=5)
	Shop_QuintupleClick_Button.pack(side="top", anchor="nw", pady=3, padx=5)

	Shop_Worker_label.pack(side="top", anchor="nw", pady=10, padx=5)

	Unpaid_Intern_Worker_Button.pack(side="top", anchor="nw", pady=0, padx=5)
	Unpaid_Intern_Worker_Button.configure(text=f"{Unpaid_Intern_Name} ({Unpaid_Intern_DPS} DPS): [{Unpaid_Intern_Price} Clicks] - {Unpaid_Intern}")

	Logitech_Mouse_Worker_Button.pack(side="top", anchor="nw", pady=3, padx=5)
	Logitech_Mouse_Worker_Button.configure(text=f"{Logitech_Mouse_Name} ({Logitech_Mouse_DPS} DPS): [{Logitech_Mouse_Price} Clicks] - {Logitech_Mouse}")

	Razor_Mouse_Worker_Button.pack(side="top", anchor="nw", padx=5, pady=3)
	Razor_Mouse_Worker_Button.configure(text=f"{Razor_Mouse_Name} ({Razor_Mouse_DPS} DPS): [{Razor_Mouse_Price} Clicks] - {Razor_Mouse}")

	Autoclicker_Worker_Button.pack(side="top", anchor="nw", padx=5, pady=3)
	Autoclicker_Worker_Button.configure(text=f"{Autoclicker_Name} ({Autoclicker_DPS} DPS): [{Autoclicker_Price} Clicks] - {Autoclicker}")
	


	Shop_Page_2_Button.pack(side="bottom", anchor="ne")




if __name__ == "__main__":

	root.title("Average Clicker Game [v2.2.0]")
	root.geometry("395x395")
	root.resizable(False, False)
	root.iconbitmap(resource_path('Assets/icon.ico'))
	root['background']='#4851e6'



	# Shop Upgrades
	Shop_DoubleClick_Button = tk.Button(root, text="Double Click [75 Clicks]", command=Double_Click_Upgrade_Item)
	Shop_TripleClick_Button = tk.Button(root, text="Triple Click: [225 Clicks]", command=Triple_Click_Upgrade_Item)
	Shop_QuintupleClick_Button = tk.Button(root, text="Quintuple Click: [1000 Clicks]", command=Quintuple_Click_Upgrade_Item)


	# Shop Workers
	Unpaid_Intern_Worker_Button = tk.Button(root, text=f"{Unpaid_Intern_Name} ({Unpaid_Intern_DPS} DPS): [{Unpaid_Intern_Price} Clicks] - {Unpaid_Intern}", command=Unpaid_Intern_Worker)
	Logitech_Mouse_Worker_Button = tk.Button(root, text=f"{Logitech_Mouse_Name} ({Logitech_Mouse_DPS} DPS): [{Logitech_Mouse_Price} Clicks] - {Logitech_Mouse}", command=Logitech_Mouse_Worker)
	Razor_Mouse_Worker_Button = tk.Button(root, text=f"{Razor_Mouse_Name} ({Razor_Mouse_DPS} DPS): [{Razor_Mouse_Price} Clicks] - {Razor_Mouse}", command=Razor_Mouse_Worker)
	Autoclicker_Worker_Button = tk.Button(root, text=f"{Autoclicker_Name} ({Autoclicker_DPS} DPS): [{Autoclicker_Price} Clicks] - {Autoclicker}", command=Autoclicker_Worker)

	# Shop Worker Upgrades
	Unpaid_Intern_Worker_Upgrade_Button = tk.Button(root, text=f"Slightly Paid Intern (0.5 -> 1 DPS): [750 Clicks]", command=Unpaid_Intern_Worker_Upgrade)
	Logitech_Mouse_Worker_Upgrade_Button = tk.Button(root, text=f"Logitech Super Light Mouse (2 -> 4.5 DPS): [3500 Clicks]", command=Logitech_Mouse_Worker_Upgrade)
	Razor_Mouse_Worker_Upgrade_Button = tk.Button(root, text=f"Razor Viper Mouse (5 -> 12.5 DPS): [12500 Clicks]", command=Razor_Mouse_Worker_Upgrade)
	Autoclicker_Worker_Upgrade_Button = tk.Button(root, text=f"Semi-OP Autoclicker (15 -> 35 DPS): [35000 Clicks]", command=Autoclicker_Worker_Upgrade)
	
	
	# Shop Labels
	Shop_ClickUpgrade_Label = tk.Label(root, text="Clicker Upgrades: ", bg="#eacb1c", font=("Helvetica",10))
	Shop_Worker_label = tk.Label(root, text="Workers:", bg="#eacb1c", font=("Helvetica",10))
	Shop_Worker_Upgrade_label = tk.Label(root, text="Worker Upgrades:", bg="#eacb1c", font=("Helvetica",10))


	# Shop Page Buttons
	Shop_Page_2_Button = tk.Button(root, text="Page 2 ->", font=("Helvetica",10), command=Shop_Page_2)
	Shop_Page_3_Button = tk.Button(root, text="Page 3 ->", font=("Helvetica",10), command=Shop_Page_3)
	Previous_Shop_Page_2_Button = tk.Button(root, text="<- Page 1", font=("Helvetica",10), command=Shop)
	Previous_Shop_Page_3_Button = tk.Button(root, text="<- Page 2", font=("Helvetica",10), command=Shop_Page_2)


	# Settings 
	settings_save_label = tk.Label(root, text="Settings Save Features: ", bg="#4851e6")
	settings_other_label = tk.Label(root, text="Settings Other Features: ", bg="#4851e6")

	reset_stats_button = tk.Button(root, text="Reset Stats", bg="red", fg="Black", activebackground="red", activeforeground="black", command=Reset_Stats)
	Stats_Button = tk.Button(root, text=f"Total Stats", command=Total_Stats)	
	Save_Button = tk.Button(root, text="Save Game Stats", command=save_system)
	Credits_Button = tk.Button(root, text="Game Credits", command=Credits)

	# Credits Labels
	Credits_Programmer_label = tk.Label(root, text="Programmer: Zacky2613", bg="#4851e6")
	Credits_Developer_label = tk.Label(root, text="Developer: Zacky2613", bg="#4851e6")
	Credits_Madewith_label = tk.Label(root, text="Made with: Python tkinter", bg="#4851e6")
	Credits_Idea_label = tk.Label(root, text="Ideas: Zacky2613, Will", bg="#4851e6")



	# ClickButton Images
	ButtonClick_Image = PhotoImage(file = resource_path('Assets/ClickButton.png'))
	ButtonClicker_Blue_Image = PhotoImage(file = resource_path("Assets/ClickButton_Blue.png"))
	ButtonClicker_Yellow_Image = PhotoImage(file = resource_path("Assets/ClickButton_Yellow.png"))

	# Other
	Blank_label = tk.Label(root, text=" ", bg="#4851e6")

	# KEY GAME VARIABLES (DO NOT TOUCH)

	# Clicks Counter
	click_label = tk.Label(root, text=f"Clicks: {Clicks}", fg="black", bg="#4851e6", font=("Helvetica",10))
	click_label.pack(anchor="sw", side="bottom")

	# Worker DPS
	Worker_label = tk.Label(root, text=f"Worker CPS: {Worker_CPS}", fg="black", bg="#4851e6", font=("Helvetica",10))
	Worker_label.pack(anchor="sw", side="top")
	
	# Shop
	Shop_button = tk.Button(root, text="Enter Shop", command=Shop)
	Shop_button.pack(anchor="ne", side="top", padx=5, pady=5)

	# Settings
	Settings_button = tk.Button(root, text="Settings", command=Settings)
	Settings_button.pack(anchor="ne", side="bottom", padx=5, pady=5)

	# ClickButton
	click_button = tk.Button(root, text="click me", width=1100, height=1200, borderwidth=0, command=on_click, bg="#4851d7", fg="#4851e6", activebackground = '#4851e6', activeforeground = '#4851e6', image = ButtonClick_Image) 
	click_button.pack(anchor = "center")

	# Developer Console
	Developer_Console_Button = tk.Button(root, text="    ", bg="#4851e6", fg="#4851e6", activebackground = '#4851e6', activeforeground = '#4851e6', borderwidth=0, command=Developer_Console)

	# Contact Label
	Contact_label = tk.Label(root, text="Report bugs: [REDACTED]@gmail.com", bg="#4851e6", font=("Helvetica",10))

	Worker_func()


def close(bind): 
	root.destroy()

root.protocol("WM_DELETE_WINDOW", save_system)
root.bind("<Escape>", close)
root.mainloop()
