import intro
import json


with open("result.json", encoding="utf8") as file:
    messages = json.load(file)


def get_most_common_words():
    words_count = dict()  # Словарь для подсчета слов
    for message in messages["messages"]:
        if isinstance(message["text"], list):  # Если это не простой текст, то игнорим
            continue
        text = message["text"]
        words = text.split()

        for word in words:
            if word not in words_count.keys():
                words_count[word] = 0
            words_count[word] += 1
    
    # Отсортируем по убыванию
    sorted_keys = sorted(words_count.keys(), key=lambda x: words_count[x], reverse=True)

    top10 = [(key, words_count[key]) for key in sorted_keys[:10]]
    result = ""
    for i, item in enumerate(top10):
        result += f"{i + 1}) «{item[0]}»: {item[1]}\n"
    
    return result


if __name__ == '__main__':
    intro.print_name()
    intro.print_info()
    intro.print_commands()

    while True:
        command = input("Enter the number of the required command: ")
        if command in "1234":
            break
        print("There is no such command!")
    
    if command == "1":
        print(get_most_common_words())