from datetime import datetime, date
import calendar



class Normalization:

    def text_normalization(self, str_name, str_name1):
        try:
            str_sentences = ""
            if (str_name[-1] == '.'): # remove the last period to avoid double periods in the last sentence
                str_name = str_name[:-1]
            sentences = list(str_name.split("."))  # Create list based on each sentence.
            for i in range(len(sentences)):  # Loop through list which is each sentence.
                sentences[i] = sentences[i].strip()  # Remove any leading or trailing spaces.
                sentences[i] = sentences[i].strip(".")  # Remove any periods.
                sentences[i] = sentences[i][:1].upper() + sentences[i][1:]  # Concatenate string with first letter upper.
                str_sentences += sentences[i] + ".\n"  # Concatenate a final string with all sentences.
            return str_sentences
        except:
            text2 = AddToFile()
            text2.add_to_file_false_hometask6(str_name1 + '\n')

# a = Normalization("Some text for the check. one more sentence.the last one.")
# print(a.text_normalization())


class Inputting:

    def __init__(self):
        self.user_choice = True

    def error_handling_for_input(self, blck1="""Choose: 
1 to add item to the \"News\"
2 to add item to the \"Private ad\"
3 to add item to the \"Word of the day\"
4 to exit
Your choice: """, count=True):
        while count:
            try:
                user_choice = int(input(blck1))
                print(f"Your choice is {user_choice}")
                while user_choice == 0:
                    user_choice = int(input(blck1))
                return user_choice
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

    def input_date_hometask6(self, year, month, day, str_name1):
        self.exp_date = date(year, month, day)
        self.dt_today = datetime.date(datetime.now())
        self.time_remaining = self.exp_date - self.dt_today
        self.time_remaining1 = self.time_remaining.days
        return self.time_remaining1, self.exp_date


class AddToFile:

    def add_to_file_hometask5(self, text):
        try:
            with open("newsfeed.txt", "x") as f:
                f.write(text)
                f.close()
        except:
            f = open(r"newsfeed.txt", "a")
            f.write(text)
            f.close()
    def add_to_file_false_hometask6(self, text):
        try:
            with open("newsfeed_false.txt", "x") as f:
                f.write(text)
                f.close()
        except:
            f = open(r"newsfeed_false.txt", "a")
            f.write(text)
            f.close()


class OperationalHometask5:

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
                text1 = AddToFile()
                text1.add_to_file_hometask5(f"News -------------------------\n{norm}{city.title()},{dt_string}\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 2:
                ad_text = input("Write the private advertisement: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(ad_text)
                d, dt = input1.input_date_hometask5()
                text1 = AddToFile()
                text1.add_to_file_hometask5(f"Private Ad -------------------\n{norm}Actual until: {d3t}, {d} days left\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 3:
                word = input("Write a word of the day: ")
                norm1 = Normalization()
                norm = norm1.text_normalization(word)
                curr_date = date.today()
                weekd = calendar.day_name[curr_date.weekday()]
                text1 = AddToFile()
                text1.add_to_file_hometask5(f"A word of the day: -----------\n{norm}Today is {weekd}\n------------------------------\n\n")
                input1.error_handling_for_input()
            elif input1.user_choice == 4:
                print("The end!")
                break
            else:
                print("Please, type only 1, 2, 3, or 4")
                input1.error_handling_for_input()



# if __name__ == "__main__":
#     x = OperationalHometask5()
#     x.while_loop()