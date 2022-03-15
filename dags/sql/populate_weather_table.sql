-- creating temporary table
DROP TABLE IF EXISTS temp_table;
CREATE TABLE temp_table(
state_name VARCHAR NOT NULL PRIMARY KEY,
description VARCHAR NOT NULL,
temperature VARCHAR NOT NULL,
feels_like VARCHAR NOT NULL,
temp_min VARCHAR NOT NULL,
temp_max VARCHAR NOT NULL,
humidity VARCHAR NOT NULL,
clouds VARCHAR NOT NULL);

-- copying from csv file to temp_table
COPY temp_table 
FROM '/Users/user/docker_stuffs/airflow_assignment/dags/sql/current_weather_data.csv' 
DELIMITER ',' CSV HEADER;

-- inserting rows from temp_table to weather_table
INSERT INTO weather_table
SELECT * FROM temp_table 
ON CONFLICT(state_name) 
DO UPDATE SET 
description=EXCLUDED.description, 
temperature=EXCLUDED.temperature, 
feels_like=EXCLUDED.feels_like, 
temp_min=EXCLUDED.temp_min, 
temp_max=EXCLUDED.temp_max, 
humidity=EXCLUDED.humidity, 
clouds=EXCLUDED.clouds;

-- 'dags/sql/current_weather_data.csv'
-- (state_name, description, temperature, feels_like, temp_min, temp_max, humidity, clouds)
