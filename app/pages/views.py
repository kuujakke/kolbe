from flask import render_template
from . import pages

#@application.route('/')
#def index():
#    return render_template('index.html', **locals())


#application.add_url_rule('/<username>', 'hello', (lambda username: header_text + say_hello(username) + home_link + footer_text))

# Add route to database overview
#application.add_url_rule('/database', 'database', (lambda: header_text + database.overview() + home_link + footer_text))

#def header():
#    return render_template('header.html')


@pages.route('/')
def index():
    return render_template('pages/index.html', title="Pages")


#def tags():
#    return header() + render_template('tags.html', tags=env.tags())


#def users():
#    return header() + render_template('users.html', users=env.users())


#def database():
#    return header() + render_template('database.html', pages=env.pages())

