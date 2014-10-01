#
# Makefile to automate some work with assigment 4
#
# Usage:
#   make benchmark  # runs all your progamms with the test_* script provided, LONG RUNNING TIME!
#   make test       # runs all against simple tests, FAST
#   make zip        # prepares a zip file of all your programs
#   make download   # download test-scripts + sample scripts again
#
# What you need to use this makefile:
#   command line, e.g. Mac OX X Terminal
#   make
#   zip
#   wget
#   python library "py.test" to run the test
# -------------------------
# your netid is used to create the zip file
NETID = jb007


benchmark:
	python test_problem1.py 
	python test_problem2.py 
	python test_problem3.py 

test:
	py.test test_assignment_4.py

zip:
	zip $(NETID)_assignment_4.zip problem1.py problem2.py problem3.py

download:
	wget -N --output-document=problem1-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem1.py
	wget -N http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem1.py
	wget -N --output-document=problem2-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem2.py
	wget -N http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem2.py
	wget -N --output-document=problem3-sample.py http://vgc.poly.edu/files/gx5003-fall2014/week4/src/problem3.py
	wget -N http://vgc.poly.edu/files//gx5003-fall2014/week4/src/test_problem3.py
