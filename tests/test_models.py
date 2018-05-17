import math

import pytest
from apistar import exceptions
from apistar_mongoengine.pagination import Pagination

from tests.models import Todo


HARDCODED_TODO_ID = '1234567890abcdef12345678'
NONEXISTENT_TODO_ID = '000000000000000000000000'


def drop_collections():
    Todo.drop_collection()


def create_todo_item(**kwargs):
    options = {
        'text': 'Sample',
        'title': 'Testing',
        'done': True,
    }
    options.update(kwargs)

    todo = Todo(**options)

    return todo.save()


def test_get_object(sconn_params):
    drop_collections()

    new_item = create_todo_item(id=HARDCODED_TODO_ID)
    feched_item = Todo.objects.get_or_404(id=HARDCODED_TODO_ID)

    assert new_item.id == feched_item.id
    assert new_item.text == feched_item.text
    assert new_item.title == feched_item.title
    assert new_item.done == feched_item.done


def test_get_or_404(sconn_params):
    drop_collections()

    new_item = create_todo_item(id=HARDCODED_TODO_ID)
    feched_item = Todo.objects.get_or_404(id=HARDCODED_TODO_ID)

    assert new_item.id == feched_item.id
    assert new_item.text == feched_item.text
    assert new_item.title == feched_item.title
    assert new_item.done == feched_item.done

    with pytest.raises(exceptions.NotFound):
        Todo.objects.get_or_404(id=NONEXISTENT_TODO_ID)


def test_first_or_404(sconn_params):
    drop_collections()

    new_item = create_todo_item(id=HARDCODED_TODO_ID)
    feched_item = Todo.objects.first_or_404(id=HARDCODED_TODO_ID)

    assert new_item.id == feched_item.id
    assert new_item.text == feched_item.text
    assert new_item.title == feched_item.title
    assert new_item.done == feched_item.done

    with pytest.raises(exceptions.NotFound):
        Todo.objects.first_or_404(id=NONEXISTENT_TODO_ID)


def test_paginate(sconn_params):
    drop_collections()

    GENERATE_X_ITEMS = 20
    PAGINATION_START_PAGE = 1
    PAGINATION_PER_PAGE = 10

    for n in range(GENERATE_X_ITEMS):
        create_todo_item(id=f'{n:024}', title=f'Item #{n}',
                         text=f'Count to {n}')

    current_page = PAGINATION_START_PAGE
    per_page = PAGINATION_PER_PAGE
    total_pages = int(math.ceil(GENERATE_X_ITEMS / float(PAGINATION_PER_PAGE)))

    with pytest.raises(exceptions.NotFound):
        Todo.objects.paginate(page=0, per_page=per_page)

    paginated = Todo.objects.paginate(page=current_page, per_page=per_page)

    assert isinstance(paginated, Pagination)
    assert paginated.page == current_page
    assert paginated.pages == total_pages
    assert paginated.total == GENERATE_X_ITEMS
    assert paginated.has_next is True
    assert paginated.next_num == current_page + 1
    assert paginated.has_prev is not True
    assert paginated.prev_num == current_page - 1

    for i, item in enumerate(paginated.items):
        adjusted_id = i + (PAGINATION_PER_PAGE * (current_page - 1))

        assert str(item.id) == f'{adjusted_id:024}'
        assert item.title == f'Item #{adjusted_id}'
        assert item.text == f'Count to {adjusted_id}'

    paginated = paginated.next()
    current_page = paginated.page

    for i, item in enumerate(paginated.items):
        adjusted_id = i + (PAGINATION_PER_PAGE * (current_page - 1))

        assert str(item.id) == f'{adjusted_id:024}'
        assert item.title == f'Item #{adjusted_id}'
        assert item.text == f'Count to {adjusted_id}'

    paginated = paginated.prev()
    current_page = paginated.page

    for i, item in enumerate(paginated.items):
        adjusted_id = i + (PAGINATION_PER_PAGE * (current_page - 1))

        assert str(item.id) == f'{adjusted_id:024}'
        assert item.title == f'Item #{adjusted_id}'
        assert item.text == f'Count to {adjusted_id}'


def test_pagination_create_from_blank_iterable(sconn_params):
    drop_collections()

    paginated = Pagination(iterable=[], page=1, per_page=1)
    assert paginated.total == 0

    with pytest.raises(exceptions.NotFound):
        Pagination(iterable=[], page=2, per_page=1)


def test_paginate_iter_pages_default_10_pages(sconn_params):
    drop_collections()

    GENERATE_X_ITEMS = 10
    PAGINATION_START_PAGE = 1
    PAGINATION_PER_PAGE = 1

    for n in range(GENERATE_X_ITEMS):
        create_todo_item(id=f'{n:024}', title=f'Item #{n}',
                         text=f'Count to {n}')

    current_page = PAGINATION_START_PAGE
    per_page = PAGINATION_PER_PAGE
    total_pages = int(math.ceil(GENERATE_X_ITEMS / float(PAGINATION_PER_PAGE)))

    paginated = Todo.objects.paginate(page=current_page, per_page=per_page)
    assert paginated.pages == total_pages

    page_nums = []
    for page_num in paginated.iter_pages():
        page_nums.append(page_num)

    assert page_nums == [1, 2, 3, 4, 5, 6, None, 9, 10]

    page_nums = list(paginated.iter_pages(left_edge=0, left_current=1,
                                          right_current=1, right_edge=0))

    assert page_nums == [1, 2, None]
