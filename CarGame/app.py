# input help:
# start - start the car 
# stop - stop the car 
# quit - exit

# other things: "I don't understand that"

# start: "Car started... Ready to go"
# stop: "Car stopped."
# exit: quits the program

exit = False

while not exit:
    command = input(">").lower()

    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - exit''')
    elif command == "start":
        print("Car started... Ready to go")
    elif command == "stop":
        print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("I don't understand that.")