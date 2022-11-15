from flask import Flask, render_template, request, jsonify

import utils

app = Flask(__name__)


@app.route("/")
def show_all():
    posts_list = utils.get_posts_all()
    return render_template('index.html', posts_list=posts_list)


@app.route("/posts/<int:post_id>/")
def show_by_id(post_id):
    viewing_post = utils.get_post_by_pk(post_id)
    comments_list = utils.get_comments_by_post_id(post_id)
    comments_count = len(comments_list)
    return render_template('post.html', comments_list=comments_list, post=viewing_post, comments_count=comments_count)


@app.route("/search/")
def search_by_keyword():
    keyword = request.args.get('s', "").lower()
    viewing_posts = utils.search_for_posts(keyword)
    posts_count = len(viewing_posts)
    return render_template('search.html', viewing_posts=viewing_posts, posts_count=posts_count)


@app.route("/users/<username>/")
def search_by_user(username):
    viewing_posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', viewing_posts=viewing_posts)


@app.route("/api/")
def api_show_all():
    posts_list = utils.get_posts_all()
    return posts_list


@app.route("/api/posts/<int:post_id>/")
def api_show_by_id(post_id):
    viewing_post = utils.get_post_by_pk(post_id)
    return jsonify(viewing_post)


@app.errorhandler(404)
def not_found(e):
    return "404 - Страница не найдена"


@app.errorhandler(500)
def server_error(e):
    return "500 - Ошибка сервера"


app.run(debug=True)