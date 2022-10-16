# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

initial_text = "Пусть будет несколько слов, содержащих 'абв', например: абваоук, коцщао, рпабва, йгурак, щьаабвы, прауц."

text_to_list = initial_text.split(" ")
output_text = ""
for word in text_to_list:
    if "абв" not in word:
        output_text += word + " "
print(initial_text, "\n")
print(output_text)
