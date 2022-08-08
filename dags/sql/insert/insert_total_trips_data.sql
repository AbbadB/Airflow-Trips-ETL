INSERT INTO total_trips (vehicle_id, total_trips)
SELECT vehicle_id,
COUNT(id) AS total_trips
FROM trip
GROUP BY vehicle_id;