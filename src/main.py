# install specified libraries used to make the code run
import keyboard
import mouse
# we inport the time function from the time library
from time import time
from pygame import mixer

def main():
    # We initialize the music libary
    mixer.init()

    mixer.music.load("jsbarrett_train-crossing.wav")

    # set t to equal the curent time at the start (normalises time to be 0 seconds so we can check how much time has pased since this initial time)
    t = time()
    timePassed = time() - t
    # the max time in seconds
    maxTime = 5

    # this is every key we check so if one of these keys are pressed the timer will reset
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                "space","enter","shift","ctrl","alt",0,1,2,3,4,5,6,7,8,9,'-',"_","+","=","'",";",'{','}','|',',',
                "UP","DOWN","LEFT","RIGHT","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Backspace"]
    while True:
        first_pos = mouse.get_position()
        for i in range(len(alphabet)):
            if(keyboard.is_pressed(alphabet[i])==True):
                mixer.music.pause()
                timePassed = 0
                t = time()
        # when the amount of time passed is greater than the maxTime allowed it will play the music on repeat
        if (timePassed > maxTime):
            mixer.music.unpause()
            mixer.music.play(loops=-1)
            timePassed = 0
            t = time()
            
        # checks if the mouse position has changed and if it has it resets the timer
        second_pos = mouse.get_position()

        if(second_pos != first_pos):
            mixer.music.pause()
            timePassed = 0
            t = time()

        # Updates the time passed
        timePassed = time() - t

if __name__ == '__main__':
    main()
