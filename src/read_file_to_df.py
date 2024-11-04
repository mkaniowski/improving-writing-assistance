import pandas as pd


def read_file_to_df(file_path):
    data = {'correct': [], 'incorrect': []}

    with open(file_path, 'r') as file:
        for line in file:
            correct, incorrects = line.strip().split(':')
            incorrect_words = incorrects.strip().split()
            for word in incorrect_words:
                data['correct'].append(correct.strip())
                data['incorrect'].append(word.strip())

    df = pd.DataFrame(data)
    return df