
text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87 """

sentence = text.split('.') # split the text into sentences
list_of_sentence = []
j = 0
for i in sentence:
    list_sentence = sentence[j].split(" ") # each sentence we split into words
    print(list_sentence[len(list_sentence)-1]) # we print the last word of each sentence
    list_of_sentence.append(list_sentence[len(list_sentence)-1]) # a list of all last words of sentences
    j+= 1

sentence_string = " ".join(list_of_sentence) # the list of last words is converted into the sentence
print(sentence_string)
new_text = text + '. ' + sentence_string # we add the new sentence to the text

# the change of 'iZ' and 'iz' to 'is'
text0 = new_text.replace('z ', 's ')
text1 = text0.replace('Z ', 's ')

# the count of all whitespaces
count = 0
for i in text:
    if(i.isspace()):
        count+= 1
print("The number of whitespaces is: ", count)

normalization = text1.split('.')
for i in normalization:
    print(i.strip().capitalize() + ". ", end='') # normalization text from letter cases point of view