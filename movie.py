import sqlite3

print("$$$$$$$$$$$$ CARNIVAL CINEMA BOOKING $$$$$$$$$$$$$$")

def setup_database():
    try:
        conn = sqlite3.connect('cinema_booking.db')
        c = conn.cursor()

        c.execute('''
        CREATE TABLE IF NOT EXISTS cinema1 (
            mname TEXT,
            phno TEXT,
            tic INTEGER,
            sex TEXT,
            fname TEXT,
            lname TEXT,
            passwd INTEGER,
            userID TEXT,
            snacks TEXT
        )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS cinema2 (
            mname TEXT,
            name TEXT,
            tickets INTEGER,
            phno TEXT,
            passwd TEXT,
            snacks TEXT
        )
        ''')

        conn.commit()
        conn.close()
        print("Database setup complete!")
    except sqlite3.Error as e:
        print(f"Database setup error: {e}")

def theater():
    print("Which screen do you want to watch movie: ")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")

    try:
        a = int(input("Choose your screen: "))
        if a in [1, 2, 3]:
            timing(a)
        else:
            print("Invalid screen choice. Please select 1, 2, or 3.")
            theater()
    except ValueError:
        print("Please enter a valid number.")
        theater()

def timing(a):
    time1 = {
        "1": "10:00-13:00",
        "2": "13:10-16:10",
        "3": "16:20-19:20",
        "4": "19:30-22:30"
    }
    time2 = {
        "1": "10:15-13:15",
        "2": "13:25-16:25",
        "3": "16:35-19:35",
        "4": "19:45-22:45"
    }
    time3 = {
        "1": "10:30-13:30",
        "2": "13:40-16:40",
        "3": "16:50-19:50",
        "4": "20:00-22:45"
    }

    if a == 1:
        print("Choose your time:")
        for key, value in time1.items():
            print(f"{key}. {value}")
        t = input("Select your time (1-4): ")
        if t in time1:
            x = time1[t]
            print("Successful! Enjoy movie at " + x)
        else:
            print("Invalid time selection. Please try again.")
            timing(a)
    elif a == 2:
        print("Choose your time:")
        for key, value in time2.items():
            print(f"{key}. {value}")
        t = input("Select your time (1-4): ")
        if t in time2:
            x = time2[t]
            print("Successful! Enjoy movie at " + x)
        else:
            print("Invalid time selection. Please try again.")
            timing(a)
    elif a == 3:
        print("Choose your time:")
        for key, value in time3.items():
            print(f"{key}. {value}")
        t = input("Select your time (1-4): ")
        if t in time3:
            x = time3[t]
            print("Successful! Enjoy movie at " + x)
        else:
            print("Invalid time selection. Please try again.")
            timing(a)
    return 0

f = 0

def movie():
    global f
    f = f + 1
    print("Which movie do you want to watch?")
    print("1. JURASSIC PARK")
    print("2. HARRY POTTER AND CURSE CHILD")
    print("3. AVENGERS END GAME")
    print("4. TANHAJI: THE UNSUNG WARRIOR")
    print("5. DIL BECHARA")
    print("6. PANGA")
    print("7. GUNJAN SAXENA")
    print("8. FAST AND FURIOUS")
    print("9. Back")

    try:
        movie_choice = int(input("Choose your movie: "))
        if movie_choice == 9:
            city()
            return 0
        elif 1 <= movie_choice <= 8:
            if f == 1:
                theater()
        else:
            print("Invalid choice. Please select a number between 1 and 9.")
            movie()
    except ValueError:
        print("Please enter a valid number.")
        movie()

def city():
    print("Where do you want to watch movie?:")
    print("1. HYDERABAD")
    print("2. MUMBAI")
    print("3. BANGALORE")
    print("4. CHENNAI")
    print("5. AHEMDABAD")
    print("6. CHANDIGARH")
    print("7. PUNE")
    print("8. KOLKATA")
    print("9. DELHI")
    print("10. KOCHI")
    print("11. OTHER")

    try:
        place = int(input("Choose your option: "))
        if 1 <= place <= 10:
            movie()
        elif place == 11:
            x = input("TYPE YOUR DESIRED PLACE, IF NOT IN OPTION: ")
            movie()
        else:
            print("Invalid choice. Please select a number between 1 and 11.")
            city()
    except ValueError:
        print("Please enter a valid number.")
        city()

def main():
    setup_database()

    try:
        city()

        print("Select seat class:")
        print("1. FIRST CLASS SEATS")
        print("2. SECOND CLASS SEATS")
        print("3. Cancel booking")

        try:
            ch = int(input("Enter your choice: "))

            try:
                conn = sqlite3.connect('cinema_booking.db')
                c1 = conn.cursor()

                if ch == 1:
                    print("WELCOME TO FIRST CLASS BOOKING")
                    mname = input("Enter the movie name: ")
                    phno = input("Enter phone number: ")

                    try:
                        tic = int(input("Enter total tickets: "))
                        if tic <= 0:
                            print("Number of tickets must be greater than zero")
                            return
                    except ValueError:
                        print("Please enter a valid number for tickets")
                        return

                    sex = input("Enter your sex (M/F/Other): ")
                    fname = input("Enter your first name: ")
                    lname = input("Enter your last name: ")

                    try:
                        passwd = int(input("Enter your password (numeric): "))
                    except ValueError:
                        print("Password must be numeric")
                        return

                    userID = input("Enter your userID: ")
                    snacks = input("Order your snacks: ")

                    try:
                        c1.execute("SELECT SUM(tic) FROM cinema1")
                        result = c1.fetchone()
                        current_tickets = result[0] if result[0] is not None else 0

                        if current_tickets + tic > 100:
                            print("Sorry, only", (100 - current_tickets), "tickets available")
                            return

                        c1.execute(
                            "INSERT INTO cinema1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (mname, phno, tic, sex, fname, lname, passwd, userID, snacks)
                        )
                        conn.commit()

                        print("Ticket booked successfully!")
                        total = 500 * tic
                        print('TOTAL AMOUNT: Rs.', total)
                        print("THANK YOU FOR VISITING CARNIVAL CINEMAS")

                        print("Ratings:")
                        rate = input("HOW WAS YOUR EXPERIENCE? (POOR/GOOD/EXCELLENT): ").upper()
                        if rate == 'POOR':
                            print("We deeply regret for the inconvenience")
                        elif rate == 'GOOD':
                            print("Do share your suggestions on how we could improve our policies")
                        else:
                            print("THANKS!! DO VISIT AGAIN")

                    except sqlite3.Error as e:
                        print(f"Database error: {e}")
                        conn.rollback()

                elif ch == 2:
                    print("WELCOME TO SECOND CLASS BOOKING")
                    c = input("Enter your movie name: ")
                    a = input("Enter your name: ")

                    try:
                        d = int(input("Enter total tickets: "))
                        if d <= 0:
                            print("Number of tickets must be greater than zero")
                            return
                    except ValueError:
                        print("Please enter a valid number for tickets")
                        return

                    b = input("Enter your phone number: ")
                    pswd = input("Enter the password: ")
                    sks = input("Order your snacks: ")

                    try:
                        c1.execute(
                            "INSERT INTO cinema2 VALUES (?, ?, ?, ?, ?, ?)",
                            (c, a, d, b, pswd, sks)
                        )
                        conn.commit()

                        print("*********************TICKET BOOKED***********************")
                        tot = 250 * d
                        print('TOTAL AMOUNT: Rs.', tot)

                    except sqlite3.Error as e:
                        print(f"Database error: {e}")
                        conn.rollback()

                elif ch == 3:
                    y = input("Do you want to cancel the booking? (YES/NO): ").lower()
                    if y == 'yes':
                        print("BOOKING CANCELLED")
                    else:
                        print("CONTINUING WITH BOOKING PROCESS")
                        main()

                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
                    main()

                conn.close()

            except sqlite3.Error as e:
                print(f"Database connection error: {e}")

        except ValueError:
            print("Please enter a valid choice (1, 2, or 3)")

    finally:
        print("///////////////ENJOY THE MOVIE AND HAVE FUN/////////////////")

if __name__ == "__main__":
    main()
