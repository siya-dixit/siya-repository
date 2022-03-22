{% include nav.html %}
## Week 1

Python Lists Vs Dictionaries 
- List is a collection of index values pairs as that of array in JS. Dictionary is a hashed structure of key and value pairs.

#### InfoDB Lists
```aidl
infoDb = []
# List with dictionary records placed in a list  
infoDb.append({  
               "FirstName": "Siya",  
               "LastName": "Dixit",  
               "DOB": "July 30",  
               "Location": "San Diego",  
               "Personal Email": "dsiya006@gmail.com",  
               "Fav_Colors":["Pink","Blue","Lavender"]  
              })  
```
#### Print the second car from Mort's Owns_Cars list
```
x = InfoDb[0]["Fav_Colors"][1] 
result: Blue
 ```

#### There is also a method called get() on the Dictionary(InfoDb[0]) that will give you the same result:
```aidl
x = InfoDb[0].get("Fav_Colors")[2]
result: Lavender
```

#### Print Content from InfoDB
```aidl
# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Colors: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Fav_Colors"]))  # join allows printing a string list with separator
    print()



def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```

#### While Loop
```aidl
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
```

#### For Loop
```aidl
# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
```
<hr style="  border-top: 8px solid #bbb;
  border-radius: 5px;">

### Tri 3 TT0 Python Menu, Replit, Github

#### Python Menu w/ data structures and try/except statements

```aidl
# menu.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import loopy
import mathpy
import funcy
import patterns


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Stringy", "stringy.py"],
    ["Listy", "listy.py"],
    ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathpy.factors],
    ["GCD", mathpy.gcd],
    ["LCM", mathpy.lcm],
    ["Primes", mathpy.primes],
]

patterns_sub_menu = [
    ["Patterns", "patterns.py"],
    ["PreFuncy", "prefuncy.py"],
    ["Funcy", funcy.ship],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```
