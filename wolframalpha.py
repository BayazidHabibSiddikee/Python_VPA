import requests

apikey = "4EQ3U6QQ49"
inp = input("What do you want to know from WolframAlpha?\n>>> ")

url = f"http://api.wolframalpha.com/v1/result?appid={apikey}&i={requests.utils.quote(inp)}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Answer:", response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except:
    try:
        import wikipedia
        ans = wikipedia.summary(inp, sentencces = 5)
        print(ans)
    except:
        print("I'm  still learning. I don't know your answer yet")
    