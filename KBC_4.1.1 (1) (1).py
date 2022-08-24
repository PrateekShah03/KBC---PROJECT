#importing required python modules
import pyttsx3
import smtplib
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

#__DATA__        
Sno= [ '1st','2nd','3rd','4th','6th','7th','8th','9th','10th','11th','12th','13th' ]
Qns= [ '(1) Which is the deepest ocean on the Earth',
       '(2) Which is the 2nd highest peak of the Himalayas',
       '(3) What is the rank of India in the world in terms of geoghaphical area',
       '(4) Which is the 3rd largest planet of our solar system',
       '(5) Which is the closest star to the Sun',
       '(6) What will be the final stage of our Sun',
       '(7) Where is Gobi desert located',
       '(8) Which is the smallest country in terms of geographical area',
       '(9) Which is the largest Moon is our solar system',
       '(10) Which is the closest known(until 10 Dec 2020) galaxy to our Milky Way galaxy',
       '(11) Which is the largest known(until 10 Dec 2020) star in our known universe',
       '(12) Which is 2nd longest river in the world',
       '(13) Which is the brightest star in night sky']
Optns= [ '(a) Pecific    (b) Atlantic    (c) Indian    (d) Arctic',
         '(a) Everest    (b) K2    (c) Kangchenjunga    (d) Nanga Parbat',
         '(a) 1st    (b) 4th   (c) 6th    (d) 7th',
         '(a) Earth    (b) Uranus    (c) Neptune    (d) Saturn',
         '(a) Proxima Century    (b) Omega Century    (c) Alpha Century    (d) Sirius',
         '(a) Black hole    (b) Neutron star    (c) Planetary nebula(White dwarf)    (d) Planetary nebula(Black dwarf)',
         '(a) India    (b) Sudan     (c) China    (d) Chad',
         '(a) Vatican City    (b) Monaco    (c) Nauru    (d) San Marino',
         '(a) Titan    (b) Callisto    (c) Ganymede    (d) Lo',
         '(a) Segue1    (b) Andromeda Galaxy(M31)    (c) Sagittarius Dwarf Sphr(SagDEG)    (d) Canis Major Dwarf',
         '(a) VY Canis Majoris    (b) Stephenson2-18    (c) UY Scuti    (d) IRAS 05346-6949',
         '(a) Yellow River    (b) Nile    (c) Mississippi    (d) Amazon',
         '(a) Sirius A    (b) Rigel    (c) Arcturus    (d) Betelgeuse']
Ans1=[ 'a','b','d','b','a','d','c','a','c','d','b','d','a']

R_Qns= ['Which is the 3rd largest continent in the world',
        'Which planet has its rotational period longer than revolutional period',
        "Which country successfully launched world's first artificial satellite to orbit the Earth",
        'What is the name first artificial satellite to orbit the Earth',
        'Which planet in our solar system has lowest average density',
        'What is the escape velocity of the Earth',
        'Which is the first man-made element',
        'Which is the largest desert in the world',
        'Which is the deepest part of the Earth',
        'Who is the first man to go into space',
        'Which is the most reactive metal',
        'Which is the largest island of the world',
        'Which is the largest lake in the world']
R_Optns= ['(a) North America     (b) Antarctica    (c) Africa    (d) South America',
          '(a) Mercury    (b) Venus    (c) Jupiter    (d) Uranus',
          '(a) USA    (b) UK   (c) Canada    (d) Soviet Union(USSR)',
          '(a) ESRO2B    (b) Sputnik 1   (c) Aryabhata    (d) Explorer 1',
          '(a) Saturn    (b) Jupiter   (c) Uranus    (d) Neptune',
          '(a) 11.7    (b) 11.4   (c)11    (d) 11.2',
          '(a) Rutherfordium    (b) Polonium   (c) Technetium    (d) Plutonium',
          '(a) Antarctica    (b) Sahara   (c) Gobi     (d) Kalahari',
          '(a) Philippine Trench    (b) Tonga Trench   (c) Mariana Trench    (d) Japan Trench',
          '(a) Rakesh Sharma    (b) Neil Armstrong    (c) ALan Shepard    (d) Yuri Gagarin',
          '(a) Potassium    (b) Caesium   (c) Sodium    (d) Francium',
          '(a) Madagascar    (b) Sumatra   (c) New Guinea    (d) Greenland',
          '(a) Caspian Sea    (b) Victoria   (c) Huron    (d) Superior',]
R_Ans1= [ 'a','b','d','b','a','d','c','a','c','d','b','d','a']
Fifty_2=['(a) Pacific    (b)Atlantic ',
         '(b) K2    (c) Kangchenjunga',
         '(c) 6th    (d) 7th',
         '(b) Uranus    (c) Neptune',
         '(a) Proxima Century    (c) Alpha Century',
         '(c) Planetary nebula(White dwarf)    (d) Planetary nebula(Black dwarf)',
         '(b) Sudan     (c) China',
         '(a) Vatican City    (d) San Marino',
         '(a) Titan    (c) Ganymede',
         '(b) Andromeda Galaxy(M31)    (d) Canis Major Dwarf',
         '(b) Stephenson2-18    (c) UY Scuti',
         '(c) Mississippi    (d) Amazon',
         '(a) Sirius A    (d) Betelgeuse']

Winng=[ 'Rs10000','Rs20000','Rs40000','Rs80000','Rs160000','Rs320000','Rs640000','Rs1250000','Rs2500000','Rs5000000','Rs10000000','Rs30000000','Rs70000000']
Alp=['a','b','c','d','A','B','C','D']
LL_Ans= ['YES','Y','y','yes','NO','N','n','no']

#__Funtions__
def  Quit():
    exit()
def speak(audio):
    print('KBC Host:'+ audio )
    engine.say(audio)
    engine.runAndWait()
def SPEAK(audio):
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning !')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon !')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening !')
def INTRO():
    speak('   !!!! Lets go through rules of the game !!!! ')
    speak(' !! The Winning after each question is as below !! ')
    speak(' (1)Rs 10,000')
    speak(' (2)Rs 20,000')
    speak(' (3)Rs 40,000')
    speak(' (4)Rs 80,000')
    speak(' (5)Rs 160,000')
    speak(' (6)Rs 320,000')
    speak(' (7)Rs 640,000')
    speak(' (8)Rs 1,250,000')
    speak(' (9)Rs 2,500,000')
    speak('(10)Rs 5,000,000')
    speak('(11)Rs 10,000,000')
    speak('(12)Rs 30,000,000')
    speak('(13)Rs 70,000,000')
    speak(' ! There are 4 stages in the game ! ')
    speak(' ! 1st stage; upto 4th question your winning will be credited after each win !')
    speak(' ! 2nd stage; From 5th to 7th if you loose at any question your final winning will be Rs 80,000 !')
    speak(' ! 3rd stage; From 8th to 11th if you loose at any question your final winning will be Rs 1,250,000 !')
    speak(' ! 4th stage; From 11th to 13th if you loose at any question your final winning will be Rs 10,000,000 !')
    speak(' ! You have 3 life lines that can be used at any stage of the game but 2 life line cannot be used for same question !')
    speak(' ! 1st life line; 50 50 ; opting for this means your 2 wrong answers will be removed !')
    speak(' ! 2nd life line; Flip The Question ; opting for this means your question will be replaced by a new question !')
    speak(' ! 3rd life line; Double Dip ; opting for this means you will be given 2 chances to attempt the question !')

def Fifty_Fifty():
    speak(Fifty_2[i])
def Flip_Question():
    SPEAK('Your replaced question is as below')
    print('Your replaced',Sno[i],' question is as below:')
    speak(R_Qns[0])
    speak('Your options are as below!')
    speak(R_Optns[0])
    Ans1.clear()
    Ans1=Ans1+R_Ans1
    sub_program1()

def Double_Dip():
    SPEAK('Choose your option for correct answer')
    Opt=input( 'Choose your option for correct answer:')
    Opt.lower()
    if Opt==Ans1[i]:
        if i < 13:
            speak('Congratulations, You won!!!')
            print('Your total winning is:', Winng[i])
        else:
            speak('!!!!!! CONGRATULATIONS , YOU ARE THE CHAMPION OF KBC; KAUN BANEGA CROREPATI !!!!!!')
            print('Your total winning is:', Winng[i])

    else:
        if Opt==Alp[0]or Opt==Alp[1]or Opt==Alp[2]or Opt==Alp[3]or Opt==Alp[4]or Opt==Alp[5]or Opt==Alp[6]or Opt==Alp[7]:
            speak(' Sorry,  You loose!!!')
            speak('Your first chance is over!!!')
            sub_program1()
        else:
            speak(' Sorry, no such option exists !!')
            speak(' Enter valid options(a,b,c,d)!!!')
            SPEAK('Choose your option for correct answer')
            Opt=input( 'Choose your option for correct answer:')
            Opt.lower()
            if Opt==Ans1[i]:
                if i<13:
                    speak('Congratulations, You won!!!')
                    print('Your total winning is:',Winng[i])
                else:
                    speak('!!!!!! CONGRATULATIONS , YOU ARE THE CHAMPION OF KBC; KAUN BANEGA CROREPATI !!!!!!')
                    print('Your total winning is:',Winng[i])
            else:
                if Opt==Alp[0]or Opt==Alp[1]or Opt==Alp[2]or Opt==Alp[3]or Opt==Alp[4]or Opt==Alp[5]or Opt==Alp[6]or Opt==Alp[7]:
                    speak(' Sorry,  You loose!!!')
                    speak('Your first chance is over!!!')
                    sub_program1()
                else:
                    speak(' Sorry, no such option exists !!')
                    speak(' You loose!!!')
                    Quit()

def sub_program3():
            SPEAK("Which Life Line do you want to use")
            LL_Optns=input("Which Life_Line do you want to use?(Enter '1' for '50_50','2' for 'Flip_Question' and '3' for 'Double_Dip'):")
            if LL_Optns=='1':
                Fifty_Fifty()
            elif LL_Optns=='2':
                Flip_Question()
            elif LL_Optns=='3':
                Double_Dip()
            else:
                speak("Enter valid option!!")
                LL_Optns=input("Which Life_Line do you want to use?(Enter '1' for '50_50','2' for 'Flip_Question' and '3' for 'Double_Dip'):")
                if LL_Optns=='1':
                    Fifty_Fifty()
                elif LL_Optns=='2':
                    Flip_Question()
                elif LL_Optns=='3':
                    Double_Dip()
                else:
                    speak('Sorry, No such option exists!!!!')
                    speak("   !!!Yor are out of game now!!!   ")
                    Quit()    
def sub_program2():
                speak(' Sorry,  You loose!!!  You are out of the game')
                if i==0 :
                    speak('You have not won any cash prize')
                    Quit()
                elif i>=4 and i<7:
                    print('Your total winning is:',Winng[3])
                    Quit()
                elif i>=7 and i<11:
                    print('Your total winning is:',Winng[6])
                    Quit()
                elif i>=11 and i<14:
                    print('Your total winning is:',Winng[10])
                    Quit()
                else:
                    print('Your total winning is:',Winng[i-1])
                    Quit()
def sub_program1():
        SPEAK('Choose your option for correct answer')
        Opt=input( 'Choose your option for correct answer:')
        Opt.lower()
        if Opt==Ans1[i]:
            if i<13:
                speak('Congratulations, You won!!!')
                print('Your total winning is:',Winng[i])
            else:
                speak('!!!!!! CONGRATULATIONS , YOU ARE THE CHAMPION OF KBC; KAUN BANEGA CROREPATI !!!!!!')
                print('Your total winning is:',Winng[i])
        else:
            if Opt==Alp[0]or Opt==Alp[1]or Opt==Alp[2]or Opt==Alp[3]or Opt==Alp[4]or Opt==Alp[5]or Opt==Alp[6]or Opt==Alp[7]:
                sub_program2()
            else :
                speak('No such option exists !!')
                sub_program2()
def sub_program():
            SPEAK('Choose your option for correct answer')
            Opt=input( 'Choose your option for correct answer:')
            Opt.lower()
            if Opt==Ans1[i]:
                if i<13:
                    speak('Congratulations, You won!!!')
                    print('Your total winning is:',Winng[i])
                else:
                    speak('!!!!!! CONGRATULATIONS , YOU ARE THE CHAMPION OF KBC; KAUN BANEGA CROREPATI !!!!!!')
                    print('Your total winning is:',Winng[i])
            else:
                if Opt==Alp[0]or Opt==Alp[1]or Opt==Alp[2]or Opt==Alp[3]or Opt==Alp[4]or Opt==Alp[5]or Opt==Alp[6]or Opt==Alp[7]:
                    sub_program2()
                else:
                    speak(' Sorry, no such option exists !!')
                    speak(' Enter valid options(a,b,c,d)!!!')
                    sub_program1()
def main_program():
        SPEAK("Do you want to you any Life Line")
        LL=input("Do you want to use any Life Line?(Enter 'YES or Y to use LL' and ' NO or N not to use LL') :")
        if LL==LL_Ans[0] or LL==LL_Ans[1] or LL==LL_Ans[2] or LL==LL_Ans[3]:
            sub_program3()
        elif LL==LL_Ans[4] or LL==LL_Ans[5] or LL==LL_Ans[6] or LL==LL_Ans[7]:
            speak('Okay, Best of luck, play on!!')
        else:
            speak("Enter valid option!!")
            LL=input("Do you want to you any Life_Line?(Enter 'YES or Y to use LL' and ' NO or N not to use LL') :")
            if LL==LL_Ans[0] or LL==LL_Ans[1] or LL==LL_Ans[2] or LL==LL_Ans[3]:
                sub_program3()
            elif LL==LL_Ans[4] or LL==LL_Ans[5] or LL==LL_Ans[6] or LL==LL_Ans[7]:
                speak('Okay, Best of luck, play on!!')
            else:
                speak('Sorry, No such option exists!!!!')
                speak("   !!!Yor are out of game now!!!   ")
                Quit()
        sub_program()

#__main__
greetMe()
speak("   !!!!!! WELCOME TO KBC; KAUN  BANEGA CROREPATI !!!!!! ")
SPEAK("Do you want to skip rule introduction part")
Intro=(input("Do you want to skip RULE INTRODUCTION PART:"))
if Intro==LL_Ans[0] or Intro==LL_Ans[1] or Intro==LL_Ans[2] or Intro==LL_Ans[3]:
    speak("Okay")
elif Intro==LL_Ans[4] or Intro==LL_Ans[5] or Intro==LL_Ans[6] or Intro==LL_Ans[7]:
    INTRO()
else:
    speak("Enter valid option!!!")
    Intro=input("Do you want to skip RULE INTRODUCTION PART(yes or no):")
    if Intro==LL_Ans[0] or Intro==LL_Ans[1] or Intro==LL_Ans[2] or Intro==LL_Ans[3]:
        speak("Okay")
    elif Intro==LL_Ans[4] or Intro==LL_Ans[5] or Intro==LL_Ans[6] or Intro==LL_Ans[7]:
        INTRO()
    else:
        speak('Sorry, You are out of game now!!!')
        Quit()
speak(" !!!!! LETS  PLAY  !!!!!")
        
for i in range(0,14):
    if i==0:
        speak('Here is the first question of the game')
    else:
        speak('Your next question is')
    print('Your',Sno[i],'question for ',Winng[i],'is =>')
    speak(Qns[i])
    speak('Your options are as below!')
    speak(Optns[i])
    SPEAK('Do you want to quit game')
    Choice=input('Do you want to QUIT game:')
    if Choice==LL_Ans[4] or Choice==LL_Ans[5] or Choice==LL_Ans[6] or Choice==LL_Ans[7]:
        main_program()
    elif Choice==LL_Ans[0] or Choice==LL_Ans[1] or Choice==LL_Ans[2] or Choice==LL_Ans[3]:
        Quit()
    else:
        speak('Enter valid options!!!')
        Choice=input('Do you want to QUIT game(yes or no):')    
        if Choice==LL_Ans[4] or Choice==LL_Ans[5] or Choice==LL_Ans[6] or Choice==LL_Ans[7]:
            main_program()
        elif Choice==LL_Ans[0] or Choice==LL_Ans[1] or Choice==LL_Ans[2] or Choice==LL_Ans[3]:
            Quit()
        else:
            speak('Sorry, You are out of game now!!!')
            break            
        
        
            
         
