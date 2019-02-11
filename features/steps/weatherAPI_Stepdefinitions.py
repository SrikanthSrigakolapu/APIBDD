from behave import *
import requests

@given('user creates a api get service')
def step_givenImpl(context):
    context.url='https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22'

@When('user submits the GET request')
def step_whenImpl(context):
    context.response=requests.get(context.url)


@Then('user validates the status code')
def step_whenImpl(context):
    print('the response code is  ')
    print(context.response.status_code)
    print("What are you seeing? You got your answer naa, just packup")