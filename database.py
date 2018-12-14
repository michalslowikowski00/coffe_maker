import sqlite3

conn = sqlite3.connect("coffee.db")
c = conn.cursor()

# c.execute("""CREATE TABLE coffee (
#             coffee text,
#             value integer
#             )""")

# c.execute("INSERT INTO coffee VALUES ('espresso', 1000)")

c.execute("SELECT * FROM coffee WHERE coffee='espresso'")
print(c.fetchone())
conn.commit()
conn.close()
