import mysql.connector
import random

mydb = mysql.connector.connect(
    host = 'localhost',
    user = '',
    password = '',
    database = 'quiz_db'
)





mycursor = mydb.cursor(buffered=True)

get_country = ("SELECT name FROM quiz_db.countries ORDER BY RAND();")

get_city = ("SELECT name FROM quiz_db.cities ORDER BY RAND();")

get_continent = ("SELECT name FROM quiz_db.continents ORDER BY RAND();")


# 42 COUNTRIES


# QUESTION GENERATOR

qtd_perguntas = 10
runtime_bool = False
contador_perguntas = 0
contador_acertos = 0
contador_erros = 0

def get_number_continents():
    get_number_of_continents = ("SELECT COUNT(id_continents) FROM continents;")
    mycursor.execute(get_number_of_continents)
    temp = mycursor.fetchone()
    num_continents = temp[0]
    return num_continents

def get_continent_from_country():
    get_country_contID_query = ("SELECT id_continents FROM countries WHERE name = %s ;")
    mycursor.execute(get_country_contID_query, (one_country[0],))
    temp = mycursor.fetchone()
    country_contID = temp[0]
    return country_contID

def check_if_continent_is_correct():
    check_if_continent_correct_query = ("SELECT name FROM continents WHERE id_continents = %s ;")
    mycursor.execute(check_if_continent_correct_query, (country_contID,))
    temp2 = mycursor.fetchone()
    name_continent = temp2[0]
    return name_continent

def get_capital(pais):
    get_capital_query = ("SELECT capital FROM countries WHERE name = %s ;")
    mycursor.execute(get_capital_query, (pais,))
    temp2 = mycursor.fetchone()
    name_capital = temp2[0]
    return name_capital

def get_country_from_cityNAME(cityNAME):
    get_country_query = ("SELECT countries.name FROM cities INNER JOIN countries on cities.id_countries = countries.id_countries AND cities.name= %s ;")
    mycursor.execute(get_country_query, (cityNAME,))
    temp2 = mycursor.fetchone()
    name_country = temp2[0]
    return name_country

def get_right_continent_from_continentID():
    get_right_continent = ("SELECT name FROM continents WHERE id_continents = %s ;")
    mycursor.execute(get_right_continent, (country_contID,))
    one_continent = mycursor.fetchone()
    return one_continent

def get_right_country_from_countryID():
    get_right_country = ("SELECT name FROM countries WHERE id_countries = %s ;")
    mycursor.execute(get_right_country, (city_countryID,))
    one_country = mycursor.fetchone()
    return one_country

def resp_yes_no():
    resp_usuario = ""
    while resp_usuario != 'yes' or 'no':
        resp_usuario = input()
        if resp_usuario == 'yes':
            return 'yes',1,1
        elif resp_usuario == 'no':
            return 'no',1,1
        else:
            print("Please answer with yes or no")

def resp_name():
    resp_usuario = ""
    valid_answer_boolean = False
    while valid_answer_boolean == False:
        resp_usuario = input()
        if check_if_integer(resp_usuario) == True:
            print("Please do not type a number.")
        elif resp_usuario == "":
            print("Please enter an answer.")
        else:
            return resp_usuario


def check_if_integer(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False


def resp_integer():
    resp_usuario = -1
    while resp_usuario < 0 or resp_usuario > 100 or None or not int:
        resp_usuario = int(input())
        if resp_usuario > 100:
            print("Please consider a reasonable amount. ")
        if resp_usuario < 0:
            print("Number can't be negative. ")
        if check_if_integer(resp_usuario) == False:
            print("Please enter an integer value. ")
        return resp_usuario



while contador_perguntas < qtd_perguntas:
    # random number generator (tipo de pergunta)
    randlist = [1,2,3,4,5]
    randchoice = random.choices(randlist, weights = [4,4,5,0.6,2], k=1)
    rand = randchoice[0]
    if rand == 1:
        mycursor.execute(get_country)
        one_country = mycursor.fetchone()
        # rand2 para dar 50/50 chance de ter country -> continent match do q previamente
        # 1 sendo correto (da match), 2 incorreto (nao da match)
        rand2 = random.randint(1,2)
        one_continent = ""
        if rand2 == 1:
            country_contID = get_continent_from_country()
            one_continent = get_right_continent_from_continentID()
        if rand2 == 2:
            mycursor.execute(get_continent)
            one_continent = mycursor.fetchone()
        resp_boolean = False
        while resp_boolean == False:
            print("Does "+one_country[0]+" belongs to "+one_continent[0]+" ?")
            country_contID = get_continent_from_country()
            # use id above (int) to put on query below
            name_continent = check_if_continent_is_correct()


            # se nome do get_continent for igual a do pais (query pelo id) logo eh correto
            if name_continent == one_continent[0]:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
            else:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
    if rand == 2:
        mycursor.execute(get_country)
        temp = mycursor.fetchone()
        one_country = temp[0]
        rand2 = random.randint(1,2)
        one_city = ""
        if rand2 == 1:
            one_city = get_capital(one_country)
        if rand2 == 2:
            mycursor.execute(get_city)
            temp = mycursor.fetchone()
            one_city = temp[0]
        resp_boolean = False
        while resp_boolean == False:
            print("Is " + one_city + " the capital of " + one_country + " ?")

            capital_of_onecountry = get_capital(one_country)


            if capital_of_onecountry == one_city:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
            else:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
    if rand == 3:
        mycursor.execute(get_city)
        temp = mycursor.fetchone()
        one_city = temp[0]
        rand2 = random.randint(1,2)
        one_country = ""
        if rand2 == 1:
            one_country = get_country_from_cityNAME(one_city)
        if rand2 == 2:
            mycursor.execute(get_country)
            temp = mycursor.fetchone()
            one_country = temp[0]
        resp_boolean = False
        while resp_boolean == False:
            print("Is " + one_city + " located in " + one_country + " ?")

            check_country = get_country_from_cityNAME(one_city)

            if one_country == check_country:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
            else:
                temp_return = resp_yes_no()
                if temp_return[0] == 'yes':
                    contador_perguntas += temp_return[1]
                    contador_erros += temp_return[2]
                    resp_boolean = True
                else:
                    contador_perguntas += temp_return[1]
                    contador_acertos += temp_return[2]
                    resp_boolean = True
    if rand == 4:
        num_continents = get_number_continents()
        resp_boolean = False
        while resp_boolean == False:
            print("How many continents are there? ")
            resp_usuario = resp_integer()
            if resp_usuario == num_continents:
                contador_perguntas += 1
                contador_acertos += 1
                resp_boolean = True
            else:
                contador_perguntas += 1
                contador_erros += 1
                resp_boolean = True
    if rand == 5:
        mycursor.execute(get_country)
        temp = mycursor.fetchone()
        one_country = temp[0]
        resp_boolean = False
        while resp_boolean == False:
            print("What is the capital of " + one_country + " ?")

            capital_of_onecountry = get_capital(one_country)

            temp_return = resp_name()

            if temp_return == capital_of_onecountry:
                contador_perguntas += 1
                contador_acertos += 1
                resp_boolean = True
            else:
                contador_perguntas += 1
                contador_erros += 1
                resp_boolean = True




print("De " + str(qtd_perguntas) + " perguntas: ")
print("Acertou " + str(contador_acertos) + " perguntas.")
print("Errou " + str(contador_erros) + " perguntas.")


mydb.close()



