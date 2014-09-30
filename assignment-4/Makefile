#
# Makefile to automate some work with assigment 4
#
# Usage:
# make test     # runs all three progamms with the test_programs supplied by TAs
# make zip      # prepares a zip file of all your programs
# make download # download sample code and test files again
#
# your netid is used to create the zip file
#
NETID = jb007


test:
	python test_problem1.py 
	python test_problem2.py 
	python test_problem3.py 

zip:
	zip $(NETID)_assignment_4.zip problem4.py

download:
	wget -N --output-document=problem1-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem1.py
	wget http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem1.py
	wget -N --output-document=problem2-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem2.py
	wget http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem2.py
	wget -N --output-document=problem3-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem3.py
	wget http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem3.py
