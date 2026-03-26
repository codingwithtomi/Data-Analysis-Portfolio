name = input("Username: ")
password = input("Password: ")

if name == "admin" and password == "secure456":
    print("Login successful!")
elif name != "admin" and password == "secure456":
    print("Login failed: incorrect username.")
elif name == "admin" and password != "secure456":
    print("Login failed: incorrect password.")
elif name != "admin" and password != "secure456":
    print("Login failed: Invalid credentials.")
