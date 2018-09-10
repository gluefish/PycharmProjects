from selenium import webdriver
from common import *

local = False;
if local:
    pg = "http://localhost/fkf/fkf.php"
else:
    pg = "http://www.gluefish.com/fkf/fkf.php"
pgid = "id01"
btnLogin1 = "btn_login"
btnLogin2 = "btn_login2"

def testlogin(thisun, thispw, thislevel):
    p("\nOpening the login page\n");
    d = webdriver.Chrome()          # d is the driver
    goto(pg, d)                     # Start up a browser session and navigate to the page
    v_id(pgid, d)                   # v is verify - that the page id is there
    cl_id(btnLogin1, d)             # cl - click on that page id
    p("Testing login\n");
    t_id("uname", thisun, d)        # t - type the id into the username space
    t_id("pword", thispw, d)        # t - type the pw into the passwore space
    cl_id(btnLogin2, d)             # cl - click on the login button
    v_id("welcome", d)              # v - verify that it made it to the welcome page
    cl_css('a[name="sitemap"]', d)  # cl - click on the sitemap button
    v_id("sitemap", d)              # verify that it made it to the sitemap page
    cl_css('a[name="logout"]', d)   # cl - click on the logout button
    v_id("fkf-php", d)              # v - verify that it made it back to the login page





