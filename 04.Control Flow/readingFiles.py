# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# # print(employee_file.readlines())
# # print(employee_file.readline())

# employee_file.close()


# employee_file = open("employees.txt", "a")
# employee_file.write("Toby - Human Resources")
# employee_file.close()


# employee_file = open("employees1.txt", "w+")
# print(employee_file.read())
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()


employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

