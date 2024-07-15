from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_menu():
    menu_dict = {
        '1': 'apples',
        '2': 'bananas',
        'x': 'exit_program'
    }
    return menu_dict

def display_menu(menu_dict):
    print('\t\t\tFruit Menu')
    print('')
    for item, value in menu_dict.items():
        print("\t\t{}. {}".format(item, value.replace('-', '').capitalize()))
    menu_selection = input("\n\t\tEnter Selection: ").lower()
    return menu_dict.get(menu_selection, "invalid_entry")

def apples():
    input("You selected apples.")
    return 'false'

def bananas():
    input("You selected bananas.")
    return 'false'

def invalid_entry():
    input("Invalid Entry!!")
    return 'false'

def exit_program():
    print("Good Bye!!!")
    return 'true'

def main():
    done_selecting = 'false'
    while done_selecting != 'true':
        clear_screen()
        get_selection = display_menu(get_menu())
        done_selecting = eval(get_selection+"()")

if __name__ == "__main__":
    main()
