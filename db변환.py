import pandas as pd
import sqlite3
#음식정보 ( 요리이름,요리종류,재료,양념,국가,칼로리)
# CSV 읽기
df = pd.read_csv('cook_ingredient.csv')
# DB 연결
conn = sqlite3.connect('cook.db')
# to_sql 사용 (이미 있으면 덮어쓰기)
df.to_sql('cook_ingredient', conn, if_exists='replace', index=False)
conn.close()
# 레시피 (음식이름,레시피,인분,난이도,요리종류)
df = pd.read_csv('cook_recipe.csv')
conn = sqlite3.connect('cook.db')
df.to_sql('cook_recipe', conn, if_exists='replace', index=False)
conn.close()