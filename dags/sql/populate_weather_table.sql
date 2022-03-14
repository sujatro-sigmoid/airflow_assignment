COPY weather_table 
FROM 'dags/sql/current_weather_data.csv' 
DELIMITER ',' CSV HEADER;