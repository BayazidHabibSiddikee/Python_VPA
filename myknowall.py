from mptpkg import print_say
def know_all():
    import requests
    apikey = "4EQ3U6QQ49"
    inp = input("What do you want to know?\n>>> ")
    url = f"http://api.wolframalpha.com/v1/result?appid={apikey}&i={requests.utils.quote(inp)}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print_say("Answer:", response.text)
        else:
            print_say(f"Error: {response.status_code} - {response.text}")
    except:
        try:
            import wikipedia
            ans = wikipedia.summary(inp, sentencces = 5)
            print_say(ans)
        except:
            print_say("I'm  still learning. I don't know your answer yet")
know_all()