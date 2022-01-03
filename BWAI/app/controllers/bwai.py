'''
Bwai Controller Module
'''
from flask import current_app
from modules.kcBERT_run_v2.run import inference


def bwai_judge(sentence):
    '''
    Bwai Judge
    -> 문장 내 욕설 판단 함수

    Params
    ---------
    mongo_cli > 몽고디비 커넥션
    sentence > 문장
    '''
    ai_result = inference(sentence)
    result = {'tokens': ai_result[3],
              'prob_per_token': [float(prob) for prob in ai_result[4]],
              'judge': False}

    for bad_word in current_app.config['BWAI_BAD_WORDS']:
        for idx, token in enumerate(result['tokens']):
            if bad_word in token:
                result['prob_per_token'][idx] = 1

    for bad_word in current_app.config['BWAI_BAD_WORDS']:
        if bad_word in sentence:
            result['judge'] = True
            return result

    if ai_result[1]:
        result['judge'] = True
        
    return result

def bwai_probability(sentence):
    '''
    Bwai probability
    -> 문장 내 욕설 확률 반환 함수

    Params
    ---------
    mongo_cli > 몽고디비 커넥션
    sentence > 문장
    '''
    ai_result = inference(sentence)
    result = {'tokens': ai_result[3],
              'prob_per_token': [float(prob) for prob in ai_result[4]]}

    for bad_word in current_app.config['BWAI_BAD_WORDS']:
        for idx, token in enumerate(result['tokens']):
            if bad_word in token:
                result['prob_per_token'][idx] = 1

    result['probability'] = {'normal': float(ai_result[0][0]),
                             'bad': float(ai_result[0][1])}        

    return result

def bwai_masking(sentence):
    '''
    Bwai masking
    -> 문장 내 욕설 마스킹 함수

    Params
    ---------
    mongo_cli > 몽고디비 커넥션
    sentence > 문장
    '''
    ai_result = inference(sentence)
    result = {'tokens': ai_result[3],
              'prob_per_token': [float(prob) for prob in ai_result[4]],
              'masking': ai_result[2]}

    for bad_word in current_app.config['BWAI_BAD_WORDS']:
        for idx, token in enumerate(result['tokens']):
            if bad_word in token:
                result['prob_per_token'][idx] = 1

    return result
