# Principles of Urban Informatics
# Assignment 4
# tests (with py.test) for all three problems
#
# Usage:
#    py.test test_assignment_4.py   # if all the programs run correctly you won't see much output
#                                   # if one run of a program returns incorrect values the whole output of that run will be printed
#
# What you need to use this:
#    just the py.test library
#    http://pytest.org/latest/
#
# by brigitte.jellinek@nyu.edu
#


#
# tests like these are used in professional software development
# to make sure that the program as a whole does what it's supposed to do,
# and to make sure that single methods or classes to what they're supposed to do
#

from problem1 import solveOnlyLists, solveDict, solveSorted

#
# each test case is a method starting with test_
# in each test case you can use all of python to prepare
# data for the test.
# then you run the method you want to test, and
# write an ASSERTION about what the result of the method should be
#


#
# this tests the built-in function len,
# which doesnt' make much sense
# but shows off how to write a test case:
def test_len():
  list = [1,2,3,2,1]
  assert len(list) == 5

def test_solveOnlyLists():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )

def test_solveDict():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )

def test_solveSorted():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )


from problem2 import searchGreaterNotSorted, searchGreaterSorted, searchGreaterBinSearch, searchInRange

def test_searchGreaterNotSorted():
  assert 4 == searchGreaterNotSorted( [5,4,1,3,5], 2) 
  assert 0 == searchGreaterNotSorted( [2,4,2,0,-3,5], 5) 
  assert 1 == searchGreaterNotSorted( [1,0,2,-1,2,10], 2) 

def test_searchGreaterSorted():
  assert 4 == searchGreaterSorted( [1,2,3,4,5,5], 2) 
  assert 0 == searchGreaterSorted( [-3,0,2,4,5], 5) 
  assert 1 == searchGreaterSorted( [-1,0,1,2,2,10], 2) 

def test_searchGreaterBinSearch():
  assert 0 == searchGreaterBinSearch( [], 2) 
  assert 0 == searchGreaterBinSearch( [1,2], 2) 
  assert 1 == searchGreaterBinSearch( [1,2], 1) 
  assert 2 == searchGreaterBinSearch( [1,2], 0) 
  assert 0 == searchGreaterBinSearch( [1,2,3], 3) 
  assert 1 == searchGreaterBinSearch( [1,2,3], 2) 
  assert 2 == searchGreaterBinSearch( [1,2,3], 1) 
  assert 3 == searchGreaterBinSearch( [1,2,3], 0) 
  assert 3 == searchGreaterBinSearch( [1,3,4,5,5], 3) 
  assert 5 == searchGreaterBinSearch( [-3,0,2,2,4,5], -1)
  assert 4 == searchGreaterBinSearch( [1,2,3,4,5,5], 2) 
  assert 0 == searchGreaterBinSearch( [-3,0,2,4,5], 5) 
  assert 1 == searchGreaterBinSearch( [-1,0,1,2,2,10], 2) 

def test_searchInRange():
  # NO LONGER VALID! CHANGED WITH VERSION 2 of ASSIGNMENT
  # assert 0 == searchInRange( [1,3,4,5,5],         3,  3) 
  assert 0 == searchInRange( [1,3,4,5,5],         1,  2) 
  # NO LONGER VALID! CHANGED WITH VERSION 2 of ASSIGNMENT
  #assert 4 == searchInRange( [-3,0,2,2,4,5],     -1,  5) 
  assert 5 == searchInRange( [-3,0,2,2,4,5],     -1,  5) 
  assert 2 == searchInRange( [-1,0,1,1,2,10,10],  2, 11) 

  
from problem3 import buildNaive,queryNaive,buildOneDim,queryOneDim,buildTwoDim,queryTwoDim
  
#  def buildNaive(points,n):
#  def queryNaive(x0, y0, x1, y1):
def test_naive():
  buildNaive( [[0.5, 0.3], [0.1, 0.1]], 0 )
  assert 2 == queryNaive( 0,0,     1,1 )
  assert 1 == queryNaive( 0,0,     0.2,0.2 )
  assert 0 == queryNaive( 0,0,     0.04,0.03 )

#  def buildOneDim(points,n):
#  def queryOneDim(x0, y0, x1, y1):
def test_OneDim():
  buildOneDim( [[0.5,0.5]], 2 )
  assert 1 == queryOneDim( 0,0,     1,1 )
  assert 1 == queryOneDim( 0,0,     0.5,0.5 )
  assert 0 == queryOneDim( 0,0,     0.1,0.1 )
  assert 0 == queryOneDim( 0,0,     0,0 )
  buildOneDim( [[0.5, 0.3], [0.1, 0.1]], 2 )
  assert 2 == queryOneDim( 0,0,     1,1 )
  assert 1 == queryOneDim( 0,0,     0.2,0.2 )
  assert 0 == queryOneDim( 0,0,     0.05,1 )
  assert 0 == queryOneDim( 0,0,     1,0.05 )

#  def buildTwoDim(points,n):
#  def queryTwoDim(x0, y0, x1, y1):
def test_TwoDim():
  buildTwoDim( [[0.5,0.5]], 2 )
  assert 1 == queryTwoDim( 0,0,     1,1 )
  assert 1 == queryTwoDim( 0,0,     0.5,0.5 )
  assert 0 == queryTwoDim( 0,0,     0.1,0.1 )
  assert 0 == queryTwoDim( 0,0,     0,0 )
  buildTwoDim( [[0.5, 0.3], [0.1, 0.1]], 2 )
  assert 2 == queryTwoDim( 0,0,     1,1 )
  assert 1 == queryTwoDim( 0,0,     0.2,0.2 )
  assert 0 == queryTwoDim( 0,0,     0.05,1 )
  assert 0 == queryTwoDim( 0,0,     1,0.05 )
  buildTwoDim( [[0,0],[1,0],[0,1],[1,1],[0.5,0.5],[0.51,0.5],[0.5,0.51]], 2 )
  assert 7 == queryTwoDim( 0,0,     1,1 )
  assert 3 == queryTwoDim( 0.1,0.1, 0.9,0.9 )
  assert 0 == queryTwoDim( 0.2,0,   0.4,1   )
  assert 0 == queryTwoDim( 0,0.2,   1,0.4   )

def test_random_651695():
  # generated with peters script
  points = [(0.19654727954016182, 0.6929758513093242), (0.031433735846355004, 0.5842957116406512), (0.3336821682894283, 0.24918868129420613), (0.5619901380658144, 0.0379087813736837), (0.97194849055367, 0.60126992070537), (0.3232795682583486, 0.011900758627663044), (0.7076043029436758, 0.654338871664529), (0.1899116176046418, 0.9557259603196117), (0.18527300134631186, 0.41016662133046167), (0.3660598991339056, 0.7418072400587598), (0.7928570794161018, 0.8567445680315682), (0.6243223965848989, 0.9145094355212648), (0.05753191266149904, 0.1558424699567793), (0.5089639183032092, 0.5906598223447258), (0.9332266654965963, 0.24518847411897438), (0.760072399524236, 0.7956082018529484), (0.7414152726458605, 0.1258607094042974), (0.16174293221988534, 0.025348311629374343), (0.4308154015287061, 0.2962084706607203), (0.15815798923507596, 0.7981361964165704), (0.9615698846027019, 0.4497865106867508), (0.01942293457508293, 0.31833396068386677), (0.11176376744631467, 0.48234483786973703), (0.8516961816711355, 0.840525469901666), (0.6445766991356664, 0.017476975635071224), (0.15420063786648952, 0.6772766771724038), (0.9801296851130873, 0.2420115400103986), (0.8914755481758567, 0.5460144143818731), (0.36613749223186276, 0.13589317493855035), (0.6041274405385023, 0.6977487739555166), (0.7716523797417036, 0.26897348079983796), (0.9997797354506368, 0.85853814371356), (0.161604066522533, 0.8013127535856345), (0.2822953368734096, 0.38195035722144066), (0.43014277737383977, 0.3230124545383338), (0.94059574105891, 0.023602463703519483), (0.9176124932028887, 0.6553489291398422), (0.3629877432075812, 0.5135203444160555), (0.20785557615021721, 0.35894285609841015), (0.8066575177401687, 0.757729411363143)]
  buildNaive( points, 20 )
  assert 1 == queryNaive( 0.096562,0.626627, 0.190642,0.785395 )
  buildOneDim( points, 20 )
  assert 1 == queryOneDim( 0.096562,0.626627, 0.190642,0.785395 )
  buildTwoDim( points, 20 )
  assert 1 == queryTwoDim( 0.096562,0.626627, 0.190642,0.785395 )
