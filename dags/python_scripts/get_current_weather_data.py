def get_current_weather_data():

    import requests, json
    import logging
    import pandas as pd
    from airflow.exceptions import AirflowException
    from python_scripts.credentials_rapidapi_key import get_rapidapi_key
    

    query_states = ["Assam", "Chandigarh", "Delhi", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Maharashtra", "Punjab", "Sikkim", "West Bengal"]

    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': get_rapidapi_key()
        }

    df = pd.DataFrame()
    for state in query_states:
        
        response = requests.request("GET", url, headers=headers, params={"q":state})
        try:
            if response.status_code == 200:
                dict_info = json.loads(response.text)
                # We need State, Description, Temperature, Feels Like Temperature, 
                # Min Temperature, Max Temperature, Humidity, Clouds.
                state_name = dict_info["name"]
                description = dict_info["weather"][0]["description"]
                temperature = dict_info["main"]["temp"]
                feels_like = dict_info["main"]["feels_like"]
                temp_min = dict_info["main"]["temp_min"]
                temp_max = dict_info["main"]["temp_max"]
                humidity = dict_info["main"]["humidity"]
                clouds = dict_info["clouds"]["all"]

                row = pd.DataFrame([[state_name, description, temperature, feels_like,
                temp_min, temp_max, humidity, clouds]])
                df = pd.concat([df, row])

            else:
                raise Exception
        except:
            print(2)
            logging.error(f"Request for {state} unsuccessful with status code: {response.status_code}")    
            logging.info(f"JSON Response:\n{response.text}")
            raise AirflowException
    
    df.columns=["state_name", "description", "temperature",
    "feels_like", "temp_min", "temp_max", "humidity", "clouds"]
    df.to_csv("dags/sql/current_weather_data.csv", index=False)

if __name__=="__main__":
    get_current_weather_data()
