import requests
import smtplib

api_key = "****************************"

EMAIL = "****@******.com"
PASS = "***************"

# API_Website = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

# 5_day_forcast = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"

parameters = {
    "lat": 25.2048,
    "lon": 55.2708,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
# print(weather_data["list"][0]["weather"][0]["id"])

weather_conditions_12_hr = weather_data["list"]

condition_codes = [weather_data["list"][i]["weather"][0]["id"] for i in range(0, 4) if weather_data["list"][i]["weather"][0]["id"] >= 500]
print(condition_codes)

# for i in range(0, 4):
#     if weather_data["list"][i]["weather"][0]["id"] >= 500 or weather_data["list"][i]["weather"][0]["id"] <= 590:
#         print("Bring an Umbrella")

will_rain = False
for i in condition_codes:
    if 700 > i >= 500:
        will_rain = True
if will_rain is True:
    # print("Bring an Umbrella")
    with smtplib.SMTP("smtp.*******.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="*****@******.com",
            msg="Subject: Rain Alert!!\n\nIt's gonna rain today. Bring an umbrella."
        )