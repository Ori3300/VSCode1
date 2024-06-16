import sys

try:
    with open('text.txt', 'w') as file:
        file.write("hello bye hello hello Hello Hi 2 2 2")


    with open('text.txt', 'r') as file:
        text = file.read()

    print(text)

    words_list = text.split(" ")

    words_count_dict = {}

    for word in words_list:     
        if word not in words_count_dict:
            words_count_dict[word] = 1
        else:
            words_count_dict[word] += 1

    words_count_list_sorted = sorted(words_count_dict.items(), key= lambda item: item[1], reverse=True)

    n = int(sys.argv[1])

    for i in range(n):
        print(words_count_list_sorted[i])
except:
    print("Error")



