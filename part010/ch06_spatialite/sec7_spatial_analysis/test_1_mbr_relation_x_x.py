# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file
################################################################################
import os,shutil,stat
import sqlite3 as sqlite
tmp_db = '/tmp/xx_new_db.sqlite'
if os.path.exists(tmp_db):
    os.remove(tmp_db)

shutil.copy("xx_china.db", tmp_db)
os.chmod(tmp_db, stat.S_IRUSR + stat.S_IWUSR)
conn = sqlite.connect(tmp_db)
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()
################################################################################
recs = cursor.execute("SELECT count (*) FROM gshhs;")
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT count(*) FROM gshhs WHERE MBRContains(
    GeomFromText('POLYGON((554000 4692000, 770000 4692000, 770000 4925000,
    554000 4925000, 554000 4692000))'), geom)'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT count(*) FROM gshhs WHERE MBRContains( BuildMBR(554000, 
    4692000, 770000, 4925000), geom);'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT count (*) FROM gshhs WHERE MBRContains(BuildMBR (654000,
    4692000, 770000, 4924000), geom);'''
cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT count (*) FROM gshhs WHERE MBRWithin( geom , BuildMBR (
    754000, 4692000, 770000, 4924000))'''
res = cursor.execute(sql)
for rec in cursor:
    print(rec)
################################################################################
sql = '''SELECT count (*) FROM HighWays WHERE MBRIntersects(BuildMBR(
    754000, 4692000, 770000, 4924000), geometry)'''
cursor.execute(sql)
for rec in cursor:
    print(rec)