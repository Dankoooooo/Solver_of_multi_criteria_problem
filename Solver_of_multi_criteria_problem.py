import numpy as np
from math import fabs
import matplotlib.pyplot as plt
import cProfile
from memory_profiler import profile
import pandas as pd
import time


import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image

root = None
photo = None

class MainWindow:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1024x720")
        self.root.title("Solver of multi-criteria problems")
        self.photo = None
        self.main_menu()

    def main_menu(self):
        main_frame = ctk.CTkFrame(master=self.root, fg_color='#DCF2F1')
        main_frame.pack(padx=0, pady=0, fill="both", expand=True)

        self.menu_template(main_frame)
        self.root.mainloop()

    def logo_template(self, parent_frame):
        logo_frame = ctk.CTkFrame(master=parent_frame,height=150, fg_color='#7FC7D9')
        logo_frame.pack(fill="both")
        logo_label = ctk.CTkLabel(logo_frame, fg_color='#365486', width=700, height=60, corner_radius=56 )
        logo_label.place(relx=0.4, rely=0.5, anchor="center")
        logo_label_text = ctk.CTkLabel(logo_label, text="Solver of multi-criteria problems", text_color='#DCF2F1', width=350, height=50, corner_radius=56, font=("Inter",24) )
        logo_label_text.place(relx=0.65, rely=0.5, anchor="center")
        logo_label_place = ctk.CTkLabel(logo_frame, text="Place for logo", fg_color='#0F1035', text_color='#DCF2F1', width=140, height=120, corner_radius=20, font=("Inter",24) )
        logo_label_place.place(relx=0.115, rely=0.5, anchor="center")
        
        image = Image.open("img/bg_img_1.png")
        image = image.resize((1440, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        label = tk.Label(parent_frame, image=self.photo, borderwidth=0)
        label.image = self.photo
        label.place(relx=0,rely=0.79)

    def menu_template(self, parent_frame):
        self.logo_template(parent_frame)
        main_menu_label = ctk.CTkLabel(parent_frame, text="Main menu", fg_color='#365486', text_color='#DCF2F1', width=200, height=60, corner_radius=10, font=("Inter",28) )
        main_menu_label.place(relx=0.5, rely=0.26, anchor="center")

        line_frame = ctk.CTkFrame(master=parent_frame, width=1440, height=2, fg_color='#7FC7D9')
        line_frame.pack(padx=0,pady=75,fill="both")

        buttons_frame = ctk.CTkFrame(master=parent_frame,height=300, fg_color='#DCF2F1')
        buttons_frame.place(relx=0.5,rely=0.56,anchor="center")

        create_problem_button = ctk.CTkButton(buttons_frame, text="Create problem", fg_color='#0F1035', text_color='#DCF2F1', width=180, height=45, corner_radius=10, font=("Inter",18), command=self.open_create_problem_window)
        create_problem_button.place(relx=0.5,rely=0.1,anchor="center")

        results_button = ctk.CTkButton(buttons_frame, text="Results", fg_color='#0F1035', text_color='#DCF2F1', width=180, height=45, corner_radius=10, font=("Inter",18), command=self.show_results)
        results_button.place(relx=0.5,rely=0.3,anchor="center")

        reports_button = ctk.CTkButton(buttons_frame, text="Reports", fg_color='#0F1035', text_color='#DCF2F1', width=180, height=45, corner_radius=10, font=("Inter",18), command=self.show_reports)
        reports_button.place(relx=0.5,rely=0.5,anchor="center")

        exit_button = ctk.CTkButton(buttons_frame, text="Exit", fg_color='#0F1035', text_color='#DCF2F1', width=180, height=45, corner_radius=10, font=("Inter",18), command=self.exit_program)
        exit_button.place(relx=0.5,rely=0.7,anchor="center")

    def open_create_problem_window(self):
        root_create_problem = ctk.CTkToplevel(self.root)
        root_create_problem.geometry("1024x720")
        root_create_problem.title("Create problem")

        root_create_problem.lift()
        root_create_problem.attributes('-topmost', True)
        create_problem_frame = ctk.CTkFrame(master=root_create_problem,width=1024,height=720, fg_color='#FFFFFF')
        create_problem_frame.pack(padx=0, pady=0, fill="both", expand=True)
        self.logo_template(create_problem_frame)


        main_leftside_frame = ctk.CTkFrame(master=create_problem_frame,width=480,height=450,fg_color='#D9D9D9')
        main_leftside_frame.place(relx=0.25, rely=0.525, anchor="center")
        main_rightside_frame = ctk.CTkFrame(master=create_problem_frame,width=480,height=450,fg_color='#D9D9D9')
        main_rightside_frame.place(relx=0.75, rely=0.525, anchor="center")

        leftside_frame = ctk.CTkFrame(master=main_leftside_frame,width=512,height=30,fg_color='#DCF2F1')
        leftside_frame.place(relx=0.5, rely=0.025, anchor="center")
        line_frame = ctk.CTkFrame(master=leftside_frame, width=480, height=2, fg_color='#7FC7D9')
        line_frame.place(relx=0.5, rely=0.5, anchor="center")
        logo_label_text = ctk.CTkLabel(master=leftside_frame, text="Objective functions to be optimized",fg_color="#DCF2F1", text_color='#0F1035', width=250, height=16, font=("Inter",14) )
        logo_label_text.place(relx=0.5, rely=0.5, anchor="center")


        rightside_frame = ctk.CTkFrame(master=main_rightside_frame,width=512,height=30,fg_color='#DCF2F1')
        rightside_frame.place(relx = 0.5, rely = 0.025,anchor="center")
        line_frame = ctk.CTkFrame(master=rightside_frame, width=480, height=2, fg_color='#7FC7D9')
        line_frame.place(relx=0.5, rely=0.5, anchor="center")
        logo_label_text = ctk.CTkLabel(master=rightside_frame, text="Created problem",fg_color="#DCF2F1", text_color='#0F1035', width=150, height=16, font=("Inter",14) )
        logo_label_text.place(relx=0.5, rely=0.5, anchor="center")

        scrollable_frame = ctk.CTkScrollableFrame(main_leftside_frame, width=450,height=100,fg_color="#FFFFFF")
        scrollable_frame.place(relx=0.5, rely=0.3, anchor="center")

        objective_directions = ["Max", "Min"]
        add_button_frame = ctk.CTkFrame(main_leftside_frame,  width=450,height=10,fg_color="#0F1035")
        add_button_frame.place(relx = 0.5, rely = 0.58,anchor="center")

        def add_row():
            str = ctk.CTkFrame(scrollable_frame, width=440, height=30,fg_color="#FFFFFF")
            str.pack(padx=0)

            options = ctk.CTkOptionMenu(str, values=objective_directions, width=60,height=30, font=("Inter",14), fg_color="#DCF2F1",text_color="#0F1035")
            options.pack(padx=2, pady=2, side="left")
            func_input = ctk.CTkEntry(str, placeholder_text="Function",width=100,height=30,font=("Inter",14),placeholder_text_color="#7FC7D9",text_color="#0F1035",fg_color="#FFFFFF")
            func_input.pack(padx=2, pady=2, side="left")
            exp_input = ctk.CTkEntry(str, placeholder_text="Expression",width=260,height=30,font=("Inter",14),placeholder_text_color="#7FC7D9",text_color="#0F1035",fg_color="#FFFFFF")
            exp_input.pack(padx=2, pady=2, side="left")

        
        add_button = ctk.CTkButton(add_button_frame, text="Add function",height=10,width=30, command=add_row)
        add_button.pack(padx=2, pady=2, side="left")


        # cons_scrollable_frame = ctk.CTkScrollableFrame(main_leftside_frame,width=450,height=50, fg_color="#FFFFFF")
        # cons_scrollable_frame.place(relx=0.5, rely=0.8, anchor="center")

        # scrollable_result_frame = ctk.CTkScrollableFrame(main_rightside_frame, width=450, fg_color="#FFFFFF")
        # scrollable_result_frame.place(relx=0.5, rely=0.3, anchor="center")

        
    def show_reports(self):
        print("Reports were shown")

    def show_results(self):
        print("Results were shown")

    def exit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    window = MainWindow()
    window.main_menu()


