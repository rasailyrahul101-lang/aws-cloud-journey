# #Variables
# name = "Rahul"
# age = 22
# is_cloud_engineer = True
# course = "AWS Cloud Engineering"

# #Print output
# print("Name:", name)
# print("Age:", age)
# print("Cloud Engineer:", is_cloud_engineer)

# #f-string - clenaer way to print
# print(f"My name is {name} and i am learning {course}")

# # User input
# city = input("Where are you from? ")
# print(f"Cool! {city} is a great place to learn cloud engineering!")

# # If/else
# experience = input("Have you used AWS before? (yes/no) ")

# if experience == "yes":
#     print("Great! You have a head start!")
# elif experience == "no":
#     print("No worries! Everyone starts from zero!")
# else:
#     print("Please answer yes or no!")

# # List of AWS services
# aws_services = ["EC2", "S3", "Lambda", "RDS", "VPC"]

# # Loop through list
# print("\nAWS Services I will learn:")
# for service in aws_services:
#     print(f"  - {service}")

# # Loop with range
# print("\nWeeks in my roadmap:")
# for week in range(1, 9):
#     print(f"  Week {week}")

# # While loop
# print("\nCountdown to cloud engineer:")
# count = 5
# while count > 0:
#     print(f"  {count}...")
#     count -= 1
# print("  🚀 Launch!")


# # Basic function
# def greet_engineer(name, skill):
#     return f"Hello {name}! Your skill is {skill}."

# # Call the function
# message = greet_engineer("Rahul", "AWS")
# print(message)

# # Function with default value
# def describe_service(service, provider="AWS"):
#     return f"{service} is a service by {provider}"

# print(describe_service("EC2"))
# print(describe_service("Blob Storage", "Azure"))

# # Function that does calculation
# def calculate_hosts(cidr):
#     hosts = (2 ** (32 - cidr)) - 2
#     return f"/{cidr} network has {hosts} usable hosts"

# print(calculate_hosts(24))
# print(calculate_hosts(16))
# print(calculate_hosts(28))


# # Write to a file
# with open("aws_services.txt", "w") as f:
#     f.write("EC2 - Virtual Machine\n")
#     f.write("S3 - Object Storage\n")
#     f.write("Lambda - Serverless\n")
#     f.write("RDS - Database\n")
#     f.write("VPC - Virtual Network\n")

# print("File written successfully!")

# # Read from a file
# with open("aws_services.txt", "r") as f:
#     contents = f.read()
#     print("\nFile contents:")
#     print(contents)

# # Read line by line
# with open("aws_services.txt", "r") as f:
#     print("Line by line:")
#     for line in f:
#         print(f"  {line.strip()}")

# Import built-in libraries
# import os
# import datetime

# # os library — interact with operating system
# current_directory = os.getcwd()
# print(f"Current directory: {current_directory}")

# # List files in current directory
# files = os.listdir(".")
# print(f"\nFiles in directory:")
# for file in files:
#     print(f"  - {file}")

# # datetime library — work with dates and times
# now = datetime.datetime.now()
# print(f"\nCurrent date and time: {now}")
# print(f"Year: {now.year}")
# print(f"Month: {now.month}")
# print(f"Day: {now.day}")

# # Check if a file exists
# if os.path.exists("aws_services.txt"):
#     print("\naws_services.txt exists ✅")
# else:
#     print("\naws_services.txt not found ❌")

# def check_port(port):

#     if port == 80 :
#         return f"{port} port provides http"
#     elif port == 443 :
#         return f"{port} port provides https"
#     elif port == 22 :
#         return f"{port} port provides ssh"
#     elif port == 3306 :
#         return f"{port} port connects mysql"
#     else:
#         return "Unknown Sevice"
    
# port = int(input("Enter port number:"))
# result = check_port(port)
# print(result)


import os    
with open("my_journey.txt","w") as f:
    f.write("Name : Rahul\n")
    f.write("City : Pokhara\n")
    f.write("Goal : AWS CLoud Engineer")

with open("my_journey.txt","r") as f:
    for line in f:
        print(f"{line.strip()}")


if os.path.exists("my_journey.txt"):
    print("\n it exist.")
else:
    print("\n doesnt exist.")