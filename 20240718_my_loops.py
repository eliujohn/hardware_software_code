def while_counter(num):
    while num > 0:
        print("while count: {}".format(num))
        num += -1
def for_counter(num):
    for count in range(num,0, -1):
        pritn("For count:{}".format(count))
def main():
    counter = 10
    while_counter(counter)
    for_counter(counter)

if __name__ == "__main__":
    main():
