INSERT INTO total_moving_time (vehicle_id, total_moving_time)
SELECT vehicle_id,
SUM(total_moving) AS total_moving_time
FROM trip
GROUP BY vehicle_id;