from datetime import datetime, date
import calendar
import os
import re


class Normalization:
    def __init__(self, str_name, str_name1):
        self.str_name = str_name
        self.str_name1 = str_name1

    def text_normalization(self):
        try:
            self.str_sentences = ""
            if (self.str_name[-1] == '.'): # remove the last period to avoid double periods in the last sentence
                self.str_name = self.str_name[:-1]
            sentences = list(self.str_name.split("."))  # Create list based on each sentence.
            for i in range(len(sentences)):  # Loop through list which is each sentence.
                sentences[i] = sentences[i].strip()  # Remove any leading or trailing spaces.
                sentences[i] = sentences[i].strip(".")  # Remove any periods.
                sentences[i] = sentences[i][:1].upper() + sentences[i][1:]  # Concatenate string with first letter upper.
                self.str_sentences += sentences[i] + ".\n"  # Concatenate a final string with all sentences.
            return self.str_sentences
        except:
            print('hello?')
            text2 = AddToFile()
            text2.add_to_file_false(self.str_name1)

# a = Normalization("Some text for the check. one more sentence.the last one.")
# print(a.text_normalization())


class Inputting:
    def __init__(self, blck1="""Choose: 
1 to add item to the \"News\"
2 to add item to the \"Private ad\"
3 to add item to the \"Word of the day\"
4 to exit
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

    def input_date(self):
        self.year = int(input("Input the expiration date. Year: "))
        self.month = int(input("Input the expiration date. Month: "))
        self.day = int(input("Input the expiration date. Day: "))
        self.exp_date = date(self.year, self.month, self.day)
        self.dt_today = datetime.date(datetime.now())
        self.time_remaining = self.exp_date - self.dt_today
        self.time_remaining1 = self.time_remaining.days
        return self.time_remaining1, self.exp_date

    def input_date1(self, year, month, day):
        self.exp_date = date(year, month, day)
        self.dt_today = datetime.date(datetime.now())
        self.time_remaining = self.exp_date - self.dt_today
        self.time_remaining1 = self.time_remaining.days
        return self.time_remaining1, self.exp_date


class AddToFile:
    def add_to_file(self, text):
        try:
            with open("newsfeed.txt", "x") as f:
                f.write(text)
                f.close()
        except:
            f = open(r"newsfeed.txt", "a")
            f.write(text)
            f.close()
    def add_to_file_false(self, text):
        try:
            with open("newsfeed_false.txt", "x") as f:
                f.write(text)
                f.close()
        except:
            f = open(r"newsfeed_false.txt", "a")
            f.write(text)
            f.close()


class Operational:

    def while_loop(self):
        input1 = Inputting()
        input1.error_handling_for_input()
        while input1.user_choice:
            if input1.user_choice == 1:
                news_text = input("Write the news: ")
                city = input("The origin of the news (City): ")
                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                norm1 = Normalization(news_text)
                norm = norm1.text_normalization()
                text1 = AddToFile()
                text1.add_to_file(f"News -------------------------\n{norm}{city.title()},{dt_string}\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 2:
                ad_text = input("Write the private advertisement: ")
                norm1 = Normalization(ad_text)
                norm = norm1.text_normalization()
                d, dt = input1.input_date()
                text1 = AddToFile()
                text1.add_to_file(f"Private Ad -------------------\n{norm}Actual until: {d3t}, {d} days left\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 3:
                word = input("Write a word of the day: ")
                norm1 = Normalization(word)
                norm = norm1.text_normalization()
                curr_date = date.today()
                weekd = calendar.day_name[curr_date.weekday()]
                text1 = AddToFile()
                text1.add_to_file(f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 4:
                print("The end!")
                break
            else:
                print("Please, type only 1, 2, 3, or 4")
                input1.error_handling_for_input()


class Operational1:

    def main_code(self):
        with open(r'C:\Users\Sofiia_Kalishchuk\hometasks_python_dqe\data') as f:
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
                    norm1 = Normalization(listy1[i][1], listy1[i])
                    norm = norm1.text_normalization()
                    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    text1 = AddToFile()
                    text1.add_to_file(
                        f"News -------------------------\n{norm}{listy1[i][2].title()}, {dt_string}\n------------------------------\n\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false(str(listy1[i]) + "\n")
            elif listy1[i][0] == listy[1]:
                print('it is ADs line')
                len_attr = len(listy1[i])
                if len_attr == 5:
                    norm1 = Normalization(listy1[i][1], listy1[i])
                    norm = norm1.text_normalization()
                    matched1 = re.match('[2][0][2-9][2-9]', (listy1[i][2]))
                    matched2 = re.match('[1-12]', (listy1[i][3]))
                    matched3 = re.match('[1-31]', (listy1[i][4]))
                    is_match1 = bool(matched1)
                    is_match2 = bool(matched2)
                    is_match3 = bool(matched3)
                    if is_match1 == True and is_match2 == True and is_match3 == True:
                        input1 = Inputting()
                        d, dt = input1.input_date1(int(listy1[i][2]), int(listy1[i][3]), int(listy1[i][4]))
                        text1 = AddToFile()
                        text1.add_to_file(
                            f"Private Ad -------------------\n{norm}Actual until: {dt}, {d} days left\n------------------------------\n\n")
                    else:
                        text2 = AddToFile()
                        text2.add_to_file_false(str(listy1[i]) + "\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false(str(listy1[i]) + "\n")
            else:
                print('it is WORD OF THE DAY line')
                len_attr = len(listy1[i])
                listy[i].strip('')
                if len_attr == 2:
                    norm1 = Normalization(listy1[i][1], listy1[i])
                    norm = norm1.text_normalization()
                    curr_date = date.today()
                    weekd = calendar.day_name[curr_date.weekday()]
                    text1 = AddToFile()
                    text1.add_to_file(
                        f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n")
                else:
                    text2 = AddToFile()
                    text2.add_to_file_false(str(listy1[i]) + "\n")

        #os.remove(r'C:\Users\Sofiia_Kalishchuk\hometasks_python_dqe\data')


# if __name__ == "__main__":
#     x = Operational()
#     x.while_loop()