import praw

user_agent = "cross-platform:ps4-deals-bot:v1.0.0 (by u/The_G1ver)"

def authenticate():
    '''authenticates via oauth and returns an instance of reddit'''

    reddit = praw.Reddit(
        user_agent = user_agent,
        client_id = '6CcXfaLenPVKah4IrKjYQQ',
        client_secret = '5kjuloG4_3la8Hn0sP1TkdAkrRQ0rw',
        username = 'PS4Deals_Bot',
        password = "ToServeByPostingDeals!"
    )

    return reddit


def post_comment(text, prev_comment):
    '''takes a comment object, adds the specified text as a reddit comment, and returns a comment object'''

    return prev_comment.reply(text)


def post_comment_by_id(text, reddit, parent_id):
    '''adds the specified text as a reddit comment and returns a comment object'''

    prev_comment = reddit.submission(id=parent_id)

    return prev_comment.reply(text)
