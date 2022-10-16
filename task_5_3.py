# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('text.txt', 'r') as source:
    list_source = str(source.readline()).split(" ")
print(list_source)
output = []

# алгоритм для кодирования сообщения
for word in list_source:
    count = 0
    iteration = 0
    for char in word:
        if char == word[count]:
            iteration += 1
        else:
            output.append(f'{iteration}{word[count]}')
            count += iteration
            iteration = 1
    output.append(f'{iteration}{word[count]} ')
             
with open('output_1.txt', 'w') as target:
    target.write("".join(output))
print("".join(output))
         
with open('output_1.txt', 'r') as coded_source:
    list_coded = str(coded_source.readline()).split(" ")

# алгоритм для декодирования сообщения
digit = ''
decoded_message = []
for w in list_coded:
    count = 0
    
    for char in w:
        if char.isdigit():
            digit += char
        else:
            letter = str(char)
            decoded_message.append(letter*int(digit))
            count += 1
            digit = ''
    decoded_message.append(" ")

with open('output.txt', "w") as decoded:
    decoded.write("".join(decoded_message))
print("".join(decoded_message))
