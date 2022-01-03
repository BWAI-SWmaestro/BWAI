import numpy as np
from tqdm import tqdm
from modules.kcBERT_run_v2.run import inference

def make_bad_word_set():
    bad_words = list(np.loadtxt("./modules/filter_based_on_match_string/src/bad_word_list/bad_word.csv", delimiter=',', dtype=np.unicode, encoding='utf-8'))

    result = []
    for word in tqdm(bad_words):
        ai_result = inference(word)
        if not ai_result[1]:
            result.append(word)
            print(result)

if __name__ == "__main__":
    make_bad_word_set()
