INSERT INTO total_distance (vehicle_id, total_distance)
SELECT vehicle_id,
SUM(total_distance) AS total_distance
FROM trip
GROUP BY vehicle_id;