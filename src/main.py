import keyboard
import mouse
from time import time
from pygame import mixer

def main():

    mixer.init()

    mixer.music.load("train_Crossing_Bell.mp3")

    t = time()
    timePassed = time() - t
    maxTime = 5

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
                
        if (timePassed > maxTime):
            mixer.music.unpause()
            mixer.music.play(loops=-1)
            timePassed = 0
            t = time()
            

        second_pos = mouse.get_position()

        if(second_pos != first_pos):
            mixer.music.pause()
            timePassed = 0
            t = time()

        timePassed = time() - t

if __name__ == '__main__':
    main()
