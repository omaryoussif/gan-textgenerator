with open('data/qa_Video_Games.json', 'r') as file:
    data = file.readlines()

with open('clean/qa_Video_Games.txt', 'w') as txt_file:
    for line in data:
        obj = eval(line.strip())
        if 'question' in obj and 'answer' in obj:
            txt_file.write(obj['question'] + '\n')
            txt_file.write(obj['answer'] + '\n\n')