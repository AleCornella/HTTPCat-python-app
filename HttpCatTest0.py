import requests
from PIL import Image
while True:

    def ControlloHTTPStat(HTTPstat): #funzione che verifica se il codice ricerato è esitente e consente di evitare errori
        t = open("txt.txt", "r")
        f = t.read()
        for lines in f:
            #print(f)
            if HTTPstat in f:
                return True
                ##print("c'è")
            elif HTTPstat == "q":
                return True
            else:
                return False

 
    stat = input("Che erore vuoi cercare? (digita 'q' per uscire) ")
    if ControlloHTTPStat(stat):
        if stat == "q":
            break
        else:
            img = requests.get(f"https://http.cat/{stat}") #richiesta al sito
            imgfile = open("/home/alessandro/img.jpeg", "wb") #change this path with your favorite path
            imgfile.write(img.content)
            imgfile.close()
            img = Image.open("/home/alessandro/img.jpeg") #change this path with your favorite path
            img.show()
    else:
        print("C'è stato un problema... ):\n\nIl problema potrebbe essere stato causato da un errore HTTP insistente provare a inserire un'altro codice\n Se l'errore persiste contattami a alessandro.cornella@gmail.com")
