from logintest import testlogin
from common import *
import csv

unx = "bad@bad.bad"
pwx = "badpw"
un0 = "FKFTest0@gluefish.com"
pw0 = "Level0"
un1 = "FKFTest1@gluefish.com"
pw1 = "Level1"
un2 = "FKFTest2@gluefish.com"
pw2 = "Level2"
un3 = "FKFTest3@gluefish.com"
pw3 = "Level3"
un4 = "FKFTest4@gluefish.com"
pw4 = "Level4"
un5 = "FKFTest5@gluefish.com"
pw5 = "Level5"

p("\nTesting Login with Bad Username")
testlogin(unx, pwx, "xx")

p("\nTesting Login with Bad Password")
testlogin(un1, pwx, "1x")

p("\nTesting Login with Good Username, Password and Level 0 Access")
testlogin(un0, pw0, "0")

p("\nTesting Login with Good Username, Password and level 1 access")
testlogin(un1, pw1, "1")

p("\nTesting Login with Good Username, Password and Level 2 Access")
testlogin(un2, pw2, "2")

p("\nTesting Login with Good Username, Password and level 3 access")
testlogin(un3, pw3, "3")

p("\nTesting Login with Good Username, Password and Level 4 Access")
testlogin(un4, pw4, "4")

"""""
See https://docs.python.org/2/library/csv.html#
Also see https://realpython.com/python-csv/ for nicely formatted output
  using panda
  
Open a local parameters csv file for reading

Open the result csv file for writing

For each column in the paremeters,

  for each row in the column,

    execute the parameter

    capture the result to the result csv file

  Write overall result to the result csv file

Close both files

"""""





