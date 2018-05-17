from typing import List

from apistar import http

from models import PostModel
from types_ import PostType  # because types is part of the standard library


def create_post(post: PostType) -> http.JSONResponse:
    instance = PostModel(**post)
    instance.save()

    return http.JSONResponse(PostType(instance), status_code=201)


def get_post(post_id: str) -> PostType:
    instance = PostModel.filter(id=post_id).first_or_404()

    return PostType(instance)


def list_posts() -> List[PostType]:
    return [PostType(post) for post in PostModel.objects.all()]
