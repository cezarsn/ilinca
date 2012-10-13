
import tkinter
import random
import os


def genereaza_fisier(file_input_name , file_output_name, nr_litere):
    '''(str, str, int) ->str

    Return a file named file_output_name of words that are nr_litere long based on file_input_name

    * finded words must be not present in the input file
    * the files should not contain numbers
    * if the word does not exist should be created plus the same word capital


    >>>genereaza_fisier("dump_cuvinte.txt", "cuvinte_3.txt", 3)
    '''

    try:
        file_input = open(file_input_name, "r", encoding="iso-8859-15")
        file_output = open(file_output_name, "r", encoding="iso-8859-15")
    except IOError as e:
        print("I had the following error: %s" % e)
    
    cuvant = ""
    lista_cuvinte_pe_linie = []
    lista_cuvinte_unice = []
    
    for line in file_output:
        lista_cuvinte_unice.append(line.strip())

    lungime_lista_initiala = len(lista_cuvinte_unice)

    
    print("I imported the following number of unique words: %i\n" % len(lista_cuvinte_unice))

    file_output.close()
    file_output = open(file_output_name, "a", encoding="iso-8859-15")

    for line in file_input:
        lista_cuvinte_pe_linie = line.split(" ")
        for elem in lista_cuvinte_pe_linie:
            cuvant = elem.strip().lower()
            if cuvant.isalpha() and len(cuvant) == nr_litere and (cuvant not in lista_cuvinte_unice):
                lista_cuvinte_unice.append(cuvant)

    lungime_lista_finala = len(lista_cuvinte_unice)
    print(len(lista_cuvinte_unice))

    for cuvant in lista_cuvinte_unice[lungime_lista_initiala:lungime_lista_finala]:
        file_output.write(cuvant + "\n")
        file_output.write(cuvant.capitalize() + "\n")

    file_input.close()
    file_output.close()

    print("File %s\%s was generated with %i unique words" % (os.path.abspath(os.curdir),file_output_name,len(lista_cuvinte_unice)))

    return file_output_name


class myGui:
    
    def __init__(self):
        fisier = "cuvinte.txt"
        self.cuvinte = self.genereaza_cuvinte(3, fisier)
        self.main_window = tkinter.Tk()
        self.main_frame = tkinter.Frame(master = self.main_window, borderwidth=5, bg = 'cyan' )
        self.main_frame.pack(side = "top")
        self.label1 = tkinter.Label(master = self.main_frame, text = "die Anfang",font=("Helvetica Bold", 120), width=150)
        self.label1.pack( side = "top" )
        self.button1 = tkinter.Button(master = self.main_window, text = "Next", command = self.change_the_word)
        self.button1.pack (side = "top")
        self.label1.pack_propagate(0)
        

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

        Pocedura care schimba cuvintul si scoate cuvintul din lista de cuvinte generate 

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
        
