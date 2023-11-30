# Write your MySQL query statement below
#  it can be solved using self join and we can move a column down by using the -1


select t1.id from 

Weather t1,Weather t2

where datediff(t1.recordDate,t2.recordDate)=1 and t1.temperature>t2.temperature;
