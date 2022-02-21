from datetime import datetime

def text_normalization(strName):
    strSentences = ""
    words = list(strName.split(". ")) # Create list based on each sentence.
    for i in range(len(words)): # Loop through list which is each sentence.
        words[i] = words[i].strip() # Remove any leading or trailing spaces.
        words[i] = words[i].strip(".") # Remove any periods.
        words[i] = words[i][:1].upper() + words[i][1:] # Concatenate string with first letter upper.
        strSentences += words[i] + ".\n" # Concatenate a final string with all sentences.
    return strSentences

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
        global news_text
        news_text = input("Write the news: ")
        city = input("The origin of the news (City): ")
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        a = text_normalization(news_text)
        add_to_file(f"News -------------------------\n{a}{city}, {dt_string}\n")
        text_input(a1)
    elif user_choice == 2:
        ad_text = input("Write the private advertisement: ")
        exp_date = input("Write an expiration date: ")
        text_input(a1)
    elif user_choice == 3:
        word = input("Write a word of the day: ")
        text_input(a1)
    else:
        user_choice = False
print("The end!")
