COPY 
(SELECT vehicle_id,
COUNT(trip) AS total_trips,
SUM(total_distance) AS total_distance,
SUM(total_moving) AS total_moving_time,
SUM(total_idle) AS total_idle_time
FROM trip
GROUP BY vehicle_id)
TO '/tmp/report.csv'
DELIMITER ';' CSV HEADER