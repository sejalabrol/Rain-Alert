# Rain Alert
A python code that sends an alert in the form of a text message to the user's mobile number when it's going to rain within the next 12 hours in the user's mentioned location.

## Screenshots
<img src="https://user-images.githubusercontent.com/87208681/126847108-83a0591d-0a7a-4657-9ecf-e321c242b55e.jpeg" width="400">

## Tools
 - [Twilio](https://www.twilio.com/)
 - [OpenWeather](https://openweathermap.org/)
 - [LatLong.net](https://www.latlong.net/)
 - [PythonAnywhere](https://www.pythonanywhere.com/) (for deployment)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`OWP_API_KEY` `TWILIO_ACCOUNT_SID` `TWILIO_AUTH_TOKEN` `SENDERS_NUMBER` `RECEIVERS_NUMBER` `LATITUDE` `LONGITUDE`

Refer to the [env template](https://github.com/sejalabrol/rain-alert/blob/main/.env.template)

## Run Locally
Clone the project
```bash
  git clone https://github.com/sejalabrol/rain-alert
```
Go to the project directory
```bash
  cd rain-alert
```
Create a .env file and enter environment variables
```bash
  cp .env.template .env
```
[Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) (optional but recommended) 
```bash
  python -m venv venv
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Run the project
```bash
  python main.py
```
## Deployment
This project is deployed on [PythonAnywhere](https://www.pythonanywhere.com/)
