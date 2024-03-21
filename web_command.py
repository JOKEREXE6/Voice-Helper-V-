import webbrowser

def google_search(query):
    if query == '':
        return

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def youtube_search(query):
    if query == '':
        return

    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open( url )

def reddit_search(query):
    if query == '':
        return
    youtube_main = ()

    url = f"https://www.reddit.com/search/?q={query}"
    webbrowser.open( url )


