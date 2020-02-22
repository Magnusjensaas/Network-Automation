import random
import os


#while loop to allow script to be run again upon finishing and clears the console.
while True:
    clear = lambda: os.system("cls")
    clear()
    clear = lambda: os.system("clear")
    clear()

#Prints the name of the program in color.
    print('''\033[0;34;40m
    Password Generator
    ==================
    \033[0;37;40m\n''')


#Defining wordlist and  numberlist
    words = ["monitor", "format", "forbudt", "teknologisk", "hyppig", "montert", "kinoen", "trommer", "rabatt", "paradis", "sektorer","analysert", "brukbar", "imponere", "fallende", "livsfarlig", "fritiden", "skygge", "adaptiv", "adjunkt", "adgang", "advent", "agenda", "airbag", "akedag", "albuer" "alltid", "alpint", "analog", "anelse", "angrep", "gjennom", "tilbake", "skriver", "samtidig", "hvordan", "viktig", "veldig", "penger", "funnet", "personer", "trondheim", "bergen", "stavanger", "sandefjord", "million", "publisert", "minutter", "internet", "spiller", "stedet", "kristiansand", "kristiansund" "finnmark", "nordland" "telemark", "finnes", "arbeid", "trenger", "problem", "sitter", "skjedde", "sverige", "enkelte", "enkelt", "svensk", "nordmann", "biler", "internasjonale", "politisk", "kommunen", "kommune", "startet", "egentlig", "fotball", "tidlig", "ganske", "begynte", "alvorlig", "betale", "europa", "krever", "direkte", "sykehus", "kontor", "tastatur", "skjerm", "kjenner", "stille", "sentrum", "jugend", "terminal", "klokken", "regner", "antall", "skolen", "familie", "familien", "slutten", "sulten", "musikk", "trener", "publikum", "advokat", "frykter", "danmark", "tyskland", "spania", "london", "ulykke", "frankrike", "endelig", "bestemt", "totalt", "offentlig", "england"]
    word = set(words)
    nums = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55" ,"56", "57", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    number = 1
    number = int(number)

    print('\nhere is your password:\n ')


#Shuffles the wordlist and joins two words whit a "-" between them, also adds a two digit number from the numbers list.
    random.shuffle(words)
    random.shuffle(nums)
    string  = "-".join(words[:2])
    numbers = "-".join(nums[:1])
    password = "{string}{numbers}".format(string=string, numbers=numbers)
    print ("\033[0;31;40m"+ password + "\033[0;37;40m\n")


#While loop to ask the user if they want to run the generator once more or not.
    while True:
        answer = input("Run again? (\033[0;32;40my/\033[0;31;40mn\033[0;37;40m): ")
        if answer in ("y", "n"):
            break
        print ("Invalid input")
    if answer == "y":
        continue
    else:
        print ("Goodbye")
        break



