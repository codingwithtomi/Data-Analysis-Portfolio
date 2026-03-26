first_name = input("First name: ")
last_name = input("Last name: ")
company = input("Company: ")

username = f"{first_name}.{last_name}"
website = f"{company}.com"
email = f"{username}@{website}".lower().replace(" ", "")
print(f"Generated email: {email}")


# First name: John
# Last name: Smith
# Company: Company: Acme Corp Acme Corp
# Generated email: john.smith@acmecorp.com
