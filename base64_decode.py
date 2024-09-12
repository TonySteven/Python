import base64

book_org = r"/Users/steven/PycharmProjects/Python/json/book/base64_org.txt"

book_decode = open(r"/Users/steven/PycharmProjects/Python/json/book/base64_decode.txt", 'a')

with open(book_org) as f:
    for line in f.readlines():
        book_decode.write(str(base64.b64decode(line), encoding='utf-8'))
