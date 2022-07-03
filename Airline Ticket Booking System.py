try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter.font import BOLD, ITALIC
    import mysql.connector
    import random
    import time
    import smtplib, ssl

    DB = mysql.connector.connect(
        host = "localhost",
        user = "#USERNAME#",
        password = "#YOUR SQL PASSWORD#"
    )
    SQLcursor = DB.cursor()

    try:
        SQLcursor.execute("CREATE DATABASE Airline_Ticket_Info;")

        SQLcursor.execute("USE Airline_Ticket_Info;")

        SQLcursor.execute("CREATE TABLE signup_info (unique_user_id INT NOT NULL,first_name VARCHAR(100) NOT NULL,last_name VARCHAR(100) NOT NULL,contact_number CHAR(13) NOT NULL,email_id VARCHAR(100) NOT NULL, user_password VARCHAR(500) CHARACTER SET BINARY NOT NULL, PRIMARY KEY(unique_user_id));")

        SQLcursor.execute("CREATE TABLE passenger_flight_info (unique_user_id INT NOT NULL, passenger_full_name VARCHAR(), passenger_contact_no INT(), passenger_email_id VARCHAR(), passenger_passport_number CHAR(), passenger_unique_mark VARCHAR(), passenger_identity_proof VARCHAR(), passenger_luggage_weight INT(), passenger_food_type VARCHAR(), passenger_require_disability_equipment VARCHAR(3), passenger_other_requirements VARCHAR(500), passenger_flight_departure VARCHAR(100), passenger_flight_arrival VARCHAR(100), passenger_trip_type VARCHAR(10), passenger_flight_selected VARCHAR(100), passenger_flight_code CHAR(10), passenger_flight_departure_time CHAR(10), passenger_flight_departure_location VARCHAR(100), passenger_flight_arrival_location VARCHAR(100), passenger_flight_average_time CHAR(15), passenger_flight_cost CHAR(15), PRIMARY KEY(unique_user_id));")

        messagebox.showwarning("Restart Application", "Some changes have been made to database of this application, please Restart this application")

    except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DatabaseError) as e:
        try:
            SQLcursor.execute("use Airline_Ticket_Info;")
            SQLcursor.execute("CREATE TABLE signup_info (unique_user_id INT NOT NULL,first_name VARCHAR(100) NOT NULL,last_name VARCHAR(100) NOT NULL,contact_number CHAR(13) NOT NULL,email_id VARCHAR(100) NOT NULL, user_password VARCHAR(500) CHARACTER SET BINARY NOT NULL, PRIMARY KEY(unique_user_id));")

            SQLcursor.execute("CREATE TABLE passenger_flight_info (unique_user_id INT NOT NULL, passenger_flight_departure VARCHAR(100), passenger_flight_arrival VARCHAR(100), passenger_trip_type VARCHAR(10), passenger_flight_selected VARCHAR(100), passenger_flight_code CHAR(10), passenger_flight_departure_time CHAR(10), passenger_flight_departure_location VARCHAR(100), passenger_flight_arrival_location VARCHAR(100), passenger_flight_average_time CHAR(15), passenger_flight_cost CHAR(15), PRIMARY KEY(unique_user_id));")

            messagebox.showwarning("Restart Application", "Please Restart this application")

        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DatabaseError) as d:
            pass

            win = Tk()

            win.title("Flight Ticket Booking System System")
            win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")

            win.maxsize(width=1000, height=700)
            win.minsize(width=1000, height=700)

            icon = PhotoImage(file='#PASTE THE LOCATION YOU COPIED OF ICON.PNG FILE#')
            icon_label = Label(win, image=icon)
            icon_label.place(x=330, y=100)
            system_name_label = Label(win, text="Flight Ticket Booking System", font=("Calibri", 40, BOLD))
            system_name_label.place(x=180, y=470)

            def fetching_application_status():
                fetching_status = Label(win, text="Fetching application status...", font=("Calibri", 15))
                fetching_status.place(x=390, y=575)

                win.after(2000, fetching_status.place_forget)                

            def application_status():
                database_connected = Label(win, text="✓ Database Connected", font=("Calibri", 15))
                database_connected.place(x=182, y= 575)

                fetching_data = Label(win, text="✓ Data Fetched", font=("Calibri", 15))
                fetching_data.place(x=425, y=575)

                starting_application = Label(win, text="✓ Application Started", font=("Calibri", 15))
                starting_application.place(x=613, y= 575)

                win.after(2000, database_connected.place_forget)
                win.after(2000, fetching_data.place_forget)
                win.after(2000, starting_application.place_forget)

            win.after(3000, fetching_application_status)
            win.after(5000, application_status)
            win.after(7000, icon_label.place_forget)
            win.after(7000, system_name_label.place_forget)

            def main_application():
                win.title("Flight Ticket Booking System System - Sign-Up/Sign-In")

                label_signup_or_signin = Label(win, text="Sign-Up or Sign-In?", font=("Calibri", 35, BOLD, ITALIC), fg="Black")
                label_signup_or_signin.place(x=315, y=180)

                unique_user_id_random = random.randint(10000, 99999999)
                unique_user_id = unique_user_id_random            

                def switch_to_signup_window():
                    label_signup_or_signin.place_forget()
                    signup_button.place_forget()
                    signin_button.place_forget()
                    
                    signup_label = Label(win, text="Sign-Up", font=("Calibri", 35, BOLD, ITALIC), fg="Black")
                    signup_label.place(x=430, y=140)

                    signup_firstname = Label(win, text="First Name:", font=("Calibri", 18), fg="Black")
                    signup_firstname.place(x=353, y=220)
                    signup_firstname_entry = Entry(win, width=15, font=("Calibri", 18))
                    signup_firstname_entry.place(x=475, y=225)

                    signup_lastname = Label(win, text="Last Name:", font=("Calibri", 18), fg="Black")
                    signup_lastname.place(x=355, y=261)
                    signup_lastname_entry = Entry(win, width=15, font=("Calibri", 18))
                    signup_lastname_entry.place(x=475, y=265)

                    signup_contactNumber = Label(win, text="Contact Number:", font=("Calibri", 16), fg="Black")
                    signup_contactNumber.place(x=317, y=298)
                    signup_contactNumberCountryCode = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                    signup_contactNumberCountryCode.place(x=338, y=321)
                    signup_contactNumber_entry = Entry(win, width=15, font=("Calibri", 18))
                    signup_contactNumber_entry.place(x=475, y=305)

                    signup_emailID = Label(win, text="Email ID:", font=("Calibri", 18), fg="Black")
                    signup_emailID.place(x=377, y=343)
                    signup_emailID_entry = Entry(win, width=15, font=("Calibri", 18))
                    signup_emailID_entry.place(x=475, y=347)

                    signup_password = Label(win, text="Password:", font=("Calibri", 18), fg="Black")
                    signup_password.place(x=359, y=385)
                    signup_password_entry = Entry(win, width=15, font=("Calibri", 18), show="*")
                    signup_password_entry.place(x=475, y=388)

                    def submit_sign_up_credentials():
                        firstname = signup_firstname_entry.get()
                        lastname = signup_lastname_entry.get()
                        contactNumber = signup_contactNumber_entry.get()
                        emailID = signup_emailID_entry.get()
                        password = signup_password_entry.get()

                        SQLcursor.execute("SELECT COUNT(*) FROM signup_info WHERE email_id = %s", (emailID,))
                        email_already_exists_result = SQLcursor.fetchone()[0]
                        
                        if email_already_exists_result == 1:
                            messagebox.showerror("Flight Ticket Booking System System", "The email you've entered already exists, please go back and sign in.")
                        
                        elif email_already_exists_result == 0:
                            inserting_signup_credentials_into_database = "INSERT INTO signup_info(unique_user_id, first_name, last_name, contact_number, email_id, user_password) VALUES(%s, %s, %s, %s, %s, %s)"
                            values_of_signup_credentials = (unique_user_id, firstname, lastname, contactNumber, emailID, password)

                            SQLcursor.execute(inserting_signup_credentials_into_database, values_of_signup_credentials)
                            DB.commit()

                            messagebox.showinfo("Success", "Your sign-up credentials has been saved, please restart the application and sign-in")
                        else:
                            pass

                    submit_signup_credentials = Button(win, text="Submit", font=("Calibri", 15, BOLD), activebackground="#b5bab6", command=submit_sign_up_credentials)
                    submit_signup_credentials.place(x=462, y=450)

                def switch_to_signin_window():                
                    label_signup_or_signin.place_forget()
                    signup_button.place_forget()
                    signin_button.place_forget()

                    signin_label = Label(win, text="Sign-In", font=("Calibri", 35, BOLD, ITALIC), fg="Black")
                    signin_label.place(x=430, y=140)
 
                    signin_email_id = Label(win, text="Email ID:", font=("Calibri", 18), fg="Black")
                    signin_email_id.place(x=370, y=220)
                    signin_email_id_entry = Entry(win, width=15, font=("Calibri", 18))
                    signin_email_id_entry.place(x=475, y=225)

                    signin_password = Label(win, text="Password:", font=("Calibri", 18), fg="Black")
                    signin_password.place(x=360, y=260)
                    signin_password_entry = Entry(win, width=15, font=("Calibri", 18), show="*")
                    signin_password_entry.place(x=475, y=265)

                    def submit_sign_in_credentials():
                        email_id = signin_email_id_entry.get()
                        password = signin_password_entry.get()

                        SQLcursor.execute("SELECT COUNT(*) FROM signup_info WHERE email_id=%s AND user_password=%s", (email_id, password))
                        result = SQLcursor.fetchone()[0]

                        if result == 1:
                            signin_label.place_forget()
                            signin_email_id.place_forget()
                            signin_email_id_entry.place_forget()
                            signin_password.place_forget()
                            signin_password_entry.place_forget()
                            submit_signin_credentials.place_forget()

                            win.title("Flight Ticket Booking System - Flight Route")

                            departure = Label(win, text="FROM:", font=("Calibri", 25), fg="Black" )
                            departure.place(x=5, y=10)
                            departure_entry = Entry(win, width=20, font=("Calibri", 18))
                            departure_entry.place(x=10, y=55)

                            arrival_location = Label(win, text="TO:", font=("Calibri", 25), fg="Black")
                            arrival_location.place(x=380, y=10)
                            arrival_location_entry = Entry(win, width=20, font=("Calibri", 18))
                            arrival_location_entry.place(x=380, y=55)

                            trip_type = Label(win, text="TRIP TYPE:", font=("Calibri", 25), fg="Black")
                            trip_type.place(x=751, y=10)
                            trip_type_combobox = ttk.Combobox(win, state="readonly", width=18, font=("Calibri", 17), values = ("", "Round-Trip", "One-Way"))
                            trip_type_combobox.current(0)
                            trip_type_combobox.place(x=753, y=54)

                            def check_details_and_search_flights():
                                trip_type_combobox_value = trip_type_combobox.get()
                                if trip_type_combobox_value == "" and len(departure_entry.get()) == 0 and len(arrival_location_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System Info", "Enter all details first!")
                                elif trip_type_combobox_value == "" and len(departure_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System Info", "Please enter Departure city and choose Trip Type!")
                                elif trip_type_combobox_value == "" and len(arrival_location_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System Info", "Please enter Arrival city and choose Trip Type!")
                                elif len(departure_entry.get()) == 0 and len(arrival_location_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System Info", "Please enter Departure and Arrival city!")
                                elif trip_type_combobox_value == "":
                                    messagebox.showerror("Flight Ticket Booking System System", "Please choose Trip Type!")
                                elif len(departure_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System System", "Please enter Departure city!")
                                elif len(arrival_location_entry.get()) == 0:
                                    messagebox.showerror("Flight Ticket Booking System System", "Please enter Arrival city!")
                                elif (trip_type_combobox_value == "Round-Trip" or trip_type_combobox_value == "One-Way") and len(departure_entry.get()) > 0 and len(arrival_location_entry.get()) > 0:

                                    win.title("Flight Ticket Booking System System - Available Flights")

                                    flight_name_dict = {"B82A3": "Boeing Airliner Professional (Boeing 777-300ER)",
                                    "A380": "Airbus Dreamliner (Airbus A330-300)",
                                    "D71": "AirAsia X (Airbus A321neo)",
                                    "AA1": "American Airlines (Airbus A321)",
                                    "AS1": "Alaska Airlines (Boeing 737-800)",
                                    "SJ251": "SpiceJet (Boeing 787-9)",
                                    "AI01": "AirIndia (Boeing 777-300ER/Airbus A330-300)",
                                    "AC47": "AirCanada (De Havilland Canada DHC-8-300)",
                                    "USA57": "United States Airline (Embraer 175)",
                                    "JH28I": "Jin Hao (Various (319/320/321)",
                                    "QK1": "Air Canada Express (Boeing 737-800)",
                                    "KE1": "Korean Air Lines (Airbus A330-300)",
                                    "LH1": "Lufthansa (Boeing 787-9)",
                                    "QR1": "Qatar Airways (Boeing 747-400F/Boeing 747-8F)",
                                    "UA1": "United Airlines (Airbus A321)",
                                    "5X1": "UPS Airlines (Airbus A320neo)",
                                    "WN1": "Southwest Airlines (Boeing 737-800)",
                                    "EMI": "Emirates (Airliner 659-800)",
                                    "EGT7": "Egyptian Airlines (Boeing 787-800)",
                                    "SA67": "Star Air (Boeing 737-300)",
                                    "IGO": "Indigo (Airbus 689-550)",
                                    "VTI": "Vistara Airlines (Boeing 737-800)",
                                    "LLR": "Alliance Air (Airbus A330-300/Boeing 747-8F)"
                                    }

                                    submit_choosed_flight_details.place_forget()

                                    IACA_code_flight_1, random_flight_name_1 = random.choice(list(flight_name_dict.items()))
                                    IACA_code_flight_2, random_flight_name_2 = random.choice(list(flight_name_dict.items()))
                                    IACA_code_flight_3, random_flight_name_3 = random.choice(list(flight_name_dict.items()))
                                    IACA_code_flight_4, random_flight_name_4 = random.choice(list(flight_name_dict.items()))
                                    IACA_code_flight_5, random_flight_name_5 = random.choice(list(flight_name_dict.items()))
                                    
                                    searching_available_flights = ttk.Progressbar(win, orient=HORIZONTAL, length=150, mode="indeterminate")
                                    searching_available_flights.place(x=430, y=177)

                                    search_flights_label = Label(win, text="Searching Available Flights...", font=("Calibri", 20))
                                    search_flights_label.place(x=365, y=198)

                                    searching_available_flights['value'] = 20
                                    win.update_idletasks()
                                    time.sleep(0.5)

                                    searching_available_flights['value'] = 40
                                    win.update_idletasks()
                                    time.sleep(0.5)

                                    searching_available_flights['value'] = 60
                                    win.update_idletasks()
                                    time.sleep(0.5)

                                    searching_available_flights['value'] = 80
                                    win.update_idletasks()
                                    time.sleep(0.5)

                                    searching_available_flights['value'] = 100
                                    win.update_idletasks()
                                    time.sleep(0.5)

                                    search_flights_label.place_forget()
                                    searching_available_flights.place_forget()

                                    flights_available = Label(win, text="Flights Available:", font=("Calibri", 30, BOLD, UNDERLINE, ITALIC), fg="Black")
                                    flights_available.place(x=10, y=100)

                                    def get_flight_details():
                                        getting_flight_details = ttk.Progressbar(win, orient=HORIZONTAL, length=150, mode="indeterminate")
                                        getting_flight_details.place(x=410, y=405)

                                        getting_flight_details['value'] = 20
                                        win.update_idletasks()
                                        time.sleep(0.5)

                                        getting_flight_details['value'] = 40
                                        win.update_idletasks()
                                        time.sleep(0.5)

                                        getting_flight_details['value'] = 60
                                        win.update_idletasks()
                                        time.sleep(0.5)

                                        getting_flight_details['value'] = 80
                                        win.update_idletasks()
                                        time.sleep(0.5)

                                        getting_flight_details['value'] = 100
                                        win.update_idletasks()
                                        time.sleep(0.5)

                                        getting_flight_details.place_forget()
                                        
                                        flight_cost_USD_dict = {"983.53", "256.47", "734.43", "1347.45", "1395.56", "987.43", "453.97", "456.24", "546.78", "1056.32"}
                                        flight_cost_USD = random.choice(list(flight_cost_USD_dict))

                                        flight_MinuteTime_list = {': 01 AM', ': 02 AM', ': 03 AM', ': 04 AM', ': 05 AM', ': 06 AM', ': 07 AM', ': 08 AM', ': 09 AM', ': 10 AM', ': 11 AM', ': 12 AM', ': 13 AM', ': 14 AM', ': 15 AM', ': 16 AM', ': 17 AM', ': 18 AM', ': 19 AM', ': 20 AM', ': 21 AM', ': 22 AM', ': 23 AM', ': 24 AM', ': 25 AM', ': 26 AM', ': 27 AM', ': 28 AM', ': 29 AM', ': 30 AM', ': 31 AM', ': 32 AM', ': 33 AM', ': 34 AM', ': 35 AM', ': 36 AM', ': 37 AM', ': 38 AM', ': 39 AM', ': 40 AM', ': 41 AM', ': 42 AM', ': 43 AM', ': 44 AM', ': 45 AM', ': 46 AM', ': 47 AM', ': 48 AM', ': 49 AM', ': 50 AM', ': 51 AM', ': 52 AM', ': 53 AM', ': 54 AM', ': 55 AM', ': 56 AM', ': 57 AM', ': 58 AM', ': 59 AM', ': 60 AM', ': 01 PM', ': 02 PM', ': 03 PM', ': 04 PM', ': 05 PM', ': 06 PM', ': 07 PM', ': 08 PM', ': 09 PM', ': 10 PM', ': 11 PM', ': 12 PM', ': 13 PM', ': 14 PM', ': 15 PM', ': 16 PM', ': 17 PM', ': 18 PM', ': 19 PM', ': 20 PM', ': 21 PM', ': 22 PM', ': 23 PM', ': 24 PM', ': 25 PM', ': 26 PM', ': 27 PM', ': 28 PM', ': 29 PM', ': 30 PM', ': 31 PM', ': 32 PM', ': 33 PM', ': 34 PM', ': 35 PM', ': 36 PM', ': 37 PM', ': 38 PM', ': 39 PM', ': 40 PM', ': 41 PM', ': 42 PM', ': 43 PM', ': 44 PM', ': 45 PM', ': 46 PM', ': 47 PM', ': 48 PM', ': 49 PM', ': 50 PM', ': 51 PM', ': 52 PM', ': 53 PM', ': 54 PM', ': 55 PM', ': 56 PM', ': 57 PM', ': 58 PM', ': 59 PM', ': 60 PM'}
                                        flight_HourTime = random.randint(00,24)
                                        flight_MinuteTime = random.choice(list(flight_MinuteTime_list))
                                        flight_time = flight_HourTime, flight_MinuteTime


                                        average_flight_time = random.randint(120, 360)

                                        win.title("Flight Ticket Booking System System - Flight Details")

                                        if flight_name_var.get() == 0:
                                            messagebox.showerror("Flight Ticket Booking System System", "Please select a flight first!")
                                        elif flight_name_var.get() == 1:
                                            flight_details = Label(win, text="Flight Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                            flight_details.place(x=10, y=395)
                                            
                                            flight_name_label = Label(win, text="Flight Name:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_name_label.place(x=10, y=448)
                                            flight_code_label = Label(win, text="Flight Code:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_code_label.place(x=10, y=480)
                                            flight_departure_time_label = Label(win, text="Flight Departure Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_time_label.place(x=10, y=510)
                                            flight_departure_location_label = Label(win, text="Flight Departure Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_location_label.place(x=10, y=540)
                                            flight_arrival_location_label = Label(win, text="Flight Arrival Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_arrival_location_label.place(x=10, y=570)
                                            average_FlightFly_time_label = Label(win, text="Average Flight Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            average_FlightFly_time_label.place(x=10, y=600)
                                            flight_cost_label = Label(win, text="Flight Cost:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_cost_label.place(x=10, y=630)

                                            flight_name = Label(win, text=random_flight_name_1, font=("Calibri", 18), fg="Black")
                                            flight_name.place(x=141, y=448)
                                            flight_code = Label(win, text=IACA_code_flight_1, font=("Calibri", 18), fg="Black")
                                            flight_code.place(x=133, y=480)
                                            flight_departure_time = Label(win, text=flight_time, font=("Calibri", 18), fg="Black")
                                            flight_departure_time.place(x=240, y=510)
                                            flight_departure_location = Label(win, text=departure_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_departure_location.place(x=276,y=540)
                                            flight_arrival_location = Label(win, text=arrival_location_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_arrival_location.place(x=240, y=570)
                                            average_FlightFly_time = Label(win, text=(average_flight_time, 'minutes'), font=("Calibri", 18), fg="Black")
                                            average_FlightFly_time.place(x=220, y=600)
                                            flight_cost = Label(win, text=("USD", flight_cost_USD), font=("Calibri", 18), fg="Black")
                                            flight_cost.place(x=126, y=630)

                                            def save_and_continue():
                                                departure.place_forget()
                                                departure_entry.place_forget()
                                                arrival_location.place_forget()
                                                arrival_location_entry.place_forget()
                                                trip_type.place_forget()
                                                trip_type_combobox.place_forget()
                                                flights_available.place_forget()
                                                no_flight_name.place_forget
                                                flight_name_1.place_forget()
                                                flight_name_2.place_forget()
                                                flight_name_3.place_forget()
                                                flight_name_4.place_forget()
                                                flight_name_5.place_forget()
                                                flight_name_submitButton.place_forget()
                                                flight_details.place_forget()
                                                flight_name_label.place_forget()
                                                flight_code_label.place_forget()
                                                flight_departure_time_label.place_forget()
                                                flight_departure_location_label.place_forget()
                                                flight_arrival_location_label.place_forget()
                                                average_FlightFly_time_label.place_forget()
                                                flight_cost_label.place_forget()
                                                flight_name.place_forget()
                                                flight_code.place_forget()
                                                flight_departure_time.place_forget()
                                                flight_departure_location.place_forget()
                                                flight_arrival_location.place_forget()
                                                average_FlightFly_time.place_forget()
                                                flight_cost.place_forget()
                                                save_flightSelection_and_continue.place_forget()
                                                
                                                win.title("Flight Ticket Booking System System - Passenger Details")
                                                win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                win.maxsize(width=1000, height=70)
                                                win.minsize(width=1000, height=700)

                                                header = Label(win, text="Passenger Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                                header.place(x=370, y=0)
                                                sub_header = Label(win, text="Filling out all the details are mandatory", font=("Calibri", 13), fg="Black")
                                                sub_header.place(x=378, y=50)

                                                passenger_full_name = Label(win, text="Full Name:", font=("Calibri", 20), fg="Black")
                                                passenger_full_name.place(x=5, y=85)
                                                passenger_full_name_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_full_name_entry.place(x=130, y=87)

                                                passenger_contact_number = Label(win, text="Contact Number:", font=("Calibri", 20), fg="Black")
                                                passenger_contact_number.place(x=5, y=125)
                                                passenger_contact_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_contact_number_entry.place(x=199, y=127)
                                                passenger_contact_number_country_code = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                                                passenger_contact_number_country_code.place(x=35, y=155)

                                                passenger_email_id = Label(win, text="Email ID:", font=("Calibri", 20), fg="Black")
                                                passenger_email_id.place(x=5, y=185)
                                                passenger_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_email_id_entry.place(x=110, y=187)

                                                passenger_passport_number = Label(win, text="Passport number:", font=("Calibri", 20), fg="Black")
                                                passenger_passport_number.place(x=5, y=225)
                                                passenger_passport_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_passport_number_entry.place(x=208, y=227)

                                                passenger_unique_mark = Label(win, text="Unique Mark     :", font=("Calibri", 20), fg="Black")
                                                passenger_unique_mark.place(x=5, y=265)
                                                passenger_unique_mark_entry = Entry(win, width=30, font=("Calibri", 20))
                                                passenger_unique_mark_entry.place(x=192, y=267)

                                                def onClick_passenger_unique_mark_info():
                                                    win_unique_mark_info = Tk()
                                                    win_unique_mark_info.title("Flight Ticket Booking System System - Unique Mark Info")
                                                    win_unique_mark_info.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                    win_unique_mark_info.maxsize(width=600, height=200)
                                                    win_unique_mark_info.minsize(width=600, height=200)

                                                    info_icon = Label(win_unique_mark_info, text="ⓘ", font=("Calibri", 95), fg="Black")
                                                    info_icon.place(x=13, y=10)

                                                    unique_mark_info = Label(win_unique_mark_info, text='''Unique mark is a mark on passengers visible\nbody that can be easily identified by anyone.\nThis information is important incase if airport\nauthorities need to verify the passengers identity.\n''', font=("Calibri", 15), fg="Black")
                                                    unique_mark_info.place(x=150, y=12)

                                                    def destroy_win_unique_mark_info():
                                                        win_unique_mark_info.destroy()
                                                    destrory_unique_mark_info_win = Button(win_unique_mark_info, text="Okay", font=("Calibri", 14), command=destroy_win_unique_mark_info)
                                                    destrory_unique_mark_info_win.place(x=315, y=130)

                                                passenger_unique_mark_info = Button(win, text="ⓘ", font=("Calibri", 9), fg="Black", command=onClick_passenger_unique_mark_info)
                                                passenger_unique_mark_info.place(x=155, y=272)

                                                passenger_identity_proof = Label(win, text="Identity Proof:", font=("Calibri", 20), fg="Black")
                                                passenger_identity_proof.place(x=5, y=305)
                                                passenger_identity_proof_combobox = ttk.Combobox(win, state="readonly", width=36, font=("Calibri", 17), values = ("", "Aadhar Card", "Voter ID", "School/Company/Institution Recognized Card", "Driving License", "Birth Certificate", "Identity Certificate", "Service Identity Card"))
                                                passenger_identity_proof_combobox.current(0)
                                                passenger_identity_proof_combobox.place(x=170, y=312)

                                                passenger_luggage = Label(win, text="Exact total luggage passenger will be carrying (in Kgs):", font=("Calibri", 20), fg="Black")
                                                passenger_luggage.place(x=5, y=345)
                                                passenger_luggage_entry = Entry(win, width=3, font=("Calibri", 20))
                                                passenger_luggage_entry.place(x=600, y=347)

                                                passenger_food_type = Label(win, text="Passengers food preferred choice:", font=("Calibri", 20), fg="Black")
                                                passenger_food_type.place(x=5, y=385)
                                                passenger_food_type_combobox = ttk.Combobox(win, state="readonly", width=13, font=("Calibri", 17), values = ("", "Veg. Food", "Non-Veg. Food"))
                                                passenger_food_type_combobox.current(0)
                                                passenger_food_type_combobox.place(x=380, y=392)

                                                passenger_with_walking_diability = Label(win, text="Does passenger require any walking disability equipments?:", font=("Calibri", 20), fg="Black")
                                                passenger_with_walking_diability.place(x=5, y=425)
                                                passenger_with_walking_diability_combobox = ttk.Combobox(win, state="readonly", width=3, font=("Calibri", 17), values = ("", "Yes", "No"))
                                                passenger_with_walking_diability_combobox.current(0)
                                                passenger_with_walking_diability_combobox.place(x=663, y=430)

                                                passenger_other_requirements = Label(win, text="Passengers other requirements:", font=("Calibri", 20), fg="Black")
                                                passenger_other_requirements.place(x=5, y=465)
                                                passenger_other_requirements_entry = Entry(win, width=26, font=("Calibri", 20))
                                                passenger_other_requirements_entry.place(x=360, y=470)

                                                def continue_filled_passengers_details():
                                                    if passenger_full_name_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_contact_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_email_id_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_passport_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_unique_mark_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_identity_proof_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_luggage_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_food_type_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_with_walking_diability_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_other_requirements_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!") 
                                                    else:
                                                        processing_saving_passenger_details = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                        processing_saving_passenger_details.place(x=370, y=570)
                                                        processing_saving_passenger_details_progressBar = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                        processing_saving_passenger_details_progressBar.place(x=370, y=600)

                                                        
                                                        processing_saving_passenger_details_progressBar['value'] = 20
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 40
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        insert = (
                                                            "INSERT INTO passenger_and_flight_info (unique_user_id, passenger_full_name, passenger_contact_no, passenger_email_id, passenger_passport_number, passenger_unique_mark, passenger_identity_proof, passenger_luggage_weight, passenger_food_type, passenger_require_disability_equipment, passenger_flight_departure, passenger_flight_arrival, passenger_trip_type, passenger_flight_selected, passenger_flight_code, passenger_flight_departure_location, passenger_flight_arrival_location, passenger_flight_average_time, passenger_flight_cost)"
                                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                        )
                                                        data = (unique_user_id, passenger_full_name_entry.get(), passenger_contact_number_entry.get(), passenger_email_id_entry.get(), passenger_passport_number_entry.get(), passenger_unique_mark_entry.get(), passenger_identity_proof_combobox.get(), passenger_luggage_entry.get(), passenger_food_type_combobox.get(), passenger_with_walking_diability_combobox.get(), departure_entry.get(), arrival_location_entry.get(), trip_type_combobox.get(), random_flight_name_1, IACA_code_flight_1, departure_entry.get(), arrival_location_entry.get(), average_flight_time, flight_cost_USD)
                                                        
                                                        SQLcursor.execute(insert, data)
                                                        DB.commit()

                                                        processing_saving_passenger_details_progressBar['value'] = 60
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 80
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 100
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        header.place_forget()
                                                        sub_header.place_forget()
                                                        passenger_full_name.place_forget()
                                                        passenger_full_name_entry.place_forget()
                                                        passenger_contact_number.place_forget()
                                                        passenger_contact_number_country_code.place_forget()
                                                        passenger_contact_number_entry.place_forget()
                                                        passenger_email_id.place_forget()
                                                        passenger_email_id_entry.place_forget()
                                                        passenger_passport_number.place_forget()
                                                        passenger_passport_number_entry.place_forget()
                                                        passenger_unique_mark.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_unique_mark_info.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_identity_proof.place_forget()
                                                        passenger_identity_proof_combobox.place_forget()
                                                        passenger_luggage.place_forget()
                                                        passenger_luggage_entry.place_forget()
                                                        passenger_food_type.place_forget()
                                                        passenger_food_type_combobox.place_forget()
                                                        passenger_with_walking_diability.place_forget()
                                                        passenger_with_walking_diability_combobox.place_forget()
                                                        passenger_other_requirements.place_forget()
                                                        passenger_other_requirements_entry.place_forget()
                                                        processing_saving_passenger_details.place_forget()
                                                        processing_saving_passenger_details_progressBar.place_forget()
                                                        passengers_details_continue.place_forget()

                                                        terms_and_conditions_header = Label(win, text="Terms and Conditions", font=("Calibri", 25, BOLD, UNDERLINE), fg="Black")
                                                        terms_and_conditions_header.place(x=352, y=5)
                                                        terms_and_conditions = Label(win, text="To proceed, you need to agree to the all the terms and conditons mentioned below. \n 1. The data you have entered till now will be handed over to the respected authorities securely. \n 2. Flight history and other various data will be kept in our systems for giving you smooth experice each time you use this software. \n 3. Airline companies may contact you any time within working days. \n 4. If your luggage weighs over 50 Kgs, you'll be charged $10/kg. \n \n IF YOU AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK CONTINUE.\n IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK EXIT", wraplength=950, justify=LEFT, font=("Calibri", 18), fg="Black")
                                                        terms_and_conditions.place(x=5, y=50)

                                                        def TC_continue_button():
                                                            DB.commit()

                                                            terms_and_conditions_agreed_label = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                            terms_and_conditions_agreed_label.place(x=370, y=570)
                                                            terms_and_conditions_agreed = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                            terms_and_conditions_agreed.place(x=370, y=600)

                                                            terms_and_conditions_agreed['value'] = 20
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 40
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 60
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 80
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 100
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed.place_forget()
                                                            terms_and_conditions_agreed_label.place_forget()
                                                            terms_and_conditions_header.place_forget()
                                                            terms_and_conditions.place_forget()
                                                            TC_continue.place_forget()
                                                            TC_exit.place_forget()

                                                            win.title("Flight Ticket Booking System System - Email Confirmation")

                                                            user_email_id = Label(win, text="Enter your email below to finish processing your details and receive your ticket.", font=("Calibri", 25), wraplength=800)
                                                            user_email_id.place(x=135, y=200)
                                                            user_email_id_warning = Label(win, text="Make sure you enter valid email address, also the email must be in the correct format (example@exapmle.com) or else, the software application will close and all the information will be discared. This is done to prevent some unknown from gaining access to your data.", font=("Calibri", 12), wraplength=800)
                                                            user_email_id_warning.place(x=120, y=390)
                                                            user_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                            user_email_id_entry.place(x=363, y=290)

                                                            user_email_body = "THANK YOU FOR BOOKING YOUR FLIGHT TICKET WITH FLIGHT TICKET BOOKING SYSTEM\n\nHere are your final details, incase if you wish to change any of your detail/s or cancel your ticket, reply to this email.\n\nUnique ID: ", unique_user_id, "Name: ", passenger_full_name_entry.get()

                                                            def send_email():
                                                                user_email_id.place_forget()
                                                                user_email_id_entry.place_forget()
                                                                user_email_id_warning.place_forget()
                                                                user_email_id_submit.place_forget()

                                                                try:
                                                                    sending_email = Label(win, text="Sending you the ticket on your email. Please Wait...", font=("Calibri", 25), wraplength=800)
                                                                    sending_email.place(x=153, y=285)

                                                                    port = 465   
                                                                    smtp_server = "smtp.gmail.com"
                                                                    flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                    users_email = user_email_id_entry.get()
                                                                    flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                    email_body = user_email_body
                                                                    context = ssl.create_default_context()
                                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                        server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                        server.sendmail(flight_ticket_booking_system_email, users_email, email_body)
                                                                        sending_email.place_forget()

                                                                    ticket_booked = Label(win, text="✔", font=("Calibri", 110, BOLD), fg="Black")
                                                                    ticket_booked.place(x=440, y=180)

                                                                    email_sent = Label(win, text="We have sent you your flight ticket on your registered email ID, kindly check your inbox.", font=("Calibri", 15, BOLD), fg="Black")
                                                                    email_sent.place(x=135, y=360)

                                                                    def resend_email():
                                                                        port = 465
                                                                        smtp_server = "smtp.gmail.com"
                                                                        flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                        users_email = user_email_id_entry.get()
                                                                        flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                        email_body = user_email_body

                                                                        context = ssl.create_default_context()
                                                                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                            server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                            server.sendmail(flight_ticket_booking_system_email, users_email, email_body)

                                                                            email_sent = Label(win, text="Email sent", font=("Calibri", 12))
                                                                            email_sent.place(x=463, y=444)

                                                                    email_not_received_button = Button(win, text="Resend Email", command=resend_email)
                                                                    email_not_received_button.place(x=455, y=410)
                                                                except smtplib.SMTPRecipientsRefused:
                                                                    messagebox.showerror("Flight Ticket Booking System", "Email is not valid or its not in the correct format!\nThe software will close automatically in 5 seconds.")
                                                                    time.sleep(5)
                                                                    win.destroy()
                                                            user_email_id_submit = Button(win, text="Submit", font=("Calibri", 13), command=send_email)
                                                            user_email_id_submit.place(x=468, y=340)

                                                        TC_continue = Button(win, text="Continue", font=("Calibri", 18), command=TC_continue_button)
                                                        TC_continue.place(x=455, y=500)

                                                        def TC_exit_button():
                                                            win.destroy()
                                                        TC_exit = Button(win, text="Exit", font=("Calibri", 18), command=TC_exit_button)
                                                        TC_exit.place(x=482, y=560)

                                                passengers_details_continue = Button(win, text="Continue", font=("Calibri", 15), command=continue_filled_passengers_details)
                                                passengers_details_continue.place(x=460, y=520)
                                            save_flightSelection_and_continue = Button(win, text="Save Selection and Continue", command=save_and_continue)
                                            save_flightSelection_and_continue.place(x=410, y=660)
                                        elif flight_name_var.get() == 2:
                                            flight_details = Label(win, text="Flight Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                            flight_details.place(x=10, y=395)
                                            
                                            flight_name_label = Label(win, text="Flight Name:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_name_label.place(x=10, y=448)
                                            flight_code_label = Label(win, text="Flight Code:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_code_label.place(x=10, y=480)
                                            flight_departure_time_label = Label(win, text="Flight Departure Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_time_label.place(x=10, y=510)
                                            flight_departure_location_label = Label(win, text="Flight Departure Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_location_label.place(x=10, y=540)
                                            flight_arrival_location_label = Label(win, text="Flight Arrival Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_arrival_location_label.place(x=10, y=570)
                                            average_FlightFly_time_label = Label(win, text="Average Flight Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            average_FlightFly_time_label.place(x=10, y=600)
                                            flight_cost_label = Label(win, text="Flight Cost:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_cost_label.place(x=10, y=630)

                                            flight_name = Label(win, text=random_flight_name_2, font=("Calibri", 18), fg="Black")
                                            flight_name.place(x=141, y=448)
                                            flight_code = Label(win, text=IACA_code_flight_2, font=("Calibri", 18), fg="Black")
                                            flight_code.place(x=133, y=480)
                                            flight_departure_time = Label(win, text=flight_time, font=("Calibri", 18), fg="Black")
                                            flight_departure_time.place(x=240, y=510)
                                            flight_departure_location = Label(win, text=departure_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_departure_location.place(x=276,y=540)
                                            flight_arrival_location = Label(win, text=arrival_location_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_arrival_location.place(x=240, y=570)
                                            average_FlightFly_time = Label(win, text=(average_flight_time, 'minutes'), font=("Calibri", 18), fg="Black")
                                            average_FlightFly_time.place(x=220, y=600)
                                            flight_cost = Label(win, text=("USD", flight_cost_USD), font=("Calibri", 18), fg="Black")
                                            flight_cost.place(x=126, y=630)

                                            def save_and_continue():
                                                departure.place_forget()
                                                departure_entry.place_forget()
                                                arrival_location.place_forget()
                                                arrival_location_entry.place_forget()
                                                trip_type.place_forget()
                                                trip_type_combobox.place_forget()
                                                flights_available.place_forget()
                                                no_flight_name.place_forget
                                                flight_name_1.place_forget()
                                                flight_name_2.place_forget()
                                                flight_name_3.place_forget()
                                                flight_name_4.place_forget()
                                                flight_name_5.place_forget()
                                                flight_name_submitButton.place_forget()
                                                flight_details.place_forget()
                                                flight_name_label.place_forget()
                                                flight_code_label.place_forget()
                                                flight_departure_time_label.place_forget()
                                                flight_departure_location_label.place_forget()
                                                flight_arrival_location_label.place_forget()
                                                average_FlightFly_time_label.place_forget()
                                                flight_cost_label.place_forget()
                                                flight_name.place_forget()
                                                flight_code.place_forget()
                                                flight_departure_time.place_forget()
                                                flight_departure_location.place_forget()
                                                flight_arrival_location.place_forget()
                                                average_FlightFly_time.place_forget()
                                                flight_cost.place_forget()
                                                save_flightSelection_and_continue.place_forget()
                                                
                                                win.title("Flight Ticket Booking System System - Passenger Details")
                                                win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                win.maxsize(width=1000, height=70)
                                                win.minsize(width=1000, height=700)

                                                header = Label(win, text="Passenger Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                                header.place(x=370, y=0)
                                                sub_header = Label(win, text="Filling out all the details are mandatory", font=("Calibri", 13), fg="Black")
                                                sub_header.place(x=378, y=50)

                                                passenger_full_name = Label(win, text="Full Name:", font=("Calibri", 20), fg="Black")
                                                passenger_full_name.place(x=5, y=85)
                                                passenger_full_name_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_full_name_entry.place(x=130, y=87)

                                                passenger_contact_number = Label(win, text="Contact Number:", font=("Calibri", 20), fg="Black")
                                                passenger_contact_number.place(x=5, y=125)
                                                passenger_contact_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_contact_number_entry.place(x=199, y=127)
                                                passenger_contact_number_country_code = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                                                passenger_contact_number_country_code.place(x=35, y=155)

                                                passenger_email_id = Label(win, text="Email ID:", font=("Calibri", 20), fg="Black")
                                                passenger_email_id.place(x=5, y=185)
                                                passenger_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_email_id_entry.place(x=110, y=187)

                                                passenger_passport_number = Label(win, text="Passport number:", font=("Calibri", 20), fg="Black")
                                                passenger_passport_number.place(x=5, y=225)
                                                passenger_passport_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_passport_number_entry.place(x=208, y=227)

                                                passenger_unique_mark = Label(win, text="Unique Mark     :", font=("Calibri", 20), fg="Black")
                                                passenger_unique_mark.place(x=5, y=265)
                                                passenger_unique_mark_entry = Entry(win, width=30, font=("Calibri", 20))
                                                passenger_unique_mark_entry.place(x=192, y=267)

                                                def onClick_passenger_unique_mark_info():
                                                    win_unique_mark_info = Tk()
                                                    win_unique_mark_info.title("Flight Ticket Booking System System - Unique Mark Info")
                                                    win_unique_mark_info.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                    win_unique_mark_info.maxsize(width=600, height=200)
                                                    win_unique_mark_info.minsize(width=600, height=200)

                                                    info_icon = Label(win_unique_mark_info, text="ⓘ", font=("Calibri", 95), fg="Black")
                                                    info_icon.place(x=13, y=10)

                                                    unique_mark_info = Label(win_unique_mark_info, text='''Unique mark is a mark on passengers visible\nbody that can be easily identified by anyone.\nThis information is important incase if airport\nauthorities need to verify the passengers identity.\n''', font=("Calibri", 15), fg="Black")
                                                    unique_mark_info.place(x=150, y=12)

                                                    def destroy_win_unique_mark_info():
                                                        win_unique_mark_info.destroy()
                                                    destrory_unique_mark_info_win = Button(win_unique_mark_info, text="Okay", font=("Calibri", 14), command=destroy_win_unique_mark_info)
                                                    destrory_unique_mark_info_win.place(x=315, y=130)

                                                passenger_unique_mark_info = Button(win, text="ⓘ", font=("Calibri", 9), fg="Black", command=onClick_passenger_unique_mark_info)
                                                passenger_unique_mark_info.place(x=155, y=272)

                                                passenger_identity_proof = Label(win, text="Identity Proof:", font=("Calibri", 20), fg="Black")
                                                passenger_identity_proof.place(x=5, y=305)
                                                passenger_identity_proof_combobox = ttk.Combobox(win, state="readonly", width=36, font=("Calibri", 17), values = ("", "Aadhar Card", "Voter ID", "School/Company/Institution Recognized Card", "Driving License", "Birth Certificate", "Identity Certificate", "Service Identity Card"))
                                                passenger_identity_proof_combobox.current(0)
                                                passenger_identity_proof_combobox.place(x=170, y=312)

                                                passenger_luggage = Label(win, text="Exact total luggage passenger will be carrying (in Kgs):", font=("Calibri", 20), fg="Black")
                                                passenger_luggage.place(x=5, y=345)
                                                passenger_luggage_entry = Entry(win, width=3, font=("Calibri", 20))
                                                passenger_luggage_entry.place(x=600, y=347)

                                                passenger_food_type = Label(win, text="Passengers food preferred choice:", font=("Calibri", 20), fg="Black")
                                                passenger_food_type.place(x=5, y=385)
                                                passenger_food_type_combobox = ttk.Combobox(win, state="readonly", width=13, font=("Calibri", 17), values = ("", "Veg. Food", "Non-Veg. Food"))
                                                passenger_food_type_combobox.current(0)
                                                passenger_food_type_combobox.place(x=380, y=392)

                                                passenger_with_walking_diability = Label(win, text="Does passenger require any walking disability equipments?:", font=("Calibri", 20), fg="Black")
                                                passenger_with_walking_diability.place(x=5, y=425)
                                                passenger_with_walking_diability_combobox = ttk.Combobox(win, state="readonly", width=3, font=("Calibri", 17), values = ("", "Yes", "No"))
                                                passenger_with_walking_diability_combobox.current(0)
                                                passenger_with_walking_diability_combobox.place(x=663, y=430)

                                                passenger_other_requirements = Label(win, text="Passengers other requirements:", font=("Calibri", 20), fg="Black")
                                                passenger_other_requirements.place(x=5, y=465)
                                                passenger_other_requirements_entry = Entry(win, width=26, font=("Calibri", 20))
                                                passenger_other_requirements_entry.place(x=360, y=470)

                                                def continue_filled_passengers_details():
                                                    if passenger_full_name_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_contact_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_email_id_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_passport_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_unique_mark_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_identity_proof_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_luggage_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_food_type_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_with_walking_diability_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_other_requirements_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!") 
                                                    else:
                                                        processing_saving_passenger_details = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                        processing_saving_passenger_details.place(x=370, y=570)
                                                        processing_saving_passenger_details_progressBar = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                        processing_saving_passenger_details_progressBar.place(x=370, y=600)

                                                        
                                                        processing_saving_passenger_details_progressBar['value'] = 20
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 40
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        insert = (
                                                            "INSERT INTO passenger_and_flight_info (unique_user_id, passenger_full_name, passenger_contact_no, passenger_email_id, passenger_passport_number, passenger_unique_mark, passenger_identity_proof, passenger_luggage_weight, passenger_food_type, passenger_require_disability_equipment, passenger_flight_departure, passenger_flight_arrival, passenger_trip_type, passenger_flight_selected, passenger_flight_code, passenger_flight_departure_location, passenger_flight_arrival_location, passenger_flight_average_time, passenger_flight_cost)"
                                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                        )
                                                        data = (unique_user_id, passenger_full_name_entry.get(), passenger_contact_number_entry.get(), passenger_email_id_entry.get(), passenger_passport_number_entry.get(), passenger_unique_mark_entry.get(), passenger_identity_proof_combobox.get(), passenger_luggage_entry.get(), passenger_food_type_combobox.get(), passenger_with_walking_diability_combobox.get(), departure_entry.get(), arrival_location_entry.get(), trip_type_combobox.get(), random_flight_name_2, IACA_code_flight_2, departure_entry.get(), arrival_location_entry.get(), average_flight_time, flight_cost_USD)
                                                        
                                                        SQLcursor.execute(insert, data)
                                                        DB.commit()

                                                        processing_saving_passenger_details_progressBar['value'] = 60
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 80
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 100
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        header.place_forget()
                                                        sub_header.place_forget()
                                                        passenger_full_name.place_forget()
                                                        passenger_full_name_entry.place_forget()
                                                        passenger_contact_number.place_forget()
                                                        passenger_contact_number_country_code.place_forget()
                                                        passenger_contact_number_entry.place_forget()
                                                        passenger_email_id.place_forget()
                                                        passenger_email_id_entry.place_forget()
                                                        passenger_passport_number.place_forget()
                                                        passenger_passport_number_entry.place_forget()
                                                        passenger_unique_mark.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_unique_mark_info.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_identity_proof.place_forget()
                                                        passenger_identity_proof_combobox.place_forget()
                                                        passenger_luggage.place_forget()
                                                        passenger_luggage_entry.place_forget()
                                                        passenger_food_type.place_forget()
                                                        passenger_food_type_combobox.place_forget()
                                                        passenger_with_walking_diability.place_forget()
                                                        passenger_with_walking_diability_combobox.place_forget()
                                                        passenger_other_requirements.place_forget()
                                                        passenger_other_requirements_entry.place_forget()
                                                        processing_saving_passenger_details.place_forget()
                                                        processing_saving_passenger_details_progressBar.place_forget()
                                                        passengers_details_continue.place_forget()

                                                        terms_and_conditions_header = Label(win, text="Terms and Conditions", font=("Calibri", 25, BOLD, UNDERLINE), fg="Black")
                                                        terms_and_conditions_header.place(x=352, y=5)
                                                        terms_and_conditions = Label(win, text="To proceed, you need to agree to the all the terms and conditons mentioned below. \n 1. The data you have entered till now will be handed over to the respected authorities securely. \n 2. Flight history and other various data will be kept in our systems for giving you smooth experice each time you use this software. \n 3. Airline companies may contact you any time within working days. \n 4. If your luggage weighs over 50 Kgs, you'll be charged $10/kg. \n \n IF YOU AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK CONTINUE.\n IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK EXIT", wraplength=950, justify=LEFT, font=("Calibri", 18), fg="Black")
                                                        terms_and_conditions.place(x=5, y=50)

                                                        def TC_continue_button():
                                                            DB.commit()

                                                            terms_and_conditions_agreed_label = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                            terms_and_conditions_agreed_label.place(x=370, y=570)
                                                            terms_and_conditions_agreed = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                            terms_and_conditions_agreed.place(x=370, y=600)

                                                            terms_and_conditions_agreed['value'] = 20
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 40
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 60
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 80
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 100
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed.place_forget()
                                                            terms_and_conditions_agreed_label.place_forget()
                                                            terms_and_conditions_header.place_forget()
                                                            terms_and_conditions.place_forget()
                                                            TC_continue.place_forget()
                                                            TC_exit.place_forget()

                                                            win.title("Flight Ticket Booking System System - Email Confirmation")

                                                            user_email_id = Label(win, text="Enter your email below to finish processing your details and receive your ticket.", font=("Calibri", 25), wraplength=800)
                                                            user_email_id.place(x=135, y=200)
                                                            user_email_id_warning = Label(win, text="Make sure you enter valid email address, also the email must be in the correct format (example@exapmle.com) or else, the software application will close and all the information will be discared. This is done to prevent some unknown from gaining access to your data.", font=("Calibri", 12), wraplength=800)
                                                            user_email_id_warning.place(x=120, y=390)
                                                            user_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                            user_email_id_entry.place(x=363, y=290)

                                                            user_email_body = "THANK YOU FOR BOOKING YOUR FLIGHT TICKET WITH FLIGHT TICKET BOOKING SYSTEM\n\nHere are your final details, incase if you wish to change any of your detail/s or cancel your ticket, reply to this email.\n\nUnique ID: ", unique_user_id, "Name: ", passenger_full_name_entry.get()

                                                            def send_email():
                                                                user_email_id.place_forget()
                                                                user_email_id_entry.place_forget()
                                                                user_email_id_warning.place_forget()
                                                                user_email_id_submit.place_forget()

                                                                try:
                                                                    sending_email = Label(win, text="Sending you the ticket on your email. Please Wait...", font=("Calibri", 25), wraplength=800)
                                                                    sending_email.place(x=153, y=285)

                                                                    port = 465   
                                                                    smtp_server = "smtp.gmail.com"
                                                                    flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                    users_email = user_email_id_entry.get()
                                                                    flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                    email_body = user_email_body
                                                                    context = ssl.create_default_context()
                                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                        server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                        server.sendmail(flight_ticket_booking_system_email, users_email, email_body)
                                                                        sending_email.place_forget()

                                                                    ticket_booked = Label(win, text="✔", font=("Calibri", 110, BOLD), fg="Black")
                                                                    ticket_booked.place(x=440, y=180)

                                                                    email_sent = Label(win, text="We have sent you your flight ticket on your registered email ID, kindly check your inbox.", font=("Calibri", 15, BOLD), fg="Black")
                                                                    email_sent.place(x=135, y=360)

                                                                    def resend_email():
                                                                        port = 465
                                                                        smtp_server = "smtp.gmail.com"
                                                                        flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                        users_email = user_email_id_entry.get()
                                                                        flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                        email_body = user_email_body

                                                                        context = ssl.create_default_context()
                                                                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                            server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                            server.sendmail(flight_ticket_booking_system_email, users_email, email_body)

                                                                            email_sent = Label(win, text="Email sent", font=("Calibri", 12))
                                                                            email_sent.place(x=463, y=444)

                                                                    email_not_received_button = Button(win, text="Resend Email", command=resend_email)
                                                                    email_not_received_button.place(x=455, y=410)
                                                                except smtplib.SMTPRecipientsRefused:
                                                                    messagebox.showerror("Flight Ticket Booking System", "Email is not valid or its not in the correct format!\nThe software will close automatically in 5 seconds.")
                                                                    time.sleep(5)
                                                                    win.destroy()
                                                            user_email_id_submit = Button(win, text="Submit", font=("Calibri", 13), command=send_email)
                                                            user_email_id_submit.place(x=468, y=340)

                                                        TC_continue = Button(win, text="Continue", font=("Calibri", 18), command=TC_continue_button)
                                                        TC_continue.place(x=455, y=500)

                                                        def TC_exit_button():
                                                            win.destroy()
                                                        TC_exit = Button(win, text="Exit", font=("Calibri", 18), command=TC_exit_button)
                                                        TC_exit.place(x=482, y=560)

                                                passengers_details_continue = Button(win, text="Continue", font=("Calibri", 15), command=continue_filled_passengers_details)
                                                passengers_details_continue.place(x=460, y=520)
                                            save_flightSelection_and_continue = Button(win, text="Save Selection and Continue", command=save_and_continue)
                                            save_flightSelection_and_continue.place(x=410, y=660)
                                        elif flight_name_var.get() == 3:
                                            flight_details = Label(win, text="Flight Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                            flight_details.place(x=10, y=395)
                                            
                                            flight_name_label = Label(win, text="Flight Name:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_name_label.place(x=10, y=448)
                                            flight_code_label = Label(win, text="Flight Code:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_code_label.place(x=10, y=480)
                                            flight_departure_time_label = Label(win, text="Flight Departure Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_time_label.place(x=10, y=510)
                                            flight_departure_location_label = Label(win, text="Flight Departure Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_location_label.place(x=10, y=540)
                                            flight_arrival_location_label = Label(win, text="Flight Arrival Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_arrival_location_label.place(x=10, y=570)
                                            average_FlightFly_time_label = Label(win, text="Average Flight Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            average_FlightFly_time_label.place(x=10, y=600)
                                            flight_cost_label = Label(win, text="Flight Cost:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_cost_label.place(x=10, y=630)

                                            flight_name = Label(win, text=random_flight_name_3, font=("Calibri", 18), fg="Black")
                                            flight_name.place(x=141, y=448)
                                            flight_code = Label(win, text=IACA_code_flight_3, font=("Calibri", 18), fg="Black")
                                            flight_code.place(x=133, y=480)
                                            flight_departure_time = Label(win, text=flight_time, font=("Calibri", 18), fg="Black")
                                            flight_departure_time.place(x=240, y=510)
                                            flight_departure_location = Label(win, text=departure_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_departure_location.place(x=276,y=540)
                                            flight_arrival_location = Label(win, text=arrival_location_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_arrival_location.place(x=240, y=570)
                                            average_FlightFly_time = Label(win, text=(average_flight_time, 'minutes'), font=("Calibri", 18), fg="Black")
                                            average_FlightFly_time.place(x=220, y=600)
                                            flight_cost = Label(win, text=("USD", flight_cost_USD), font=("Calibri", 18), fg="Black")
                                            flight_cost.place(x=126, y=630)

                                            def save_and_continue():
                                                departure.place_forget()
                                                departure_entry.place_forget()
                                                arrival_location.place_forget()
                                                arrival_location_entry.place_forget()
                                                trip_type.place_forget()
                                                trip_type_combobox.place_forget()
                                                flights_available.place_forget()
                                                no_flight_name.place_forget
                                                flight_name_1.place_forget()
                                                flight_name_2.place_forget()
                                                flight_name_3.place_forget()
                                                flight_name_4.place_forget()
                                                flight_name_5.place_forget()
                                                flight_name_submitButton.place_forget()
                                                flight_details.place_forget()
                                                flight_name_label.place_forget()
                                                flight_code_label.place_forget()
                                                flight_departure_time_label.place_forget()
                                                flight_departure_location_label.place_forget()
                                                flight_arrival_location_label.place_forget()
                                                average_FlightFly_time_label.place_forget()
                                                flight_cost_label.place_forget()
                                                flight_name.place_forget()
                                                flight_code.place_forget()
                                                flight_departure_time.place_forget()
                                                flight_departure_location.place_forget()
                                                flight_arrival_location.place_forget()
                                                average_FlightFly_time.place_forget()
                                                flight_cost.place_forget()
                                                save_flightSelection_and_continue.place_forget()
                                                
                                                win.title("Flight Ticket Booking System System - Passenger Details")
                                                win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                win.maxsize(width=1000, height=70)
                                                win.minsize(width=1000, height=700)

                                                header = Label(win, text="Passenger Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                                header.place(x=370, y=0)
                                                sub_header = Label(win, text="Filling out all the details are mandatory", font=("Calibri", 13), fg="Black")
                                                sub_header.place(x=378, y=50)

                                                passenger_full_name = Label(win, text="Full Name:", font=("Calibri", 20), fg="Black")
                                                passenger_full_name.place(x=5, y=85)
                                                passenger_full_name_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_full_name_entry.place(x=130, y=87)

                                                passenger_contact_number = Label(win, text="Contact Number:", font=("Calibri", 20), fg="Black")
                                                passenger_contact_number.place(x=5, y=125)
                                                passenger_contact_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_contact_number_entry.place(x=199, y=127)
                                                passenger_contact_number_country_code = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                                                passenger_contact_number_country_code.place(x=35, y=155)

                                                passenger_email_id = Label(win, text="Email ID:", font=("Calibri", 20), fg="Black")
                                                passenger_email_id.place(x=5, y=185)
                                                passenger_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_email_id_entry.place(x=110, y=187)

                                                passenger_passport_number = Label(win, text="Passport number:", font=("Calibri", 20), fg="Black")
                                                passenger_passport_number.place(x=5, y=225)
                                                passenger_passport_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_passport_number_entry.place(x=208, y=227)

                                                passenger_unique_mark = Label(win, text="Unique Mark     :", font=("Calibri", 20), fg="Black")
                                                passenger_unique_mark.place(x=5, y=265)
                                                passenger_unique_mark_entry = Entry(win, width=30, font=("Calibri", 20))
                                                passenger_unique_mark_entry.place(x=192, y=267)

                                                def onClick_passenger_unique_mark_info():
                                                    win_unique_mark_info = Tk()
                                                    win_unique_mark_info.title("Flight Ticket Booking System System - Unique Mark Info")
                                                    win_unique_mark_info.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                    win_unique_mark_info.maxsize(width=600, height=200)
                                                    win_unique_mark_info.minsize(width=600, height=200)

                                                    info_icon = Label(win_unique_mark_info, text="ⓘ", font=("Calibri", 95), fg="Black")
                                                    info_icon.place(x=13, y=10)

                                                    unique_mark_info = Label(win_unique_mark_info, text='''Unique mark is a mark on passengers visible\nbody that can be easily identified by anyone.\nThis information is important incase if airport\nauthorities need to verify the passengers identity.\n''', font=("Calibri", 15), fg="Black")
                                                    unique_mark_info.place(x=150, y=12)

                                                    def destroy_win_unique_mark_info():
                                                        win_unique_mark_info.destroy()
                                                    destrory_unique_mark_info_win = Button(win_unique_mark_info, text="Okay", font=("Calibri", 14), command=destroy_win_unique_mark_info)
                                                    destrory_unique_mark_info_win.place(x=315, y=130)

                                                passenger_unique_mark_info = Button(win, text="ⓘ", font=("Calibri", 9), fg="Black", command=onClick_passenger_unique_mark_info)
                                                passenger_unique_mark_info.place(x=155, y=272)

                                                passenger_identity_proof = Label(win, text="Identity Proof:", font=("Calibri", 20), fg="Black")
                                                passenger_identity_proof.place(x=5, y=305)
                                                passenger_identity_proof_combobox = ttk.Combobox(win, state="readonly", width=36, font=("Calibri", 17), values = ("", "Aadhar Card", "Voter ID", "School/Company/Institution Recognized Card", "Driving License", "Birth Certificate", "Identity Certificate", "Service Identity Card"))
                                                passenger_identity_proof_combobox.current(0)
                                                passenger_identity_proof_combobox.place(x=170, y=312)

                                                passenger_luggage = Label(win, text="Exact total luggage passenger will be carrying (in Kgs):", font=("Calibri", 20), fg="Black")
                                                passenger_luggage.place(x=5, y=345)
                                                passenger_luggage_entry = Entry(win, width=3, font=("Calibri", 20))
                                                passenger_luggage_entry.place(x=600, y=347)

                                                passenger_food_type = Label(win, text="Passengers food preferred choice:", font=("Calibri", 20), fg="Black")
                                                passenger_food_type.place(x=5, y=385)
                                                passenger_food_type_combobox = ttk.Combobox(win, state="readonly", width=13, font=("Calibri", 17), values = ("", "Veg. Food", "Non-Veg. Food"))
                                                passenger_food_type_combobox.current(0)
                                                passenger_food_type_combobox.place(x=380, y=392)

                                                passenger_with_walking_diability = Label(win, text="Does passenger require any walking disability equipments?:", font=("Calibri", 20), fg="Black")
                                                passenger_with_walking_diability.place(x=5, y=425)
                                                passenger_with_walking_diability_combobox = ttk.Combobox(win, state="readonly", width=3, font=("Calibri", 17), values = ("", "Yes", "No"))
                                                passenger_with_walking_diability_combobox.current(0)
                                                passenger_with_walking_diability_combobox.place(x=663, y=430)

                                                passenger_other_requirements = Label(win, text="Passengers other requirements:", font=("Calibri", 20), fg="Black")
                                                passenger_other_requirements.place(x=5, y=465)
                                                passenger_other_requirements_entry = Entry(win, width=26, font=("Calibri", 20))
                                                passenger_other_requirements_entry.place(x=360, y=470)

                                                def continue_filled_passengers_details():
                                                    if passenger_full_name_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_contact_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_email_id_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_passport_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_unique_mark_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_identity_proof_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_luggage_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_food_type_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_with_walking_diability_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_other_requirements_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!") 
                                                    else:
                                                        processing_saving_passenger_details = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                        processing_saving_passenger_details.place(x=370, y=570)
                                                        processing_saving_passenger_details_progressBar = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                        processing_saving_passenger_details_progressBar.place(x=370, y=600)

                                                        
                                                        processing_saving_passenger_details_progressBar['value'] = 20
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 40
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        insert = (
                                                            "INSERT INTO passenger_and_flight_info (unique_user_id, passenger_full_name, passenger_contact_no, passenger_email_id, passenger_passport_number, passenger_unique_mark, passenger_identity_proof, passenger_luggage_weight, passenger_food_type, passenger_require_disability_equipment, passenger_flight_departure, passenger_flight_arrival, passenger_trip_type, passenger_flight_selected, passenger_flight_code, passenger_flight_departure_location, passenger_flight_arrival_location, passenger_flight_average_time, passenger_flight_cost)"
                                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                        )
                                                        data = (unique_user_id, passenger_full_name_entry.get(), passenger_contact_number_entry.get(), passenger_email_id_entry.get(), passenger_passport_number_entry.get(), passenger_unique_mark_entry.get(), passenger_identity_proof_combobox.get(), passenger_luggage_entry.get(), passenger_food_type_combobox.get(), passenger_with_walking_diability_combobox.get(), departure_entry.get(), arrival_location_entry.get(), trip_type_combobox.get(), random_flight_name_3, IACA_code_flight_3, departure_entry.get(), arrival_location_entry.get(), average_flight_time, flight_cost_USD)
                                                        
                                                        SQLcursor.execute(insert, data)
                                                        DB.commit()

                                                        processing_saving_passenger_details_progressBar['value'] = 60
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 80
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 100
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        header.place_forget()
                                                        sub_header.place_forget()
                                                        passenger_full_name.place_forget()
                                                        passenger_full_name_entry.place_forget()
                                                        passenger_contact_number.place_forget()
                                                        passenger_contact_number_country_code.place_forget()
                                                        passenger_contact_number_entry.place_forget()
                                                        passenger_email_id.place_forget()
                                                        passenger_email_id_entry.place_forget()
                                                        passenger_passport_number.place_forget()
                                                        passenger_passport_number_entry.place_forget()
                                                        passenger_unique_mark.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_unique_mark_info.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_identity_proof.place_forget()
                                                        passenger_identity_proof_combobox.place_forget()
                                                        passenger_luggage.place_forget()
                                                        passenger_luggage_entry.place_forget()
                                                        passenger_food_type.place_forget()
                                                        passenger_food_type_combobox.place_forget()
                                                        passenger_with_walking_diability.place_forget()
                                                        passenger_with_walking_diability_combobox.place_forget()
                                                        passenger_other_requirements.place_forget()
                                                        passenger_other_requirements_entry.place_forget()
                                                        processing_saving_passenger_details.place_forget()
                                                        processing_saving_passenger_details_progressBar.place_forget()
                                                        passengers_details_continue.place_forget()

                                                        terms_and_conditions_header = Label(win, text="Terms and Conditions", font=("Calibri", 25, BOLD, UNDERLINE), fg="Black")
                                                        terms_and_conditions_header.place(x=352, y=5)
                                                        terms_and_conditions = Label(win, text="To proceed, you need to agree to the all the terms and conditons mentioned below. \n 1. The data you have entered till now will be handed over to the respected authorities securely. \n 2. Flight history and other various data will be kept in our systems for giving you smooth experice each time you use this software. \n 3. Airline companies may contact you any time within working days. \n 4. If your luggage weighs over 50 Kgs, you'll be charged $10/kg. \n \n IF YOU AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK CONTINUE.\n IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK EXIT", wraplength=950, justify=LEFT, font=("Calibri", 18), fg="Black")
                                                        terms_and_conditions.place(x=5, y=50)

                                                        def TC_continue_button():
                                                            DB.commit()

                                                            terms_and_conditions_agreed_label = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                            terms_and_conditions_agreed_label.place(x=370, y=570)
                                                            terms_and_conditions_agreed = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                            terms_and_conditions_agreed.place(x=370, y=600)

                                                            terms_and_conditions_agreed['value'] = 20
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 40
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 60
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 80
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 100
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed.place_forget()
                                                            terms_and_conditions_agreed_label.place_forget()
                                                            terms_and_conditions_header.place_forget()
                                                            terms_and_conditions.place_forget()
                                                            TC_continue.place_forget()
                                                            TC_exit.place_forget()

                                                            win.title("Flight Ticket Booking System System - Email Confirmation")

                                                            user_email_id = Label(win, text="Enter your email below to finish processing your details and receive your ticket.", font=("Calibri", 25), wraplength=800)
                                                            user_email_id.place(x=135, y=200)
                                                            user_email_id_warning = Label(win, text="Make sure you enter valid email address, also the email must be in the correct format (example@exapmle.com) or else, the software application will close and all the information will be discared. This is done to prevent some unknown from gaining access to your data.", font=("Calibri", 12), wraplength=800)
                                                            user_email_id_warning.place(x=120, y=390)
                                                            user_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                            user_email_id_entry.place(x=363, y=290)

                                                            user_email_body = "THANK YOU FOR BOOKING YOUR FLIGHT TICKET WITH FLIGHT TICKET BOOKING SYSTEM\n\nHere are your final details, incase if you wish to change any of your detail/s or cancel your ticket, reply to this email.\n\nUnique ID: ", unique_user_id, "Name: ", passenger_full_name_entry.get()

                                                            def send_email():
                                                                user_email_id.place_forget()
                                                                user_email_id_entry.place_forget()
                                                                user_email_id_warning.place_forget()
                                                                user_email_id_submit.place_forget()

                                                                try:
                                                                    sending_email = Label(win, text="Sending you the ticket on your email. Please Wait...", font=("Calibri", 25), wraplength=800)
                                                                    sending_email.place(x=153, y=285)

                                                                    port = 465   
                                                                    smtp_server = "smtp.gmail.com"
                                                                    flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                    users_email = user_email_id_entry.get()
                                                                    flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                    email_body = user_email_body
                                                                    context = ssl.create_default_context()
                                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                        server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                        server.sendmail(flight_ticket_booking_system_email, users_email, email_body)
                                                                        sending_email.place_forget()

                                                                    ticket_booked = Label(win, text="✔", font=("Calibri", 110, BOLD), fg="Black")
                                                                    ticket_booked.place(x=440, y=180)

                                                                    email_sent = Label(win, text="We have sent you your flight ticket on your registered email ID, kindly check your inbox.", font=("Calibri", 15, BOLD), fg="Black")
                                                                    email_sent.place(x=135, y=360)

                                                                    def resend_email():
                                                                        port = 465
                                                                        smtp_server = "smtp.gmail.com"
                                                                        flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                        users_email = user_email_id_entry.get()
                                                                        flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                        email_body = user_email_body

                                                                        context = ssl.create_default_context()
                                                                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                            server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                            server.sendmail(flight_ticket_booking_system_email, users_email, email_body)

                                                                            email_sent = Label(win, text="Email sent", font=("Calibri", 12))
                                                                            email_sent.place(x=463, y=444)

                                                                    email_not_received_button = Button(win, text="Resend Email", command=resend_email)
                                                                    email_not_received_button.place(x=455, y=410)
                                                                except smtplib.SMTPRecipientsRefused:
                                                                    messagebox.showerror("Flight Ticket Booking System", "Email is not valid or its not in the correct format!\nThe software will close automatically in 5 seconds.")
                                                                    time.sleep(5)
                                                                    win.destroy()
                                                            user_email_id_submit = Button(win, text="Submit", font=("Calibri", 13), command=send_email)
                                                            user_email_id_submit.place(x=468, y=340)

                                                        TC_continue = Button(win, text="Continue", font=("Calibri", 18), command=TC_continue_button)
                                                        TC_continue.place(x=455, y=500)

                                                        def TC_exit_button():
                                                            win.destroy()
                                                        TC_exit = Button(win, text="Exit", font=("Calibri", 18), command=TC_exit_button)
                                                        TC_exit.place(x=482, y=560)

                                                passengers_details_continue = Button(win, text="Continue", font=("Calibri", 15), command=continue_filled_passengers_details)
                                                passengers_details_continue.place(x=460, y=520)
                                            save_flightSelection_and_continue = Button(win, text="Save Selection and Continue", command=save_and_continue)
                                            save_flightSelection_and_continue.place(x=410, y=660)
                                        elif flight_name_var.get() == 4:
                                            flight_details = Label(win, text="Flight Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                            flight_details.place(x=10, y=395)
                                            
                                            flight_name_label = Label(win, text="Flight Name:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_name_label.place(x=10, y=448)
                                            flight_code_label = Label(win, text="Flight Code:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_code_label.place(x=10, y=480)
                                            flight_departure_time_label = Label(win, text="Flight Departure Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_time_label.place(x=10, y=510)
                                            flight_departure_location_label = Label(win, text="Flight Departure Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_location_label.place(x=10, y=540)
                                            flight_arrival_location_label = Label(win, text="Flight Arrival Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_arrival_location_label.place(x=10, y=570)
                                            average_FlightFly_time_label = Label(win, text="Average Flight Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            average_FlightFly_time_label.place(x=10, y=600)
                                            flight_cost_label = Label(win, text="Flight Cost:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_cost_label.place(x=10, y=630)

                                            flight_name = Label(win, text=random_flight_name_4, font=("Calibri", 18), fg="Black")
                                            flight_name.place(x=141, y=448)
                                            flight_code = Label(win, text=IACA_code_flight_4, font=("Calibri", 18), fg="Black")
                                            flight_code.place(x=133, y=480)
                                            flight_departure_time = Label(win, text=flight_time, font=("Calibri", 18), fg="Black")
                                            flight_departure_time.place(x=240, y=510)
                                            flight_departure_location = Label(win, text=departure_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_departure_location.place(x=276,y=540)
                                            flight_arrival_location = Label(win, text=arrival_location_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_arrival_location.place(x=240, y=570)
                                            average_FlightFly_time = Label(win, text=(average_flight_time, 'minutes'), font=("Calibri", 18), fg="Black")
                                            average_FlightFly_time.place(x=220, y=600)
                                            flight_cost = Label(win, text=("USD", flight_cost_USD), font=("Calibri", 18), fg="Black")
                                            flight_cost.place(x=126, y=630)

                                            def save_and_continue():
                                                departure.place_forget()
                                                departure_entry.place_forget()
                                                arrival_location.place_forget()
                                                arrival_location_entry.place_forget()
                                                trip_type.place_forget()
                                                trip_type_combobox.place_forget()
                                                flights_available.place_forget()
                                                no_flight_name.place_forget
                                                flight_name_1.place_forget()
                                                flight_name_2.place_forget()
                                                flight_name_3.place_forget()
                                                flight_name_4.place_forget()
                                                flight_name_5.place_forget()
                                                flight_name_submitButton.place_forget()
                                                flight_details.place_forget()
                                                flight_name_label.place_forget()
                                                flight_code_label.place_forget()
                                                flight_departure_time_label.place_forget()
                                                flight_departure_location_label.place_forget()
                                                flight_arrival_location_label.place_forget()
                                                average_FlightFly_time_label.place_forget()
                                                flight_cost_label.place_forget()
                                                flight_name.place_forget()
                                                flight_code.place_forget()
                                                flight_departure_time.place_forget()
                                                flight_departure_location.place_forget()
                                                flight_arrival_location.place_forget()
                                                average_FlightFly_time.place_forget()
                                                flight_cost.place_forget()
                                                save_flightSelection_and_continue.place_forget()
                                                
                                                win.title("Flight Ticket Booking System System - Passenger Details")
                                                win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                win.maxsize(width=1000, height=70)
                                                win.minsize(width=1000, height=700)

                                                header = Label(win, text="Passenger Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                                header.place(x=370, y=0)
                                                sub_header = Label(win, text="Filling out all the details are mandatory", font=("Calibri", 13), fg="Black")
                                                sub_header.place(x=378, y=50)

                                                passenger_full_name = Label(win, text="Full Name:", font=("Calibri", 20), fg="Black")
                                                passenger_full_name.place(x=5, y=85)
                                                passenger_full_name_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_full_name_entry.place(x=130, y=87)

                                                passenger_contact_number = Label(win, text="Contact Number:", font=("Calibri", 20), fg="Black")
                                                passenger_contact_number.place(x=5, y=125)
                                                passenger_contact_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_contact_number_entry.place(x=199, y=127)
                                                passenger_contact_number_country_code = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                                                passenger_contact_number_country_code.place(x=35, y=155)

                                                passenger_email_id = Label(win, text="Email ID:", font=("Calibri", 20), fg="Black")
                                                passenger_email_id.place(x=5, y=185)
                                                passenger_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_email_id_entry.place(x=110, y=187)

                                                passenger_passport_number = Label(win, text="Passport number:", font=("Calibri", 20), fg="Black")
                                                passenger_passport_number.place(x=5, y=225)
                                                passenger_passport_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_passport_number_entry.place(x=208, y=227)

                                                passenger_unique_mark = Label(win, text="Unique Mark     :", font=("Calibri", 20), fg="Black")
                                                passenger_unique_mark.place(x=5, y=265)
                                                passenger_unique_mark_entry = Entry(win, width=30, font=("Calibri", 20))
                                                passenger_unique_mark_entry.place(x=192, y=267)

                                                def onClick_passenger_unique_mark_info():
                                                    win_unique_mark_info = Tk()
                                                    win_unique_mark_info.title("Flight Ticket Booking System System - Unique Mark Info")
                                                    win_unique_mark_info.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                    win_unique_mark_info.maxsize(width=600, height=200)
                                                    win_unique_mark_info.minsize(width=600, height=200)

                                                    info_icon = Label(win_unique_mark_info, text="ⓘ", font=("Calibri", 95), fg="Black")
                                                    info_icon.place(x=13, y=10)

                                                    unique_mark_info = Label(win_unique_mark_info, text='''Unique mark is a mark on passengers visible\nbody that can be easily identified by anyone.\nThis information is important incase if airport\nauthorities need to verify the passengers identity.\n''', font=("Calibri", 15), fg="Black")
                                                    unique_mark_info.place(x=150, y=12)

                                                    def destroy_win_unique_mark_info():
                                                        win_unique_mark_info.destroy()
                                                    destrory_unique_mark_info_win = Button(win_unique_mark_info, text="Okay", font=("Calibri", 14), command=destroy_win_unique_mark_info)
                                                    destrory_unique_mark_info_win.place(x=315, y=130)

                                                passenger_unique_mark_info = Button(win, text="ⓘ", font=("Calibri", 9), fg="Black", command=onClick_passenger_unique_mark_info)
                                                passenger_unique_mark_info.place(x=155, y=272)

                                                passenger_identity_proof = Label(win, text="Identity Proof:", font=("Calibri", 20), fg="Black")
                                                passenger_identity_proof.place(x=5, y=305)
                                                passenger_identity_proof_combobox = ttk.Combobox(win, state="readonly", width=36, font=("Calibri", 17), values = ("", "Aadhar Card", "Voter ID", "School/Company/Institution Recognized Card", "Driving License", "Birth Certificate", "Identity Certificate", "Service Identity Card"))
                                                passenger_identity_proof_combobox.current(0)
                                                passenger_identity_proof_combobox.place(x=170, y=312)

                                                passenger_luggage = Label(win, text="Exact total luggage passenger will be carrying (in Kgs):", font=("Calibri", 20), fg="Black")
                                                passenger_luggage.place(x=5, y=345)
                                                passenger_luggage_entry = Entry(win, width=3, font=("Calibri", 20))
                                                passenger_luggage_entry.place(x=600, y=347)

                                                passenger_food_type = Label(win, text="Passengers food preferred choice:", font=("Calibri", 20), fg="Black")
                                                passenger_food_type.place(x=5, y=385)
                                                passenger_food_type_combobox = ttk.Combobox(win, state="readonly", width=13, font=("Calibri", 17), values = ("", "Veg. Food", "Non-Veg. Food"))
                                                passenger_food_type_combobox.current(0)
                                                passenger_food_type_combobox.place(x=380, y=392)

                                                passenger_with_walking_diability = Label(win, text="Does passenger require any walking disability equipments?:", font=("Calibri", 20), fg="Black")
                                                passenger_with_walking_diability.place(x=5, y=425)
                                                passenger_with_walking_diability_combobox = ttk.Combobox(win, state="readonly", width=3, font=("Calibri", 17), values = ("", "Yes", "No"))
                                                passenger_with_walking_diability_combobox.current(0)
                                                passenger_with_walking_diability_combobox.place(x=663, y=430)

                                                passenger_other_requirements = Label(win, text="Passengers other requirements:", font=("Calibri", 20), fg="Black")
                                                passenger_other_requirements.place(x=5, y=465)
                                                passenger_other_requirements_entry = Entry(win, width=26, font=("Calibri", 20))
                                                passenger_other_requirements_entry.place(x=360, y=470)

                                                def continue_filled_passengers_details():
                                                    if passenger_full_name_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_contact_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_email_id_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_passport_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_unique_mark_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_identity_proof_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_luggage_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_food_type_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_with_walking_diability_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_other_requirements_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!") 
                                                    else:
                                                        processing_saving_passenger_details = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                        processing_saving_passenger_details.place(x=370, y=570)
                                                        processing_saving_passenger_details_progressBar = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                        processing_saving_passenger_details_progressBar.place(x=370, y=600)

                                                        
                                                        processing_saving_passenger_details_progressBar['value'] = 20
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 40
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        insert = (
                                                            "INSERT INTO passenger_and_flight_info (unique_user_id, passenger_full_name, passenger_contact_no, passenger_email_id, passenger_passport_number, passenger_unique_mark, passenger_identity_proof, passenger_luggage_weight, passenger_food_type, passenger_require_disability_equipment, passenger_flight_departure, passenger_flight_arrival, passenger_trip_type, passenger_flight_selected, passenger_flight_code, passenger_flight_departure_location, passenger_flight_arrival_location, passenger_flight_average_time, passenger_flight_cost)"
                                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                        )
                                                        data = (unique_user_id, passenger_full_name_entry.get(), passenger_contact_number_entry.get(), passenger_email_id_entry.get(), passenger_passport_number_entry.get(), passenger_unique_mark_entry.get(), passenger_identity_proof_combobox.get(), passenger_luggage_entry.get(), passenger_food_type_combobox.get(), passenger_with_walking_diability_combobox.get(), departure_entry.get(), arrival_location_entry.get(), trip_type_combobox.get(), random_flight_name_4, IACA_code_flight_4, departure_entry.get(), arrival_location_entry.get(), average_flight_time, flight_cost_USD)
                                                        
                                                        SQLcursor.execute(insert, data)
                                                        DB.commit()

                                                        processing_saving_passenger_details_progressBar['value'] = 60
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 80
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 100
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        header.place_forget()
                                                        sub_header.place_forget()
                                                        passenger_full_name.place_forget()
                                                        passenger_full_name_entry.place_forget()
                                                        passenger_contact_number.place_forget()
                                                        passenger_contact_number_country_code.place_forget()
                                                        passenger_contact_number_entry.place_forget()
                                                        passenger_email_id.place_forget()
                                                        passenger_email_id_entry.place_forget()
                                                        passenger_passport_number.place_forget()
                                                        passenger_passport_number_entry.place_forget()
                                                        passenger_unique_mark.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_unique_mark_info.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_identity_proof.place_forget()
                                                        passenger_identity_proof_combobox.place_forget()
                                                        passenger_luggage.place_forget()
                                                        passenger_luggage_entry.place_forget()
                                                        passenger_food_type.place_forget()
                                                        passenger_food_type_combobox.place_forget()
                                                        passenger_with_walking_diability.place_forget()
                                                        passenger_with_walking_diability_combobox.place_forget()
                                                        passenger_other_requirements.place_forget()
                                                        passenger_other_requirements_entry.place_forget()
                                                        processing_saving_passenger_details.place_forget()
                                                        processing_saving_passenger_details_progressBar.place_forget()
                                                        passengers_details_continue.place_forget()

                                                        terms_and_conditions_header = Label(win, text="Terms and Conditions", font=("Calibri", 25, BOLD, UNDERLINE), fg="Black")
                                                        terms_and_conditions_header.place(x=352, y=5)
                                                        terms_and_conditions = Label(win, text="To proceed, you need to agree to the all the terms and conditons mentioned below. \n 1. The data you have entered till now will be handed over to the respected authorities securely. \n 2. Flight history and other various data will be kept in our systems for giving you smooth experice each time you use this software. \n 3. Airline companies may contact you any time within working days. \n 4. If your luggage weighs over 50 Kgs, you'll be charged $10/kg. \n \n IF YOU AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK CONTINUE.\n IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK EXIT", wraplength=950, justify=LEFT, font=("Calibri", 18), fg="Black")
                                                        terms_and_conditions.place(x=5, y=50)

                                                        def TC_continue_button():
                                                            DB.commit()

                                                            terms_and_conditions_agreed_label = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                            terms_and_conditions_agreed_label.place(x=370, y=570)
                                                            terms_and_conditions_agreed = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                            terms_and_conditions_agreed.place(x=370, y=600)

                                                            terms_and_conditions_agreed['value'] = 20
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 40
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 60
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 80
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 100
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed.place_forget()
                                                            terms_and_conditions_agreed_label.place_forget()
                                                            terms_and_conditions_header.place_forget()
                                                            terms_and_conditions.place_forget()
                                                            TC_continue.place_forget()
                                                            TC_exit.place_forget()

                                                            win.title("Flight Ticket Booking System System - Email Confirmation")

                                                            user_email_id = Label(win, text="Enter your email below to finish processing your details and receive your ticket.", font=("Calibri", 25), wraplength=800)
                                                            user_email_id.place(x=135, y=200)
                                                            user_email_id_warning = Label(win, text="Make sure you enter valid email address, also the email must be in the correct format (example@exapmle.com) or else, the software application will close and all the information will be discared. This is done to prevent some unknown from gaining access to your data.", font=("Calibri", 12), wraplength=800)
                                                            user_email_id_warning.place(x=120, y=390)
                                                            user_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                            user_email_id_entry.place(x=363, y=290)

                                                            user_email_body = "THANK YOU FOR BOOKING YOUR FLIGHT TICKET WITH FLIGHT TICKET BOOKING SYSTEM\n\nHere are your final details, incase if you wish to change any of your detail/s or cancel your ticket, reply to this email.\n\nUnique ID: ", unique_user_id, "Name: ", passenger_full_name_entry.get()

                                                            def send_email():
                                                                user_email_id.place_forget()
                                                                user_email_id_entry.place_forget()
                                                                user_email_id_warning.place_forget()
                                                                user_email_id_submit.place_forget()

                                                                try:
                                                                    sending_email = Label(win, text="Sending you the ticket on your email. Please Wait...", font=("Calibri", 25), wraplength=800)
                                                                    sending_email.place(x=153, y=285)

                                                                    port = 465   
                                                                    smtp_server = "smtp.gmail.com"
                                                                    flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                    users_email = user_email_id_entry.get()
                                                                    flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                    email_body = user_email_body
                                                                    context = ssl.create_default_context()
                                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                        server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                        server.sendmail(flight_ticket_booking_system_email, users_email, email_body)
                                                                        sending_email.place_forget()

                                                                    ticket_booked = Label(win, text="✔", font=("Calibri", 110, BOLD), fg="Black")
                                                                    ticket_booked.place(x=440, y=180)

                                                                    email_sent = Label(win, text="We have sent you your flight ticket on your registered email ID, kindly check your inbox.", font=("Calibri", 15, BOLD), fg="Black")
                                                                    email_sent.place(x=135, y=360)

                                                                    def resend_email():
                                                                        port = 465
                                                                        smtp_server = "smtp.gmail.com"
                                                                        flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                        users_email = user_email_id_entry.get()
                                                                        flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                        email_body = user_email_body

                                                                        context = ssl.create_default_context()
                                                                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                            server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                            server.sendmail(flight_ticket_booking_system_email, users_email, email_body)

                                                                            email_sent = Label(win, text="Email sent", font=("Calibri", 12))
                                                                            email_sent.place(x=463, y=444)

                                                                    email_not_received_button = Button(win, text="Resend Email", command=resend_email)
                                                                    email_not_received_button.place(x=455, y=410)
                                                                except smtplib.SMTPRecipientsRefused:
                                                                    messagebox.showerror("Flight Ticket Booking System", "Email is not valid or its not in the correct format!\nThe software will close automatically in 5 seconds.")
                                                                    time.sleep(5)
                                                                    win.destroy()
                                                            user_email_id_submit = Button(win, text="Submit", font=("Calibri", 13), command=send_email)
                                                            user_email_id_submit.place(x=468, y=340)

                                                        TC_continue = Button(win, text="Continue", font=("Calibri", 18), command=TC_continue_button)
                                                        TC_continue.place(x=455, y=500)

                                                        def TC_exit_button():
                                                            win.destroy()
                                                        TC_exit = Button(win, text="Exit", font=("Calibri", 18), command=TC_exit_button)
                                                        TC_exit.place(x=482, y=560)

                                                passengers_details_continue = Button(win, text="Continue", font=("Calibri", 15), command=continue_filled_passengers_details)
                                                passengers_details_continue.place(x=460, y=520)
                                            save_flightSelection_and_continue = Button(win, text="Save Selection and Continue", command=save_and_continue)
                                            save_flightSelection_and_continue.place(x=410, y=660)
                                                
                                        elif flight_name_var.get() == 5:
                                            flight_details = Label(win, text="Flight Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                            flight_details.place(x=10, y=395)
                                            
                                            flight_name_label = Label(win, text="Flight Name:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_name_label.place(x=10, y=448)
                                            flight_code_label = Label(win, text="Flight Code:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_code_label.place(x=10, y=480)
                                            flight_departure_time_label = Label(win, text="Flight Departure Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_time_label.place(x=10, y=510)
                                            flight_departure_location_label = Label(win, text="Flight Departure Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_departure_location_label.place(x=10, y=540)
                                            flight_arrival_location_label = Label(win, text="Flight Arrival Location:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_arrival_location_label.place(x=10, y=570)
                                            average_FlightFly_time_label = Label(win, text="Average Flight Time:", font=("Calibri", 18, BOLD), fg="Black")
                                            average_FlightFly_time_label.place(x=10, y=600)
                                            flight_cost_label = Label(win, text="Flight Cost:", font=("Calibri", 18, BOLD), fg="Black")
                                            flight_cost_label.place(x=10, y=630)

                                            flight_name = Label(win, text=random_flight_name_5, font=("Calibri", 18), fg="Black")
                                            flight_name.place(x=141, y=448)
                                            flight_code = Label(win, text=IACA_code_flight_5, font=("Calibri", 18), fg="Black")
                                            flight_code.place(x=133, y=480)
                                            flight_departure_time = Label(win, text=flight_time, font=("Calibri", 18), fg="Black")
                                            flight_departure_time.place(x=240, y=510)
                                            flight_departure_location = Label(win, text=departure_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_departure_location.place(x=276,y=540)
                                            flight_arrival_location = Label(win, text=arrival_location_entry.get(), font=("Calibri", 18), fg="Black")
                                            flight_arrival_location.place(x=240, y=570)
                                            average_FlightFly_time = Label(win, text=(average_flight_time, 'minutes'), font=("Calibri", 18), fg="Black")
                                            average_FlightFly_time.place(x=220, y=600)
                                            flight_cost = Label(win, text=("USD", flight_cost_USD), font=("Calibri", 18), fg="Black")
                                            flight_cost.place(x=126, y=630)

                                            def save_and_continue():
                                                departure.place_forget()
                                                departure_entry.place_forget()
                                                arrival_location.place_forget()
                                                arrival_location_entry.place_forget()
                                                trip_type.place_forget()
                                                trip_type_combobox.place_forget()
                                                flights_available.place_forget()
                                                no_flight_name.place_forget
                                                flight_name_1.place_forget()
                                                flight_name_2.place_forget()
                                                flight_name_3.place_forget()
                                                flight_name_4.place_forget()
                                                flight_name_5.place_forget()
                                                flight_name_submitButton.place_forget()
                                                flight_details.place_forget()
                                                flight_name_label.place_forget()
                                                flight_code_label.place_forget()
                                                flight_departure_time_label.place_forget()
                                                flight_departure_location_label.place_forget()
                                                flight_arrival_location_label.place_forget()
                                                average_FlightFly_time_label.place_forget()
                                                flight_cost_label.place_forget()
                                                flight_name.place_forget()
                                                flight_code.place_forget()
                                                flight_departure_time.place_forget()
                                                flight_departure_location.place_forget()
                                                flight_arrival_location.place_forget()
                                                average_FlightFly_time.place_forget()
                                                flight_cost.place_forget()
                                                save_flightSelection_and_continue.place_forget()
                                                
                                                win.title("Flight Ticket Booking System System - Passenger Details")
                                                win.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                win.maxsize(width=1000, height=70)
                                                win.minsize(width=1000, height=700)

                                                header = Label(win, text="Passenger Details", font=("Calibri", 30, BOLD, ITALIC, UNDERLINE), fg="Black")
                                                header.place(x=370, y=0)
                                                sub_header = Label(win, text="Filling out all the details are mandatory", font=("Calibri", 13), fg="Black")
                                                sub_header.place(x=378, y=50)

                                                passenger_full_name = Label(win, text="Full Name:", font=("Calibri", 20), fg="Black")
                                                passenger_full_name.place(x=5, y=85)
                                                passenger_full_name_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_full_name_entry.place(x=130, y=87)

                                                passenger_contact_number = Label(win, text="Contact Number:", font=("Calibri", 20), fg="Black")
                                                passenger_contact_number.place(x=5, y=125)
                                                passenger_contact_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_contact_number_entry.place(x=199, y=127)
                                                passenger_contact_number_country_code = Label(win, text="(with country code)", font=("Calibri", 10), fg="Black")
                                                passenger_contact_number_country_code.place(x=35, y=155)

                                                passenger_email_id = Label(win, text="Email ID:", font=("Calibri", 20), fg="Black")
                                                passenger_email_id.place(x=5, y=185)
                                                passenger_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_email_id_entry.place(x=110, y=187)

                                                passenger_passport_number = Label(win, text="Passport number:", font=("Calibri", 20), fg="Black")
                                                passenger_passport_number.place(x=5, y=225)
                                                passenger_passport_number_entry = Entry(win, width=20, font=("Calibri", 20))
                                                passenger_passport_number_entry.place(x=208, y=227)

                                                passenger_unique_mark = Label(win, text="Unique Mark     :", font=("Calibri", 20), fg="Black")
                                                passenger_unique_mark.place(x=5, y=265)
                                                passenger_unique_mark_entry = Entry(win, width=30, font=("Calibri", 20))
                                                passenger_unique_mark_entry.place(x=192, y=267)

                                                def onClick_passenger_unique_mark_info():icon.ico
                                                    win_unique_mark_info = Tk()
                                                    win_unique_mark_info.title("Flight Ticket Booking System System - Unique Mark Info")
                                                    win_unique_mark_info.iconbitmap("#PASTE THE LOCATION YOU COPIED OF ICON.ICO FILE#")
                                                    win_unique_mark_info.maxsize(width=600, height=200)
                                                    win_unique_mark_info.minsize(width=600, height=200)

                                                    info_icon = Label(win_unique_mark_info, text="ⓘ", font=("Calibri", 95), fg="Black")
                                                    info_icon.place(x=13, y=10)

                                                    unique_mark_info = Label(win_unique_mark_info, text='''Unique mark is a mark on passengers visible\nbody that can be easily identified by anyone.\nThis information is important incase if airport\nauthorities need to verify the passengers identity.\n''', font=("Calibri", 15), fg="Black")
                                                    unique_mark_info.place(x=150, y=12)

                                                    def destroy_win_unique_mark_info():
                                                        win_unique_mark_info.destroy()
                                                    destrory_unique_mark_info_win = Button(win_unique_mark_info, text="Okay", font=("Calibri", 14), command=destroy_win_unique_mark_info)
                                                    destrory_unique_mark_info_win.place(x=315, y=130)

                                                passenger_unique_mark_info = Button(win, text="ⓘ", font=("Calibri", 9), fg="Black", command=onClick_passenger_unique_mark_info)
                                                passenger_unique_mark_info.place(x=155, y=272)

                                                passenger_identity_proof = Label(win, text="Identity Proof:", font=("Calibri", 20), fg="Black")
                                                passenger_identity_proof.place(x=5, y=305)
                                                passenger_identity_proof_combobox = ttk.Combobox(win, state="readonly", width=36, font=("Calibri", 17), values = ("", "Aadhar Card", "Voter ID", "School/Company/Institution Recognized Card", "Driving License", "Birth Certificate", "Identity Certificate", "Service Identity Card"))
                                                passenger_identity_proof_combobox.current(0)
                                                passenger_identity_proof_combobox.place(x=170, y=312)

                                                passenger_luggage = Label(win, text="Exact total luggage passenger will be carrying (in Kgs):", font=("Calibri", 20), fg="Black")
                                                passenger_luggage.place(x=5, y=345)
                                                passenger_luggage_entry = Entry(win, width=3, font=("Calibri", 20))
                                                passenger_luggage_entry.place(x=600, y=347)

                                                passenger_food_type = Label(win, text="Passengers food preferred choice:", font=("Calibri", 20), fg="Black")
                                                passenger_food_type.place(x=5, y=385)
                                                passenger_food_type_combobox = ttk.Combobox(win, state="readonly", width=13, font=("Calibri", 17), values = ("", "Veg. Food", "Non-Veg. Food"))
                                                passenger_food_type_combobox.current(0)
                                                passenger_food_type_combobox.place(x=380, y=392)

                                                passenger_with_walking_diability = Label(win, text="Does passenger require any walking disability equipments?:", font=("Calibri", 20), fg="Black")
                                                passenger_with_walking_diability.place(x=5, y=425)
                                                passenger_with_walking_diability_combobox = ttk.Combobox(win, state="readonly", width=3, font=("Calibri", 17), values = ("", "Yes", "No"))
                                                passenger_with_walking_diability_combobox.current(0)
                                                passenger_with_walking_diability_combobox.place(x=663, y=430)

                                                passenger_other_requirements = Label(win, text="Passengers other requirements:", font=("Calibri", 20), fg="Black")
                                                passenger_other_requirements.place(x=5, y=465)
                                                passenger_other_requirements_entry = Entry(win, width=26, font=("Calibri", 20))
                                                passenger_other_requirements_entry.place(x=360, y=470)

                                                def continue_filled_passengers_details():
                                                    if passenger_full_name_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_contact_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_email_id_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_passport_number_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_unique_mark_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_identity_proof_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_luggage_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_food_type_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_with_walking_diability_combobox.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!")
                                                    elif passenger_other_requirements_entry.get() == "":
                                                        messagebox.showerror("Flight Ticket Booking System", "Must ensure that you've filled all the details!") 
                                                    else:
                                                        processing_saving_passenger_details = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                        processing_saving_passenger_details.place(x=370, y=570)
                                                        processing_saving_passenger_details_progressBar = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                        processing_saving_passenger_details_progressBar.place(x=370, y=600)

                                                        
                                                        processing_saving_passenger_details_progressBar['value'] = 20
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 40
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        insert = (
                                                            "INSERT INTO passenger_and_flight_info (unique_user_id, passenger_full_name, passenger_contact_no, passenger_email_id, passenger_passport_number, passenger_unique_mark, passenger_identity_proof, passenger_luggage_weight, passenger_food_type, passenger_require_disability_equipment, passenger_flight_departure, passenger_flight_arrival, passenger_trip_type, passenger_flight_selected, passenger_flight_code, passenger_flight_departure_location, passenger_flight_arrival_location, passenger_flight_average_time, passenger_flight_cost)"
                                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                        )
                                                        data = (unique_user_id, passenger_full_name_entry.get(), passenger_contact_number_entry.get(), passenger_email_id_entry.get(), passenger_passport_number_entry.get(), passenger_unique_mark_entry.get(), passenger_identity_proof_combobox.get(), passenger_luggage_entry.get(), passenger_food_type_combobox.get(), passenger_with_walking_diability_combobox.get(), departure_entry.get(), arrival_location_entry.get(), trip_type_combobox.get(), random_flight_name_5, IACA_code_flight_5, departure_entry.get(), arrival_location_entry.get(), average_flight_time, flight_cost_USD)
                                                        
                                                        SQLcursor.execute(insert, data)
                                                        DB.commit()

                                                        processing_saving_passenger_details_progressBar['value'] = 60
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 80
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        processing_saving_passenger_details_progressBar['value'] = 100
                                                        win.update_idletasks()
                                                        time.sleep(0.5)

                                                        header.place_forget()
                                                        sub_header.place_forget()
                                                        passenger_full_name.place_forget()
                                                        passenger_full_name_entry.place_forget()
                                                        passenger_contact_number.place_forget()
                                                        passenger_contact_number_country_code.place_forget()
                                                        passenger_contact_number_entry.place_forget()
                                                        passenger_email_id.place_forget()
                                                        passenger_email_id_entry.place_forget()
                                                        passenger_passport_number.place_forget()
                                                        passenger_passport_number_entry.place_forget()
                                                        passenger_unique_mark.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_unique_mark_info.place_forget()
                                                        passenger_unique_mark_entry.place_forget()
                                                        passenger_identity_proof.place_forget()
                                                        passenger_identity_proof_combobox.place_forget()
                                                        passenger_luggage.place_forget()
                                                        passenger_luggage_entry.place_forget()
                                                        passenger_food_type.place_forget()
                                                        passenger_food_type_combobox.place_forget()
                                                        passenger_with_walking_diability.place_forget()
                                                        passenger_with_walking_diability_combobox.place_forget()
                                                        passenger_other_requirements.place_forget()
                                                        passenger_other_requirements_entry.place_forget()
                                                        processing_saving_passenger_details.place_forget()
                                                        processing_saving_passenger_details_progressBar.place_forget()
                                                        passengers_details_continue.place_forget()

                                                        terms_and_conditions_header = Label(win, text="Terms and Conditions", font=("Calibri", 25, BOLD, UNDERLINE), fg="Black")
                                                        terms_and_conditions_header.place(x=352, y=5)
                                                        terms_and_conditions = Label(win, text="To proceed, you need to agree to the all the terms and conditons mentioned below. \n 1. The data you have entered till now will be handed over to the respected authorities securely. \n 2. Flight history and other various data will be kept in our systems for giving you smooth experice each time you use this software. \n 3. Airline companies may contact you any time within working days. \n 4. If your luggage weighs over 50 Kgs, you'll be charged $10/kg. \n \n IF YOU AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK CONTINUE.\n IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS GIVEN ABOVE, CLICK EXIT", wraplength=950, justify=LEFT, font=("Calibri", 18), fg="Black")
                                                        terms_and_conditions.place(x=5, y=50)

                                                        def TC_continue_button():
                                                            DB.commit()

                                                            terms_and_conditions_agreed_label = Label(win, text="Processing and Saving your details...", font=("Calibri", 15), fg="Black")
                                                            terms_and_conditions_agreed_label.place(x=370, y=570)
                                                            terms_and_conditions_agreed = ttk.Progressbar(win, orient=HORIZONTAL, length=310)
                                                            terms_and_conditions_agreed.place(x=370, y=600)

                                                            terms_and_conditions_agreed['value'] = 20
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 40
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 60
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 80
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed['value'] = 100
                                                            win.update_idletasks()
                                                            time.sleep(0.5)

                                                            terms_and_conditions_agreed.place_forget()
                                                            terms_and_conditions_agreed_label.place_forget()
                                                            terms_and_conditions_header.place_forget()
                                                            terms_and_conditions.place_forget()
                                                            TC_continue.place_forget()
                                                            TC_exit.place_forget()
                                                            

                                                            win.title("Flight Ticket Booking System System - Email Confirmation")

                                                            user_email_id = Label(win, text="Enter your email below to finish processing your details and receive your ticket.", font=("Calibri", 25), wraplength=800)
                                                            user_email_id.place(x=135, y=200)
                                                            user_email_id_warning = Label(win, text="Make sure you enter valid email address, also the email must be in the correct format (example@exapmle.com) or else, the software application will close and all the information will be discared. This is done to prevent some unknown from gaining access to your data.", font=("Calibri", 12), wraplength=800)
                                                            user_email_id_warning.place(x=120, y=390)
                                                            user_email_id_entry = Entry(win, width=20, font=("Calibri", 20))
                                                            user_email_id_entry.place(x=363, y=290)

                                                            user_email_body = "THANK YOU FOR BOOKING YOUR FLIGHT TICKET WITH FLIGHT TICKET BOOKING SYSTEM\n\nHere are your final details, incase if you wish to change any of your detail/s or cancel your ticket, reply to this email.\n\nUnique ID: ", unique_user_id, "Name: ", passenger_full_name_entry.get()

                                                            def send_email():
                                                                user_email_id.place_forget()
                                                                user_email_id_entry.place_forget()
                                                                user_email_id_warning.place_forget()
                                                                user_email_id_submit.place_forget()

                                                                try:
                                                                    sending_email = Label(win, text="Sending you the ticket on your email. Please Wait...", font=("Calibri", 25), wraplength=800)
                                                                    sending_email.place(x=153, y=285)

                                                                    port = 465   
                                                                    smtp_server = "smtp.gmail.com"
                                                                    flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                    users_email = user_email_id_entry.get()
                                                                    flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                    email_body = user_email_body
                                                                    context = ssl.create_default_context()
                                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                        server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                        server.sendmail(flight_ticket_booking_system_email, users_email, email_body)
                                                                        sending_email.place_forget()

                                                                    ticket_booked = Label(win, text="✔", font=("Calibri", 110, BOLD), fg="Black")
                                                                    ticket_booked.place(x=440, y=180)

                                                                    email_sent = Label(win, text="We have sent you your flight ticket on your registered email ID, kindly check your inbox.", font=("Calibri", 15, BOLD), fg="Black")
                                                                    email_sent.place(x=135, y=360)

                                                                    def resend_email():
                                                                        port = 465
                                                                        smtp_server = "smtp.gmail.com"
                                                                        flight_ticket_booking_system_email = "#GOOGLE ACCOUNT EMAIL#"
                                                                        users_email = user_email_id_entry.get()
                                                                        flight_ticket_booking_system_password = '#GOOGLE ACCOUNT PASSWORD#'
                                                                        email_body = user_email_body

                                                                        context = ssl.create_default_context()
                                                                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                                            server.login(flight_ticket_booking_system_email, flight_ticket_booking_system_password)
                                                                            server.sendmail(flight_ticket_booking_system_email, users_email, email_body)

                                                                            email_sent = Label(win, text="Email sent", font=("Calibri", 12))
                                                                            email_sent.place(x=463, y=444)

                                                                    email_not_received_button = Button(win, text="Resend Email", command=resend_email)
                                                                    email_not_received_button.place(x=455, y=410)
                                                                except smtplib.SMTPRecipientsRefused:
                                                                    messagebox.showerror("Flight Ticket Booking System", "Email is not valid or its not in the correct format!\nThe software will close automatically in 5 seconds.")
                                                                    time.sleep(5)
                                                                    win.destroy()
                                                            user_email_id_submit = Button(win, text="Submit", font=("Calibri", 13), command=send_email)
                                                            user_email_id_submit.place(x=468, y=340)

                                                        TC_continue = Button(win, text="Continue", font=("Calibri", 18), command=TC_continue_button)
                                                        TC_continue.place(x=455, y=500)

                                                        def TC_exit_button():
                                                            win.destroy()
                                                        TC_exit = Button(win, text="Exit", font=("Calibri", 18), command=TC_exit_button)
                                                        TC_exit.place(x=482, y=560)

                                                passengers_details_continue = Button(win, text="Continue", font=("Calibri", 15), command=continue_filled_passengers_details)
                                                passengers_details_continue.place(x=460, y=520)
                                            save_flightSelection_and_continue = Button(win, text="Save Selection and Continue", command=save_and_continue)
                                            save_flightSelection_and_continue.place(x=410, y=660)
                                        else:
                                            messagebox.showerror("Flight Ticket Booking System System", "An error occured, please try again!")

                                    flight_name_var = IntVar()
                                    no_flight_name = Radiobutton(win, text="", value=0, font=("Calibri", 18), fg="Black")
                                    flight_name_1 = Radiobutton(win, text=random_flight_name_1, variable=flight_name_var, value=1, font=("Calibri", 18), fg="Black")
                                    flight_name_1.place(x=5, y=160)
                                    flight_name_2 = Radiobutton(win, text=random_flight_name_2, variable=flight_name_var, value=2, font=("Calibri", 18), fg="Black")
                                    flight_name_2.place(x=5, y=200)
                                    flight_name_3 = Radiobutton(win, text=random_flight_name_3, variable=flight_name_var, value=3, font=("Calibri", 18), fg="Black")
                                    flight_name_3.place(x=5, y=240)
                                    flight_name_4 = Radiobutton(win, text=random_flight_name_4, variable=flight_name_var, value=4, font=("Calibri", 18), fg="Black")
                                    flight_name_4.place(x=5, y=280)
                                    flight_name_5 = Radiobutton(win, text=random_flight_name_5, variable=flight_name_var, value=5, font=("Calibri", 18), fg="Black")
                                    flight_name_5.place(x=5, y=320)
                                    flight_name_submitButton = Button(win, text="Get Flight Details", command=get_flight_details)
                                    flight_name_submitButton.place(x=425, y=365)
                                else:
                                    messagebox.showerror("Flight Ticket Booking System System", "An error occured, please try again!")
                            submit_choosed_flight_details = Button(win, text="Search Flights", command=check_details_and_search_flights)
                            submit_choosed_flight_details.place(x=455, y=130)
                        elif result == 0:
                            messagebox.showerror("Flight Ticket Booking System System", "Username or Password Incorrect.\n Note: You must sign-up first to sign-in.")
                        else:
                            messagebox.showerror("Flight Ticket Booking System System", "An error occoured, please try restarting the application.\n If error still persists, please reach to us at airlineticketbookingsystem@test.com")

                        DB.commit()
                    submit_signin_credentials = Button(win, text="Submit", font=("Calibri", 15, BOLD), activebackground="#b5bab6", command=submit_sign_in_credentials)
                    submit_signin_credentials.place(x=462, y=325)

                signup_button = Button(win, text="Sign-Up", height=3, width=15, activebackground="#b5bab6", command=switch_to_signup_window)
                signup_button.place(x=425, y=275)
                signin_button = Button(win, text="Sign-In", height=3, width=15, activebackground="#b5bab6", command=switch_to_signin_window)
                signin_button.place(x=425, y=365)

            win.after(7100, main_application)
            win.mainloop()
except (ImportError, KeyboardInterrupt, MemoryError, OSError, RuntimeError, SystemError, SystemExit, UnboundLocalError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError) as e:
    messagebox.showwarning("Flight Ticket Booking System System", "An error occured while starting the application. Try restarting the application.")
