INSERT INTO total_idle_time (vehicle_id, total_idle_time)
SELECT vehicle_id,
SUM(total_idle) AS total_idle_time
FROM trip
GROUP BY vehicle_id;