# OTT Login Program

username = input("Enter the User Name: ").strip()
password = input("Enter the Password: ").strip()

subscription = True
attempts = 3

print("\n------- LOGIN -------")

while attempts > 0:
    user = input("Enter the Username: ").strip()
    pwd = input("Enter the Password: ").strip()

    if user == username and pwd == password:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("Invalid Credentials")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Account Locked")

else:

    while True:
        print("\n------ OTT PLATFORM ------")
        print("1. View Subscription")
        print("2. Watch Movies")
        print("3. Watch Series")
        print("4. Search Content")
        print("5. Logout")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            if subscription:
                print("Premium Subscription Active")
            else:
                print("No Active Subscription")

        elif choice == "2":
            if subscription:
                print("\nMovies Available")
                print("1. Godavari")
                print("2. Love Today")
                print("3. Dear")

                movie = input("Select Movie Number: ")

                if movie == "1":
                    print("Playing Godavari...")
                elif movie == "2":
                    print("Playing Love Today...")
                elif movie == "3":
                    print("Playing Dear...")
                else:
                    print("Invalid Movie Selection")
            else:
                print("Please Buy Subscription")

        elif choice == "3":
            if subscription:
                print("\nSeries Available")
                print("1. Stranger Things")
                print("2. Wednesday")
                print("3. Money Heist")

                series = input("Select Series Number: ")

                if series == "1":
                    print("Playing Stranger Things...")
                elif series == "2":
                    print("Playing Wednesday...")
                elif series == "3":
                    print("Playing Money Heist...")
                else:
                    print("Invalid Series Selection")
            else:
                print("Please Buy Subscription")

        elif choice == "4":
            search = input("Enter Movie/Series Name: ").strip().lower()

            if search == "godavari":
                print("Godavari Found")
            elif search == "love today":
                print("Love Today Found")
            elif search == "dear":
                print("Dear Found")
            elif search == "stranger things":
                print("Stranger Things Found")
            elif search == "wednesday":
                print("Wednesday Found")
            elif search == "money heist":
                print("Money Heist Found")
            else:
                print("Content Not Available")

        elif choice == "5":
            print("Logged Out Successfully")
            break

        else:
            print("Invalid Choice. Please Try Again.") s