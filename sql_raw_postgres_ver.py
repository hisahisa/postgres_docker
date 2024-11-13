import psycopg2
from memory_profiler import profile

# PostgreSQL接続情報
DATABASE_URI = "dbname=usda user=user password=password host=localhost port=5432"

# サーバーサイドカーソルを使ったデータ取得
@profile()
def fetch_data_with_server_side_cursor():
    # psycopg2のコネクションを作成
    conn = psycopg2.connect(DATABASE_URI)

    # サーバーサイドカーソルを宣言（ここでカーソル名を指定）
    with conn.cursor(name="my_server_side_cursor") as cursor:
        # クエリを実行
        cursor.execute("SELECT * FROM public.nut_data")

        # 1000行ずつフェッチして処理
        while True:
            rows = cursor.fetchmany(10000)
            if not rows:
                break
            for row in rows:
                pass  # 必要に応じてデータを処理
                # print(row)

    conn.close()


# 関数を実行
fetch_data_with_server_side_cursor()
