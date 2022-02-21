from datetime import datetime, date
import calendar


class Normalization:
    def __init__(self, str_name):
        self.str_name = str_name

    def text_normalization(self):
        self.str_sentences = ""
        if (self.str_name[-1] == '.'): # remove the last period to avoid double periods in the last sentence
            self.str_name = self.str_name[:-1]
        words = list(self.str_name.split("."))  # Create list based on each sentence.
        for i in range(len(words)):  # Loop through list which is each sentence.
            words[i] = words[i].strip()  # Remove any leading or trailing spaces.
            words[i] = words[i].strip(".")  # Remove any periods.
            words[i] = words[i][:1].upper() + words[i][1:]  # Concatenate string with first letter upper.
            self.str_sentences += words[i] + ".\n"  # Concatenate a final string with all sentences.
        return self.str_sentences
# a = Normalization("Some text for the check. one more sentence.the last one.")
# print(a.text_normalization())

class Inputting:
    def __init__(self, blck="""Hello!
Choose 1 to add item to the \"News\"
Choose 2 to add item to the \"Private ad\"
Choose 3 to add item to the \"Word of the day\"
Choose 4 to exit
Your choice: """, blck1="""1 to add item to the \"News\"
2 to add item to the \"Private ad\"
3 to add item to the \"Word of the day\"
4 to exit
Your choice: """):
        self.blck = blck
        self.blck1 = blck1

    def text_input(self, text):
        global user_choice
        user_choice = int(input(text))
        print(f"Your choice is {user_choice}")
        return user_choice

    def error_handling_for_input(self):
        try:
            self.text_input(self.blck)
        except:
            print("Please, type only 1, 2, 3, or 4")
            self.text_input(self.blck1)

    def input_date(self):
        self.year = int(input("Input the expiration date. Year: "))
        self.month = int(input("Input the expiration date. Month: "))
        self.day = int(input("Input the expiration date. Day: "))
        self.exp_date = date(self.year, self.month, self.day)
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


class Operational:
    def __init__(self, a="""Choose 1 to add item to the \"News\"
Choose 2 to add item to the \"Private ad\"
Choose 3 to add item to the \"Word of the day\"
Choose 4 to exit
Your choice: """):
        self.a = a

    def while_loop(self):
        global user_choice
        input1 = Inputting()
        input1.error_handling_for_input()
        while user_choice:
            if user_choice == 1:
                news_text = input("Write the news: ")
                city = input("The origin of the news (City): ")
                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                norm1 = Normalization(news_text)
                norm = norm1.text_normalization()
                text1 = AddToFile()
                text1.add_to_file(f"News -------------------------\n{norm}{city.title()}, {dt_string}\n------------------------------\n\n")
                input1.text_input(self.a)
            elif user_choice == 2:
                ad_text = input("Write the private advertisement: ")
                norm1 = Normalization(ad_text)
                norm = norm1.text_normalization()
                d, dt = input1.input_date()
                text1 = AddToFile()
                text1.add_to_file(f"Private Ad -------------------\n{norm}Actual until: {dt}, {d} days left\n------------------------------\n\n")
                input1.text_input(self.a)
            elif user_choice == 3:
                word = input("Write a word of the day: ")
                norm1 = Normalization(word)
                norm = norm1.text_normalization()
                curr_date = date.today()
                weekd = calendar.day_name[curr_date.weekday()]
                text1 = AddToFile()
                text1.add_to_file(f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n")
                input1.text_input(self.a)
            elif user_choice == 4:
                print("The end!")
                user_choice = False
            else:
                pass
                print("Please, type only 1, 2, 3, or 4")
                input1.text_input(self.a)

if __name__ == "__main__":
    x = Operational()
    x.while_loop()