import sqlite3

# 新しいデータベースファイルを作成する
conn = sqlite3.connect('pdf_gpt.db')
# カーソルを取得する
cur = conn.cursor()
cur.execute('''CREATE TABLE question_answer
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                title TEXT,
                question TEXT,
                openAI_key TEXT,
                answer TEXT)''')

    # 例: INSERT INTO ステートメントを実行する
url = 'https://example.com'
title_name = 'test'
question = 'What is the meaning of life?'
openAI_key = 'your-key'
answer = '42'

cur.execute("INSERT INTO question_answer(url, title, question, openAI_key, answer) VALUES(?, ?, ?, ?, ?)", (url, title_name, question, openAI_key, answer))

# 変更を保存し、接続を閉じる
conn.commit()
conn.close()