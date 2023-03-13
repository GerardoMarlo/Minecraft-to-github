import git
import os
import datetime
from pathlib import Path





CURRENT_PATH = os.getcwd()
USERNAME = ""
url =""
ID_WORLD_NAME_PATTERN="levelname.txt"
mundo = "config"
foldername = ""

init_dir=os.path.expanduser("~\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\")



#**********************************Funciones**********************************

def find(name, path):
    #Creamos diccionario para almacenar nombre desencriptado con su path
    #routes_dic = dict([])
    routes_dic = {"config":"..."}
    for root, dirs, files in os.walk(path):
        if name in files:
            path = os.path.join(root, name)
            f = open(path,"r")
            worldName = f.read()
            routes_dic[worldName]= path #ingresamos valores a diccionario
            print(worldName)
    return(routes_dic)


def iniciaGit(nombre,url): #push

    try:
        os.chdir(str(Path(worldPath).parents[0]))
        NOW = str(datetime.datetime.now())

        os.system("git init")
        os.system("git add .")  
        os.system('git commit -m "{0}{1}"'.format(nombre,NOW))
        print(("git commit -m '{0}-{1}'".format(nombre,NOW)))
        print("comit bien")
        os.system("git branch -M main")
        os.system("git remote add origin {0}".format(url))
        os.system('git push -u origin main')
        print("Todo listo, gracias por jugar!")
        os.system("pause")

    except:

        print("Hubo un error avisale a marlo")
        os.system("pause")
    
def pullGit(url):
    try:
        os.chdir(str(Path(worldPath).parents[1]))
        

        os.system("git pull {0}".format(url))
        print("Todo listo para jugar! :)")
        os.system("pause")

    except:

        print("Hubo un error avisale a marlo")
        os.system("pause")


#******************************************************************************
state = 0
print("Hola!! Inicias o terminas de jugar?\n\n")
while state != 1 and state != 2:
    
    state = int(input('\nEscribe "1" para decir "inicio a jugar"\nEscribe "2" para decir "termino de jugar"\n' ))

if state == 1:
    if not (os.path.exists(CURRENT_PATH+"\\info.txt")):
        print("no exite info.txt")
        infoFile = open("info.txt", "x")
        while USERNAME == "":
            USERNAME = input("Ingrese su nombre de usuario: ")
        print("\n\n\n\nQué mundo de MINECRAFT deseas sincronizar con GitHub?\n")
        diccionario = find(ID_WORLD_NAME_PATTERN,init_dir)
        if mundo == "config":
            setup=input("No encuentro un mundo configurado... Estamos haciendo setup? s/n ")
            if setup == "n":
                while mundo not in diccionario:  
                    mundo = input("Ingresa el nombre del mundo aqui: ")
            else:
                pass
        while url == "":
            url = input("Ingrese link de su repositorio remoto: ")
        while foldername == "":
            foldername = input("Ingrese el nombre de su nueva carpeta: ")
            os.chdir(init_dir)
            os.system("mkdir {0}".format(foldername))
            os.chdir(init_dir+foldername)
            os.system("git init")
        
        print("Bienvenido/a {0}\nBuscando la útlima versión de tu mundo {1}\n\nEsto puede tardar un momento ... ".format(USERNAME, mundo))
        try:
           
            os.system("git pull {0}".format(url))
            print("Todo listo para jugar! :)")
            f = open(init_dir+foldername+"\\levelname.txt","r")
            mundo = f.read()
            info = []
            info.extend([foldername,"\n",url,"\n",mundo,"\n",USERNAME])
            infoFile.writelines(info)
            worldFolder = init_dir+foldername
            worldPath =(worldFolder)
            print(worldPath)
            os.system("pause")
            

        except:

            print("Hubo un error avisale a marlo")
            os.system("pause")

        # info = []
        # info.extend([foldername,"\n",url,"\n",mundo,"\n",USERNAME])
        # infoFile.writelines(info)
        # worldFolder = init_dir+foldername
        # worldPath =(worldFolder)
        # print(worldPath)
        # print("Bienvenido/a {0}\nBuscando la útlima versión de tu mundo {1}\n\nEsto puede tardar un momento ... ".format(USERNAME, mundo))
        # pullGit(url)

    else:
        infoFile = open("info.txt")
        lines = infoFile.readlines()
        foldername= lines[3].strip("\n")
        url= lines[2].strip("\n")
        USERNAME= lines[1].strip("\n")
        mundo=lines[0].strip("\n")
        print("Bienvenido/a {0}\nInicia sincronización con github para tu mundo {1}\n\nEsto puede tardar un momento ... ".format(USERNAME, mundo))
        diccionario = find(ID_WORLD_NAME_PATTERN,init_dir)
        worldFolder = diccionario[mundo]
        worldPath =(worldFolder)
        print("aqui*************"+worldPath)
        pullGit(url)
        os.system("pause")

if state == 2:
    if not (os.path.exists(CURRENT_PATH+"\\info.txt")):
        print("no exite info.txt")
        infoFile = open("info.txt", "x")
        while USERNAME == "":
            USERNAME = input("Ingrese su nombre de usuario: ")
        print("\n\n\n\nQué mundo de MINECRAFT deseas sincronizar con GitHub?\n")
        find(ID_WORLD_NAME_PATTERN,init_dir)
        print("Imprmio******************************")
        diccionario = find(ID_WORLD_NAME_PATTERN,init_dir)
        while mundo not in diccionario:  
            mundo = input("Ingresa el nombre del mundo aqui: ")
        while url == "":
            url = input("Ingrese link de su repositorio remoto: ")
        info = []
        info.extend([url,mundo,"\n",USERNAME])
        infoFile.writelines(info)
        worldFolder = diccionario[mundo]
        worldPath =(worldFolder)
        print(worldPath)
        print("Bienvenido/a {0}\nInicia sincronización con github para tu mundo {1}\n\nEsto puede tardar un momento ... ".format(USERNAME, mundo))
        iniciaGit(USERNAME,url)

    else:
        infoFile = open("info.txt")
        lines = infoFile.readlines()
        url= lines[1].strip("\n")
        USERNAME= lines[0].strip("\n")
        mundo=lines[2].strip("\n")
        print("Bienvenido/a {0}\nInicia sincronización con github para tu mundo {1}\n\nEsto puede tardar un momento ... ".format(USERNAME, mundo))
        diccionario = find(ID_WORLD_NAME_PATTERN,init_dir)
        worldFolder = diccionario[mundo]
        worldPath =(worldFolder)
        print("aqui*************"+worldPath)
        iniciaGit(USERNAME,url)


    def getpath(worldName, path):
        for root, dirs, files in os.walk(path):
            if worldName in files:
                path = os.path.join(root, worldName)
                print(path)
            


#iniciaGit(USERNAME)

#find(ID_WORLD_NAME_PATTERN,init_dir)
#getpath("Camp Enderwood", init_dir)





