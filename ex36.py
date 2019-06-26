from sys import exit

print "You are Thanos and you need one more stone to finish your infinity gauntlet"
print "There are three doors in front of you numbered 1-3"
print "Each door has its own challenge but only one leads to the soul stone"
survive = False

def start(survive):
    
    print "Choose the door you want to enter"
    
    door = int(raw_input("> "))
    
    if door == 1 and not survive:
        thor()
    
    elif door == 2 and not survive:
        gamora()
        
    elif door == 3:
        timeloop()
        
    else:
        print "Use your head a bit, dodo! Give a valid input"

def thor():
    print "You enter the room where Thor is waiting for you with stormbreaker."
    print "He throws it towards you. what do you do?"
    response = raw_input("> ")
    
    if "move aside" in response:
        print "Well done. The axe cuts your hand off and you die."
        exit(0)
        
    elif "use gauntlet" in response:
        print "wrong move, storm breaker cuts you in two & you die."
        exit(0)
        
    elif "use reality stone" in response:
        print "smart move, you survided the attack and killed Thor. You start again!"
        survive = True
        start(survive)
        
    else:
        print "Stupid move! Thor kills you and eats you for dinner. Bye Bye!"
        exit(0)
        
def gamora():
    print "Gamora waits for you in the room with a knife in hand. Do you kill her or capture her?"
    
    response = raw_input("> ")
    
    if "capture" in response:
        print "You exchanged her life for the stone. You have now received the soul stone."
        snap()
            
    elif "kill" in response:
        print "You killed her and survived the room. you have to go back out & choose a room again."
        survive = True
        start(survive)
        
    else:
    
        print"Too late!, you  are dead! Bye Bye."
        exit(0)
        
def timeloop():
    print "You entered the room where doctor strange captured you in a time loop. you lose! Bye Bye."
    exit(0)
    
def snap():
    print "You have all the stones now. Do you snap the finger and kill 50% of all life or use it to kill specific beings?"
    response = raw_input("> ")
    
    if "snap" in response:
        print "You successfully killed half the population. Now you can rest in the garden. Congratulations!"
        exit(0)
    else:
        print "well good luck doing ",response," Bye Bye!"
        exit(0)
        
start(survive)