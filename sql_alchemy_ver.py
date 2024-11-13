from sqlalchemy import create_engine, MetaData, Table, select, text
from sqlalchemy.orm import sessionmaker
from memory_profiler import profile

# PostgreSQL接続情報を設定
DATABASE_URI = 'postgresql://user:password@localhost:5432/usda'
# データベース接続設定
engine = create_engine(DATABASE_URI, echo=True)

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()


# サーバーサイドカーソルを使ったデータ取得
@profile()
def fetch_data_with_server_side_cursor():

    # psycopg2でサーバーサイドカーソルを使うには、stream_results=Trueにする
    with session.connection().execution_options(stream_results=True) as connection:
        cursor = connection.execution_options(yield_per=10000)  # 一度に取得する行数

        # サーバーサイドカーソルを使ってクエリ実行
        result = cursor.execute(text("SELECT * FROM public.nut_data"))

        for row in result:
            pass
#            print(row)  # データを1行ずつ処理
            # 必要に応じてここでデータ処理を行う

    session.close()

# 関数を実行
fetch_data_with_server_side_cursor()
