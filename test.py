from Classes import *
from Functions import *
from datetime import *
from uuid import uuid4
from prettytable import PrettyTable

M1=Module("PHP",1,2,"PA122")
M2=Module("CSS",1,1,"PA457")
M3=Module("Python",1,2,"PA789")
M4=Module("HTML",1,1,"PA123")
LM=[M1,M2,M3,M4]
DD=Filiere("Developpement Digital","DD",LM)
GE=Filiere("Gestion Des Entreprises","GE",LM)

F1=Formateur('P12345','Ait elka','Ismael',date(1998,8,23),LM)
F2=Formateur('P1234s5','Ait elka','Ismael',date(1998,8,23),LM)
LFO=[F1,F2]
LF=[DD,GE]
S1=Stagaire("PA2215",3,"Ait El Kamel","Ismael",date(1998,8,23),LF,11.66)
S1=Stagaire("PA2215",3,"Ait El Kamel","Ismael",date(1998,8,23),LF,11.66,12.5)
S2=Stagaire("PA2245",3,"Oudra","Brahim",date(1999,6,15),LF,11.58)
S3=Stagaire("PA2875",3,"Aassab","Hiba",date(2002,6,26),LF,14.74)
S4=Stagaire("PA2645",3,"Er-Rachedy","Yassine",date(2000,10,16),LF,14.98)
S5=Stagaire("PA2240",3,"Ait Lhassan","Ayoub",date(2004,8,20),LF,14.42)


LA=[S1,S2,S3,S4,S5]


N1=Note(1,"PA2215",12.5,17.75,15.00)
N2=Note(2,"PA2215",19.5,19.75,18.00)
N3=Note(3,"PA2215",17.5,19.25,18.00)
N4=Note(4,"PA2215",18.5,18.75,19.00)

LN=[N1,N2,N3,N4]

list1=[]
def Importation():
    with open("Data/Formateurs.csv","r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 4:
                C,N,P= info[0],info[1],info[2]
                DN = ImportDate(info[3])
                list1.append(Formateur(C,N,P,DN))
    
    for frmtr in ListFrmtr:
        modForm=[]
        for mod in LM:
            if mod.CINFrmtr == frmtr.CIN:
                modForm.append(mod)
        frmtr.Modules=modForm

    print("Touts le données valides ont été importés avec succeé ")

print("str"==" str ".strip())