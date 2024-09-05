# Global Scope

x = 10  # This value will be accessible anywhere in the file.


def function():
    print(x)


function()


# Local Scope

def another():
    y = 20  # This value of x is only limited to this function. Hence Local Scope
    print(x)


another()

# Enclosed Scope


def me():
    my_name = "Muzammil"  # enlcosed value with enclosed scope.
    print(my_name)

    def you():
        your_name = "Ammar"  # can be called here in the enclosed scope
        # but not outside this nested fucntion becuase it does not have
        # global scope
        print(your_name)

    you()


me()


# Built in functions
# Built in functions are like print(), len() etc. etc. that are already there
# They are available everywhere in the program.


# Modifying the assignment of function in local scope which is first
# defined in the global scope.


name = "Dave"
count = 1


def another():
    color = "blue"
    global count  # Modifying the global value in local scope.
    count += 1  # global count could not be printed in a single line
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
