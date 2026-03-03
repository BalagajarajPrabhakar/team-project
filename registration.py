# ============================================
#      SMART USER REGISTRATION SYSTEM
#          (NO LIBRARIES USED)
# ============================================

users = []

print("=" * 50)
print("      🌟 WELCOME TO REGISTRATION SYSTEM 🌟")
print("=" * 50)

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # ================= REGISTER =================
    if choice == "1":

        print("\n--- USER REGISTRATION ---")

        name = input("👤 Enter Name: ")

        # Email validation loop
        while True:
            email = input("📧 Enter Email: ")
            if "@" in email and "." in email:
                break
            else:
                print("❌ Invalid Email! Try again.")

        username = input("🆔 Enter Username: ")

        # Password Strength Check
        while True:
            password = input("🔒 Enter Password: ")

            if len(password) < 6:
                print("❌ Weak Password (Minimum 6 characters)")
            elif password.isalpha() or password.isdigit():
                print("⚠ Medium Password (Use letters + numbers)")
                break
            else:
                print("✅ Strong Password")
                break

        # Phone validation
        while True:
            phone = input("📱 Enter Phone Number: ")
            if phone.isdigit() and len(phone) == 10:
                break
            else:
                print("❌ Phone must be 10 digits!")

        # OTP Simulation (Without Random)
        # Creating simple OTP using last 4 digits of phone
        otp = phone[-4:]
        print("\n🔐 Your OTP is:", otp)

        user_otp = input("Enter OTP: ")

        if user_otp == otp:
            users.append({
                "name": name,
                "email": email,
                "username": username,
                "password": password,
                "phone": phone
            })
            print("🎉 Registration Successful!")
        else:
            print("❌ Wrong OTP! Registration Failed.")

    # ================= LOGIN =================
    elif choice == "2":

        print("\n--- LOGIN ---")

        login_user = input("Enter Username: ")
        login_pass = input("Enter Password: ")

        found = False

        for user in users:
            if user["username"] == login_user and user["password"] == login_pass:
                print(f"\n✅ Welcome {user['name']}!")
                found = True
                break

        if not found:
            print("❌ Invalid Username or Password!")

    # ================= EXIT =================
    elif choice == "3":
        print("Thank you for using the system 😊")
        break

    else:
        print("❌ Invalid choice! Try again.")