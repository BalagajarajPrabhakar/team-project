print("=" * 50)
print("        WELCOME TO USER REGISTRATION")
print("=" * 50)

# Name
name = input("Enter your Name: ")

# Email validation
email = input("Enter your Email: ")
while "@" not in email or "." not in email:
    print("Invalid email format! Please try again.")
    email = input("Enter your Email: ")

# Username
username = input("Create a Username: ")

# Strong Password Validation
while True:
    password = input("Create a Strong Password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print(" Password must contain at least one UPPERCASE letter.")
    elif not any(char.islower() for char in password):
        print("❌ Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("❌ Password must contain at least one number.")
    elif not any(char in "@#$%^&*!" for char in password):
        print("❌ Password must contain at least one special character (@#$%^&*!).")
    else:
        print("✅ Strong Password Created!")
        break

# Password Strength Display
if len(password) >= 12:
    strength = "Very Strong 💪"
elif len(password) >= 10:
    strength = "Strong 🙂"
else:
    strength = "Moderate 😐"

# Phone number validation
phone = input("Enter your Phone Number (10 digits): ")
while not phone.isdigit() or len(phone) != 10:
    print("Invalid phone number! Enter exactly 10 digits.")
    phone = input("Enter your Phone Number (10 digits): ")

# Hide password with stars
hidden_password = "*" * len(password)

print("\n" + "=" * 50)
print("🎉 REGISTRATION SUCCESSFUL 🎉")
print("=" * 50)

print(f"Name       : {name}")
print(f"Email      : {email}")
print(f"Username   : {username}")
print(f"Password   : {hidden_password}")
print(f"Strength   : {strength}")
print(f"Phone      : {phone}")

# Save details into file
with open("users.txt", "a") as file:
    file.write(f"{username},{password}\n")

print("\nUser details saved successfully!")

# Login System
print("\n" + "=" * 50)
print("              LOGIN SYSTEM")
print("=" * 50)

login_user = input("Enter Username: ")
login_pass = input("Enter Password: ")

if login_user == username and login_pass == password:
    print("Login Successful ✅ Welcome,", name)
else:
    print("Invalid Username or Password ❌")

print("=" * 50)


