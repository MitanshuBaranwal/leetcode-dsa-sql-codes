/* Write your T-SQL query statement below */
select firstname,lastname,city,[state]from Person P left join Address A on 
A.personid = P.personid