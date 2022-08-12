import os
import re
from hometask_5 import Normalization, AddToFile, Inputting
from datetime import datetime, date
import calendar



class FileParsing:

    def main_code(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'data')
        with open(filename) as f:
            contents = f.readlines()
            print(contents)
        contents1 = []

        for i in range(len(contents)):
            contents1.append(contents[i].strip("\n"))
        print(contents1)

        listy1 = []
        for i in range(len(contents1)):
            listy1.append(contents1[i].split("/"))
            listy1[i] = list(filter(None, listy1[i]))
        print(listy1)

        listy = ['NEWS', 'PRIVAT_AD', 'WORD_OF_THE_DAY']

        for i in range(len(listy1)):
            if listy1[i][0] == listy[0]:
                print('it is NEWS line')
                len_attr = len(listy1[i])
                if len_attr == 3:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy1[i][1], listy1[i])
                    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    text1 = AddToFile()
                    text1.add_to_file_hometask5(f"News -------------------------\n{norm}{listy1[i][2].title()}, {dt_string}\n------------------------------\n\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false_hometask6(str(listy1[i]) + "\n")
            elif listy1[i][0] == listy[1]:
                print('it is ADs line')
                len_attr = len(listy1[i])
                if len_attr == 5:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy1[i][1], listy1[i])
                    matched1 = re.match('[2][0][2-9][2-9]', (listy1[i][2]))
                    is_match1 = bool(matched1)
                    if is_match1 == True:
                        try:
                            input1 = Inputting()
                            d, dt = input1.input_date_hometask6(int(listy1[i][2]), int(listy1[i][3]), int(listy1[i][4]))
                            text1 = AddToFile()
                            text1.add_to_file_hometask5(f"Private Ad -------------------\n{norm}Actual until: {dt}, {d} days left\n------------------------------\n\n")
                        except:
                            text2 = AddToFile()
                            text2.add_to_file_false_hometask6(str(listy1[i]) + "\n")
                    else:
                        text2 = AddToFile()
                        text2.add_to_file_false_hometask6(str(listy1[i]) + "\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false_hometask6(str(listy1[i]) + "\n")
            else:
                print('it is WORD OF THE DAY line')
                len_attr = len(listy1[i])
                listy[i].strip('')
                if len_attr == 2:
                    norm1 = Normalization()
                    norm = norm1.text_normalization(listy1[i][1], listy1[i])
                    curr_date = date.today()
                    weekd = calendar.day_name[curr_date.weekday()]
                    text1 = AddToFile()
                    text1.add_to_file_hometask5(
                        f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false_hometask6(str(listy1[i]) + "\n")

        #os.remove(r'C:\Users\Sofiia_Kalishchuk\hometasks_python_dqe\data')