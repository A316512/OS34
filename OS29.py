import random
import string

num_passwords = 10
password_length = 15

for i in range(num_passwords):
    # 大文字アルファベット、小文字アルファベット、数字、記号からなるすべての文字
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # パスワードを生成
    password = ''.join(random.choice(all_characters) for i in range(password_length))
    
    print("パスワード{}:".format(i+1), password)