'''
This is an application module that allows a user to select if
running the API or not, and then run the application.
'''


MENU = '''
********* Crime Visualization Module *********
Welcome to the crime visualization application! Please choose
an option to perform a task.
(1) Update Data from Source
(2) Use saved data (up to Feb/22/22)
(3) Quit the program
'''
START = 1
END = 3
script_fn = "app.py"

def retrieve_task():
    option = -1
    while True:
        print(MENU)
        option = int(input("Option: "))
        if option >= START and option <= END:
            break
        else:
            print(f"Invalid option({option})")
    return option

OPTIONS_HANDLER = {
    1: lambda: update_data(),
    2: lambda: run_app()
}

def update_data():
    exec(open(script_fn).read())

def run_app():
    exec(open(script_fn).read())

def main():
    while True:
        option = retrieve_task()
        if option == 3:
            break
        else:
            handler = OPTIONS_HANDLER[option]
            handler()

if __name__ == "__main__":
    main()