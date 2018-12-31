import sqlite3


conn = sqlite3.connect("coffee_ingr.db")
c = conn.cursor()

c.execute(""" CREATE TABLE coffee_ingredients (
             coffee text,


        ) """)