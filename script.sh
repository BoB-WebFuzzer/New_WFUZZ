#!/bin/bash
target = "http://192.168.57.1:8080"
python3 main.py -p "http://192.168.57.1:8080/bWAPP/xss_post.php" -a "firstname=$&lastname=$&form=submit" xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -p "http://192.168.57.1:8080/bWAPP/xss_login.php" -a login=$&password=$&form=submit xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -p "http://192.168.57.1:8080/bWAPP/xss_stored_1.php" -a entry=$&blog=submit&entry_add= xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt

python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_get.php?firstname=$&lastname=$&form=submit xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_json.php?title=$&action=search xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_ajax_2-2.php?title=$ xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_ajax_1-2.php?title=$ xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_eval.php?date=$ xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/xss_href-2.php?name=$&action=vote xss C:/Users/fhdj4/PycharmProjects/newFuzz/seed/xss/output.txt

python3 main.py -p "http://192.168.57.1:8080/bWAPP/sqli_1.php -a title=$&action=search sqli C:/Users/fhdj4/PycharmProjects/newFuzz/seed/sql/sql.txt
python3 main.py -p "http://192.168.57.1:8080/bWAPP/sqli_2.php -a movie=$&action=go sqli C:/Users/fhdj4/PycharmProjects/newFuzz/seed/sql/sql.txt

python3 main.py -g "http://192.168.57.1:8080/bWAPP/sqli_1.php?title=$&action=search sqli C:/Users/fhdj4/PycharmProjects/newFuzz/seed/sql/sql.txt
python3 main.py -g "http://192.168.57.1:8080/bWAPP/sqli_2.php?movie=$&action=go sqli C:/Users/fhdj4/PycharmProjects/newFuzz/seed/sql/sql.txt

python3 main.py -g http://192.168.57.1:8080/bWAPP/directory_traversal_1.php?page=$ dirt C:/Users/fhdj4/PycharmProjects/newFuzz/seed/dirtrav/my_dir_traversal.txt


