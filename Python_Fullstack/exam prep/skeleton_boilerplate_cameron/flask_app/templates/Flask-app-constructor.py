import os

project_name = input("Project Name: ")
# location = input ("Location(file path): ")
"D:/Coding_Dojo_Classes/Python_Stack"
location = "D:/Coding_Dojo_Classes/Python_Stack"
ultimate_location = os.path.join(location,project_name)
# print(ultimate_location)
# print(location)
# os.makedirs(project_name)
# to do: make a for loop for each endpoint
# os.makedirs(f"{project_name}/flask_app/templates")
# os.makedirs(f"{project_name}/flask_app/controllers")
# os.makedirs(f"{project_name}/flask_app/models")
# os.makedirs(f"{project_name}/flask_app/config")
# os.makedirs(f"{project_name}/flask_app/static")

folders = ["","flask_app", "flask_app/templates", "flask_app/controllers", "flask_app/models", "flask_app/config", "flask_app/static"]
files = [["server.py"], ["__init__.py"]["index.html", "dashboard.html"], ["users_controller.py"], ["user_model.py"], ["mysqlconnection.py"], ["style.css"]]
# coud we make these a dictionary of folder: [files...] key value pairs?

for i in range(len(folders)):
    # print(folders[i])
    # create a folder via path location
    folder_path = os.path.join(ultimate_location, "flask_app")
    # open(folder_path, "x")
    module_path = os.path.join(folder_path)
    # print(module_path)
    os.makedirs(module_path, exist_ok=True)
    for file in files[i]:
        # print(f"{folder_path}/{file}")
        file_path = os.path.join(module_path, file)
        open(file_path, "x")

# open(file_path, "x") other flags: x, w


# make a directory for the project
# base on project name supplied by the user in the terminal
# in a specific location in the computer
# write server.py file