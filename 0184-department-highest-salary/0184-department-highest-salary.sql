



WITH RankedSalary AS (
    SELECT 
        e.name AS Employee, 
        d.name AS Department,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee AS e
    INNER JOIN Department AS d 
        ON e.departmentId = d.id
)
select Department ,Employee , Salary  from RankedSalary
where salary_rank =1