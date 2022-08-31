from datetime import datetime, date
import calendar
import os
import re
import csv
from collections import Counter
import json
import xml.etree.ElementTree as ET
import pyodbc


class Normalization:

    def text_normalization(self, str_name):
        str_sentences = ""
        if str_name[-1] == '.':  # remove the last period to avoid double periods in the last sentence
            str_name = str_name[:-1]
        sentences = list(str_name.split("."))  # Create list based on each sentence.
        for i in range(len(sentences)):  # Loop through list which is each sentence.
            sentences[i] = sentences[i].strip()  # Remove any leading or trailing spaces.
            sentences[i] = sentences[i].strip(".")  # Remove any periods.
            sentences[i] = sentences[i][:1].upper() + sentences[i][1:]  # Concatenate string with first letter upper.
            str_sentences += sentences[i] + ".\n"  # Concatenate a final string with all sentences.
        return str_sentences


class Inputting:
    def __init__(self, blck1="""Choose: 
    1 to add item to the \"News\"
    2 to add item to the \"Private ad\"
    3 to add item to the \"Word of the day\"
    4 to use the file 'data.txt'
    5 to use the file 'json_text.json'
    6 to use the file 'xml_text.xml'
    7 to exit
    
    Your choice: """, count=True, user_choice=True):
        self.blck1 = blck1
        self.count = count
        self.user_choice = user_choice

    def error_handling_for_input(self):
        while self.count:
            try:
                self.user_choice = int(input(self.blck1))
                print(f"Your choice is {self.user_choice}")
                while self.user_choice == 0:
                    self.user_choice = int(input(self.blck1))
                return self.user_choice
            except:
                print("Please, type only 1, 2, 3, or 4")

    def input_date_hometask5(self):
        self.year = int(input("Input the expiration date. Year: "))
        self.month = int(input("Input the expiration date. Month: "))
        self.day = int(input("Input the expiration date. Day: "))
        self.exp_date = date(self.year, self.month, self.day)
        self.dt_today = datetime.date(datetime.now())
        self.time_remaining = self.exp_date - self.dt_today
        self.time_remaining1 = self.time_remaining.days
        return self.time_remaining1, self.exp_date


class AddToFile:

    def add_to_file(self, text, file):
        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, file)
        try:
            with open(filename1, "x") as f:
                f.write(text)
                f.close()
        except:
            f = open(filename1, "a")
            f.write(text)
            f.close()
            pass

    def file_opening(self, input_file):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, input_file)

        try:
            if input_file == 'data.txt':
                with open(filename) as f:
                    contents = f.readlines()
                    print(contents)
                return contents
            elif input_file == 'json_text.json':
                json_dictionary = json.load(open(filename))
                print(json_dictionary)
                return json_dictionary
            elif input_file == 'xml_text.xml':
                xml_file = ET.parse(filename)
                print(xml_file)
                return xml_file
            elif input_file == 'newsfeed.txt':
                with open(filename) as file:
                    data = file.read()
                return data
        except IndexError:
            print('there is no such file')


class OperationalHometask5:

    def while_loop5(self):
        input1 = Inputting()
        input1.error_handling_for_input()
        while input1.user_choice:
            if input1.user_choice == 1:
                news_text = input("Write the news: ")
                city = input("The origin of the news (City): ")
                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                norm1 = Normalization()
                norm = norm1.text_normalization(news_text)
                text1 = AddToFile()
                text1.add_to_file(
                    f"News -------------------------\n{norm}{city.title()},{dt_string}\n------------------------------\n\n", 'newsfeed.txt')
                input1.error_handling_for_input()
            elif input1.user_choice == 2:
                ad_text = input("Write the private advertisement: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(ad_text)
                d, dt = input1.input_date_hometask5()
                text1 = AddToFile()
                text1.add_to_file(
                    f"Private Ad -------------------\n{norm}Actual until: {dt}, {d} days left\n------------------------------\n\n", 'newsfeed.txt')
                input1.error_handling_for_input()
            elif input1.user_choice == 3:
                word = input("Write a word of the day: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(word)
                curr_date = date.today()
                weekd = calendar.day_name[curr_date.weekday()]
                text1 = AddToFile()
                text1.add_to_file(
                    f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n", 'newsfeed.txt')
                input1.error_handling_for_input()
            elif input1.user_choice == 4:
                print("The end!")
                break
            else:
                print("Please, type only 1, 2, 3, or 4")
                input1.error_handling_for_input()


class FileParsing:

    def file_txt_preparation(self, contents):

        contents1 = [contents[i].strip("\n") for i in range(len(contents))]
        print(contents1)

        listy1 = [contents1[i].split("/") for i in range(len(contents1))]
        listy1 = [list(filter(None, listy1[i])) for i in range(len(listy1))]
        listy1 = list(filter(None, listy1))
        print(listy1)
        return listy1

    def file_json_preparation(self, json_dictionary):

        list_of_keys = [key for key in json_dictionary]
        print(list_of_keys)

        list_of_keys_dicts = list(json_dictionary.values())
        print(list_of_keys_dicts)
        list_of_values = [list_of_keys_dicts[i].values() for i in range(len(list_of_keys_dicts))]
        print(list(list_of_values[0]))
        new_list = [list(list_of_values[i]) for i in range(len(list_of_values))]
        print(new_list)

        for i in range(len(new_list)):
            new_list[i].insert(0, list_of_keys[i])
        print(new_list)
        new_list = [list(filter(None, new_list[i])) for i in range(len(new_list))]
        new_list = list(filter(None, new_list))
        return new_list

    def file_xml_preparation(self, xml_file):

        root = xml_file.getroot()
        list_of_text_all = []
        for child in root.iter('NEWS'):
            list_of_text = ['NEWS', '', '']
            for text in child:
                if text.tag == 'news_text':
                    list_of_text[1] = text.text
                elif text.tag == 'city':
                    list_of_text[2] = text.text
            list_of_text_all.append(list_of_text)
        for child in root.iter('PRIVAT_AD'):
            list_of_text = ['PRIVAT_AD', '', '', '', '']
            for text in child:
                if text.tag == 'ad_text':
                    list_of_text[1] = text.text
                elif text.tag == 'year':
                    list_of_text[2] = text.text
                elif text.tag == 'month':
                    list_of_text[3] = text.text
                elif text.tag == 'day':
                    list_of_text[4] = text.text
            list_of_text_all.append(list_of_text)
        for child in root.iter('WORD_OF_THE_DAY'):
            list_of_text = ['WORD_OF_THE_DAY', '']
            for text in child:
                if text.tag == 'a_word':
                    list_of_text[1] = text.text
            list_of_text_all.append(list_of_text)

        print(list_of_text_all)
        list_of_text_all = [list(filter(None, list_of_text_all[i])) for i in range(len(list_of_text_all))]
        list_of_text_all = list(filter(None, list_of_text_all))
        return list_of_text_all

    def if_clause_any_file_parsing(self, listy):
        NEWS = 'NEWS'
        PRIVAT_AD = 'PRIVAT_AD'
        WORD_OF_THE_DAY = 'WORD_OF_THE_DAY'

        for i in range(len(listy)):
            len_attr = len(listy[i])
            if listy[i][0].startswith(NEWS):
                print('This is NEWS attribute')
                news_final_list = []
                if len_attr == 3:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy[i][1])
                    city = str(listy[i][2]).replace(" ", "")
                    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    text1 = AddToFile()
                    text1.add_to_file(
                        f"News -------------------------\n{norm}{city.title()}, {dt_string}\n------------------------------\n\n", 'newsfeed.txt')
                    news_final_list = news_final_list + [norm, city.title(), dt_string]
                    y = DBConnection()
                    y.create_table('NEWS')
                    y.insert('NEWS', news_final_list)
                else:
                    text2 = AddToFile()
                    text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')
            elif listy[i][0].startswith(PRIVAT_AD):
                print('This is PRIVAT_AD attribute')
                news_final_list = []
                if len_attr == 5:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy[i][1])
                    matched1 = re.match('[2][0][2-9][2-9]', str(listy[i][2]))
                    if matched1:
                        try:
                            exp_date = date(int(listy[i][2]), int(listy[i][3]), int(listy[i][4]))
                            dt_today = datetime.date(datetime.now())
                            time_remaining = exp_date - dt_today
                            time_remaining1 = time_remaining.days
                            text1 = AddToFile()
                            text1.add_to_file(
                                f"Private Ad -------------------\n{norm}Actual until: {exp_date}, {time_remaining1} days left\n------------------------------\n\n", 'newsfeed.txt')
                            news_final_list = news_final_list + [norm, exp_date, time_remaining1]
                            y = DBConnection()
                            y.create_table('PRIVAT_AD')
                            y.insert('PRIVAT_AD', news_final_list)
                        except:
                            text2 = AddToFile()
                            text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')
                            pass
                    else:
                        text2 = AddToFile()
                        text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')
                else:
                    text2 = AddToFile()
                    text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')
            elif listy[i][0].startswith(WORD_OF_THE_DAY):
                print('This is WORD_OF_THE_DAY attribute')
                news_final_list = []
                if len_attr == 2:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy[i][1])
                    curr_date = date.today()
                    weekday = calendar.day_name[curr_date.weekday()]
                    text1 = AddToFile()
                    text1.add_to_file(
                        f"A word of the day: -----------\n{norm}Today is {weekday}\n------------------------------\n\n", 'newsfeed.txt')
                    news_final_list = news_final_list + [norm, weekday]
                    y = DBConnection()
                    y.create_table('WORD_OF_THE_DAY')
                    y.insert('WORD_OF_THE_DAY', news_final_list)
                else:
                    text2 = AddToFile()
                    text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')
            else:
                text2 = AddToFile()
                text2.add_to_file((str(listy[i]) + "\n"), 'newsfeed_false.txt')

        # os.remove(r'C:\Users\Sofiia_Kalishchuk\hometasks_python_dqe\data.txt')


class MakeTwoCsvFiles:

    def first_csv_file(self, data):

        counts = Counter(re.findall('\w+', data))
        list1 = list(counts.keys())
        list2 = list(counts.values())
        list3 = [str(list1[i].lower()) + '-' + str(list2[i]) for i in range(len(list1))]

        with open('text1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, 'unix')
            writer.writerow(list3)

    def second_csv_file(self, data):

        c = re.findall('\w+', data)
        c1 = ''.join(c)
        text = str()
        for j in c1:
            if j.isalpha():
                text = text + j

        text1 = Counter(text)
        list3 = list(text1.keys())
        sum1 = sum(text1.values())

        upper = []
        lower = []
        for j in range(len(list3)):
            u = list3[j].isupper()
            if u:
                upper.append(list3[j])
            else:
                lower.append(list3[j])

        matchy_list = []
        for low in range(len(lower)):
            for r in range(len(upper)):
                lowercase_letter = upper[r]
                if lowercase_letter.lower() == lower[low]:
                    #print('we have a match')
                    matchy_list.append(lower[low])

        seen = set()  # set for all letters from all dictionaries without duplication
        dupes = set()  # with this cycle we make the list of duplicates and elements that are not duplicated
        for i in lower:
            if i in matchy_list:
                dupes.add(i)
            else:
                seen.add(i)

        not_matchy_list = list(seen)
        not_matchy_list_values = []

        for y in range(len(not_matchy_list)):
            not_matchy_list_values.append(text1.get(not_matchy_list[y]))

        sum_for_matched = []
        upper_values = []
        for y in range(len(matchy_list)):
            low1 = str(matchy_list[y])
            first = text1.get(low1)
            up = matchy_list[y]
            up1 = up.upper()
            second = text1.get(up1)
            upper_values.append(text1.get(up1))
            summy = first + second
            sum_for_matched.append(summy)

        with open('text2.csv', 'w', newline='') as csvfile:
            headers = ['letter', 'cout_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for i in range(len(matchy_list)):
                writer.writerow(
                    {'letter': matchy_list[i], 'cout_all': sum_for_matched[i], 'count_uppercase': upper_values[i],
                     'percentage': ((sum_for_matched[i]) / sum1) * 100})
            for i in range(len(not_matchy_list)):
                writer.writerow(
                    {'letter': not_matchy_list[i], 'cout_all': not_matchy_list_values[i], 'count_uppercase': 0,
                     'percentage': ((not_matchy_list_values[i]) / sum1) * 100})


class DBConnection:

    def __init__(self):
        with pyodbc.connect('DRIVER={Sqlite3 ODBC Driver};Direct=True;Database=hometask_10.db;String Types=Unicode') as self.connection:
            self.cursor = self.connection.cursor()

    def create_table(self, table_name):

        if table_name == 'NEWS':
            if self.cursor.tables(table='NEWS', tableType='TABLE').fetchone():
                print("table NEWS exists")
            else:
                sql_text = f'''CREATE TABLE {table_name}(
                            news varchar(500) not null PRIMARY KEY,
                            city varchar(30) not null,
                            todays_date varchar(30) not null
                            )'''
                self.cursor.execute(sql_text)
                print(f"Table {table_name} has been created successfully !!")
                self.connection.commit()
        elif table_name == 'PRIVAT_AD':
            if self.cursor.tables(table='PRIVAT_AD', tableType='TABLE').fetchone():
                print("table PRIVAT_AD exists")
            else:
                sql_text = f'''CREATE TABLE {table_name}(
                            privat_ad varchar(200) not null PRIMARY KEY,
                            actual_until varchar(30) not null,
                            days_left int not null
                            )'''
                self.cursor.execute(sql_text)
                print(f"Table {table_name} has been created successfully !!")
                self.connection.commit()
        elif table_name == 'WORD_OF_THE_DAY':
            if self.cursor.tables(table='WORD_OF_THE_DAY', tableType='TABLE').fetchone():
                print("table WORD_OF_THE_DAY exists")
            else:
                sql_text = f'''CREATE TABLE {table_name}(
                            a_word varchar(30) not null PRIMARY KEY,
                            day_of_the_week varchar(11) not null
                            )'''
                self.cursor.execute(sql_text)
                print(f"Table {table_name} has been created successfully !!")
                self.connection.commit()

    def insert(self, table_name, listt):
        if table_name == 'NEWS':
            self.cursor.execute('insert into NEWS(news, city, todays_date) values(?, ?, ?)', listt[0], listt[1], str(listt[2]))
        elif table_name == 'PRIVAT_AD':
            self.cursor.execute('insert into PRIVAT_AD(privat_ad, actual_until, days_left) values(?, ?, ?)', listt[0], str(listt[1]),
                                listt[2])
        elif table_name == 'WORD_OF_THE_DAY':
            self.cursor.execute('insert into WORD_OF_THE_DAY(a_word, day_of_the_week) values(?, ?)', listt[0],
                                listt[1])
        print(f"Row was inserted  into {table_name} successfully !!")
        self.connection.commit()

    def select(self):
        self.cursor.execute('SELECT * FROM NEWS ')
        rows = self.cursor.fetchall()
        print(rows)


class HometaskFinal:

    def while_loop(self):
        input1 = Inputting()
        input1.error_handling_for_input()
        while input1.user_choice:
            if input1.user_choice == 1:
                news_text = input("Write the news: ")
                city = input("The origin of the news (City): ")
                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                norm1 = Normalization()
                norm = norm1.text_normalization(news_text)
                x = AddToFile()
                x.add_to_file(
                    f"News -------------------------\n{norm}{city.title()},{dt_string}\n------------------------------\n\n", 'newsfeed.txt')
                a = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(a)
                x1.second_csv_file(a)
                input1.error_handling_for_input()
            elif input1.user_choice == 2:
                ad_text = input("Write the private advertisement: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(ad_text)
                d, dt = input1.input_date_hometask5()
                x = AddToFile()
                x.add_to_file(
                    f"Private Ad -------------------\n{norm}Actual until: {dt}, {d} days left\n------------------------------\n\n", 'newsfeed.txt')
                a = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(a)
                x1.second_csv_file(a)
                input1.error_handling_for_input()
            elif input1.user_choice == 3:
                word = input("Write a word of the day: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(word)
                curr_date = date.today()
                weekd = calendar.day_name[curr_date.weekday()]
                x = AddToFile()
                x.add_to_file(
                    f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n", 'newsfeed.txt')
                a = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(a)
                x1.second_csv_file(a)
                input1.error_handling_for_input()
            elif input1.user_choice == 4:
                x = AddToFile()
                a = x.file_opening('data.txt')
                b = FileParsing()
                c = b.file_txt_preparation(a)
                b.if_clause_any_file_parsing(c)
                d = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(d)
                x1.second_csv_file(d)
                input1.error_handling_for_input()
            elif input1.user_choice == 5:
                x = AddToFile()
                a = x.file_opening('json_text.json')
                b = FileParsing()
                c = b.file_json_preparation(a)
                b.if_clause_any_file_parsing(c)
                d = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(d)
                x1.second_csv_file(d)
                input1.error_handling_for_input()
            elif input1.user_choice == 6:
                x = AddToFile()
                a = x.file_opening('xml_text.xml')
                b = FileParsing()
                c = b.file_xml_preparation(a)
                b.if_clause_any_file_parsing(c)
                d = x.file_opening('newsfeed.txt')
                x1 = MakeTwoCsvFiles()
                x1.first_csv_file(d)
                x1.second_csv_file(d)
                input1.error_handling_for_input()
            elif input1.user_choice == 7:
                print("The end!")
                break
            else:
                print("Please, type only 1, 2, 3, or 4")
                input1.error_handling_for_input()


