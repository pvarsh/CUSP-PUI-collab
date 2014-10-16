#
# Makefile to automate some work with assigment 6
#
# Usage:
#   make grade      # grades each problem
#   make zip        # prepares a zip file of all your programs
#   make download   # download all relevant files and unpacks into working directory
#   make install    # installs MySQL-python via pip
#
# What you need to use this makefile:
#   command line, e.g. Mac OX X Terminal
#   make
#   zip
#   wget
#   pip
#
# Ideas/ToDo:
#   Automate setup of database in mysql
# -------------------------
# your netid is used to create the zip file
NETID = your_netid


grade:
	python grade_assignment.py 

zip:
	zip $(NETID)_assignment_6.zip query1.sql query2.sql query3.sql query4.sql query5.sql query6.sql

download:
	wget -N http://vgc.poly.edu/projects/gx5003-fall2014/week6/lab/data/mta.sql
	wget -N http://vgc.poly.edu/projects/gx5003-fall2014/week6/lab/data/assignment6.zip
	unzip assignment6.zip
	rm assignment6.zip
	mv assignment6_files/grade_assignment.py .

import:
	mysql -u user_assignment6 assignment6 < dump.sql
	mysql -u user_assignment6 assignment6 < mta.sql
