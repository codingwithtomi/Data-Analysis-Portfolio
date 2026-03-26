usernames = ["admin", "moderator", "editor", "viewer"]

login = input("Enter username: ")

if login in usernames:
    print(f"Access granted. Welcome {login}!")
else:
    print(f"Access denied. '{login}' is not authorized")
