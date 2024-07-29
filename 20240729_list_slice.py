def check_number(numbers):
  number_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
  print('Only {} are binary numbers!".format(number_list[:2]))
  for number in numbers:
      if number.upper() not in number_list[:2]:
          print("{} is not binary".format(numbers))
          return 'false'
  print{"{} is an awesome binary number!".format(numbers))
  return 'true'
def main():
    stop_running = 'false'
    print("i will keep asking until you give me a valid binary number!")
    while stop_running != 'true':
        user_input = input("Enter a valid binary number:")
        stop_running = check_number(user_input)

if __name__ == "__main__":
  main()
  
