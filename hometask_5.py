from datetime import datetime, date
import calendar

def text_normalization(strName):
    strSentences = ""
    words = list(strName.split(". ")) # Create list based on each sentence.
    for i in range(len(words)): # Loop through list which is each sentence.
        words[i] = words[i].strip() # Remove any leading or trailing spaces.
        words[i] = words[i].strip(".") # Remove any periods.
        words[i] = words[i][:1].upper() + words[i][1:] # Concatenate string with first letter upper.
        strSentences += words[i] + ".\n" # Concatenate a final string with all sentences.
    return strSentences

def input_date():
    year = int(input("Input the expiration date. Year: "))
    month = int(input("Input the expiration date. Month: "))
    day = int(input("Input the expiration date. Day: "))
    exp_date = date(year, month, day)
    dt_today = datetime.date(datetime.now())
    time_remaining = exp_date - dt_today
    time_remaining1 = time_remaining.days
    print(time_remaining1)
    return time_remaining1, exp_date

def add_to_file(text):
    try:
        with open("newsfeed.txt", "x") as f:
            f.write(text)
            f.close()
    except:
        f = open(r"newsfeed.txt", "a")
        f.write(text)
        f.close()

a = """Hello!
Choose 1 to add item to the \"News\"
Choose 2 to add item to the \"Private ad\"
Choose 3 to add item to the \"Word of the day\"
Choose 4 to exit
Your choice: """
a1 = """1 to add item to the \"News\"
2 to add item to the \"Private ad\"
3 to add item to the \"Word of the day\"
4 to exit
Your choice: """

def text_input(text):
    global user_choice
    user_choice = int(input(text))
    print(f"Your choice is {user_choice}")

try:
    text_input(a)
except:
    print("Please, type only 1, 2, 3, or 4")
    text_input(a1)

while user_choice:
    if user_choice == 1:
        news_text = input("Write the news: ")
        city = input("The origin of the news (City): ")
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        a = text_normalization(news_text)
        add_to_file(f"News -------------------------\n{a}{city}, {dt_string}\n------------------------------\n\n")
        text_input(a1)
    elif user_choice == 2:
        ad_text = input("Write the private advertisement: ")
        a = text_normalization(ad_text)
        d, dt = input_date()
        add_to_file(f"Private Ad -------------------\n{a}Actual until: {dt}, {d} days left\n------------------------------\n\n")
        text_input(a1)
    elif user_choice == 3:
        word = input("Write a word of the day: ")
        a = text_normalization(word)
        curr_date = date.today()
        weekd = calendar.day_name[curr_date.weekday()]
        add_to_file(f"A word of the day: -----------\n{a}Today is {weekd}\n------------------------------\n\n")
        text_input(a1)
    else:
        user_choice = False
print("The end!")
