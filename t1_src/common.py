from selenium import webdriver
from datetime import date
import csv
import sys



#######################  csv utils ########################


def getRow(filename,rowname):
    row = -1
    f=open(filename,'rU')
    rdr = csv.reader(f)
    data = list(rdr)
    f.close()
    rows = len(data)
    for x in data:
        row = row + 1
        if data[row][0] == rowname:
            return row
    return -1


def getCol(filename,colname):
    col = -1
    f=open(filename,'rU')
    rdr = csv.reader(f)
    data = list(rdr)
    f.close()
    for x in data[0]:
        col = col + 1
        if x == colname:
            return col
    return -1


def getRC(filename,row,col):
    f=open(filename,'rU')
    rdr = csv.reader(f)
    data = list(rdr)
    f.close()
    rc = data[row][col]
    return rc


def getRows(filename):
    with open(filename, 'rU') as f:
        reader=csv.reader(f)
        next(reader, None) #skip headers
        rc = sum(1 for row in reader)
        return rc

#######################    python utils  ########################


def l_fn():
    return date.today() + ".log"


def p(string):
    sys.stdout.write(string)


def doCmd(obj,descr, cmd):
    p(descr)
    exec(cmd)
    

#######################  webdriver utils ########################
   

def cl_css(txtsel, obj):
    p("CLICK ON CSS  " + txtsel + ": ")
    try:
        obj.find_element_by_css_selector(txtsel).click()
        p("\tPASS\n")
    except:
        p("\tFAIL\n")


def goto(txtpg, obj):
    p("NAV TO        " + txtpg + ":")
    try:
        obj.get(txtpg)
        p("\tPASS\n")
    except:
        p("\tFAIL\n")


def v_id(txtid, obj):
    p("VERIFY ID     " + txtid + ": ")
    try:
        obj.find_element_by_id(txtid)
        p("\t\t\t\tPASS\n")
    except:
        p("\t\t\t\tFAIL\n")


def cl_id(txtid, obj):
    p("CLICK ON ID   " + txtid + ": ")
    try:
        obj.find_element_by_id(txtid).click()
        p("\t\t\tPASS\n")
    except:
        p("\t\t\tFAIL\n")


def t_id(txtid,txt,obj):
    p("TYPE          " + txt + ", " + txtid + ": ")
    try:
        obj.find_element_by_id(txtid).send_keys(txt)
        p("\t\tPASS\n")
    except:
        p("\t\tFAIL\n")


def setBrowser(string):
    if string == 'Firefox':
        x = webdriver.Firefox()
        return x
    if string == 'Chrome':
        x = webdriver.Chrome()
        return x  


def testIfInTitle(string, obj, cell):
    if (string in obj.title):
        #print "YES"
        Range(cell).value = [['PASS']]
    else:
        #print "NO"    
        Range(cell).value = [['FAIL']]


def testClickLink(string, obj):
    try:
        obj.find_element_by_partial_link_text(string).click()
        Range(cell).value = [['PASS']]
    except:
        Range(cell).value = [['FAIL']]  


