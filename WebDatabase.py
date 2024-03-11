### This is for fast opening of website

from colorama import Fore
def lower_string_list(my_list):
    new_list = [[x.lower() for x in sub_list] for sub_list in my_list]
    return new_list


def create_website_dictionary(website_list):
    return {website[0].lower(): website[1] for website in website_list}


website_list = websites_list = [
    ["Google", "www.google.com"],
    ["Facebook", "www.facebook.com"],
    ["YouTube", "www.youtube.com"],
    ["Amazon", "www.amazon.com"],
    ["Twitter", "www.twitter.com"],
    ["Instagram", "www.instagram.com"],
    ["LinkedIn", "www.linkedin.com"],
    ["Reddit", "www.reddit.com"],
    ["Netflix", "www.netflix.com"],
    ["Wikipedia", "www.wikipedia.org"],
    ["Microsoft", "www.microsoft.com"],
    ["Apple", "www.apple.com"],
    ["GitHub", "www.github.com"],
    ["Stack Overflow", "www.stackoverflow.com"],
    ["CNN", "www.cnn.com"],
    ["BBC", "www.bbc.com"],
    ["The New York Times", "www.nytimes.com"],
    ["National Geographic", "www.nationalgeographic.com"],
    ["Etsy", "www.etsy.com"],
    ["Pinterest", "www.pinterest.com"],
    ["Tumblr", "www.tumblr.com"],
    ["Spotify", "www.spotify.com"],
    ["Adobe", "www.adobe.com"],
    ["Dropbox", "www.dropbox.com"],
    ["Quora", "www.quora.com"],
    ["Alibaba", "www.alibaba.com"],
    ["BBC Sport", "www.bbc.com/sport"],
    ["CNN Business", "www.cnn.com/business"],
    ["The Guardian", "www.theguardian.com"],
    ["Weather.com", "weather.com"],
    ["TripAdvisor", "www.tripadvisor.com"],
    ["Chat GPT", "www.chat.openai.com"],
    ["whatsapp", "web.whatsapp.com"],
    # Add more websites as needed
]

website_list = lower_string_list(website_list)
websites_dict = create_website_dictionary(website_list)


def web_list_search(search_text):
    c = False
    try:

        website_address = websites_dict.get(search_text)

        if website_address:
            website_address = "https://" + website_address
            return website_address
        else:
            return "none"
    except Exception:

        print(Fore.RED+f"Error while searching for {search_text} in website list.")

    return "none"
