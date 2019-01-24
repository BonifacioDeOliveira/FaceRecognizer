import os
import csv
import DataGathering as DG
import TrainingModel as TM
from pandas import Series, DataFrame
from tkinter import *
import PIL.Image, PIL.ImageTk
import time
import numpy as np
import pandas as pd
import re

listausers = []
my_path = 'C:/Users/User Acer/Documents/GitHub/FaceRecognizer/dataset'
delete_path = 'C:/Users/User Acer/Documents/GitHub/FaceRecognizer'

def AddUser(face_name):
    listausers.clear()
    datasetUsers = pd.read_csv("C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv")
    names = pd.DataFrame(datasetUsers, columns=['ID','Nome'])
    tam = names.shape[0]

    for i in range (1,tam):
        search_user = names.iloc[i]
        listausers.append(search_user[1])



    face_id = tam

    DG.Add_User(face_id, face_name)

    with open('C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([face_id, face_name])
    TM.training()

#Tem como funcao adicionar um usuario e treinar um novo modelo
#AddUser()

# Tem como funcao fazer o reconhecimento do user
def recognize():
    import recognition

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

class App:

    listausers.clear()
    datasetUsers = pd.read_csv("C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv")
    names = pd.DataFrame(datasetUsers, columns=['ID','Nome'])
    tam = names.shape[0]

    for i in range (1,tam):
        search_user = names.iloc[i]
        listausers.append(search_user[1])

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.nomeLabel = Label(self.primeiroContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.primeiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.add1 = Button(self.segundoContainer)
        self.add1["text"] = "Adiciona Usuario"
        self.add1["width"] = 12
        self.add1["command"] = (lambda : (Both_Add(self.nome.get())))
        self.add1.pack()

        self.listbox = Listbox(self.quartoContainer, height=10)
        self.listbox.pack()
        self.listbox.insert('end', *listausers)
        for i in range(0,len(listausers),2):
            self.listbox.itemconfigure(i, background='#f0f0ff')

        self.add2 = Button(self.quintoContainer)
        self.add2["text"] = "Deleta Usuario"
        self.add2["width"] = 12
        self.add2["command"] = (lambda : Delete(str(self.listbox.get(ACTIVE))))
        self.add2.pack()

        self.add3 = Button(self.sextoContainer)
        self.add3["text"] = "Reconhecer"
        self.add3["width"] = 12
        self.add3["command"] = (lambda : recognize())
        self.add3.pack()

        def Both_Add(face_name):
            AddUser(face_name)

            self.msg = Label(self.terceiroContainer, text="Usuario Adicionado")
            self.msg["font"] = ("Calibri", "9", "italic")
            self.msg.pack ()
            self.msg.after(2000, self.msg.destroy)

        def Delete(nome):

            #deleta do dataset csv

            index = 0
            for i in range(len(listausers)):
                if listausers[i] == nome:
                    break
                else:
                    index+=1
            value = index+1

            DeleteUser = pd.read_csv("C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv")
            toDelete = pd.DataFrame(DeleteUser, columns=['ID','Nome'])

            toDelete.drop(index=value, inplace=True)

            lines = toDelete.shape[0]
            newIndex = []
            for i in range(lines):
                newIndex.append(i)


            toDelete['ID'] = newIndex

            os.remove(os.path.join(delete_path, 'Relacao_ID_Nome.csv'))

            toDelete.to_csv('Relacao_ID_Nome.csv', encoding='utf-8', index=False)



            #Remove as imagens do usuario
            index+=1
            for paths, dirs, files in os.walk(my_path):
                for file in files:
                    if file.startswith("User." + str(index)):
                        os.remove(os.path.join(my_path, file))
                    else:
                        pass

            #Renomeia as imagens
            files = sorted_aphanumeric(os.listdir(my_path))

            i=1
            for file in files:
                os.rename('C:/Users/User Acer/Documents/GitHub/FaceRecognizer/dataset/' + file, 'C:/Users/User Acer/Documents/GitHub/FaceRecognizer/dataset/' +'pattern'+str(i)+'.jpg')
                i+=1


            dirlist = sorted_aphanumeric(os.listdir(my_path))

            idusuario = 1
            countpictures = 1
            for file in dirlist:
                if(countpictures < 51):
                    os.rename(os.path.join(my_path, file),os.path.join(my_path,'User.' + str(idusuario) + '.' + str(countpictures) + '.jpg'))
                    countpictures+=1
                else:
                    countpictures = 1
                    idusuario+=1
                    os.rename(os.path.join(my_path, file),os.path.join(my_path,'User.' + str(idusuario) + '.' + str(countpictures) + '.jpg'))
                    countpictures+=1

            print("deleted")

            listausers.clear()
            datasetUsers = pd.read_csv("C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv")
            names = pd.DataFrame(datasetUsers, columns=['ID','Nome'])
            tam = names.shape[0]

            for i in range (1,tam):
                search_user = names.iloc[i]
                listausers.append(search_user[1])

root = Tk()
root.title("Door Opener")
App(root)
root.mainloop()



'''
Links:

https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
http://codetheory.in/introduction-to-the-python-os-walk-function-with-a-practical-example/
https://www.geeksforgeeks.org/rename-multiple-files-using-python/
https://stackoverflow.com/questions/4813061/non-alphanumeric-list-order-from-os-listdir



'''






