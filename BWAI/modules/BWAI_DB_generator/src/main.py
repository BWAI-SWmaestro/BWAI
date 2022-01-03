from pprint import pprint
from pymongo import MongoClient
from module.BWAI_DB_generator.src.controller.posts_con import (v3_remove_overlap,
                                  refact_v2_to_v3,
                                  v3_insert_length)
from secret_info import (
                         MONGO_HOST,
                         MONGO_ID,
                         MONGO_PW,
                         MONGO_DB_NAME)

if __name__ == "__main__":
    mongo_cur = MongoClient(
        'mongodb://%s:%s@%s' % (MONGO_ID,
                                MONGO_PW,
                                MONGO_HOST))

    print("1. refact_v2_to_v3")
    print("2. v3_remove_overlap")
    print("3. v3_insert_length")
    cmd = int(input("select: "))

    result = None

    if cmd == 1:
        result = refact_v2_to_v3(mongo_cur[MONGO_DB_NAME])
    elif cmd == 2:
        result = v3_remove_overlap(mongo_cur[MONGO_DB_NAME])
    elif cmd == 3:
        result = v3_insert_length(mongo_cur[MONGO_DB_NAME])

    print(result)
