text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87 """
list_of_sentence = []

def last_words_in_sentence(text_sample):
    sentence = text_sample.split('.') # split the text into sentences
    j = 0
    for i in sentence:
        list_sentence = sentence[j].split(" ") # each sentence we split into words
        print(list_sentence[len(list_sentence)-1]) # we print the last word of each sentence
        list_of_sentence.append(list_sentence[len(list_sentence)-1]) # a list of all last words of sentences
        j += 1
    sentence_string = " ".join(list_of_sentence)  # the list of last words is converted into the sentence
    print(sentence_string)
    global new_text
    new_text = text_sample + '. ' + sentence_string  # we add the new sentence to the text
    print(new_text)
#print(last_words_in_sentence(text))

def change_of_z(sample_with_added_sentence):
    # the change of 'iZ' and 'iz' to 'is'
    text0 = sample_with_added_sentence.replace('z ', 's ')
    global text1
    text1 = text0.replace('Z ', 's ')
    print(text1)

def final_text_normalization(text_sample):
    normalization = text_sample.split('.')
    for i in normalization:
        print(i.strip().capitalize() + ". ", end='') # normalization text from letter cases point of view

def count_of_all_whitespaces(text_sample):
    count = 0
    for i in text_sample:
        if(i.isspace()):
            count+= 1
    print("\nThe number of whitespaces is: ", count)

last_words_in_sentence(text)
change_of_z(new_text)
final_text_normalization(text1)
count_of_all_whitespaces(text)