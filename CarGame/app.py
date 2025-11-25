while True:
    command = input("> ").lower()
    is_running = False
    
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - exit''')
    elif command == "start":
        if is_running == True:
            print("The car is already started.")
        else:
            print("Car started... Ready to go")
            is_running = True
    elif command == "stop":
        if is_running == False:
            print("The car is already stopped.")
        else:
            print("Car stopped.")
            is_running = False
    elif command == "quit":
        break
    else:
        print("I don't understand that.")
