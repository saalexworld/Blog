saalexworld@MacBoo ~ % cd desktop/makers/week12
saalexworld@MacBoo week12 % mkdir blog_api
saalexworld@MacBoo week12 % cd blog_api 
saalexworld@MacBoo blog_api % python3 -m venv venv
saalexworld@MacBoo blog_api % . venv/bin/activate
(venv) saalexworld@MacBoo blog_api % touch req.txt
(venv) saalexworld@MacBoo blog_api % nano req.txt 
django
djangorestframework
psycopg2-binary
pillow
(venv) saalexworld@MacBoo blog_api % pip3 install req.txt 
(venv) saalexworld@MacBoo blog_api % django-admin startproject blog_api .
(venv) saalexworld@MacBoo blog_api % code .



e: adminadmin@adminadmin.com
n: admin
p: admin