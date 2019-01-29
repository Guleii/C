import sqlite3

class DBManager:

    def db_select_all(self, db_name='', tb_name=''):

        # 建立数据库连接
        conn = sqlite3.connect(db_name)
        # 锚定位
        cursor = conn.cursor()
        # 执行查询语句
        cursor.execute('''
                SELECT * FROM 
        ''')
        # 打印信息
        cursor.fetchall()
        # 关闭cursor
        cursor.rowcount()
        cursor.close()
        # 关闭连接
        conn.close()


def db_create_tb(self, tb_name=''):


if __name__ == '__main__':
    db_select('test.db')
