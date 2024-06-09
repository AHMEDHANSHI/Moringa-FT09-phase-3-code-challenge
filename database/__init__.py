import sqlite3
from database.__init__ import DATABASE_NAME
COON=sqlite3.connect(DATABASE_NAME)
CURSOR=COON.cursor()