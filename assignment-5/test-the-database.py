#!/usr/bin/python
#
# Test Script to find out
#    if your database and MySQLdb in python is working
#
# Usage:
#   python test-the-database.py
# 
#   BUT! you might have to fill in your password in line 23 first!
#
# see also http://blog.brigitte-jellinek.at/2014/10/setting-up-python-mysql-on-mac/
#
#
#

import MySQLdb
import sys

                     
connection = MySQLdb.connect(
  'localhost',  # the host the database server is running on.
  'root',       # the database user you use to connect to the database server
  '',           # the passwort for that database user
  'test'        # the name of the database.  test is always there
);

cursor = connection.cursor()
cursor.execute("SELECT VERSION()")

version = cursor.fetchone()
  
print "Database version : %s " % version
