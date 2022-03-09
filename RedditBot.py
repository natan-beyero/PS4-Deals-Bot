import requests
import requests.auth
import praw

user_agent = "cross-platform:ps4-deals-bot:v1.0.0 (by u/The_G1ver)"

global first_comment
first_comment = True

reddit_object = None

def authenticate():

    reddit = praw.Reddit(
        user_agent = user_agent,
        client_id = '6CcXfaLenPVKah4IrKjYQQ',
        client_secret = '5kjuloG4_3la8Hn0sP1TkdAkrRQ0rw',
        username = 'PS4Deals_Bot',
        password = "ToServeByPostingDeals!"
    )
    
    global reddit_object
    reddit_object = reddit

    return reddit_object

    # client_auth = requests.auth.HTTPBasicAuth('6CcXfaLenPVKah4IrKjYQQ', '5kjuloG4_3la8Hn0sP1TkdAkrRQ0rw')
    # post_data = {"grant_type": "password", "username": "PS4Deals_Bot", "password": "ToServeByPostingDeals!"}
    # headers = {"User-Agent": user_agent}
    # response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    # return response.json()

def post_comment(text, prev_comment):
    return prev_comment.reply(text)

def post_comment_by_id(text, reddit, parent_id):

    #url = "https://www.reddit.com/user/PS4Deals_Bot/comments/t70o8t/test_01/"
#
    #thing_id = url.split("/")[6]
    
    print('reddit_object:', type(reddit_object))

    prev_comment = reddit.submission(id=parent_id)

#
   # if first_comment:
   #     first_comment = False
   #     return str(prev_comment.add_comment(text))

    
    output = prev_comment.reply(text)
    return output

    #API_method = "/api/compose/"
#
#
    #headers = {"Authorization": response_json['token_type'] + " " + response_json["access_token"],
    #           "User-Agent": user_agent
    #}
#
    ## data = {"id": "t3_" + thing_id,
    ##         "dir": "1"
    ## }
#
    #data = {"grant_type": "password",
    #        "username": "PS4Deals_Bot",
    #        "password": "ToServeByPostingDeals!",
#
    #        'api_type': 'submit',
    #        'return_rtjson': True,
    #        'thing_id': thing_id,
    #        'text': 'first comment!',
    #}
#
#
#
    #response = requests.post("https://oauth.reddit.com" + API_method, headers=headers, data=data)
    #print(response.json())
#
    # response = requests.post("https://oauth.reddit.com" + API_method, headers=headers, data=data)
