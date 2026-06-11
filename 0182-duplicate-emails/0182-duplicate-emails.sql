# Write your MySQL query statement below
select distinct(email) from Person where email in (
    select email  as numbers from Person group by email having count(*) >  1 
)
