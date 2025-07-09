from agents import Agent, Runner, function_tool
from main import config
from dotenv import load_dotenv
import os
import requests


load_dotenv()
api_key_ = os.getenv("WEATHER_API_KEY")  

@function_tool
def get_weather(city: str) -> str:
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={api_key_}&q={city}"
        )
        data = response.json()
        
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        
        return f"The current weather in {city} is {temp}°C with {condition}."

    except Exception as e:
        return f"Sorry, I couldn't fetch the weather. Error: {e}"

agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful assistant. Your task is to help the user with their queries.",
    tools=[get_weather]
)

result = Runner.run_sync(
    agent,
    input="What is the current weather in Hyderabad today?",
    run_config=config
)

print(result.final_output)
