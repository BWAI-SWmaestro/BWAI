'''
Label Controller Module
'''
from bson import ObjectId
from tqdm import tqdm

def refact_v2_to_v3(db):
    old_posts = list(db['posts_labeled_v2'].find(
        {},
        {
            '_id': 0,
            'post': 1,
            'title': 1,
            'is_bad_word': 1,
            'title_is_bad_word': 1,
            'labeling': 1
        }
    ))

    for posts in tqdm(old_posts):
        #### TITLE Work ####
        new_posts = {}
        new_posts['string'] = posts['title']
        if posts['title_is_bad_word']:
            new_posts['label'] = 1
        else:
            new_posts['label'] = 0
        new_posts['labeling_confirm'] = posts['labeling']
        db['posts_labeled_v3'].insert_one(new_posts)

        #### POSTS Work ####
        for i in range(len(posts['post'])):
            new_posts = {}
            new_posts['string'] = posts['post'][i]
            if posts['is_bad_word'][i]:
                new_posts['label'] = 1
            else:
                new_posts['label'] = 0
            new_posts['labeling_confirm'] = posts['labeling']
            db['posts_labeled_v3'].insert_one(new_posts)

    return "success"

def v3_remove_overlap(db):
    '''
    Document 중복제거 함수.

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object

    Return
    ---------
    Status result > success
    '''
    posts = list(db['posts_labeled_v3'].find())
    overlap_check = set()
    for post in tqdm(posts):
        if post['string'] in overlap_check:
            db['posts_labeled_v3'].delete_one({'_id': post['_id']})
        else:
            overlap_check.add(post['string'])
    return "success"

def v3_insert_length(db):
    '''
    Document 길이 등록 함수

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object

    Return
    ---------
    Status result > success
    '''
    posts = list(db['posts_labeled_v3'].find())
    for post in tqdm(posts):
        length = len(post['string'])
        db['posts_labeled_v3'].update_one({'_id': post['_id']}, {'$set': {'length': length}})
    return "success"