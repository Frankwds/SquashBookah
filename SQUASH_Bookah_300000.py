#The goal must be to upload a functioning program on folk.ntnu that anyone can use.
# TODO Make sure to store future bookings in an .xml file or something. Check with this whenever ThaGreatSquashBookah300000 is opened, and possibly start the clock again, in case of some reboot or smth.
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk

class squashbookah30000():
    def __init__(self):
        self.booking_tool()
        
        
    def login_navigate(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.sit.no/")
        self.driver.set_window_size(1100, 800)
        self.driver.find_element(By.CSS_SELECTOR, ".content > #loginbutton > span").click()
        self.driver.find_element(By.ID, "loginbBtnClick").click()
        self.driver.find_element(By.ID, "edit-name").send_keys(("{}".format(self.username)))
        self.driver.find_element(By.ID, "edit-pass").send_keys(("{}".format(self.password)))
        self.driver.find_element(By.ID, "edit-submit--4").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Trening").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Book treningstid").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Squash").click()
        time.sleep(4)
        self.driver.switch_to.frame(0)

    def booking_tool(self):
        self.tool_root = tk.Tk()
        self.tool_root.wm_title("SquashBookah300000")
        self.datetime_today = datetime.datetime.today()
        
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
        self.date_entry.insert(3, "{}.01.2021".format((self.datetime_today.day)+2))

        
        self.from_time_entry = tk.Entry(main_tool_frame, justify = "center")
        self.from_time_entry.grid(row = 5, column = 2, padx = 4, pady = 2)
        self.from_time_entry.insert(3, "13:30")
        
        self.to_time_entry = tk.Entry(main_tool_frame, justify = "center")
        self.to_time_entry.grid(row = 6, column = 2, padx = 4, pady = 2)
        self.to_time_entry.insert(3, "14:30")
        
        self.track_entry = tk.Entry(main_tool_frame, justify = "center")
        self.track_entry.grid(row = 5, column = 3, padx = 4, pady = 2)
        self.track_entry.insert(3,"1")
        
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
        self.username_entry.insert(3,"frankwd@stud.ntnu.no")
        
        password_label = tk.Label(login_frame, text = "Password:")
        password_label.grid(row = 0, column = 2)
        password_label.configure(bg = '#fffca2')

        self.password_entry = tk.Entry(login_frame, justify = "center", show ='●')
        self.password_entry.grid(row = 0, column = 3)
        self.password_entry.insert(3,"Hqd59ev55283")

        button_frame = tk.Frame(main_tool_frame)
        button_frame.grid(row = 111, column = 1, columnspan = 3, sticky = "NSEW", padx = 60, pady = '5')
        button_frame.configure(bg = '#fffca2')

        self.make_booking_button = tk.Button(button_frame, text = "Make bookah", font=(11), command = self.make_bookah)
        self.make_booking_button.grid(row = 0, column = 1, columnspan = 1, padx = '10')
        
        self.cancel_booking_button = tk.Button(button_frame, text = "Cancel", font=(11), command = self.quit_bookah)
        self.cancel_booking_button.grid(row = 0, column = 2, columnspan = 1, padx = 10, ipadx = 20)
    
        self.error_display = tk.Label(main_tool_frame, text = "", justify = "center")
        self.error_display.grid(row = 10, column = 1, columnspan = 3)
        self.error_display.configure(bg = '#fffca2')
    
        self.tool_root.mainloop()


    def quit_bookah(self):
        self.tool_root.destroy()

    def make_bookah(self):
        
        self.get_entry_info()
        error_free = self.check_entries() #Check booking form for errors.
        
        while error_free == True:
            
            error_free = self.time_to_row()
            if error_free == False:
                break
            self.tool_root.destroy()
            self.calculate_wait_time()
            self.wait()
            break #Temporary break, just a kaffekok
##            self.login_navigate()
#            try:
#                    
#                self.book_squash()
#                
#                self.unbook_squash()
#                break
#                # TODO Open window for user, saying booking is succsessfull
#            except:
#                pass
#                # TODO Open window with error message for user, for eksample "time is allready booked"
            
    def calculate_wait_time(self):
        day_delta = self.datetime_bookah_date.day - self.datetime_today.day
        
        if day_delta > 2 or (day_delta == 2 and self.datetime_today.hour < 21): # if booking is two days from now, or more. And you can't just book right away because booking opens at 21:00.
            nine_O_clock_two_days_before_bookah = datetime.datetime(self.datetime_bookah_date.year, self.datetime_bookah_date.month, self.datetime_bookah_date.day-2, 20, 59)
            self.wait_time = nine_O_clock_two_days_before_bookah - self.datetime_today
            print(type(self.wait_time), self.wait_time)
        
        elif day_delta < 2 or (day_delta == 2 and self.datetime_today.hour >= 21):
            self.wait_time = self.datetime_today - self.datetime_today
            print(type(self.wait_time), (self.wait_time))
            
        
    
    
    def wait(self):
        pass
        #wait for self.wait_time seconds, find som way to idle for the given time. THEN execute from the dark, like a great squashbookah300000
        
        
        
        
        
        
#        if booking_date == tomorrow:
#            pass # Book immediately
#        else:
#            idle_days = booked_date - this_date
#            idle_time = 19_oclock - this_time
#            idle_for = idle_days + idle_time
#            
#            self.idle()
        
    def get_entry_info(self):
        
        self.date = self.date_entry.get()
        self.from_time = self.from_time_entry.get()
        self.to_time = self.to_time_entry.get()
        self.track = self.track_entry.get()
        self.username = self.username_entry.get()
        self.password  = self.password_entry.get()

    def check_entries(self):
        
        
        try: # Everything date
            self.datetime_bookah_date = datetime.datetime.strptime(self.date, "%d.%m.%Y") #Yeah, not being used my ass.
                                 # IF an exception occurs here the date entry is False.
            if self.datetime_bookah_date <= self.datetime_today:
                self.error_display.configure(text = "You cannot make a booking today or in the past.")
                return False
        except ValueError:
            self.error_display.configure(text = "The correct date format is DD.MM.YYYY")
            return False
            
        
        try: # Everything time
            to_time = datetime.datetime.strptime(self.to_time, "%H:%M")
            from_time = datetime.datetime.strptime(self.from_time, "%H:%M")
            if from_time.minute != 30 and from_time.minute != 0:
                self.error_display.configure(text = "You cannot book from this time. Correct time format is HH:00 or HH:30")
                return False
            if to_time.minute != 30 and to_time.minute != 0:
                self.error_display.configure(text = "You cannot bookah to this time. Correct time format is HH:00 or HH:30")
                return False
            if to_time < from_time:
                self.error_display.configure(text = "Please switch position of the times to bookah. ")
                return False
            if to_time == from_time:
                self.error_display.configure(text = "You have to book at least 30 minutes.. ")
                return False
        except ValueError:
            self.error_display.configure(text = "The correct time format is HH:MM")
            return False
        

        try:  # Everything track
            if int(self.track) < 1 or int(self.track) > 3:
                self.error_display.configure(text = "Bookable tracks are 1, 2 or 3.")
                return False
        except ValueError:
            self.error_display.configure(text = "Bookable tracks are 1, 2 or 3, please use numbers form.")
            return False
    
        return True # Well bookah'd 
    
    
    def check_if_open(self, day, open_time, close_time, from_time, to_time):
        if from_time < open_time: # if before it opens
            self.error_display.configure(text = "You cannot book a track this early on a {}".format(day))
            return False
        if to_time > close_time: #If past closing hour
            self.error_display.configure(text = "You cannot book a track this late on a {}".format(day))
            return False
    
    def check_if_bookable_time(self, day, from_time, to_time, gap_start, gap_end):
        gap_s = gap_start.strftime('%H:%M')
        gap_e = gap_end.strftime('%H:%M')

        if from_time > gap_start and from_time < gap_end:
            self.error_display.configure(text = "You cannot book between {} and {} on a {}".format(gap_s, gap_e, day))
            return False
        
        if to_time > gap_start and to_time < gap_end:
            self.error_display.configure(text = "You cannot book between {} and {} on a {}".format(gap_s, gap_e, day))
            return False
    
    
    def time_to_row(self):

        date_time_date = datetime.datetime.strptime(self.date, "%d.%m.%Y")
        day = date_time_date.strftime('%A')
        
        to_time = datetime.datetime.strptime(self.to_time, "%H:%M")
        from_time = datetime.datetime.strptime(self.from_time, "%H:%M")
        half_hour = datetime.timedelta(minutes = 30)
        
        row = 2
        self.bookah_rows = []
        
        while to_time > from_time:
            
            if day == 'Wednessday': #            Opens: 0730, Closes: 2200
                open_time = datetime.datetime.strptime('07:30', "%H:%M")
                close_time = datetime.datetime.strptime('22:00', "%H:%M")
                gap_start = datetime.datetime.strptime('17:30', "%H:%M")
                gap_end = datetime.datetime.strptime('21:00', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                
                if row_time >= gap_start and row_time <= gap_end: #there is a row gap between these times
                    pass
                else:
                    row += 1
                
                bookable_time = self.check_if_bookable_time(day, from_time, to_time, gap_start, gap_end)
                if bookable_time == False:
                    return False
                
            if day == 'Thursday': #            Opens: 0730, Closes: 2200
                open_time = datetime.datetime.strptime('07:30', "%H:%M")
                close_time = datetime.datetime.strptime('22:00', "%H:%M")
                gap_start = datetime.datetime.strptime('17:00', "%H:%M")
                gap_end = datetime.datetime.strptime('20:00', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                
                if row_time >= gap_start and row_time <= gap_end: #there is a row gap between these times
                    pass
                else:
                    row += 1
                
                bookable_time = self.check_if_bookable_time(day, from_time, to_time, gap_start, gap_end)
                if bookable_time == False:
                    return False
                
            if day == 'Friday': #            Opens: 0730, Closes: 2200
                open_time = datetime.datetime.strptime('07:30', "%H:%M")
                close_time = datetime.datetime.strptime('22:00', "%H:%M")
                gap_start = datetime.datetime.strptime('16:00', "%H:%M")
                gap_end = datetime.datetime.strptime('17:30', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                
                if row_time >= gap_start and row_time <= gap_end: #there is a row gap between these times
                    pass
                else:
                    row += 1
                
                bookable_time = self.check_if_bookable_time(day, from_time, to_time, gap_start, gap_end)
                if bookable_time == False:
                    return False
        
    
            elif day == 'Saturday': #            Opens: 1000, Closes: 2000
                open_time = datetime.datetime.strptime('10:00', "%H:%M")
                close_time = datetime.datetime.strptime('20:00', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                row += 1
                
                
                
    
            elif day == 'Sunday': #     Opens: 1000, Gap: 1830-2000, closes: 2200
                open_time = datetime.datetime.strptime('10:00', "%H:%M")
                close_time = datetime.datetime.strptime('22:00', "%H:%M")
                gap_start = datetime.datetime.strptime('18:30', "%H:%M")
                gap_end = datetime.datetime.strptime('20:00', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                
                if row_time >= gap_start and row_time < gap_end: #there is a row gap between these times
                    pass
                else:
                    row += 1
                bookable_time = self.check_if_bookable_time(day, from_time, to_time, gap_start, gap_end)
                if bookable_time == False:
                    return False

            else: #Monday, Tuesday;     Opens: 0730, Gap: 1800-1930, closes: 2200
                open_time = datetime.datetime.strptime('07:30', "%H:%M")
                close_time = datetime.datetime.strptime('22:00', "%H:%M")
                gap_start = datetime.datetime.strptime('18:00', "%H:%M")
                gap_end = datetime.datetime.strptime('21:00', "%H:%M")
                
                is_open = self.check_if_open(day, open_time, close_time, from_time, to_time)
                if is_open == False: #If past closing hour
                    return False
                if row == 2:
                    row_time = open_time
                if row_time == from_time:
                    self.bookah_rows.append(row)
                    from_time = from_time + half_hour
                row_time = row_time + half_hour
                
                if row_time >= gap_start and row_time <= gap_end: #there is a row gap between these times
                    pass
                else:
                    row += 1
                
                bookable_time = self.check_if_bookable_time(day, from_time, to_time, gap_start, gap_end)
                if bookable_time == False:
                    return False
                
                
                
                
        if len(self.bookah_rows) > 4:
            self.error_display.configure(text = "You cannot book more that 2 hours on any given day")
            return False
        print(self.bookah_rows)
#            from_time = from_time + half_hour #ONly to kill the loop fast
        

    
    def book_squash(self):
        for row in self.bookah_rows:
            tomorrow = '2'
            print((tomorrow, str(row), str(self.track)))
            self.driver.find_element(By.CSS_SELECTOR, (".ResourceDay:nth-child({}) > .ResourceRow:nth-child({}) .ResourceClass:nth-child({}) span").format(tomorrow, str(row), str(self.track))).click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
            time.sleep(2)
        
    def unbook_squash(self):
        
        for row in self.bookah_rows:
            tomorrow = '2'
            self.driver.find_element(By.CSS_SELECTOR, (".ResourceDay:nth-child({}) > .ResourceRow:nth-child({}) .ResourceClass:nth-child({}) span").format(tomorrow, str(row), str(self.track))).click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
            time.sleep(2)
#            driver.quit()


squashbookah30000()




















