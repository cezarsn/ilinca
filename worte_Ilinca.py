import tkinter
import random


class myGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(master = self.main_window, text = "die Meerjungfrau",font=("Helvetica Bold", 120))
        self.label1.pack( side = "top" )
        self.button1 = tkinter.Button(master = self.main_window, text = "Next", command = self.change_the_word)
        self.button1.pack (side = "top")

    def change_the_word(self):
##        cuvinte = { "wer" : 100,
##                    "was" : 100,
##                    "vor" : 100
##                    }
        cuvinte = ["wer", "wie", "vor"]

        id = random.randrange(0,3)

        self.label1['text'] = cuvinte[id]
        cuvinte.pop(id)
        return None

        
        tkinter.mainloop()

        
##cuvinte = { "wer" : 100,
##            "was" : 100,
##            "vor" : 100
##            }
##if "vor" in cuvinte.keys():
##    print("existing word")
##else:
##    print("add the word to the dictionary")


if __name__ == "__main__" :
    my_gui = myGui()
        
