# Exploring the Web with requests package
import requests

url = 'https://www.udemy.com/course/ai-hero-a-12-month-journey-taking-you-from-zero-to-expert/learn/lecture/52116181#overview'

response = requests.get(url)

print(response.text)
print(response.content)