
import tkinter
import random




class myGui:
    
    def __init__(self):
        fisier = "cuvinte.txt"
        self.cuvinte = self.genereaza_cuvinte(3, fisier)
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(master = self.main_window, text = "die Meerjungfrau",font=("Helvetica Bold", 120))
        self.label1.pack( side = "top" )
        self.button1 = tkinter.Button(master = self.main_window, text = "Next", command = self.change_the_word)
        self.button1.pack (side = "top")

    def genereaza_cuvinte(self, lungime, fisier):
        '''

        Procedura care incarca dint-un fisier  cuvintele si genereaza o lista de cuvinte de o anumita lungime


        '''
        list = []
        
        try:
            file = open(fisier, "r", encoding="iso-8859-15")
            for line in file:
                list.append(line)
            return list
        except:
            return ["The file was not found"]

    def change_the_word(self):
        ''' (obj) -> None

        Pocedura care schimba cuvintul si scoate cuvintul din lista de silabe generate 

        '''
        if len(self.cuvinte) != 0:
            id = random.randrange(0,len(self.cuvinte))
            self.label1['text'] = self.cuvinte[id]
            self.cuvinte.pop(id)
        else:
            self.label1['text'] = "Fertig !!! :-)"
            
        return None

        
        tkinter.mainloop()

        

if __name__ == "__main__" :
    my_gui = myGui()
        
