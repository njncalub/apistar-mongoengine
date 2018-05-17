from apistar import Route

from views import create_post, get_post, list_posts


routes = [
    Route("/posts/", "POST", create_post),
    Route("/posts/{post_id}", "GET", get_post),
    Route("/posts/", "GET", list_posts),
]
