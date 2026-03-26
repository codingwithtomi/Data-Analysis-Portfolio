# prompt the user to write an email and strip
# if email does not have 1 @ symbol, print error message
#

email = input("Enter email: ").strip().replace(" ", "")
if "@" not in email:
    print("Invalid: missing @ symbol")
elif email.count("@") != 1:
    print("Invalid email")
else:
    username, domain = email.split("@")

    if username == "" or domain == "":
        print("Invalid email")
    elif not "." in domain:
        print("Invalid domain")
    else:
        print("Valid email")
