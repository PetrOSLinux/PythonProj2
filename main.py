import random
SEPS = "---"

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
    

def bull_check(genernr, usernr):
    """Porovnani uziv a pc cisla na bulls (uhodnuta hodnota i pozice cisla)."""
    bull, genernr_new, usernr_new = int(), list(), list()
    if len(usernr) <= 4:
        for eachn in range(len(usernr)):
            if genernr[eachn] == usernr[eachn]:
                bull += 1
            else:
                genernr_new.append(genernr[eachn])
                usernr_new.append(usernr[eachn])
    if len(usernr) > 4:
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
    for eachsym in range(10):
        eachsym = str(eachsym)
        listgener.update({eachsym:genernr.count(eachsym)})
        listuser.update({eachsym:usernr.count(eachsym)})
        if usernr.count(eachsym) == genernr.count(eachsym) and\
            listuser[eachsym] != 0:
            cow += 1
    return cow

def bull_cow_answer(generated_nr, user_nr): 
    """Konstrukce odpovedi bull a cow funkci."""
    answ_bull, answ_cow = str(), str()
    bullcheck = bull_check(generated_nr, user_nr)
    cowcheck = cow_check(bullcheck)
    if cowcheck != 1:
        answ_cow = f'Cows: {cowcheck*"☺"}'
    elif cowcheck == 1:
        answ_cow = f'Cow: {cowcheck*"☺"}'
        
    if bullcheck[0] != 1:
        answ_bull = f'Bulls: {bullcheck[0]*"☻"}'
    elif bullcheck[0] == 1:
        answ_bull = f'Bull: {bullcheck[0]*"☻"}'
    return(answ_bull, answ_cow)

def check_user_input(inpnumber, gennr):
    """Overeni spravnosti uziv cisla a
    vytvoreni nasledne odpovedi s pomoci bull_cow_answer fce."""
    outcom = str()
    bc_answers = f'{bull_cow_answer(gennr, inpnumber)[0]}\n{bull_cow_answer(gennr, inpnumber)[1]}'
    if inpnumber == gennr: 
        print(bc_answers)
        print(f'Gratulaceeee! Super správně! Číslo je {gennr} :)')
        outcom = "done" 
        print(SEPS*17)
        print('...Chceš zkusit znovu? A/N')
        repe = input()
        if repe == "A" or repe == "a":
            print(SEPS*23)
            game_progress()
        else:
            exit()

    if len(inpnumber) == 0:
        outcom = "error"
        print("Zadej prosím znovu, číslo musí být 4místné.")

    elif len(inpnumber) != 0: 
        if len(inpnumber) != 4:
            print("Zadej prosím znovu, číslo musí být 4místné.")
            outcom = "error"

        if inpnumber[0] == "0":
                print("Zadej prosím znovu, první číslice nesmí být 0.")
                outcom = "error"

        if inpnumber.isnumeric() is False:
                print("Zadej prosím znovu, číslo musí obsahovat pouze číslice.")
                outcom = "error"

        for jedn in inpnumber:
            if inpnumber.count(jedn) > 1:
                print("Zadej prosím znovu, žádná číslice se nesmí opakovat.")
                outcom = "error"
                break
        print(bc_answers)
        
    if outcom != "error" and inpnumber != gennr:
         print("Zadej prosím znovu. Struktura čísel je správná, hodnota však není rovna počítačem generovanému číslu.")
         outcom = "error"
    print(SEPS*17)
    return outcom

def game_progress():
    """Uzivatelske rozhrani programu a zadani vstupu uzivatelem."""
    print(f'Ahoj!\n{SEPS*17}\nVytvořila jsem pro Tebe náhodné 4místné číslo.')
    random_number = generate_nr()
    print(f'Zahrajme si s ním hru \"Bulls and cows\"!')
    print(SEPS*17)
    print('Zadej jakékoliv číslo:')
    usercis = input()
    while check_user_input(usercis, random_number) == "error":
        usercis = input("Nové číslo: ")

if __name__ == "__main__":
    game_progress()
