
import os
from colorama import *
import webbrowser
init(autoreset=True)
os.system("python3 ANTNUXTOOLKIT.py")
os.system("cls")
print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
def asciiart():
    print('\33[34m' +"   ____        __      _   ________      __      _   __    __   __     __  ")
    print('\33[34m' +"  (    )      /  \    / ) (___  ___)    /  \    / )  ) )  ( (  (_ \   / _)")
    print('\33[34m' +"  / /\ \     / /\ \  / /      ) )      / /\ \  / /  ( (    ) )   \ \_/ /   ")
    print('\33[34m' +" ( (__) )    ) ) ) ) ) )     ( (       ) ) ) ) ) )   ) )  ( (     \   /    ")
    print('\33[34m' +"  )    (    ( ( ( ( ( (       ) )     ( ( ( ( ( (   ( (    ) )    / _ \    ")
    print('\33[34m' +" /  /\  \   / /  \ \/ /      ( (      / /  \ \/ /    ) \__/ (   _/ / \ \_  ")
    print('\33[34m' +"/__(  )__\ (_/    \__/       /__\    (_/    \__/     \______/  (__/   \__) ")

    print('\33[34m' + " ________     ____       ____     _____        __   ___    _____   ________ ")
    print('\33[34m' +"(___  ___)   / __ \     / __ \   (_   _)      () ) / __)  (_   _) (___  ___) ")
    print('\33[34m' +"   ) )      / /  \ \   / /  \ \    | |        ( (_/ /       | |       ) )    ")
    print('\33[34m' +"   ( (     ( ()  () ) ( ()  () )   | |        ()   (        | |      ( (     ")
    print('\33[34m' +"   ) )     ( ()  () ) ( ()  () )   | |   __   () /\ \       | |       ) )    ")
    print('\33[34m' +"   ( (      \ \__/ /   \ \__/ /  __| |___) )  ( (  \ \     _| |__    ( (     ")
    print('\33[34m' +"   /__\      \____/     \____/   \________/   ()_)  \_\   /_____(    /__\    ")
    print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
def next():
    input("-------------------------------premi invio per continuare...--------------------------")

print("1. ipconfig")
print("2. Port Scan")
print("3. DDoS")
print("4. Windows Activator")
print("5. PS4 Tools")
print("6. Information Gathering")
print("7. Extra")
print("8. ")
scelta = int(input("> "))
if scelta == 1:                                                       #IPCONFIG
    os.system("ipconfig")
    input("-------------------------------premi invio per continuare...--------------------------")
    os.system("cls")
    os.system("start ANTNUXTOOLKIT.py")
if scelta == 2:                                                       #NMAP PORTSCAN
    os.system("cls")
    asciiart()
    targetNMAP = input("inserisci il target: ")
    os.system("nmap " + targetNMAP )
    input("-------------------------------premi invio per continuare...--------------------------")
    os.system("cls")
    os.system("start ANTNUXTOOLKIT.py")
if scelta == 3:                                                       #DDoS
    os.system("cls")
    asciiart()
    print("1. bastarddosser")
    print("2. stresser.ai")
    print("3. ping")
    print("4. Torna Indietro")
    scelta1 = int(input("> "))
    if scelta1 == 1:
        try:
            os.system("start tools/stresser")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
        except:
            print("error 104")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
    if scelta1 == 2:
            try:
                urL3='https://stresser.ai'
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(urL3)
                input("-------------------------------premi invio per continuare...--------------------------")
                os.system("cls")
                os.system("start ANTNUXTOOLKIT.py")
            except:
                print("https://stresser.ai")
    if scelta1 == 3:
        ipaddr = input('inserisci il target: ')
        os.system("ping " + ipaddr)
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")
    if scelta1 == 4:
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")



if scelta == 4:                                                #WINDOWS ACTIVATOR
    os.system("cls")
    asciiart()
    print('\33[31m' + "se riscontri problemi avvia il file come amministratore")
    print("1. Windows 10 Home")
    print("2. Windows 10 Pro")
    print("3. Windows 10 Enterprise")
    print("4. Torna Indietro")
    scelta2 = int(input("> "))
    if scelta2 == 1:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /ato")
        input("-------------------------------premi invio per continuare...--------------------------")
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")
    if scelta2 == 2:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /ato")
        input("-------------------------------premi invio per continuare...--------------------------")
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")
    if scelta2 == 3:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /ato")
        os.system("start ANTNUXTOOLKIT.py")
        input("-------------------------------premi invio per continuare...--------------------------")
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")
    if scelta2 == 4:
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")
if scelta == 5:                                                         #PS4 TOOLS
    os.system("cls")
    asciiart()
    print("1. LANC REMASTERED")
    print("2. Profile Script")
    print("3. Save Wizard")
    print("4. Torna Indietro")
    scelta3 = int(input("> "))
    if scelta3 == 1:
        try:
            os.system("start tools/LANC/LancRemastered.exe")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
        except:
            os.system("start install.py")
    if scelta3 == 3:
        os.system("cls")
        asciiart()
        print("1. install Save Wizard")
        print("2. install Save Editor")
        print("3. install MoneyFreeze Save")
        print("4. Torna Indietro")
        scelta6 = int(input("> "))
        if scelta3 == 4:
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")

        if scelta6 == 1:
            try:
                urL6='https://www.savewizard.net/swps4max.zip'
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(urL6)
                os.system("cls")
                os.system("start ANTNUXTOOLKIT.py")
            except:
                print("https://www.savewizard.net/swps4max.zip")
            
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
            input("-------------------------------premi invio per continuare...--------------------------")
        if scelta6 == 2:
            os.system("start tools/saveeditor.exe")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
        if scelta6 == 3:
            try:
                urL9='https://drive.google.com/file/d/1Fm-kZmlt34-kVhfLGqI8PJkedfw6wVJ2/view'
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(urL9)
                input("-------------------------------premi invio per continuare...--------------------------")
                os.system("cls")
                os.system("start ANTNUXTOOLKIT.py")
            except:
                print("https://drive.google.com/file/d/1Fm-kZmlt34-kVhfLGqI8PJkedfw6wVJ2/view")
        if scelta6 == 4:
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")
                

    
    if scelta3 ==2:
        os.system("cls")
        asciiart()
        print("1. Download Script")
        print("2. Video Tutorial")
        print("3. Torna Indietro")
        scelta4 = int(input("> "))
        if scelta4 == 1:
            try:
                urL='https://github.com/KuromeSan/BetterManagementPage'
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(urL)
                os.system("cls")
                os.system("start ANTNUXTOOLKIT.py")
            except:
                print("https://github.com/KuromeSan/BetterManagementPage")


        if scelta4 == 2:
            try:
                urL1='https://www.youtube.com/watch?v=hZaPvTp0Q7M'
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(urL1)
                input("-------------------------------premi invio per continuare...--------------------------")
                os.system("cls")
                os.system("start ANTNUXTOOLKIT.py")
            except:
                print("https://www.youtube.com/watch?v=hZaPvTp0Q7M")
if scelta == 6:                                                              #INFORMATION GATHERING
    os.system("cls")
    asciiart()
    print("1. sherlock")
    print("2. FBI TOOL")
    print("3. ????")
    print("4. ????")
    print("5. ????")
    print("6. Torna Indietro")

if scelta == 7:                                                                 #EXTRA
    os.system("cls")
    asciiart()
    print("1. Anon-SMS")
    print("2. ????")
    print("3. ????")
    print("4. ????")
    print("5. ????")
    print("6. Torna Indietro")
    scelta5 = int(input("> "))
    if scelta5 == 1:
        try:
            os.system("start tools/Anon-SMS/send")
            os.system("start tools/Anon-SMS/send")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("start ANTNUXTOOLKIT.py")
        except:
            print("error 104")
            input("-------------------------------premi invio per continuare...--------------------------")
            os.system("cls")
            os.system("start ANTNUXTOOLKIT.py")

    if scelta5 == 6:
        os.system("cls")
        os.system("start ANTNUXTOOLKIT.py")







    



        



    
    








