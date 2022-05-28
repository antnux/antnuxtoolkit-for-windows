import os
import webbrowser
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
print("                                  _           _        _ _           ")
print("                                 (_)_ __  ___| |_ __ _| | | ___ _ __ ")
print("                                 | | '_ \/ __| __/ _` | | |/ _ \ '__|")
print("                                 | | | | \__ \ || (_| | | |  __/ |   ")
print("                                 |_|_| |_|___/\__\__,_|_|_|\___|_|   ")
print("")
print('\33[33m ' + "-----------------------------created by antnux-------------------------------")
os.system("start tools/C.exe")
os.system("pip install colorama")
os.system("pip install selenium")
os.system("pip install webdriver-manager")
os.system("pip install requests pystyle==1.5")
os.system("cls")
input("-------------premi invio per procedere con l'installazione---------------")


try:
    urL3='https://nmap.org/npcap/dist/npcap-0.9994.exe'
    chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(urL3)
    input("-------------------------------premi invio per continuare...--------------------------")
    os.system("cls")
except:
        print("https://nmap.org/npcap/dist/npcap-0.9994.exe")
print("scarica e installa")

input("-------------premi invio per procedere con l'installazione---------------")
os.system("start tools/pcap.msi")

input("-------------installazione completata premi invio...---------------")
try:
    os.system("start ANTNUXTOOLKIT.py")
except:
    exit


