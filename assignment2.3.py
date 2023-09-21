user_input = input("Enter seconds: ")
user_input = int(user_input)
hours = user_input // 3600 
seconds = user_input % 3600
minutes = user_input // 60
seconds = user_input % 60
print (user_input, "seconds is", hours, "hours",minutes, "minutes", seconds, "seconds")
