import os
import csv
import DataGathering as DG
import TrainingModel as TM
import recognition as rec
from pandas import Series, DataFrame


def AddUser():

    faceID, face_name = DG.Add_User()
    print(faceID)
    print(face_name)
    with open('C:/Users/User Acer/Documents/GitHub/FaceRecognizer/Relacao_ID_Nome.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([faceID, face_name])

def train():
    TM.training()

def Reco():
    rec.recognize()

#Tem como funcao adicionar um usuario
AddUser()

# Ao se adicionar um usuario deve se treinar o modelo
train()

# Tem como funcao fazer o reconhecimento do user
Reco()

