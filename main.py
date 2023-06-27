from twilio.rest import Client
import requests
import random


#using twilio account, this will send the message to the phone number given
def send_text_message(destination: str, message: str):
    account_sid = 'information goes here'
    auth_token = 'information goes here'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="sender phone number goes here",
        to=destination
    )

    print(message.sid)


def main():
    #grab json from the weather website
    api_key = "4592728656e072a40cb51bef8a0fa33b"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    #specify location
    city_name = "Wisconsin, Madison"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        #grab necessary information, location of information in the json is on their website
        current_temperature = x["main"]["temp"]

        # coordx = x["coord"]["lon"]
        # coordy = x["coord"]["lat"]
        # convert C to F
        text = (" Temperature = " +
                str((current_temperature - 273.15) * (9 / 5) + 32) + "F" +
                "\ncity = Madison")

        randomNumber = random.randint(0, 10)

        if randomNumber == 7:
            text += "\n" + "Today is a lucky day:)"

    else:
        print(" City Not Found ")

    #send message
    send_text_message("phone number goes here", text)


if __name__ == "__main__":
    main()
