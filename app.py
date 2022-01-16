
from flask import Flask, render_template, request

from utiis import get_post_with_comments_count, get_post_by_bk, get_comments_by_bk

app = Flask(__name__)


@app.route('/',)
def page_index():
    posts = get_post_with_comments_count()
    return render_template("index.html", posts=posts, )


@app.route('/posts/<int:post_pk>',)
def page_post(post_pk):
    post = get_post_by_bk(post_pk)
    comments = get_comments_by_bk(post_pk)
    return render_template("post.html", comments=comments, post=post)


app.run()
