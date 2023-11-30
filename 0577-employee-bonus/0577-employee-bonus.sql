# Write your MySQL query statement below

#  we can use left outer join - since we want to consider all those who dont have a bonus

select name,bonus from

(
    select t1.name ,t2.bonus from Employee t1 left outer join Bonus t2 

on t1.empId=t2.empId
) 

as subquerry where bonus<1000 or bonus is Null;
