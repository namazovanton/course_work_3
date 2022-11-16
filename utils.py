import json


class ValueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


def get_posts_all(path='data/posts.json'):
    """Загружает файл 'posts.json'"""
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_comments_all(path='data/comments.json'):
    """Загружает файл 'comments.json'"""
    with open(path, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return comments


def get_posts_by_user(user_name):
    """Ищет посты по имени автора"""
    posts_by_user = []
    posts_list = get_posts_all()
    user_names = [post["poster_name"].lower() for post in posts_list]
    if user_name.lower() not in user_names:
        raise ValueError("Пользователь не найден")
    for post in posts_list:
        if user_name.lower() in post["poster_name"].lower():
            posts_by_user.append(post)
    return posts_by_user


def get_comments_by_post_id(post_id):
    """Ищет комментарии по id"""
    comments_by_id = []
    posts_list = get_posts_all()
    comments_list = get_comments_all()
    list_of_existing_posts = [int(post["pk"]) for post in posts_list]
    list_of_post_id_in_comments = [int(comment["post_id"]) for comment in comments_list]

    if int(post_id) not in list_of_existing_posts:
        raise ValueError("Пост не существует")
    elif int(post_id) not in list_of_post_id_in_comments:
        comments_by_id = []
    for comment in comments_list:
        if int(post_id) == int(comment["post_id"]):
            comments_by_id.append(comment)
    return comments_by_id


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts_by_query = []
    posts_list = get_posts_all()
    for post in posts_list:
        if query.lower() in post["content"].lower():
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts_list = get_posts_all()
    for post in posts_list:
        if pk == int(post["pk"]):
            return post
        else:
            continue
