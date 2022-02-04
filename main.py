import intro
import json
import os


def get_most_common_words():
    words_count = dict()  # Словарь для подсчета слов
    ignore_list = [  # Слова для игнорирования
        "я", "а", "ты", "ну", "что", "в", "и", "не", "меня", "у", "на", "это", "то", 
        "как", "так", "с", "тебя", "мне", "да", "она", "когда", "если", "тебе", "все", 
        "по", "уже", "бы", "но", "он", ",", "тоже", "тип", "за", "просто", "будет", 
        "же", "ща", "че", "там"
    ]
    for message in messages["messages"]:
        if isinstance(message["text"], list):  # Если это не простой текст, то игнорим
            continue
        text = message["text"]
        words = text.split()

        for word in words:
            word = word.capitalize()
            if word.lower() in ignore_list:  # Если слово в игнорируемых словах,
                continue  # то пропускаем
            if word not in words_count.keys():
                words_count[word] = 0
            words_count[word] += 1
    
    # Отсортируем по убыванию
    sorted_keys = sorted(words_count.keys(), key=lambda x: words_count[x], reverse=True)

    top10 = [(key, words_count[key]) for key in sorted_keys[:10]]
    result = ""
    for i, item in enumerate(top10):
        result += f"  {i + 1}) «{item[0]}»: {item[1]}\n"
    
    return result


def get_most_active_days():
    messages_count = dict()
    for message in messages["messages"]:
        date = message["date"][:10]
        if date not in messages_count.keys():
            messages_count[date] = 0
        messages_count[date] += 1
    
    sorted_keys = sorted(messages_count.keys(), key=lambda x: messages_count[x], reverse=True)

    top10 = [(key, messages_count[key]) for key in sorted_keys[:10]]
    result = ""
    for i, item in enumerate(top10):
        result += f"  {i + 1}) «{item[0]}»: {item[1]}\n"
    
    return result


def get_average_messages_per_day():
    messages_count = dict()
    for message in messages["messages"]:
        date = message["date"][:10]
        if date not in messages_count.keys():
            messages_count[date] = 0
        messages_count[date] += 1
    
    just_nums = list(messages_count.values())
    average = sum(just_nums) / len(just_nums)

    return f"  Average number of messages per day: {int(average)}"


def get_most_active_interlocutor():
    messages_count = dict()
    for message in messages["messages"]:
        if message["type"] == "message":
            user_id = message["from_id"]
            user_name = message["from"]

            if (user_id, user_name) not in messages_count.keys():
                messages_count[(user_id, user_name)] = 0
            messages_count[(user_id, user_name)] += 1
    
    result = ""
    summa = sum(list(messages_count.values()))
    for key in messages_count.keys():
        result += f"  {key[1]}: {messages_count[key]} messages ({round(messages_count[key] / summa * 100, 2)}%)\n"
    
    return result


def get_time_to_read():
    TIME_FOR_READ_WORD = 0.43675
    time_sum = 0
    for message in messages["messages"]:
        if not isinstance(message["text"], list):
            words = message["text"].split()
            time_sum += len(words) * TIME_FOR_READ_WORD
        if message.get("media_type") in ["voice_message", "video_file", "video_message"]:
            time_sum += message.get("duration_seconds", 0.5)
    
    return f"  To read the entire correspondence, you will need +- {round(time_sum)} seconds." \
           + f"\n  This is {round(time_sum / 60)} minutes or {round(time_sum / 60 / 60, 1)} hours" \
           + f" or {round(time_sum / 60 / 60 / 24, 2)} days ;)" \
           + "\n  !!This is not an exact value!!"


if __name__ == '__main__':
    intro.print_name()
    intro.print_info()

    # Получение файла
    while True:
        path = input("Enter the absolute path to the saved chat history json-file: ")
        if os.path.exists(path):
            break
        print("The file could not be found, please try again")

    with open(path, encoding="utf8") as file:
        messages = json.load(file)

    intro.print_commands()
    # Получение команды
    while True:
        command = input("Enter the number of the required command: ")
        if command in "12345":
            break
        print("There is no such command!")
    
    if command == "1":
        print(get_most_common_words())
    elif command == "2":
        print(get_most_active_days())
    elif command == "3":
        print(get_average_messages_per_day())
    elif command == "4":
        print(get_most_active_interlocutor())
    elif command == "5":
        print(get_time_to_read())
