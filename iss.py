
#!/usr/bin/python3

iss = {"message": "success", "timestamp": 1593527983, "iss_position": {"longitude": "37.6029", "latitude": "-50.6039"}}


#user _input = input("Where are you located?")

print("\nWhat is the ISS location?")
print("\nThe ISS is located in position latitude of : " + iss["iss_position"]["latitude"] + " and" +  " longitude of: " + iss["iss_position"]["longitude"])
print("\nDo you want to continue? [Y/n]")
user_input = input()

#while user_input == "Y" or user_input == "y":


if user_input == "Y" or user_input == "y":
    print("\nWhat is the ISS timestamp?")
    print("\nThe ISS timestamp value is: ", iss["timestamp"])
    print(iss.get("message")+ "!")
else:
    print("Thank you for your service!")


