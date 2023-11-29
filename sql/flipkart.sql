show databases;

Create database flipkart;

use flipkart;

show tables;

select * from accounts_activation;

select * from auth_user;

delete from auth_user where id = 5; 

select * from vendor_vendor;

select * from vendor_address;

delete from vendor_address where id = 5;

select * from vendor_logo;

select * from category_category;

select * from vendor_country;

select * from vendor_state;

select * from vendor_city;

select * from vendor_city LIMIT 5000;

select * from vendor_city LIMIT 1001, 2000;

select * from vendor_city LIMIT 2001, 3000;

select * from vendor_city LIMIT 3001, 4000;

select * from vendor_city LIMIT 4001, 5000;

select * from vendor_state where country_id = 3;

select * from vendor_city where state_id = 112;

Drop database flipkart;


