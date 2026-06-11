DELETE FROM Person 
WHERE id IN (
    SELECT id FROM (
        SELECT p.id 
        FROM Person as p 
        INNER JOIN Person as q 
        ON p.email = q.email AND p.id > q.id
    ) as temp
);
