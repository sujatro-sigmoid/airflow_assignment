-- creating weather table
CREATE TABLE IF NOT EXISTS weather_table(
state_name VARCHAR NOT NULL PRIMARY KEY UNIQUE,
description VARCHAR NOT NULL,
temperature VARCHAR NOT NULL,
feels_like VARCHAR NOT NULL,
temp_min VARCHAR NOT NULL,
temp_max VARCHAR NOT NULL,
humidity VARCHAR NOT NULL,
clouds VARCHAR NOT NULL);
