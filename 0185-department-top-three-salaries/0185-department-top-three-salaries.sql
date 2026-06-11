# Write your MySQL query statement below
with rankedSalary as (
    select e.name as Employee , d.name as Department  , e.salary as salary ,   DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    from Employee as e 
    inner join Department as d
    on e.departmentId  = d.id
)
select Department , Employee , Salary   from rankedSalary
where salary_rank >=1 and salary_rank  <=3 