WITH query1 AS ( 
    SELECT count(*) AS totalRequestByUnbannedUsers, request_at 
    FROM trips 
    WHERE client_id NOT IN ( 
          SELECT users_id FROM Users WHERE banned = 'Yes' 
        ) 
      and driver_id  NOT IN ( 
          SELECT users_id FROM Users WHERE banned = 'Yes' 
        )  
      and request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY request_at 
    having (count(*)>0)
), 
query2 AS ( 
    SELECT count(*) AS totalRequestCancelledByUnbannedUsers, request_at 
    FROM trips 
    WHERE (status = 'cancelled_by_driver' or status = 'cancelled_by_client')  
    and  client_id NOT IN ( 
          SELECT users_id FROM Users WHERE banned = 'Yes' 
        ) 
    and driver_id  NOT IN ( 
          SELECT users_id FROM Users WHERE banned = 'Yes' 
        )  
    and request_at BETWEEN '2013-10-01' AND '2013-10-03'
    

    GROUP BY request_at 
)
SELECT q1.request_at as Day ,  
        ROUND(IFNULL(q2.totalRequestCancelledByUnbannedUsers, 0) / q1.totalRequestByUnbannedUsers, 2) AS `Cancellation Rate`
FROM query1 AS q1
LEFT JOIN query2 AS q2 
    ON q1.request_at = q2.request_at
ORDER BY Day;