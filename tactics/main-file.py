#author : V-M4K4R0V
#add music , graphics , national anthem
from pathlib import Path
from enemies import world_map
from age import comrade_age
from tur import the_map
way1 = Path("pics")
way2 = Path("national anthems")

print("Privyet!! Comrade")

#im = Image.open('/home/o11q/Desktop/git clone/chto-takoe-stolitsa/mozer racha/put.jpg')
#print(im.format, im.size, im.mode)

comrade_user = input('Enter your name : ') #NameError
B_year = input('Enter your birth year : ')
age = 2020 - int(B_year)

comrade_age(age) #ft_age

R_SPY = open('/home/o11q/Desktop/git clone/Flying-wedge/tactics/names.txt','r')

i = 19 #fix STRING INDEX   

print("You know what ill call you " + R_SPY.readline(i))
chooose = input("is it okay to call you "  + R_SPY.readline(i) + "[YES]or[NO] : ").upper() #fix \n

#ADD A LOOP
def choosing_the_enemy(chooose):
    if(chooose == 'NO'):
            print("SYKAA!! GET OUT U FUCKING WESTERN SPY")
    elif(chooose == 'YES'):
        print("SO! my APYR what country  u want to invade today ?")
        enemy = input("choose your enemy : ").lower()
        world_map(enemy) #enemies from enemies.py
    else:
        print("you fucking donkey i said yes or not")
        #playsound('audio.mp3') #ownage pranks ill slap ur ass like 3abas
R_SPY.close() #close theTXT FILE
