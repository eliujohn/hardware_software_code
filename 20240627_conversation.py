def conversation():
    print("do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes" :
        print("thats good - the united states needs more coders!!")
    else:
        print("perhaps you will change your mind")
    print("goodbye")
def main():
    print("welcome to my conversation program")
    conversation()
    print("thanks for chatting with me")
if __name__ == "__main__":
    main()
