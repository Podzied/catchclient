import s as catchlient


email_address = f"hsdgsd@zumruttepe.com"  # Construct an example email
inbox_data = catchlient.getinbox(email_address)

print(inbox_data)


# Step 3: Retrieve content of the first email, if available
for email in inbox_data["emails"]:
    body = catchlient.getemail(email["link"])
    print(body)

# if inbox_data["emails"]:
#     email_link = inbox_data["emails"][1]["link"]
#     message_body = catchlient.getemail(email_link)
#     print("\nMessage Body of First Email:")
#     print(message_body)
# else:
#     print("No emails to fetch content from.")
