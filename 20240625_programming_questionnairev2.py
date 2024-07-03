def main():
    name = input("what is your name?")
    print("We want to know if you want to learn to program!")
    print()
    print("Do you want to learn how to program?" + name + "?")
    answer = input()
    if answer == "yes":
        print("Well, thats Great! lets get started," + name)
    elif answer == "no":
        print("Well atleast try to learn!")
    else:
        print("Your not funny. Answer the question.")


if __name__ == "__main__":
    main()
