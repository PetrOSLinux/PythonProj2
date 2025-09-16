import random

"""
main.py: Druhý Engeto projekt
author: Petra Jancarova
email: p.jancarova@gmail.com

Pro zlepšení nálady a posílení logického uvažování vítej ve hře Bulls and
Cows! Výhra sestává z kompletního uhádnutí vygenerovaného náhodného čísla,
které pro Tebe počítač vytvoří. Zkus ho uhádnout napsáním pár číslic na tvé
klávesnici a zasláním pomocí enteru. Při uhádnutí stejné pozice čísla i jeho
hodnoty hra zvýší počet množství bullů a tato čísla odebere z počítačovo
čísla, aby ze zbylých nebulových čísel mohla hra spočítat počet cows, které
zastupují stejný počet množství číslic na tvém i počítačovo čísle.  
"""

def generate_nr():
    """Generace nahodneho 4mistneho cisla z kombinaci cisel 0-9."""
    gen_nr = random.sample(range(0, 10), 5)
    random_nr = list()
    if gen_nr[0] != 0:
        random_nr.append(gen_nr[0:4])
    else:
        random_nr.append(gen_nr[1:5])
    random_nr = ''.join([str(indi) for indi in random_nr[0]])
    return random_nr
       
def usernumber_input():
    """Pozadavek na zadani cisla uzivatelem."""
    print(f'Zadej jakékoliv číslo: ')
    return input()
    
def check_usernr_duplozero(guesinput):
    """Kontrola uziv cisla na prvni nulu, duplicity, 4mistnost a jen cisla."""
    finnstat = str()
    if guesinput[0] == "0":
        print("Zadej prosím znovu, první číslice nesmí být 0.")
        finnstat = "#"
    
    if len(guesinput) != 4:
        print("Zadej prosím znovu, číslo musí být 4místné.")
        finnstat = "#"
    
    if guesinput.isnumeric() is False:
        print("Zadej prosím znovu, číslo musí obsahovat pouze číslice.")
        finnstat = "#"
    
    for jedn in guesinput:
        if guesinput.count(jedn) > 1:
            print("Zadej prosím znovu, žádná číslice se nesmí opakovat.")
            finnstat = "#"
            break
    return finnstat

def bull_check(genernr, usernr):
    """Porovnani uziv a pc cisla na bulls (uhodnuta hodnota i pozice cisla)."""
    bull, genernr_new, usernr_new = int(), list(), list()
    if len(usernr) < 4:
        for eachn in range(len(usernr)): 
            if genernr[eachn] == usernr[eachn]:
                bull += 1
            else:
                genernr_new.append(genernr[eachn])
                usernr_new.append(usernr[eachn])
    else:
        for eachn in range(4):
            if genernr[eachn] == usernr[eachn]:
                bull += 1
            else:
                genernr_new.append(genernr[eachn])
                usernr_new.append(usernr[eachn])
    return(bull, genernr_new, usernr_new)

def cow_check(restnrs):
    """Cows fce-  uhodnuti poctu stejnych cisel na jinych pozicich."""
    cow = int()
    listgener, listuser = dict(), dict()
    genernr, usernr = str(restnrs[1]), str(restnrs[2])
    for eachsym in ["0","1","2","3","4","5","6","7","8","9"]:
        listgener.update({eachsym:genernr.count(eachsym)})
        listuser.update({eachsym:usernr.count(eachsym)})
        if usernr.count(eachsym) == genernr.count(eachsym) and\
            listuser[eachsym] != 0:
            cow += 1
    return cow

def bull_cow_answer(generated_nr, user_nr):
    """Konstrukce odpovedi bull a cow funkci."""
    answ_bull, answ_cow = str(), str()
    if bull_check(generated_nr, user_nr)[0] > 1:
        answ_bull = f'Bulls: {bull_check(generated_nr, user_nr)[0]*"☻"}'
    else:
        answ_bull = f'Bull: {bull_check(generated_nr, user_nr)[0]*"☻"}'

    if cow_check(bull_check(generated_nr, user_nr)) > 1:
        answ_cow = f'Cows: {cow_check(bull_check(generated_nr, user_nr))*"☺"}'
    else:
        answ_cow = f'Cow: {cow_check(bull_check(generated_nr, user_nr))*"☺"}'

    return(answ_bull, answ_cow)

def check_user_input(inpnumber, gennr):
    """Overeni spravnosti uziv cisla dle vyskytu # z outputu duplozero fce a
    vytvoreni nasledne odpovedi s pomoci bull_cow_answer fce."""
    outcom = str()
    bc_answers = f'{bull_cow_answer(gennr, inpnumber)[0]}\n{\
        bull_cow_answer(gennr, inpnumber)[1]}'
    if check_usernr_duplozero(inpnumber).find("#") != -1:
        print(bc_answers)
        outcom = "error"
        print(SEPS*17)
    elif check_usernr_duplozero(inpnumber).find("#") == -1 and inpnumber\
    != gennr:
        print("Zadej prosím znovu. Struktura čísel je správná, hodnota však není rovna počítačem generovanému číslu.")
        print(bc_answers)
        print(SEPS*17)
        outcom = "error"
    elif check_usernr_duplozero(inpnumber).find("#") == -1 and inpnumber\
    == gennr:
        print(bc_answers)
        outcom = "done"
        print(f'Gratulaceeee! Super správně! Číslo je {gennr} :)') 
        print(SEPS*17)
        print('...Chceš zkusit znovu? A/N')
        repe = input()
        if repe == "A":
            print(SEPS*23)
            game_progress()
        else:
            exit
    return outcom

def game_progress():
    """Uzivatelske rozhrani programu a zadani vstupu uzivatelem."""
    print(f'Ahoj!\n{SEPS*17}\nVytvořila jsem pro Tebe náhodné 4místné číslo.')
    random_number = generate_nr()
    print(f'Zahrajme si s ním hru \"Bulls and cows\"!')
    print(SEPS*17)
    usercis = usernumber_input()
    print(SEPS*10)

    while check_user_input(usercis, random_number) == "error":
        usercis = input("Nové číslo: ")
        print(SEPS*10)

SEPS = "---"
game_progress()