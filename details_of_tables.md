# store-management-system
#click on raw before viewing 
DATABASE NAME = project
NAMES OF SQL TABLES AND THEIR STRUCTURES 

inventory
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| prod_no   | int(5)      | NO   | PRI | NULL    |       |
| prod_name | varchar(30) | YES  |     | NULL    |       |
| quantity  | int(5)      | YES  |     | NULL    |       |
| price     | int(5)      | YES  |     | NULL    |       |
| category  | varchar(20) | YES  |     | NULL    |       |
| shelf     | varchar(5)  | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+

bills
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| bill_no | int(5)      | YES  | PRI | NULL    |       |
| date    | varchar(10) | YES  |     | NULL    |       |
| email   | varchar(30) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

bills_data
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| bill_no   | int(5)      | YES  | PRI | NULL    |       |
| prod_no   | int(5)      | YES  |     | NULL    |       |
| prod_name | varchar(20) | YES  |     | NULL    |       |
| price     | int(5)      | YES  |     | NULL    |       |
| quantity  | int(3)      | YES  |     | NULL    |       |
| amount    | int(5)      | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+

users 
+----------+------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| username | varchar(20) | YES  | PRI | NULL    |       |
| password | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
