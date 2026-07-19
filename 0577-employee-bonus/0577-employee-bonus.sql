
with query as  (
select emp.name  , t.bonus  from Employee as emp
left join Bonus as t on t.empId = emp.empId
) 

select name , bonus from query
where bonus is null or bonus < 1000