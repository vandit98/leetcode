# Write your MySQL query statement below

# first we extract those visits that are not in transactions- then just create a column customer_id and their no of visits

# we can use inner join
 select Distinct  customer_id,
COUNT(*) OVER (PARTITION BY customer_id) AS count_no_trans
    from     (select t1.visit_id,t1.customer_id,t2.transaction_id from

Visits t1 left outer join Transactions t2

on t1.visit_id=t2.visit_id   


where t2.transaction_id is Null) as subquery


order by count_no_trans DESC;

