import tkinter as tk

class testing():
    def __init__(self):
        self.booking_tool()
        
        
    def booking_tool(self):
        self.tool_root = tk.Tk()
        self.tool_root.wm_title("SquashBookah300000")
        
        main_tool_frame = tk.Frame(self.tool_root)
        main_tool_frame.grid()
        main_tool_frame.configure(bg = '#fffca2')
                                  
        title_label = tk.Label(main_tool_frame, text = "  Da great SHUASHbookah 300000")
        title_label.grid(row = 1, column = 1, columnspan = 4, ipadx = 1)
        title_label.configure(font = '14', bg = '#fffca2')

        line_label = tk.Label(main_tool_frame, text = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        line_label.grid(row = 2, column = 1, columnspan = 5)
        line_label.configure(fg = 'gray', bg = '#fffca2')
        line_label.configure(bg = '#fffca2')

        info_label = tk.Label(main_tool_frame, text = "Velg når du ønsker å booke bane:")
        info_label.grid(row = 3, column = 1, ipadx = 1, columnspan = 4)
        info_label.configure(font = '12', bg = '#fffca2')

        date_label = tk.Label(main_tool_frame, text = "Velg dato: ")
        date_label.grid(row = 4, column = 1, ipadx = 1, columnspan = 1)
        date_label.configure(bg = '#fffca2')

        time_label = tk.Label(main_tool_frame, text = "Velg tid: Max 2 timer")
        time_label.grid(row = 4, column = 2, ipadx = 1)
        time_label.configure(bg = '#fffca2')
        
        track_label = tk.Label(main_tool_frame, text = "Velg bane:")
        track_label.grid(row = 4, column = 3, ipadx = 1)
        track_label.configure(bg = '#fffca2')
        
        self.date_entry = tk.Entry(main_tool_frame, justify = "center")
        self.date_entry.grid(row = 5, column = 1, padx = 2, pady = 2)
        self.date_entry.insert(3, "19.12.2020")

        
        self.from_time_entry = tk.Entry(main_tool_frame, justify = "center")
        self.from_time_entry.grid(row = 5, column = 2, padx = 4, pady = 2)
        self.from_time_entry.insert(3, "00:00")
        
        self.to_time_entry = tk.Entry(main_tool_frame, justify = "center")
        self.to_time_entry.grid(row = 6, column = 2, padx = 4, pady = 2)
        self.to_time_entry.insert(3, "00:00")
        
        self.track_entry = tk.Entry(main_tool_frame, justify = "center")
        self.track_entry.grid(row = 5, column = 3, padx = 4, pady = 2)
        self.track_entry.insert(3,"1-3")
        
        time_info_label = tk.Label(main_tool_frame, text = "Accepted times for booking end in :00 or :30")
        time_info_label.grid(row = 7, column = 1, columnspan = 3, ipadx = 1)
        time_info_label.configure(bg = '#fffca2')
        
        line_label2 = tk.Label(main_tool_frame, text = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        line_label2.grid(row = 8, column = 1, columnspan = 3)
        line_label2.configure(fg = 'gray', bg = '#fffca2')
        line_label2.configure(bg = '#fffca2')
        
        login_frame = tk.Frame(main_tool_frame, bd = 2)
        login_frame.grid(row = 9, column = 1, columnspan = 3, sticky = "NSEW")
        login_frame.configure(bg = '#fffca2')
                              
        username_label = tk.Label(login_frame, text = "Username:")
        username_label.grid(row = 0, column = 0)
        username_label.configure(bg = '#fffca2')
                            
        self.username_entry = tk.Entry(login_frame, justify = "center")
        self.username_entry.grid(row = 0, column = 1)

        password_label = tk.Label(login_frame, text = "Password:")
        password_label.grid(row = 0, column = 2)
        password_label.configure(bg = '#fffca2')

        self.password_entry = tk.Entry(login_frame, justify = "center", show ='●')
        self.password_entry.grid(row = 0, column = 3)

        button_frame = tk.Frame(main_tool_frame)
        button_frame.grid(row = 11, column = 1, columnspan = 3, sticky = "NSEW", padx = '100', pady = '5')
        button_frame.configure(bg = '#fffca2')

        self.make_booking_button = tk.Button(button_frame, text = "Make booking", font=(11))
        self.make_booking_button.grid(row = 0, column = 1, columnspan = 1, padx = '10')
        self.cancel_booking_button = tk.Button(button_frame, text = "Cancel", font=(11))
        self.cancel_booking_button.grid(row = 0, column = 2, columnspan = 1, padx = '10')
    
        self.error_display = tk.Label(main_tool_frame, text = "", justify = "center")
        self.error_display.grid(row = 10, column = 1, columnspan = 3)
   
        self.tool_root.mainloop()
        
        
testing()