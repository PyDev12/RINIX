# import 
import time 
import os 

# Input set
def KC():
    kc =input("")
    
    if kc == "help":
        print("help - Shows a list of commands")
        print("quit - exit - close - Quits the kernel program")
        print("clear - cls - clears the screen of the terminal")
        print("patches - Displays the patchnotes")
        KC()
    
    # close vairables 
    if kc == "quit":
        time.sleep(2)  
        quit()

    if kc == "exit":
        time.sleep(2)
        quit()
    
    if kc == "close":
        time.sleep(2)
        quit()


    # close vairables
    
    # clear vairables
    if kc == "clear":
        os.system("clear")
        KC()
        
    if kc == "cls":
        os.system("clear")
        KC()

    # clear vairables

    if kc == "patches":
        print("Version 0.3 Patchnotes")
        print("changed message for bad command to Invalid command ")
        KC()

    if kc != "help":
       if kc != "quit":
           if kc != "clear":
               if kc != "patches":
                   if kc != "exit":
                       if kc != "close":
                           if kc != "cls":
                                print("Invalid command")
                                KC()




KC()
