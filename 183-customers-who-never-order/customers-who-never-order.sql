/* Write your T-SQL query statement below */
select name as customers from customers c where c.id not in 
(select customerid from Orders)