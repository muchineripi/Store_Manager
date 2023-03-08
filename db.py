import sqlite3

sql_create = '''
CREATE TABLE IF NOT EXISTS orders 
(id INTEGER PRIMARY KEY, 
item text, 
customer text, 
seller text, 
price text);
'''

sql_fetch = 'SELECT * FROM orders'

sql_insert = 'INSERT INTO orders VALUES (null, ?, ?, ?, ?)'

sql_remove = 'DELETE FROM orders WHERE id = ?'

sql_update = 'UPDATE orders SET item = ?, customer = ?, seller = ?, price = ? WHERE id = ?'

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(sql_create)
        self.conn.commit()

    def fetch(self):
        self.cur.execute(sql_fetch)
        return self.cur.fetchall()

    def insert(self, item, customer, seller, price):
        self.cur.execute(sql_insert, (item, customer, seller, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute(sql_remove, (id, ))

    def update(self, id, item, customer, seller, price):
        self.cur.execute(sql_update, (item, customer, seller, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')

# db.insert('laptop', 'John Doe', 'Apple', '999')
# db.insert('phone', 'Elias Mashayamombe', 'Samsung', '500')
# db.insert('mouse', 'Mary Chimuti', 'Gadgets', '20')
# db.insert('charger', 'Susan Carston', 'Huawei', '110')
# db.insert('monitor', 'Tim Duncan', 'Logitec', '399')
# db.insert('tablet', 'Robert Mugabe', 'Sony', '240')
# db.insert('hdmi', 'Micheal Jodarn', 'Hassana Electronics', '5')
